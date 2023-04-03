# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from payment.models import payment_status as paystat
import requests
import json
# This function is for fetching the user data.


def cart_details_update(id):
    ship_dict = {}
    cart = paystat.objects.filter(cart_id=id)
    for data in cart.values():
        data
    ship_dict['Cart id'] = data['cart_id']

    # Data is ready for calling the shipment_updates API.
    url = 'http://127.0.0.1:8004/cart_reg_update/'
    data = json.dumps(ship_dict)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=data, headers=headers)
    api_resp = json.loads(response.content.decode('utf-8'))
    return api_resp
