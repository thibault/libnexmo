# -*- coding: utf-8 -*-

from __future__ import unicode_literals


# https://docs.nexmo.com/index.php/sms-api/send-message / Responses Code
class NexmoError(Exception):
    """Base exception for all Nexmo errors."""
    pass


class InvalidCredentialsError(NexmoError):
    """The api_key / api_secret you supplied is either invalid or disabled"""
    pass


NEXMO_CODE_TO_EXCEPTION = {
    4: InvalidCredentialsError,
}


def status_to_error(status):
    """Gets the correct exception class from the given status."""
    ErrorClass = NEXMO_CODE_TO_EXCEPTION.get(status, NexmoError)
    return ErrorClass
