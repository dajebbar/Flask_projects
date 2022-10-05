#!/usr/bin/env python
# coding: utf-8

import pickle
from flask import (
    Flask,
    render_template,
    request,
    jsonify
)

app = Flask(__name__)

file = 'model_C=1.0.bin'

with open(file, 'rb') as f_in:
    dv, model = pickle.load(f_in)


@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0,1]
    
    card = y_pred >= .5
    
    return jsonify({
        'card_probability': float(y_pred.round(3)),
        'card': bool(card)
    })
    
if __name__=='__main__':
    app.run(debug=True)