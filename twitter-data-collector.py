import sys
import tweepy
import config
import pandas as pd

auth = tweepy.OAuthHandler(config.api_key, config.api_secret_key)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth)
df = pd.DataFrame(columns=['tweet_id', 'text', 'likes', 'retweets'])

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        df.loc[len(df)] = [
                status.id,
                status.text,
                status.favorite_count,
                status.retweet_count
            ]
        
        print(f'number of fetched tweets: {len(df)} ', end='\r')
        sys.stdout.flush()


    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream



if __name__ == '__main__':
    print('Press CTR+C to exit ...')
    try:
        streamingAPI = tweepy.streaming.Stream(auth, CustomStreamListener())
        streamingAPI.filter(track=['iphone12', 'iphone 12'], languages=["en"])
    except KeyboardInterrupt:
        print(len(df))
        df.to_csv('tweets.csv', sep=';')
        sys.exit(0)