# -*- coding: utf-8 -*-

from mailtrigger.trigger.helper import Helper
from mailtrigger.trigger.trigger import TriggerException


def test_init():
    try:
        _ = Helper(None)
    except TriggerException as e:
        assert str(e) == 'invalid helper configuration'


def test_helper():
    helper = None

    try:
        helper = Helper(None)
    except TriggerException as e:
        assert str(e) == 'invalid helper configuration'

    assert len(Helper.help()) == 0

    msg, status = helper.run(None)
    assert len(msg) != 0
    assert status is False

    event = {
        'content': '',
        'date': '',
        'from': 'foo@example.com',
        'subject': '',
        'to': ''
    }

    msg, status = helper.run(event)
    assert len(msg) != 0
    assert status is False

    event = {
        'content': '',
        'date': '',
        'from': 'name@example.com',
        'subject': '',
        'to': ''
    }

    msg, status = helper.run(event)
    assert len(msg) != 0
    assert status is False

    event = {
        'content': '',
        'date': '',
        'from': 'name@example.com',
        'subject': '[trigger]',
        'to': ''
    }

    msg, status = helper.run(event)
    assert len(msg) != 0
    assert status is False

    event = {
        'content': '@help',
        'date': '',
        'from': 'name@example.com',
        'subject': '[trigger]',
        'to': ''
    }

    msg, status = helper.run(event)
    assert len(msg) != 0
    assert status is True
