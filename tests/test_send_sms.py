# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from decimal import Decimal as D

import responses

from libnexmo import Nexmo
from libnexmo.response import NexmoResponse


API_KEY = 'my_api_key'
API_SECRET = 'my_api_secret'
nexmo = Nexmo(API_KEY, API_SECRET)
FRM = '+33123456789'
TO = '+33987654321'
MSG = 'Please remember to pick up the bread before coming'


@responses.activate
def test_response_type():
    """The correct exception should be raised when invalid credentials are used."""
    responses.add(
        responses.POST,
        'https://rest.nexmo.com/sms/json',
        body='''{
            "message-count":"1",
            "messages":[{
                "to":"33123456789",
                "message-id":"0200000044CF5208",
                "status":"0",
                "remaining-balance":"6.40600000",
                "message-price":"0.04500000",
                "network":"20823"
            }]
        }''',
        status=200,
        content_type='application/json')
    response = nexmo.send_sms(FRM, TO, MSG)
    assert isinstance(response, NexmoResponse)


@responses.activate
def test_response_single_message():
    """The response is correctly populated with a single message."""
    responses.add(
        responses.POST,
        'https://rest.nexmo.com/sms/json',
        body='''{
            "message-count":"1",
            "messages":[{
                "to":"33123456789",
                "message-id":"0200000044CF5208",
                "status":"0",
                "remaining-balance":"6.40600000",
                "message-price":"0.04500000",
                "network":"20823"
            }]
        }''',
        status=200,
        content_type='application/json')
    response = nexmo.send_sms(FRM, TO, MSG)

    assert response.total_price == D('0.045')
    assert response.message_count == 1
    assert response.remaining_balance == D('6.406')
    assert response.messages[0].message_id == '0200000044CF5208'
    assert response.messages[0].message_price == D('0.045')


@responses.activate
def test_response_multiple_messages():
    """The response is correctly populated with multiples messages."""
    responses.add(
        responses.POST,
        'https://rest.nexmo.com/sms/json',
        body='''{
            "message-count":"3",
            "messages":[{
                "status":"0",
                "message-id":"00000124",
                "to":"33123456789",
                "remaining-balance":"1.10",
                "message-price":"0.05",
                "network":"23410"
            },{
                "status":"0",
                "message-id":"00000125",
                "to":"33123456789",
                "remaining-balance":"1.05",
                "message-price":"0.05",
                "network":"23410"
            },{
                "status":"0",
                "message-id":"00000126",
                "to":"33123456789",
                "remaining-balance":"1.00",
                "message-price":"0.05",
                "network":"23410"
            }]
        }''',
        status=200,
        content_type='application/json')
    response = nexmo.send_sms(FRM, TO, MSG)

    assert response.total_price == D('0.15')
    assert response.message_count == 3
    assert response.remaining_balance == D('1')
    assert response.messages[1].message_id == '00000125'
    assert response.messages[1].message_price == D('0.05')
