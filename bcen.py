import os
from twitter.twitter_wrapper import TwitterApi
from discord.discord_wrapper import DiscordApi

class BCENTask:
	account_id = os.environ.get('BCEN_ACCOUNT_ID')
	web_hook = os.environ.get('BATTLECAT_WEBHOOK')

	def __init__(self, consumer_key, consumer_secret, access_token, access_secret):
		self.twitter = TwitterApi(consumer_key, consumer_secret, access_token, access_secret)
		self.discord = DiscordApi(self.web_hook)

	def handle_tweet(self, tweet):
		message = '【BCEN】- Disabled filter to test translation engine\n\n'+tweet.text
		self.discord.send_discord_message(message)

	def execute(self):
		print("Starting up BCENTask....")
		self.twitter.on_status_change(self.account_id, self.handle_tweet)
