from email.policy import default
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return '<h3>Main page</h3>'

@app.route('/json', methods=['POST', 'GET'])
def json():
    x = {
        'firstname': 'ali-riad',
        'lastname': 'boubekri',
        'age' : 4,
        'lang': ['french', 'english'],
    }
    return f'<h3>Infos:</h3>\n{x}'


@app.route('/contact', methods=['GET', 'POST'], defaults={'name': 'Ali-Riad'})
@app.route('/contact/<string:name>', methods=['GET', 'POST'])
def contact(name):
    return f'Hello {name}! You are in the contact page.'

if __name__=='__main__':
    app.run(debug=True)