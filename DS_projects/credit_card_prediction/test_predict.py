#!/usr/bin/env python
# coding: utf-8

import requests

customer_id = 'xyz-123'
url = 'http://http://127.0.0.1:5000/'

customer = {
    "reports": 0, 
    'age':47.75000, 
    'incomme':1.5000,
    "share": 0.000800,
    "expenditure": 0.0000,
    "owner": "yes",
    'selfemp':'no', 
    'dependents':0, 
    'months':60, 
    'majorcards': 1,
    'active':0,
 }

response = requests.post(url, json=customer).json()
print(response)

if response['card']:
    print( )
else:
    print(f'Card for costumer with id: {customer_id} has been Rejected')