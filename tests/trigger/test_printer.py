# -*- coding: utf-8 -*-

from mailtrigger.trigger.printer import Printer
from mailtrigger.trigger.trigger import TriggerException


def test_init():
    try:
        _ = Printer(None)
    except TriggerException as err:
        assert str(err) == 'invalid printer configuration'


def test_trigger():
    config = {
        'debug': True,
        'filter': {
            'from': [
                'name@example.com'
            ],
            'subject': '[trigger]'
        },
        'name': 'output.xlsx'
    }

    _printer = None

    try:
        _printer = Printer(config)
    except TriggerException as err:
        assert str(err) == 'invalid printer configuration'

    assert len(Printer.help()) == 0

    msg, status = _printer.run(None)
    assert msg == ''
    assert status is False

    event = {
        'content': '',
        'date': '',
        'from': 'name@example.com',
        'subject': '',
        'to': ''
    }

    msg, status = _printer.run(event)
    assert msg == ''
    assert status is False

    event = {
        'content': '',
        'date': '',
        'from': 'name@example.com',
        'subject': '[trigger]',
        'to': ''
    }

    msg, status = _printer.run(event)
    assert msg == ''
    assert status is False

    event = {
        'content': '@help',
        'date': '',
        'from': 'name@example.com',
        'subject': '[trigger]',
        'to': ''
    }

    msg, status = _printer.run(event)
    assert msg == ''
    assert status is False