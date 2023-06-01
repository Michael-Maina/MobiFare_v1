#!/usr/bin/env python3

import requests
import base64
import datetime
from requests.auth import HTTPBasicAuth

consumer_key = 'pa5PLASxAViWAH6wERSnmW8vrWwGKam1'
consumer_secret = 'dvU9LvsYu3GtD1vs'
shortcode = '174379'
passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
phone_number = '254718024636'
amount = 10
callback_url = 'https://sandbox.safaricom.co.ke/mpesa/'

# Generate the access token
def generate_access_token():
    url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    response = requests.get(url, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    access_token = response.json()['access_token']
    return access_token

# Generate the password
def generate_password():
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    data = shortcode + passkey + timestamp
    encoded_data = base64.b64encode(data.encode('utf-8'))
    password = encoded_data.decode('utf-8')
    return password

# Send the STK push request
def send_stk_push():
    access_token = generate_access_token()
    password = generate_password()

    url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    payload = {
        'BusinessShortCode': shortcode,
        'Password': password,
        'Timestamp': datetime.datetime.now().strftime('%Y%m%d%H%M%S'),
        'TransactionType': 'CustomerPayBillOnline',
        'Amount': amount,
        'PartyA': phone_number,
        'PartyB': shortcode,
        'PhoneNumber': phone_number,
        'CallBackURL': callback_url,
        'AccountReference': 'STK Push Test',
        'TransactionDesc': 'STK Push Test'
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.json())


send_stk_push()
