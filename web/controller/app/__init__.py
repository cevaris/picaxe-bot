import os 

import logging
from logging.handlers import RotatingFileHandler

from flask import Flask
from celery import Celery


app = Flask(__name__)


# Globals
compiler_path = os.environ['COMPILER_PATH'] 
usb_port = os.environ['USB_PORT']



# Celery
celery = Celery('app', broker=os.environ['REDIS_URL'])
celery.conf.add_defaults(app.config)


# Logging
LOG_FILENAME = 'logs/dev.log'
handler = logging.handlers.RotatingFileHandler(
  LOG_FILENAME,
  maxBytes=1024 * 1024 * 100,
  backupCount=20
)
handler.setLevel(logging.DEBUG)
app.logger.addHandler(handler)

from app import views
from app import tasks