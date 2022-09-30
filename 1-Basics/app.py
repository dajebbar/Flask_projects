from flask import Flask, jsonify, request

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
    return f'<h3>Infos:</h3>\n{jsonify(x)}'


@app.route('/contact', methods=['GET', 'POST'], defaults={'name': 'Ali-Riad'})
@app.route('/contact/<string:name>', methods=['GET', 'POST'])
def contact(name):
    return f'Hello {name}! You are in the contact page.'

@app.route('/query', methods=['GET', 'POST'])
def query():
    name = request.args.get('name')
    location = request.args.get('loc')
    ip = request.args.get('ip')
    return (
        f'<h3>Hello {name}! Your are from {location}. You are in a query page</h3>'
        f'<h2>your Ip adress is {ip}<h2>'
    )


if __name__=='__main__':
    app.run(debug=True)