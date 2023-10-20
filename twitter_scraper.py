import snscrape.modules.twitter as sntwitter

import tweepy as ts

# Replace the tweet ID below with the ID of the tweet you want to scrape
tweet_id = 1513639102339588099

# Construct a URL for the tweet using its ID
url = f'https://twitter.com/GazetaRu/status/{tweet_id}'

tweet_list = []

# Scrape the tweet using its URL
print(sntwitter.TwitterSearchScraper(f'url:'+url).get_items())

tweets = sntwitter.TwitterSearchScraper(f'url:'+url).get_items()

for tweet in tweets:
    # print(tweet.content)
   print(tweet)