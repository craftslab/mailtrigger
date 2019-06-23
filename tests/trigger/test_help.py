# -*- coding: utf-8 -*-

from mailtrigger.trigger.help import Help
from mailtrigger.trigger.trigger import TriggerException


def test_help():
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
