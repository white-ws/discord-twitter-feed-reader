import feedparser
import os
import re
import pytz
import redis
from dateutil import parser
from datetime import datetime
from discord.discord_wrapper import DiscordApi

class RedditRss:
	web_hook = os.environ.get('BATTLECAT_WEBHOOK')

	def __init__(self, subreddit, keywords):
		self.discord = DiscordApi(self.web_hook)
		self.regex = re.compile('.*reddit.com/r/{}/.*'.format(subreddit))
		self.keywords = keywords
		redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
		self.redis =  redis.from_url(redis_url)


	def read_rss(self, user, process):
		rss_path = "https://www.reddit.com/user/{}/submitted/.rss".format(user)
		rss = feedparser.parse(rss_path)

		lastReadData = self.redis.get('lastRead_{}'.format(user))
		if lastReadData is None:
			print("Storing first lastRead for {}..".format(user))
			lastRead = datetime.now(pytz.utc)
			self.redis.set('lastRead_{}'.format(user), lastRead)
		else:
			lastRead = parser.parse(lastReadData)

		for entry in rss.entries:
			entryDate = parser.parse(entry.date)
			# DEBUG
			print("[DEBUG] Entry Date={}".format(entryDate))
			print("[DEBUG] lastRead={}".format(lastRead))
			# DEBUG
			if entryDate < lastRead or self.regex.search(entry.link) == None or not any(keyword in entry.title for keyword in self.keywords):
				break
			rss_entry = RssEntry(entry.title, entry.link, entry.author)
			process(rss_entry)
			self.redis.set('lastRead_{}'.format(user), datetime.now(pytz.utc))

			print("[DEBUG] set new last read")

class RssEntry:
	def __init__(self, title, link, author):
		self.title = title
		self.link = link
		self.author = author
