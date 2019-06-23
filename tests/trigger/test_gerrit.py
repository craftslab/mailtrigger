# -*- coding: utf-8 -*-

from mailtrigger.trigger.gerrit import Gerrit
from mailtrigger.trigger.trigger import TriggerException


def test_gerrit():
    gerrit = None

    try:
        gerrit = Gerrit(None)
    except TriggerException as err:
        assert str(err) == 'invalid gerrit configuration'

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

    try:
        gerrit = Gerrit(config)
    except TriggerException as err:
        assert str(err) == 'invalid gerrit configuration'

    assert len(Gerrit.help()) != 0

    msg, status = gerrit.run(None)
    assert msg == ''
    assert status is False

    event = {
        'content': '',
        'date': '',
        'from': 'name@example.com',
        'subject': '',
        'to': ''
    }

    msg, status = gerrit.run(event)
    assert msg == ''
    assert status is False

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
