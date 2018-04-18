import os
import requests
from twitter.twitter_wrapper import TwitterApi

def handle_tweet(tweet): 
	print(tweet.text)
	send_discord_message(tweet.text)

def send_discord_message(message):
	data = {
		'content': message
	}

	response = requests.post(web_hook, data = data)


consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_secret = os.environ.get('ACCESS_TOKEN_SECRET')

account_id = os.environ.get('TWITTER_ACCOUNT_ID')
web_hook = os.environ.get('DISCORD_WEBHOOK')

twitter = TwitterApi(consumer_key, consumer_secret, access_token, access_secret)
twitter.on_status_change(account_id, handle_tweet)