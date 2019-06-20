# -*- coding: utf-8 -*-

import json
import os

from mailtrigger.mailer.receiver import Receiver, ReceiverException

CONFIG = '../../mailtrigger/config/mailer.json'


def test_receiver():
    def _load(name):
        with open(name, 'r') as f:
            data = json.load(f)
        return data

    config = _load(os.path.join(os.path.dirname(__file__), CONFIG))
    config['debug'] = True

    receiver = Receiver(config)
    assert receiver is not None

    try:
        receiver.connect()
    except ReceiverException as err:
        assert str(err) == 'failed to connect pop3 server'

    try:
        _, _ = receiver.stat()
    except ReceiverException as err:
        assert str(err) == 'required to connect pop3 server'

    try:
        _ = receiver.receive()
    except ReceiverException as err:
        assert str(err) == 'required to connect pop3 server'

    assert receiver.disconnect() is None
