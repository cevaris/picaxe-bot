import os 

from flask import Flask
from celery import Celery

celery = Celery('botApp', broker='redis://localhost:6379/0')
root = os.path.abspath(__file__)
app = Flask(__name__)

from app import views
