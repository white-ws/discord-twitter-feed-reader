import oauth2 as oauth
import base64
import requests

OAUTH2_TOKEN_URL = 'https://api.twitter.com/oauth2/token'

class AppOnlyAuth():

	def __init__(self, consumer_key, consumer_secret):
		self.consumer_key = consumer_key
		self.consumer_secret = consumer_secret

	def get_access_token(self):
		client_credentials = get_encoded_credentials(self.consumer_key, self.consumer_secret)
		access_token = request_bearer_token(client_credentials)		

		return access_token

def get_encoded_credentials(consumer_key, consumer_secret):
	bearer_token_credentials = "{}:{}".format(consumer_key, consumer_secret)
	return base64.b64encode(bearer_token_credentials.encode('utf-8')).decode('utf-8')

def request_bearer_token(client_credentials):
	url =  OAUTH2_TOKEN_URL
	headers = {
		'Authorization': 'Basic :{}'.format(client_credentials),
		'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
	}
	data = 'grant_type=client_credentials'

	response = requests.post(url, data = data, headers = headers)

	if response.status_code != requests.codes.ok:
		raise Exception('Invalid credentials')

	return response.json().get('access_token')