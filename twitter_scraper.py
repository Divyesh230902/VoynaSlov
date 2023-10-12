import tweepy

USER_KEY = "lXKBvt2L8Q6pAh2BJWeiHwyGy"
USER_KEY_SECRET = "lqjeJKG3SvBwNEOpbKbr6o3LwHRUEHkfIU9wr25NzFlT2KUiJL"

ACCESS_TOKEN = "1460465110992883714-nuQy76o6KlL7sUMEVbo1VvAVreV9IF"
ACCESS_TOKEN_SECRET = "i3c0jNkao3grtYSzno5bApOQTRL1dIru3eiIyqssHrAR0"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(USER_KEY, USER_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

# Tweet ID to scrape
tweet_id = "1498705460060430343"

# Scrape tweet by ID
tweet = api.get_status(tweet_id)

# Print tweet text
print(tweet.text)
