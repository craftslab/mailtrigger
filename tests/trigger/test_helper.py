# -*- coding: utf-8 -*-

from mailtrigger.trigger.helper import Helper
from mailtrigger.trigger.trigger import TriggerException


def test_init():
    try:
        _ = Helper(None)
    except TriggerException as err:
        assert str(err) == 'invalid helper configuration'


def test_trigger():
    config = {
        'debug': True,
        "filter": [
            {
                "from": "name@example.com",
                "subject": "[trigger]"
            }
        ]
    }

    _helper = None

    try:
        _helper = Helper(config)
    except TriggerException as err:
        assert str(err) == 'invalid helper configuration'

    assert len(Helper.help()) == 0

    msg, status = _helper.run(None)
    assert len(msg) != 0
    assert status is False

    event = {
        'content': '',
        'date': '',
        'from': 'foo@example.com',
        'subject': '',
        'to': ''
    }

    msg, status = _helper.run(event)
    assert len(msg) != 0
    assert status is False

    event = {
        'content': '',
        'date': '',
        'from': 'name@example.com',
        'subject': '',
        'to': ''
    }

    msg, status = _helper.run(event)
    assert len(msg) != 0
    assert status is False

    event = {
        'content': '',
        'date': '',
        'from': 'name@example.com',
        'subject': '[trigger]',
        'to': ''
    }

    msg, status = _helper.run(event)
    assert len(msg) != 0
    assert status is False

    event = {
        'content': '@help',
        'date': '',
        'from': 'name@example.com',
        'subject': '[trigger]',
        'to': ''
    }

    msg, status = _helper.run(event)
    assert len(msg) != 0
    assert status is True
