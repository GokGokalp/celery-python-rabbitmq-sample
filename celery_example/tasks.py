from __future__ import absolute_import
from celery_example.celery import app
import time


@app.task
def hello_world():
    print('hello world task begins')
    time.sleep(2)
    print('hello world task finished')
    return 'hello'
    
