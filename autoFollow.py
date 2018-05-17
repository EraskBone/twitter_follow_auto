import tweepy
import time
import sys
from datetime import datetime

CONSUMER_KEY = 'PhmPFIDjTcbaxeRmqXqK0KZVR'
CONSUMER_SECRET = 'TLIWUadER3B5zySncWwHT7aG1Vyg8evWelvfT9Z9wXXznqQ6uR'
ACCESS_TOKEN = '87425177-4dkwezCSg5Ux58X2NId3WE2XilzzSX9K7hv2KG9KQ'
ACCESS_SECRET = '6htnT5yE0zgGC67lfHZ4y9DU21jGwufRtDkfXgQZoJKW7'

#Tweepy
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
#APIインスタンスを作成
api = tweepy.API(auth)

for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print(follower.screen_name)
