from flask import Flask
from celery import Celery

celery = Celery('botApp', broker='redis://localhost:6379/0')

app = Flask(__name__)
from app import views
