import tempfile
import os
import time
import subprocess

from app import celery


from app import compiler_path
from app import usb_port

@celery.task
def move(feet,bot_script):

  print "Moving forward %s spaces" % feet
  time.sleep(10)
  
  temp_file = tempfile.NamedTemporaryFile()
  with temp_file as writer:
    writer.write(bot_script)
    writer.flush()
  
    command = [os.path.abspath(compiler_path), "-c%s" % usb_port, temp_file.name]
    print ' '.join(command)
    p = subprocess.Popen(command, stdout=subprocess.PIPE)
    output, err = p.communicate()
    print  output