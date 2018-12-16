import os
from py_translator import Translator
from twitter.twitter_wrapper import TwitterApi
from discord.discord_wrapper import DiscordApi

class BCTask:
	account_jp_id = os.environ.get('BCJP_ACCOUNT_ID')
	account_en_id = os.environ.get('BCEN_ACCOUNT_ID')
	web_hook = os.environ.get('BATTLECAT_WEBHOOK')
	names = os.environ.get('BC_BOT_NAMES')
	avatars = os.environ.get('BC_BOT_AVATARS')
	translator = Translator()

	def __init__(self, consumer_key, consumer_secret, access_token, access_secret):
		self.twitter = TwitterApi(consumer_key, consumer_secret, access_token, access_secret)
		self.discord = DiscordApi(self.web_hook, self.names, self.avatars)
		self.handle = {
			self.account_jp_id: self.handle_tweet_jp,
			self.account_en_id: self.handle_tweet_en
		}

	def handle_tweet_jp(self, tweet):
		try:
			text = self.translator.translate(tweet.text, dest='en').text
		except:
			print("Error translating tweet: {}".format(tweet.text))
			text = tweet.text
			
		message = '\n==============================\n【Twitter】【BCJP】- Battle Cat JP Twitter\n==============================\n\n'+text
		self.discord.send_discord_message(message)

	def handle_tweet_en(self, tweet):
		message = '\n==============================\n【Twitter】【BCEN】- Battle Cat EN Twitter\n==============================\n\n'+tweet.text
		self.discord.send_discord_message(message)

	def handle_tweet(self, tweet):
		self.handle[tweet.userId](tweet)

	def execute(self):
		print("Starting up BCTask....")
		account_ids = [self.account_en_id, self.account_jp_id]
		self.twitter.on_status_change(account_ids, self.handle_tweet)
