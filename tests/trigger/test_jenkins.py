# -*- coding: utf-8 -*-

from mailtrigger.trigger.jenkins import Jenkins
from mailtrigger.trigger.trigger import TriggerException


def test_init():
    try:
        _ = Jenkins(None)
    except TriggerException as e:
        assert str(e) == 'invalid jenkins configuration'


def test_trigger():
    trigger_config = {
        'debug': True,
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
        jenkins = Jenkins(trigger_config)
    except TriggerException as e:
        assert str(e) == 'invalid jenkins configuration'

    assert len(Jenkins.help()) == 0

    msg, status = jenkins.run(None)
    assert len(msg) != 0
    assert status is False

    event = {
        'content': '',
        'date': '',
        'from': 'foo@example.com',
        'subject': '',
        'to': ''
    }

    msg, status = jenkins.run(event)
    assert len(msg) != 0
    assert status is False

    event = {
        'content': '',
        'date': '',
        'from': 'name@example.com',
        'subject': '',
        'to': ''
    }

    msg, status = jenkins.run(event)
    assert len(msg) != 0
    assert status is False

    event = {
        'content': '',
        'date': '',
        'from': 'name@example.com',
        'subject': '[trigger]',
        'to': ''
    }

    msg, status = jenkins.run(event)
    assert len(msg) != 0
    assert status is False
