from os import access
import twitter
import config

def collect_tweets(term: str, count: int=10) -> list:
    api = twitter.Api(consumer_key=config.api_key,
                      consumer_secret=config.api_secret_key, 
                      access_token_key=config.access_token, 
                      access_token_secret=config.access_token_secret)

    return api.GetSearch(term, count=count)

def collect_tweets_text(term: str, count: int=10) -> list:
    tweets = collect_tweets(term, count)
    return [tweet.text for tweet in tweets]


if __name__ == '__main__':
    print(collect_tweets_text('#trump', 10))