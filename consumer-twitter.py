
import tweepy
from kafka import KafkaProducer
import json
import time
import sys

configuration = json.load(open(sys.argv[1], 'r'))

consumer_token = configuration['consumer_token'] 
consumer_secret = configuration['consumer_secret'] 
access_token = configuration['access_token'] 
access_token_secret = configuration['access_token_secret'] 

producer = KafkaProducer(bootstrap_servers=configuration['kafka_server'])

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

class CidaenTwitterConsumer(tweepy.StreamListener):
    def on_status(self, tweet):
        text = tweet.text
        favorite_count = tweet.favorite_count
        lang =  tweet.lang 
        quote_count = tweet.quote_count
        retweet_count = tweet.retweet_count
        user = tweet.user.screen_name
        hashtags = tweet.entities["hashtags"]
        urls = [ urlobj['expanded_url'] for urlobj in tweet.entities["urls"]],
        created_at = str(tweet.created_at)
        if tweet.place: 
            country = tweet.place.country
        else:
            country = tweet.user.location
        tweet_info = {
            'text': text,
            'lang': lang,
            'user': user,
            'hashtags': hashtags,
            'urls': urls,
            'created_at': created_at,
            'country': country 
        }
        producer.send(configuration['kafka_topic'], json.dumps(tweet_info).encode('utf-8'))

twitter_stream_listener = CidaenTwitterConsumer()
twitter_stream = tweepy.Stream(auth = api.auth, listener=twitter_stream_listener)
time_sleeped = 0

while True:
    twitter_stream.filter(track=configuration['keywords'], languages=configuration['languages'])
    time.sleep(600)




