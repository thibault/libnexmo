# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from decimal import Decimal as D


class NexmoResponse(object):
    """A convenient wrapper to manipulate the Nexmo json response.

    The class makes it easy to retrieve information about sent messages, total
    price, etc.

    Example::

        >>> response = nexmo.send_sms(frm, to, txt)
        >>> print response.total_price
        0.15
        >>> print response.remaining_balance
        1.00
        >>> print response.message_count:
        3
        >>> for message in response.messages:
        ...     print message.message_id, message.message_price
        00000124 0.05
        00000125 0.05
        00000126 0.05

    The class only handles successfull responses, since errors raise
    exceptions in the :class:`~Nexmo` class.

    """

    def __init__(self, json_data):
        self.messages = [NexmoMessage(data) for data in json_data['messages']]
        self.message_count = len(self.messages)
        self.total_price = sum(msg.message_price for msg in self.messages)
        self.remaining_balance = min(msg.remaining_balance for msg in self.messages)


class NexmoMessage(object):
    """A wrapper to manipulate a single `message` entry in a Nexmo response.

    When a text messages is sent in several parts, Nexmo will return a status
    for each and everyone of them.

    The class does nothing more than simply wrapping the json data for easy
    access.

    """
    def __init__(self, json_data):
        data = {
            'to': json_data['to'],
            'message_id': json_data['message-id'],
            'status': int(json_data['status']),
            'remaining_balance': D(json_data['remaining-balance']),
            'message_price': D(json_data['message-price']),
            'network': json_data['network']
        }
        self.__dict__.update(data)
