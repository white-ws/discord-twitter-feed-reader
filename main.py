import os
import time
from ac import ACTask
from bcen import BCENTask
from bcjp import BCJPTask
from concurrent.futures import ThreadPoolExecutor

consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_secret = os.environ.get('ACCESS_TOKEN_SECRET')

bcjp_task = BCJPTask(consumer_key, consumer_secret, access_token, access_secret)
bcen_task = BCENTask(consumer_key, consumer_secret, access_token, access_secret)
ac_task = ACTask(consumer_key, consumer_secret, access_token, access_secret)

print("Script started.")
executor = ThreadPoolExecutor(max_workers=3)
time.sleep(300)
executor.submit(bcjp_task.execute)
time.sleep(300)
executor.submit(bcen_task.execute)
time.sleep(300)
executor.submit(ac_task.execute)
