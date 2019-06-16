# -*- coding: utf-8 -*-

import logging
import json
import os

from mailtrigger.mailer.receiver import Receiver, ReceiverException

CONFIG = '../../mailtrigger/config/mailer.json'


def test_receiver():
    def _load(name):
        with open(name, 'r') as f:
            data = json.load(f)
        return data

    log = logging.getLogger('test_scheduler')

    config = _load(os.path.join(os.path.dirname(__file__), CONFIG))
    config['debug'] = True

    try:
        receiver = Receiver(config)
        receiver.connect()
        log.debug('count: %s. size: %s' % receiver.stat())
        _ = receiver.retrieve()
        receiver.disconnect()
    except ReceiverException as err:
        log.error(str(err))

    assert True
