from flask import render_template

from app import app
from tasks import deploy

@app.route('/')
@app.route('/index')
def index():
    return "Bot Controller"

@app.route('/robot/go/<feet>')
def move_forward(feet):
  bot_script = render_template('forward.html', time=(int(int(feet)*2.150)))
  deploy.delay(bot_script)
  return render_template('bot_script.html', direction='forward', feet=feet, bot_script=bot_script)
  # return "Moving forward %s \n" % (feet, bot_script)


@app.route('/robot/square/<feet>')
def move_forward(feet):
  bot_script = render_template('square.html', time=(int(int(feet)*2.150)))
  deploy.delay(bot_script)
  return render_template('bot_script.html', direction='in a Square of', feet=feet, bot_script=bot_script)



