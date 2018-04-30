import os
from discord.discord_wrapper import DiscordApi

class RedditTask:
	web_hook = os.environ.get('BATTLECAT_WEBHOOK')

	def __init__(self, consumer_key, consumer_secret, access_token, access_secret):
		self.discord = DiscordApi(self.web_hook)

	def execute(self):
		print("Starting up RedditTask....")
