import os
import time
from ac import ACTask
from bc import BCTask
from reddit_task import RedditTask
from concurrent.futures import ThreadPoolExecutor

consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_secret = os.environ.get('ACCESS_TOKEN_SECRET')

bc_task = BCTask(consumer_key, consumer_secret, access_token, access_secret)
ac_task = ACTask(consumer_key, consumer_secret, access_token, access_secret)
reddit_task = RedditTask()

print("Script started.")
# executor = ThreadPoolExecutor(max_workers=3)
# time.sleep(60)
# executor.submit(ac_task.execute)
# time.sleep(60)
# executor.submit(bc_task.execute)
reddit_task.execute()