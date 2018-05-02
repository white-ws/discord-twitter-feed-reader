import feedparser
import os
import pytz
import re
from dateutil import parser
from datetime import datetime
from discord.discord_wrapper import DiscordApi

class RedditRss:
	web_hook = os.environ.get('BATTLECAT_WEBHOOK')

	def __init__(self):
		self.discord = DiscordApi(self.web_hook)
		self.regex = re.compile('.*reddit.com/r/battlecats/.*')
		self.lastRead = None

	def read_rss(self, user, process):
		rss_path = "https://www.reddit.com/user/{}/submitted/.rss".format(user)
		rss = feedparser.parse(rss_path)
		for entry in rss.entries:
			if self.lastRead is None:
				print("First loop: skipped..")
				self.lastRead = datetime.now(pytz.utc)
				break
			entryDate = parser.parse(entry.date)
			if entryDate >= self.lastRead and self.regex.search(entry.link) != None:
				rss_entry = RssEntry(entry.title, entry.link, entry.author)
				process(rss_entry)
				continue
			print(entryDate)
			print(self.lastRead)
			print(entryDate >= self.lastRead)
			break
		self.lastRead = datetime.now(pytz.utc)

class RssEntry: 
	def __init__(self, title, link, author):
		self.title = title
		self.link = link
		self.author = author