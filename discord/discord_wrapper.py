import requests
import random

class DiscordApi:

	def __init__(self, webhook, usernames = None, avatars = None):
		self.webhook = webhook
		if (usernames != None):
			self.usernames = usernames.split(",")
			self.avatars = avatars.split(",")
		else: 
			self.usernames = None
			self.avatars = None

	def send_discord_message(self, message):
		data = {
			'content': message
		}

		if (self.usernames != None):
			index = random.randint(0, len(self.usernames))
			data['username'] = self.usernames[index]
			data['avatar_url'] = self.avatars[index]
		response = requests.post(self.webhook, data = data)