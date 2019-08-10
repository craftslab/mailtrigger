# -*- coding: utf-8 -*-

from mailtrigger.trigger.printer import Printer
from mailtrigger.trigger.trigger import TriggerException


def test_init():
    try:
        _ = Printer(None)
    except TriggerException as e:
        assert str(e) == 'invalid printer configuration'


def test_trigger():
    trigger_config = {
        'debug': True,
        "file": "output.xlsx"
    }

    printer = None

    try:
        printer = Printer(trigger_config)
    except TriggerException as e:
        assert str(e) == 'invalid printer configuration'

    assert len(Printer.help()) == 0

    msg, status = printer.run(None)
    assert len(msg) != 0
    assert status is False

    event = {
        'content': '',
        'date': '',
        'from': 'foo@example.com',
        "subject": '',
        'to': ''
    }

    msg, status = printer.run(event)
    assert len(msg) != 0
    assert status is False

    event = {
        'content': '',
        'date': '',
        'from': 'name@example.com',
        "subject": '[foo]',
        'to': ''
    }

    msg, status = printer.run(event)
    assert len(msg) != 0
    assert status is False

    event = {
        'content': '@help',
        'date': '',
        'from': 'name@example.com',
        'subject': '[trigger]',
        'to': ['alen@example.com', 'bob@example.com']
    }

    msg, status = printer.run(event)
    assert len(msg) != 0
    assert status is True

    event = {
        'content': '@help',
        'date': '',
        'from': 'name@example.com',
        'subject': '[trigger]',
        'to': ['alen@example.com', 'bob@example.com']
    }

    msg, status = printer.run(event)
    assert len(msg) != 0
    assert status is True
