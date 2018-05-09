import os
from googletrans import Translator
from twitter.twitter_wrapper import TwitterApi
from discord.discord_wrapper import DiscordApi

class ACTask:
	account_id = os.environ.get('TWITTER_ACCOUNT_ID')
	spr5_id = os.environ.get('SPR5_ACCOUNT_ID')
	web_hook = os.environ.get('DISCORD_WEBHOOK')
	translator = Translator()

	def __init__(self, consumer_key, consumer_secret, access_token, access_secret):
		self.twitter = TwitterApi(consumer_key, consumer_secret, access_token, access_secret)
		self.discord = DiscordApi(self.web_hook)
		self.handle = {
			self.account_id: self.handle_tweet_ac,
			self.spr5_id: self.handle_tweet_ac
		}

	def handle_tweet_ac(self, tweet):
		text = self.translator.translate(tweet.text, dest='en').text
		if(text is None):
			text = tweet.text
		message = '\n' + text
		self.discord.send_discord_message(message)

	def handle_tweet(self, tweet):
		self.handle[tweet.userId](tweet)

	def execute(self):
		print("Starting up ACTask....")
		account_ids = [self.account_id, self.spr5_id]
		self.twitter.on_status_change(account_ids, self.handle_tweet)
