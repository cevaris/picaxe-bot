

from app import app
from tasks import move

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/move/forward/<feet>')
def move_forward(feet):
    move('forward', feet)
    return "Moving forward %s" % feet
