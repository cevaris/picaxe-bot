from flask import render_template

from app import app
from tasks import move

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/move/forward/<feet>')
def move_forward(feet):
  direction = 'forward'
  bot_script = render_template(('%s.html' % direction), time=(int(int(feet)*2.150)))
  move.delay(feet, bot_script)
  return "Moving forward %s" % feet
