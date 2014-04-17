import tempfile
import os

from app import celery
from subprocess import call

from flask import render_template

@celery.task
def move(direction,feet):

  print "Moving forward %s spaces" % feet
  bot_script = render_template(('%s.html' % direction), feet=feet)

  temp_file = tempfile.NamedTemporaryFile()
  # os.chmod(temp_file.name , 777 )
  with temp_file as writer:
    writer.write(bot_script)
    writer.flush()
    print temp_file.name

    print "RESULT %s" % call(['cat', temp_file.name])