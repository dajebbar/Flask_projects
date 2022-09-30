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


if __name__=='__main__':
    app.run(debug=True)