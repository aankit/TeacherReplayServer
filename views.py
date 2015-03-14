from hello import app

@app.route('/')
@app.route('/index')
def index():
    return "Building Flask From Scratch!"
