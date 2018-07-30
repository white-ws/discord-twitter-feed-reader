import os
from googletrans import Translator
from twitter.twitter_wrapper import TwitterApi
from discord.discord_wrapper import DiscordApi

class ACTask:
	account_id = os.environ.get('TWITTER_ACCOUNT_ID')
	spr5_id = os.environ.get('SPR5_ACCOUNT_ID')
	anime_id = os.environ.get('AC_ANIME_ACCOUNT_ID')
	web_hook = os.environ.get('DISCORD_WEBHOOK')
	names = os.environ.get('AC_BOT_NAMES')
	avatars = os.environ.get('AC_BOT_AVATARS')
	spr5_web_hook = os.environ.get('SPR5_WEBHOOK')
	spr5_names = os.environ.get('SPR5_BOT_NAMES')
	spr5_avatars = os.environ.get('SPR5_BOT_AVATARS')
	translator = Translator()

	def __init__(self, consumer_key, consumer_secret, access_token, access_secret):
		self.twitter = TwitterApi(consumer_key, consumer_secret, access_token, access_secret)
		self.discord = DiscordApi(self.web_hook, self.names, self.avatars)
		self.spr5_discord = DiscordApi(self.spr5_web_hook, self.spr5_names, self.spr5_avatars)
		self.handle = {
			self.account_id: self.handle_tweet_ac,
			self.spr5_id: self.handle_tweet_spr5,
			self.anime_id: self.handle_tweet_anime
		}

	def handle_tweet_ac(self, tweet):
		try:
			text = self.translator.translate(tweet.text, dest='en').text
		except:
			print("Error translating tweet: {}".format(tweet.text))
			text = tweet.text

		message = '\n==============================\n【Twitter】【AC】\n==============================\n\n'+text
		self.discord.send_discord_message(message)

	def handle_tweet_spr5(self, tweet):
		try:
			text = self.translator.translate(tweet.text, dest='en').text
		except:
			print("Error translating tweet: {}".format(tweet.text))
			text = tweet.text

		message = '\n==============================\n【Twitter】【SPR5】\n==============================\n\n'+text
		self.spr5_discord.send_discord_message(message)

	def handle_tweet_anime(self, tweet):
		try:
			text = self.translator.translate(tweet.text, dest='en').text
		except:
			print("Error translating tweet: {}".format(tweet.text))
			text = tweet.text

		message = '\n==============================\n【Twitter】【ANIME】\n==============================\n\n'+text
		self.discord.send_discord_message(message)

	def handle_tweet(self, tweet):
		self.handle[tweet.userId](tweet)

	def execute(self):
		print("Starting up ACTask....")
		account_ids = [self.account_id, self.spr5_id, self.anime_id]
		self.twitter.on_status_change(account_ids, self.handle_tweet)
