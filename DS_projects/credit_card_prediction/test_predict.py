#!/usr/bin/env python
# coding: utf-8

import requests

customer_id = 'xyz-123'
url = 'http://127.0.0.1:5000/predict'

customer_no = {
    "reports": 0, 
    "age":47.75000, 
    "incomme":1.5000,
    "share": 0.000800,
    "expenditure": 0.0000,
    "owner": "yes",
    "selfemp":"no", 
    "dependents":0, 
    "months":60, 
    "majorcards": 1,
    "active":0,
 }
customer = {
    "reports": 0, 
    "age":38.41667, 
    "incomme":5.600,
    "share": 0.093484,
    "expenditure": 436.25920,
    "owner": "yes",
    "selfemp":"no", 
    "dependents":4, 
    "months":114, 
    "majorcards": 0,
    "active":7,
 }
#  0 	 	 	 	 	yes 	no 	4 	114 	0 	7

response = requests.post(url, json=customer).json()
print(response)

if response['card']:
    print(f'Card for costumer with id: {customer_id} has been Accepted!')
else:
    print(f'Card for costumer with id: {customer_id} has been Rejected!')