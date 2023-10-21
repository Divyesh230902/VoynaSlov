import requests
from bs4 import BeautifulSoup
import os

tweets = os.walk('Twitter')
tweet_dir = {
    'root': [],
    'dirs': [],
    'tweet_id': []
}
print(tweets)
for root, dirs, files in tweets:
    tweet_dir['dirs'].append(root)
    for file in files:
        tweet_dir['root'].append(file)
        print(file)
        with open(os.path.join(root, file), 'r') as f:
            print(f.read())
            tweet_dir['tweet_id'].append(f.read())

# Replace the tweet ID below with the ID of the tweet you want to scrape
tweet_id = tweet_dir['tweet_id'][0]

# Construct a URL for the tweet using its ID
url = f'https://twitter.com/GazetaRu/status/{tweet_id}'

tweet_list = []

# Scrape the tweet using its URL
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the div with the tweet text
tweet_text = soup.find('div', class_='css-901oao css-bfa6kz r-111h2gw r-18u37iz r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-qvutc0')

# Print the tweet text
print(tweet_text.text)
