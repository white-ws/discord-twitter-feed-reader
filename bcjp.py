import os
from googletrans import Translator
from twitter.twitter_wrapper import TwitterApi
from discord.discord_wrapper import DiscordApi

class BCJPTask:
	account_id = os.environ.get('BCJP_ACCOUNT_ID')
	web_hook = os.environ.get('BATTLECAT_WEBHOOK')
	translator = Translator()

	def __init__(self, consumer_key, consumer_secret, access_token, access_secret):
		self.twitter = TwitterApi(consumer_key, consumer_secret, access_token, access_secret)
		self.discord = DiscordApi(self.web_hook)

	def handle_tweet(self, tweet):
		text = self.translator.translate(tweet.text, dest='en')
		if(text is None):
			text = tweet.text
		message = '【BCJP】- Disabled filter to test translation engine\n\n'+text
		self.discord.send_discord_message(message)

	def execute(self):
		print("Starting up BCJPTask....")
		self.twitter.on_status_change(self.account_id, self.handle_tweet)
