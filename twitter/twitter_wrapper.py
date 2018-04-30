import requests
import json
import sys
import traceback
from requests_oauthlib import OAuth1

STREAM_FILTER_STATUSES = 'https://stream.twitter.com/1.1/statuses/filter.json'

class TwitterApi:
	def __init__(self, consumer_key, consumer_secret, access_token, access_secret):
		self.auth = OAuth1(consumer_key, consumer_secret, access_token, access_secret)

	def on_status_change(self, userIds, process):
		params = {
			# 'follow':'2449437698'
			'follow': ",".join(userIds)
		}
		url = STREAM_FILTER_STATUSES

		try:
			response = requests.get(url, auth = self.auth, params = params, stream = True)

			for line in response.iter_lines():
				if line:
					try:
						jsonifiedResponse = json.loads(line)
						print(json.dumps(jsonifiedResponse, indent = 4))
						# if jsonifiedResponse["user"]["id_str"] in userIds:
						tweet = Tweet(jsonifiedResponse["text"], jsonifiedResponse["user"]["id_str"])
						process(tweet)
					except:
						print("Unexpected error: {}".format(sys.exc_info()[0]))
						traceback.print_exc()
		except:
			print("Unexpected error: {}".format(sys.exc_info()[0]))
			traceback.print_exc()

class Tweet:
	def __init__(self, text, userId):
		self.text = text
		self.userId = userId;
