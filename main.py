import os
import requests
from twitter.twitter_wrapper import TwitterApi
from discord.discord_wrapper import DiscordApi

class ACTask:

	account_id = os.environ.get('TWITTER_ACCOUNT_ID')
	web_hook = os.environ.get('DISCORD_WEBHOOK')

	def __init__(self, consumer_key, consumer_secret, access_token, access_secret):
		self.twitter = TwitterApi(consumer_key, consumer_secret, access_token, access_secret)
		self.discord = DiscordApi(web_hook)

	def handle_tweet(self, tweet):
		self.discord.send_discord_message(tweet.text)

	def execute(self):
		self.twitter.on_status_change(self.account_id, self.handle_tweet)


class BCTask:

	account_id = os.environ.get('BCJP_ACCOUNT_ID')
	web_hook = os.environ.get('BATTLECAT_WEBHOOK')

	def __init__(self, consumer_key, consumer_secret, access_token, access_secret):
		self.twitter = TwitterApi(consumer_key, consumer_secret, access_token, access_secret)
		self.discord = DiscordApi(web_hook)

	def handle_tweet(self, tweet):
		self.discord.send_discord_message(tweet.text)

	def execute(self):
		self.twitter.on_status_change(self.account_id, self.handle_tweet)


consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_secret = os.environ.get('ACCESS_TOKEN_SECRET')

#TODO ThreadPoolExecutor
