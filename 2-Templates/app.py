from flask import (
    Flask, 
    jsonify, 
    request, 
    url_for, 
    redirect, 
    session, 
    render_template,
    g,

)
import sqlite3


app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecret'

def connect_db():
    #path to database
    sql = sqlite3.connect('./data.db')
    #change output of db from tuple to dict
    sql.row_factory = sqlite3.Row

    return sql

def get_db():
    #store db output in global object 'g'
    if not hasattr(g, 'sqlite3'):
        g.sqlite_db = connect_db()

    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    #close db
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/')
def index():
    session.pop('name', None)
    return render_template('index.html')

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
    return render_template(
        'contact.html', 
        name=name, 
        display=False, 
        mylist = [i for i in range(4)],
        mydict = {'name': 'zach', 'age': 48},
    )

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