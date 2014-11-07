# -*- coding: utf-8 -*-

from __future__ import unicode_literals

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
