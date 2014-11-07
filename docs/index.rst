Welcome to Python libnexmo's documentation!
===========================================

`Python libnexmo` is a simple Python wrapper for the `Nexmo api
<https://docs.nexmo.com/index.php/sms-api>`_.

Philosophy
----------

This library intends to be a very simple tool to use the Nexmo api in your
Python project. It does not tries to pack every single one feature, but instead
focus on staying minimal and efficient. If you fill something is missing, pull
requests are welcome.

Compatibility
-------------

The library is compatible and tested against the two latest main Python version
, a.k.a 2.7 and 3.4.

Installation
------------

Installation is fairly straightforward and can be done with `pip`::

    pip install libnexmo

Example usage
-------------

Send a text message and print response status for each sms actually sent.

.. code:: python

    # -*- coding: utf-8 -*-

    from __future__ import unicode_literals

    from libnexmo import Nexmo


    API_KEY = 'my_api_key'
    API_SECRET = 'my_api_secret'
    nexmo = Nexmo(API_KEY, API_SECRET)

    frm = '+33123456789'
    to = '+33987654321'
    msg = 'Please remember to pick up the bread before coming'
    response = nexmo.send_sms(frm, to, msg)

    print response.message_count
    for msg in response.messages:
        print msg.status, msg.message_price

Contents
--------

.. toctree::
   :maxdepth: 2

   api
