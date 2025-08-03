from celery import Celery
from .celery_conf import celery_app

celery_app = Celery('A')



