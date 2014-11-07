# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import pytest
import responses

from libnexmo import Nexmo
from libnexmo.exceptions import InvalidCredentialsError


API_KEY = 'my_api_key'
API_SECRET = 'my_api_secret'
nexmo = Nexmo(API_KEY, API_SECRET)
FRM = '+33123456789'
TO = '+33987654321'
MSG = 'Please remember to pick up the bread before coming'


@responses.activate
def test_bad_credentials():
    """The correct exception should be raised when invalid credentials are used."""
    responses.add(
        responses.POST,
        'https://rest.nexmo.com/sms/json',
        body='{"message-count":"1","messages":[{"status":"4","error-text":"Bad Credentials"}]}',
        status=200,
        content_type='application/json')
    with pytest.raises(InvalidCredentialsError):
        nexmo.send_sms(FRM, TO, MSG)
