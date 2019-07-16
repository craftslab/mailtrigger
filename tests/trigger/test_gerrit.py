# -*- coding: utf-8 -*-

from mailtrigger.trigger.gerrit import Gerrit
from mailtrigger.trigger.trigger import TriggerException

PREFIX = '@gerrit '

HELP = (
    PREFIX + 'help',
    PREFIX + 'list',
    PREFIX + 'restart <host>',
    PREFIX + 'start <host>',
    PREFIX + 'stop <host>',
    PREFIX + 'abandon <host> <changenumber>',
    PREFIX + 'restore <host> <changenumber>',
    PREFIX + 'review <host> <changenumber>',
    PREFIX + 'submit <host> <changenumber>',
    PREFIX + 'version <host>'
)


def test_init():
    try:
        _ = Gerrit(None)
    except TriggerException as err:
        assert str(err) == 'invalid gerrit configuration'


def test_trigger():
    config = {
        'debug': True,
        "filter": [
            {
                "from": "name@example.com",
                "subject": "[trigger]"
            }
        ],
        "server": [
            {
                "host": "localhost",
                "pass": "pass",
                "port": 8080,
                "user": "user"
            }
        ]
    }

    gerrit = None

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
        'from': 'foo@example.com',
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

    event = {
        'content': '@gerrit ',
        'date': '',
        'from': 'name@example.com',
        'subject': '[trigger]',
        'to': ''
    }

    msg, status = gerrit.run(event)
    assert msg == ''
    assert status is False

    event = {
        'content': '@jenkins ',
        'date': '',
        'from': 'name@example.com',
        'subject': '[trigger]',
        'to': ''
    }

    msg, status = gerrit.run(event)
    assert msg == ''
    assert status is False

    for item in HELP:
        event['content'] = item
        msg, _ = gerrit.run(event)
        assert len(msg) != 0
