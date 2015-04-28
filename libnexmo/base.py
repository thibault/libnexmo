# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import re

import requests

from libnexmo.exceptions import status_to_error
from libnexmo.response import NexmoResponse


API_ENDPOINT = 'https://rest.nexmo.com'


class Nexmo(object):
    """Nexmo low level client.

    The class is the main entry point to the library. Once initialized, it
    provides shortcuts to every feature in the library.

    """
    def __init__(self, api_key, api_secret):
        """
        :arg api_key: The Nexmo api key.
        :arg api_secret: The Nexmo api secret.

        """
        self.api_key = api_key
        self.api_secret = api_secret

    def send_sms(self, frm, to, text):
        """Sends a simple text message.

        Example usage::

            >>> msg = "Cherie, n'oublie pas les gauffres !"
            >>> nexmo.send_sms('+33123456780', '+33987654321', msg)

        :arg frm: The `from` field, a phone number (international format with
            or without a leading "+" or alphanumerical).
        :arg to: The `to` field, a phone number, same format as the `frm`
            argument.
        :arg text: The message body.

        See :meth:`send_request` for return value and exceptions.

        """
        frm = re.sub('[^\d]', '', frm)
        to = re.sub('[^\d]', '', to)

        api_url = '%s/sms/json' % API_ENDPOINT
        params = {
            'api_key': self.api_key,
            'api_secret': self.api_secret,
            'from': frm,
            'to': to,
            'text': text,
        }
        return self.send_request(api_url, params, method='POST')

    def send_request(self, url, params, method='GET'):
        """Sends a raw request to the given api endpoint.

        :arg url: A Nexmpo api endpoint (json only)
        :arg params: A parameter dictionnary

        Returns a :class:`~libnexmo.NexmoResponse`.

        Raises:

            The library uses `Requests
            <http://docs.python-requests.org/en/latest/>`_ to perform http
            requests. `Requests exceptions
            <http://docs.python-requests.org/en/latest/api/#requests.exceptions.RequestException>`_
            won't be caught in case of connection error.

            Any :class:`~libnexmo.exceptions.NexmoError` subclass.

        """
        method = method.lower()
        assert method in ['get', 'post']

        response = requests.request(method, url, data=params)
        response_json = response.json()
        status = int(response_json['messages'][0]['status'])

        if status != 0:
            ErrorClass = status_to_error(status)
            error = response_json['messages'][0]['error-text']
            raise ErrorClass(error)

        return NexmoResponse(response_json)
