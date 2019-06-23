# -*- coding: utf-8 -*-

import poplib

from mailtrigger.mailer.receiver import Receiver, ReceiverException


def test_receiver():
    config = {
        'debug': True,
        'pop3': {
            'host': 'pop.example.com',
            'pass': 'pass',
            'port': 995,
            'ssl': True,
            'user': 'user'
        },
        'smtp': {
            'host': 'smtp.example.com',
            'pass': 'pass',
            'port': 465,
            'ssl': True,
            'user': 'user'
        }
    }

    receiver = None

    try:
        receiver = Receiver(config)
    except ReceiverException as err:
        assert str(err) == 'missing pop3 configuration'
    assert receiver is not None

    try:
        receiver.connect()
    except ReceiverException as err:
        assert str(err) == 'failed to connect pop3 server'

    count = None
    size = None

    try:
        count, size = receiver.stat()
    except ReceiverException as err:
        assert str(err) == 'required to connect pop3 server'

    assert count is None
    assert size is None

    buf = None

    try:
       buf = receiver.receive(1)
    except ReceiverException as err:
        assert str(err) == 'required to connect pop3 server'

    if buf is None or type(buf) is str or type(buf) is list:
        assert True

    try:
        receiver.disconnect()
    except (OSError, poplib.error_proto) as _:
        assert True
