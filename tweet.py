#!/usr/bin/env python

import tweepy, time, sys

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = '***REMOVED***'
CONSUMER_SECRET = '***REMOVED***'
ACCESS_KEY = '***REMOVED***'
ACCESS_SECRET = '***REMOVED***'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename = '/home/ianfitzpat/webapps/ianfitzpatrick_com/cloud_every_noun/nouns_to_tweet.txt'
with open(filename, 'r') as fin:
    data = fin.read().splitlines(True)
    tweet_text = 'cloud ' + data[0]
    
with open(filename, 'w') as fout:
    fout.writelines(data[1:])

api.update_status(status=tweet_text)
