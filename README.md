# Discord Twitter Feed Reader

A Python script for reading tweets from target users on twitter and post it on Discord. Using Discord Webhook and Twitter Realtime API.

Version 1.1.0 includes reading new topics submitted by targeted users from Reddit RSS feed and post it on Discord.

Developed and tested using Python 3.6.0. Deployed on Heroku.

# Usage

Open the terminal/command line to the file location and type:

```
python main.py
```

The following environment variables must be provided in order to execute the script.

```
## Twitter Authentication Credentials. These information can be found at https://apps.twitter.com/ After finishing the registration & configuration, go to your Application detail page and check out `Keys and Access Token` tab.

ACCESS_TOKEN
ACCESS_TOKEN_SECRET
CONSUMER_KEY
CONSUMER_SECRET

## Targeted Twitter Account ID, can be found at https://tweeterid.com/

TWITTER_ACCOUNT_ID

## Targeted Reddit User Account Name

REDDIT_ACCOUNTS

## Discord Webhook

DISCORD_WEBHOOK

```

# Dependencies

This project was made using following libraries:

- requests
- requests-oauthlib
- oauth2
- googletrans
- feedparser
- pytz
- python-dateutil
- datetime


# Versions

## v1.1.0
	Add mplementation for Reddit RSS Feed reading

## v1.0.0
	Add implementation for real-time Tweet reading

