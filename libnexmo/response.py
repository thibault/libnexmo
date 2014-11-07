# -*- coding: utf-8 -*-

from __future__ import unicode_literals


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
        pass
