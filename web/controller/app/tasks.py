import tempfile
import os
# from subprocess import call
import subprocess

from app import celery
from flask import render_template

from app import compiler_path
from app import usb_port

@celery.task
def move(direction,feet):

  print "Moving forward %s spaces" % feet
  bot_script = render_template(('%s.html' % direction), time=(int(int(feet)*2.150)))

  temp_file = tempfile.NamedTemporaryFile()
  with temp_file as writer:
    writer.write(bot_script)
    writer.flush()
    # print temp_file.name
    # print "RESULT %s" % call(['cat', temp_file.name]) 
    # print os.path.abspath(compiler_path)
    # print "RESULT %s" % call([compiler_path, '-c', usb_port, temp_file.name]) 
    # print "RESULT %s" % call([compiler_path, '-c', usb_port, temp_file.name]) 

    print bot_script


    # p = subprocess.Popen([compiler_path, '-s', temp_file.name], stdout=subprocess.PIPE)
    command = [os.path.abspath(compiler_path), "-c%s" % usb_port, temp_file.name]
    print ' '.join(command)
    p = subprocess.Popen(command, stdout=subprocess.PIPE)
    output, err = p.communicate()
    print  output

    

