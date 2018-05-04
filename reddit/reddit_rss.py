import feedparser
import os
import re
import pytz
from dateutil import parser
from datetime import datetime
from discord.discord_wrapper import DiscordApi

class RedditRss:
	web_hook = os.environ.get('BATTLECAT_WEBHOOK')

	def __init__(self, subreddit, keywords):
		self.discord = DiscordApi(self.web_hook)
		self.regex = re.compile('.*reddit.com/r/{}/.*'.format(subreddit))
		self.keywords = keywords
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
			if entryDate >= self.lastRead and self.regex.search(entry.link) != None and any(keyword in entry.title for keyword in self.keywords):
				rss_entry = RssEntry(entry.title, entry.link, entry.author)
				process(rss_entry)
				continue
			break
		self.lastRead = datetime.now(pytz.utc)

class RssEntry: 
	def __init__(self, title, link, author):
		self.title = title
		self.link = link
		self.author = author