import midtransclient
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from . import models
from functools import reduce
import os
from dotenv import load_dotenv

snap = midtransclient.Snap(
    is_production= os.getenv('MIDTRANS_IS_PRODUCTION') == 'True',
    server_key= os.getenv('MIDTRANS_SEVER_KEY'),
    client_key= os.getenv('MIDTRANS_CLIENT_KEY')
)

def create_transaction(transaction_data):
    params = {
        "transaction_details": {
            "order_id": transaction_data['order_id'],
            "gross_amount": transaction_data['gross_amount']
        },
        "customer_details": {
            "first_name": transaction_data['customer_name'],
            "email": transaction_data['customer_email']
        },
        "item_details": [
            *[
                {
                    "id": item['id'],
                    "price": item['price'],
                    "quantity": item['quantity'],
                    "name": item['name']
                } for item in transaction_data['items']
            ],
            {
                "id": "Tx001",
                "price": reduce(lambda x, y: x + y['price'] * y['quantity'], transaction_data['items'], 0) * 0.15,
                "quantity": 1,
                "name": "Tax Fee"
            }
        ]
    }

    try:
        transaction = snap.create_transaction(params)
        transaction_redirect_url = transaction['redirect_url']
        return transaction_redirect_url
    except Exception as e:
        return {'error': str(e)}   