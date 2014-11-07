# -*- coding: utf-8 -*-

from __future__ import unicode_literals


class NexmoError(Exception):
    """Base exception for all Nexmo errors."""
    pass


class InvalidCredentialsError(NexmoError):
    """The api_key / api_secret you supplied is either invalid or disabled"""
    pass


# https://docs.nexmo.com/index.php/sms-api/send-message / Responses Code
NEXMO_CODE_TO_EXCEPTION = {

}
