# -*- coding: utf-8 -*-

from mailtrigger.trigger.help import Help
from mailtrigger.trigger.trigger import TriggerException


def test_init():
    try:
        _ = Help(None)
    except TriggerException as err:
        assert str(err) == 'invalid help configuration'


def test_trigger():
    config = {
        'debug': True,
        'filter': {
            'from': [
                'name@example.com'
            ],
            'subject': '[trigger]'
        }
    }

    _help = None

    try:
        _help = Help(config)
    except TriggerException as err:
        assert str(err) == 'invalid help configuration'

    assert len(Help.help()) == 0

    msg, status = _help.run(None)
    assert msg == ''
    assert status is False

    event = {
        'content': '',
        'date': '',
        'from': 'name@example.com',
        'subject': '',
        'to': ''
    }

    msg, status = _help.run(event)
    assert msg == ''
    assert status is False

    event = {
        'content': '',
        'date': '',
        'from': 'name@example.com',
        'subject': '[trigger]',
        'to': ''
    }

    msg, status = _help.run(event)
    assert msg == ''
    assert status is False

    event = {
        'content': '@help',
        'date': '',
        'from': 'name@example.com',
        'subject': '[trigger]',
        'to': ''
    }

    msg, status = _help.run(event)
    assert len(msg) != 0
    assert status is True
