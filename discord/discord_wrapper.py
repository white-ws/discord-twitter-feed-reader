import requests

class DiscordApi:

	def __init__(self, webhook, username = None, avatar = None):
		self.webhook = webhook
		self.username = username
		self.avatar = avatar

	def send_discord_message(self, message):
		data = {
			'content': message
		}
		if (self.username != None):
			data['username'] = self.username
		if (self.avatar != None):
			data['avatar_url'] = self.avatar
		response = requests.post(self.webhook, data = data)
