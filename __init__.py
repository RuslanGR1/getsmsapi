# -*- coding: utf-8 -*-

"""
Virtual numbers api library
~~~~~~~~~~~~~~~~~~~~~

Usage:

    >>>from getsmsapi import Simsms

    >>>sim_sms = Simsms(api_key='your-api-key', country='RU', service='opt29')

    >>>number, order_id = sim_sms.get_number()
    >>>number, sms = sim_sms.get_code(order_id)

:copyright: (c) 2020 by Gazizov Ruslan.
:license: MIT.
"""


from .services import Simsms
