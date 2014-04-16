from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/move/forward/<n>')
def move_forward(n):
    return "Moving forward %s" % n
