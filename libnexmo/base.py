# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from libnexmo.response import NexmoResponse


API_ENDPOINT = 'https://rest.nexmo.com/'


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

        Example::

            msg = "Cherie, n'oublie pas les gauffres !"
            nexmo.send_sms('+33123456780', '+33987654321', msg)

        :arg frm: The `from` field, a phone number (international format with a
            leading "+" or alphanumerical.
        :arg to: The `to` field, a phone number.
        :arg text: The message body.

        Returns a :class:`~libnexmo.NexmoResponse`.

        """
