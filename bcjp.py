import os
import requests
from twitter.twitter_wrapper import TwitterApi
from discord.discord_wrapper import DiscordApi

def handle_tweet(tweet):
	discord.send_discord_message(tweet.text)


consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_secret = os.environ.get('ACCESS_TOKEN_SECRET')

account_id = os.environ.get('BCJP_ACCOUNT_ID')
web_hook = os.environ.get('BATTLECAT_WEBHOOK')

twitter = TwitterApi(consumer_key, consumer_secret, access_token, access_secret)
discord = DiscordApi(web_hook)

twitter.on_status_change(account_id, handle_tweet)
