# -*- coding: utf-8 -*-

from mailtrigger.trigger.jenkins import Jenkins
from mailtrigger.trigger.trigger import TriggerException


def test_init():
    try:
        _ = Jenkins(None)
    except TriggerException as err:
        assert str(err) == 'invalid jenkins configuration'


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
                "port": 8081,
                "user": "user"
            }
        ]
    }

    jenkins = None

    try:
        jenkins = Jenkins(config)
    except TriggerException as err:
        assert str(err) == 'invalid jenkins configuration'

    assert len(Jenkins.help()) != 0

    msg, status = jenkins.run(None)
    assert msg == ''
    assert status is False

    event = {
        'content': '',
        'date': '',
        'from': 'foo@example.com',
        'subject': '',
        'to': ''
    }

    msg, status = jenkins.run(event)
    assert msg == ''
    assert status is False

    event = {
        'content': '',
        'date': '',
        'from': 'name@example.com',
        'subject': '',
        'to': ''
    }

    msg, status = jenkins.run(event)
    assert msg == ''
    assert status is False

    event = {
        'content': '',
        'date': '',
        'from': 'name@example.com',
        'subject': '[trigger]',
        'to': ''
    }

    msg, status = jenkins.run(event)
    assert msg == ''
    assert status is False
