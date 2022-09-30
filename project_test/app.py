from flask import Flask

app = Flask(__name__)

# @app.route('/<name>')
# def index(name):
#     return f'<h1>Hello {name}!</h1'

@app.route('/')
def index():
    return f'<h1>Hello!</h1'

@app.route('/contact')
def contact():
    return f'<h3>You are in the contact page.</h3>'


if __name__=='__main__':
    app.run(debug=True)