from __future__ import print_function

import requests
import tweepy
import MyStreamListener as msl


# Store OAuth authentication credentials in relevant variables
access_token = "184867667-U1aAl3tFwZHubd6byj7qGn70Ms9RNiRLu3nw6Nn4"
access_token_secret = "KWjjmTlFg8lRMBrKHbBeulemChfJOask3TFxr8K35mzH0"
consumer_key = "mN28LGzE22lbj2bUfKm9TqeNW"
consumer_secret = "T5xziGDZj697WP7DXgqEe8jz4ZEClfDJuDkHlZ8KvDJG5lqHeG"

# Pass OAuth details to tweepy's OAuth handler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Initialize Stream listener
l = msl.MyStreamListener()

# Create you Stream object with authentication
stream = tweepy.Stream(auth, l)

# Filter Twitter Streams to capture data by the keywords:
stream.filter(track=['clinton', 'trump', 'sanders', 'cruz'])
