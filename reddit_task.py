import os
import time
from reddit.reddit_rss import RedditRss
from discord.discord_wrapper import DiscordApi

class RedditTask:
	web_hook = os.environ.get('BATTLECAT_WEBHOOK')
	accounts = os.environ.get('REDDIT_ACCOUNTS')

	def __init__(self):
		self.discord = DiscordApi(self.web_hook)
		self.tasks = {}
		subreddit = 'battlecats'
		keywords = ['[BCJP]', '[BCEN]', '[Announcement]', 'new', 'New', 'PONOS', 'Ponos', 'Update', 'update']
		for account in self.accounts.split(","):
			self.tasks[account] = RedditRss(subreddit, keywords)

	def handle_feed(self, entry):
		print(entry.author)
		print(entry.title)
		print(entry.link)
		message = '\n==============================\n【Reddit】{}\'s new post\n==============================\n\n'.format(entry.author)+entry.title+'\n'+entry.link
		self.discord.send_discord_message(message)

	def execute(self):
		print("Starting up RedditTask....")
		while(True):
			# print("Looping.......")
			for account in self.accounts.split(","):
				# print("For account {}".format(account))
				self.tasks[account].read_rss(account, self.handle_feed)
				time.sleep(1)
			time.sleep(60)
