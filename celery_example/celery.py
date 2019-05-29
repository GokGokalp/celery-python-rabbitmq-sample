from __future__ import absolute_import
from celery import Celery

app = Celery('celery_example',
             broker='amqp://user:123456@localhost:5672/celery',
             backend='rpc://',
             include=['celery_example.tasks'])
