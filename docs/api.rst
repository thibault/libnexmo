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
