from flask import (
    Flask,
    render_template,
    g,
    request,
)
import sqlite3

app = Flask(__name__)

def connect_db():
    #path to database
    sql = sqlite3.connect('food_log.db')
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
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/view')
def view():
    return render_template('day.html')

@app.route('/food', methods=['GET', 'POST'])
def food():
    db = get_db()

    if request.method == 'POST':
        food_name = request.form['food-name']
        protein = int(request.form['protein'])
        carbs = int(request.form['carbohydrates'])
        fat = int(request.form['fat'])
        calories = 4 * protein + 4 * carbs + 9 * fat
        db.execute('''
                    insert into food (name, protein, carbohydrates, fat, calories) 
                    values (?, ?, ?, ?, ?)''',

                    [food_name, protein, carbs, fat, calories]
        )
        db.commit()

    cur = db.execute('select name, protein, carbohydrates, fat, calories from food')
    results = cur.fetchall()
            
    return render_template('add_food.html', results=results)


if __name__=='__main__':
    app.run(debug=True)