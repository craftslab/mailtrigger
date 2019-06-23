# -*- coding: utf-8 -*-

from mailtrigger.trigger.gerrit import Gerrit
from mailtrigger.trigger.trigger import TriggerException


def test_gerrit():
    config = {
        'debug': True,
        'filter': {
            'from': [
                'name@example.com'
            ],
            'subject': '[trigger]'
        },
        'host': 'localhost',
        'port': 8080
    }

    gerrit = None

    try:
       gerrit = Gerrit(config)
    except TriggerException as err:
        assert str(err) == 'invalid gerrit configuration'

    assert len(Gerrit.help()) != 0

    event = {
        'content': '',
        'date': '',
        'from': 'name@example.com',
        'subject': '[trigger]',
        'to': ''
    }

    msg, status = gerrit.run(event)
    assert msg == ''
    assert status is False
