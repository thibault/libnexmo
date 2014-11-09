API Documentation
=================

We are trying to map the Nexmo API as closely as possible.

.. note::

    Since ``from`` is a reserved keyword in Python, we are using ``frm``
    instead.

.. py:module:: libnexmo

Nexmo
-----

.. autoclass:: Nexmo
    :members:


.. note:: Phone number formatting

    Nexmo's api expects phone numbers to be in international format, with the
    country code at the beginning and no leading "+".

    The library will therefore strip every character that is not a number, so
    you are free to use whatever format that you want.

    Examples::

        nexmo.send_sms(frm='33123456789', …)
        nexmo.send_sms(frm='+33123456789', …)
        nexmo.send_sms(frm='+33.123.456.789', …)
        nexmo.send_sms(frm='+331 23 45 67 89', …)
        nexmo.send_sms(frm='+331-23-45-67-89', …)

Response
--------

.. autoclass:: NexmoResponse
    :members:


.. py:module:: libnexmo.exceptions

Exceptions
----------

Every call to the Nexmo API can raise the following exceptions.

.. autoclass:: NexmoError
    :members:

.. autoclass:: InvalidCredentialsError
    :members:
