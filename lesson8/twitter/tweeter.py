#!/usr/bin/python

import sys
import tweepy

CONSUMER_KEY='j38Lo62X7p0pkzwMR5wBBw'
CONSUMER_SECRET='DOsiXn971LDYVnAgOg2oNpr2zLM407YxWAnuSjiiLE'
ACCESS_KEY='2382824977-eh2qGAn6svIvt9pJelj4RNV9vBIy5YBnRitC8jM'
ACCESS_SECRET='6NWgoEMy6Dfxvp8JBiL9HCsrGzQkS78MgamIhW6KrDT7K'

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api=tweepy.API(auth)
#api.update_status(sys.argv[1])

