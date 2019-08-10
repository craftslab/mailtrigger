# -*- coding: utf-8 -*-

from mailtrigger.trigger.gerrit import Gerrit
from mailtrigger.trigger.trigger import TriggerException

PREFIX = '@gerrit '

HELP = (
    PREFIX + 'abandon <host> <changenumber>',
    PREFIX + 'help',
    PREFIX + 'list',
    PREFIX + 'query <host> <changenumber>',
    PREFIX + 'rebase <host> <changenumber>',
    PREFIX + 'restart <host>',
    PREFIX + 'restore <host> <changenumber>',
    PREFIX + 'review <host> <changenumber>',
    PREFIX + 'reviewer <host> <changenumber> [add|remove] <reviewer>',
    PREFIX + 'start <host>',
    PREFIX + 'stop <host>',
    PREFIX + 'submit <host> <changenumber>',
    PREFIX + 'version <host>'
)


def test_init():
    try:
        _ = Gerrit(None)
    except TriggerException as err:
        assert str(err) == 'invalid gerrit configuration'


def test_trigger():
    global HELP

    config = {
        'debug': True,
        "filter": [
            {
                "from": "group:ldap/name",
                "subject": "[trigger]"
            },
            {
                "from": "group:name",
                "subject": "[trigger]"
            },
            {
                "from": "user:ldap",
                "subject": "[trigger]"
            },
            {
                "from": "user:name@example.com",
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
    assert len(msg) != 0
    assert status is False

    event = {
        'content': '',
        'date': '',
        'from': 'foo@example.com',
        'subject': '',
        'to': ''
    }

    msg, status = gerrit.run(event)
    assert len(msg) != 0
    assert status is False

    event = {
        'content': '',
        'date': '',
        'from': 'name@example.com',
        'subject': '',
        'to': ''
    }

    msg, status = gerrit.run(event)
    assert len(msg) != 0
    assert status is False

    event = {
        'content': '',
        'date': '',
        'from': 'name@example.com',
        'subject': '[trigger]',
        'to': ''
    }

    msg, status = gerrit.run(event)
    assert len(msg) != 0
    assert status is False

    event = {
        'content': '@gerrit ',
        'date': '',
        'from': 'name@example.com',
        'subject': '[trigger]',
        'to': ''
    }

    msg, status = gerrit.run(event)
    assert len(msg) != 0
    assert status is False

    event = {
        'content': '@jenkins ',
        'date': '',
        'from': 'name@example.com',
        'subject': '[trigger]',
        'to': ''
    }

    msg, status = gerrit.run(event)
    assert len(msg) != 0
    assert status is False

    for item in HELP:
        event['content'] = item
        msg, _ = gerrit.run(event)
        assert len(msg) != 0
