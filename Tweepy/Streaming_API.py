#!/usr/bin/env python

# https://realpython.com/twitter-bot-python-tweepy/

import tweepy

# Read access keys
import local_settings

def authenticate():
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(local_settings.api["key"], local_settings.api["secret"])
    auth.set_access_token(local_settings.access["key"], local_settings.access["secret"])

    return auth


# Stream listener
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}\n")

    def on_error(self, status):
        print("Error detected\n")


def main():

    auth = authenticate()

    api = tweepy.API(auth, wait_on_rate_limit=True,
                wait_on_rate_limit_notify=True)

    tweets_listener = MyStreamListener(api)

    stream = tweepy.Stream(api.auth, tweets_listener)

    #stream.filter(track=["Latvija", "Latvia", "Riga", "Rīga"], languages=["en"])

    track_list =["Python", "Flask", "Django"]
    print(f"Tracking: {track_list}\n")

    # start tracking for keywords in the track_list
    stream.filter(track=track_list, languages=["en"])

    
# ---------------------------------------- 

if __name__ == "__main__":
    main()
