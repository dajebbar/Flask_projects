from unicodedata import name
from flask import Flask, jsonify, request, url_for, redirect, session, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecret'

@app.route('/')
def index():
    session.pop('name', None)
    return '<h3>Main page</h3>'

@app.route('/json', methods=['GET', 'POST'])
def json():
    x = {
        'firstname': 'carlos',
        'lastname': 'montana',
        'age' : 44,
        'lang': ['french', 'english'],
    }
    if 'name' in session:
        x['name'] = session['name']
    else:
        x['name'] = 'empty'
    return jsonify(x)


@app.route('/contact', methods=['GET', 'POST'], defaults={'name': 'antonio'})
@app.route('/contact/<string:name>', methods=['GET', 'POST'])
def contact(name):
    session['name'] = name
    return render_template('contact.html', name=name, display=False)

@app.route('/query', methods=['GET', 'POST'])
def query():
    name = request.args.get('name')
    location = request.args.get('loc')
    ip = request.args.get('ip')
    return (
        f'<h3>Hello {name}! Your are from {location}. You are in a query page</h3>'
        f'<h3>your Ip adress is {ip}<h3>'
    )

@app.route('/theform')
def theform():
    return render_template('form.html')
    

@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']
    return f'<p>Hello {name} from {location}. Form sent succesfully.</p>'

@app.route('/processjson', methods=['GET', 'POST'])
def processjson():
    return jsonify({'name':'Carlos', 'location':'Mexico'})

# @app.route('/processjson', methods=['GET', 'POST'])
# def processjson():
#     data = request.get_json()
#     name = data['name']
#     location = data['location']
#     randomlist = data['randomlist']

#     return jsonify({'name':name, 'location':location, 'randomkeyinlist':randomlist[1]})

@app.route('/samepage', methods=['GET', 'POST'])
def samepage():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        name = request.form['name']
        location = request.form['location']
        return f'<p>Hello {name} from {location}. Form sent succesfully.</p>'


@app.route('/redirection_page', methods=['GET', 'POST'])
def redirection_page():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        return redirect(url_for('index'))


if __name__=='__main__':
    app.run(debug=True)