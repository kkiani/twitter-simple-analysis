# Twitter Analysis
this repository is contatins multiple jupyter notebooks to test and run simple analysis on twitter's tweets.

## Requierments
all packages that have been used in all files are listed in the requierments.txt file. you can install all of them by:
```python
pip install -r requierments.txt
```

you need to setup your own config file containing your twitter's keys. ```twitter-data-collector``` will use those to connect twitter api to gather dataset.
```python
api_key = 'API-KEY'
api_secret_key = 'API-SECRET-KEY'
access_token = 'ACCESS-TOKEN'
access_token_secret = 'ACCESS-TOKEN-SECRET'
```