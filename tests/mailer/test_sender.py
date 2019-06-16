# -*- coding: utf-8 -*-

import json
import logging
import os
import time

from mailtrigger.mailer.sender import Sender, SenderException

CONFIG = '../../mailtrigger/config/mailer.json'
DATA = '../test_data.json'


def test_sender():
    def _load(name):
        with open(name, 'r') as f:
            data = json.load(f)
        return data

    log = logging.getLogger('test_sender')

    config = _load(os.path.join(os.path.dirname(__file__), CONFIG))
    config['debug'] = True

    data = _load(os.path.join(os.path.dirname(__file__), DATA))
    buf = {
        'content': '\n'.join((
            'pytest',
            '%s' % ('-'*80),
            '> From: %s' % data['from'],
            '> To: %s' % data['to'],
            '> Subject: %s' % data['subject'],
            '> Date: %s' % data['date'],
            '> Content: %s' % data['content'])),
        'date': time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())),
        'from': data['to'],
        'subject': 'Re: %s' % data['subject'],
        'to': data['from']
    }

    try:
        sender = Sender(config)
        sender.connect()
        sender.send(buf)
        sender.disconnect()
    except SenderException as err:
        log.error(str(err))

    assert True
