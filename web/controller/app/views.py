from app import app
from tasks import move

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/move/forward/<n>')
def move_forward(n):
    move('forward', n)
    return "Moving forward %s" % n
