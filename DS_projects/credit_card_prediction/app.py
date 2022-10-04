from crypt import methods
import pickle
from flask import (
    Flask,
    render_template,
    request,
)

app = Flask(__name__)

file = 'model_C=1.0.bin'
# customer = {
#     "reports": 0, 
#     'age':47.75000, 
#     'incomme':1.5000,
#     "share": 0.000800,
#     "expenditure": 0.0000,
#     "owner": "yes",
#     'selfemp':'no', 
#     'dependents':0, 
#     'months':60, 
#     'majorcards': 1,
#     'active':0,
#  }

with open(file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        customer = {
            'reports' : float(request.form['reports']), 
            'age' : float(request.form['age']), 
            'income' : float(request.form['incomme']),
            'share' : float(request.form['share']),
            'expenditure' : float(request.form['expenditure']),
            'owner' : request.form['owner'],
            'selfemp' : request.form['selfemp'], 
            'dependents' : float(request.form['dependents']), 
            'months' : float(request.form['months']), 
            'majorcards' : float(request.form['majorcards']),
            'active' : float(request.form['active']),
        }
        X = dv.transform([customer])
        score = model.predict_proba(X)[0, 1] * 100.
        
        if score >= 50.:
            card = 'Accepted'
            # print(f'The score is {res.round(3)}%, card {card}.')
        else:
            card = 'Rejected'
            # print(f'The score is {res.round(3)}%, card {card}.')
        return f'''<div>
                    <ul>
                    <li>reports={customer['reports']}</li>
                    <li>age={customer['age']}</li>
                    <li>income={customer['income']}</li>
                    <li>share={customer['share']}</li>
                    <li>expenditure={customer['expenditure']}</li>
                    <li>owner={customer['owner']}</li>
                    <li>selfemp={customer['selfemp']}</li>
                    <li>dependents={customer['dependents']}</li>
                    <li>months={customer['months']}</li>
                    <li>majorcards={customer['majorcards']}</li>
                    <li>active={customer['active']}</li>
                    </ul>
                    <p>The score is <b>{score.round(3)}%</b>.</p> 
                    <p>So customer is <b>{card}<b>!</p>
                </div>'''
    
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)