from flask import (
    Flask,
)

app = Flask(__name__)

@app.route('/')
def index():
    return None

@app.route('/view')
def view():
    return None

@app.route('/add_food')
def add_food():
    return None


if __name__=='__main__':
    app.run(debug=True)