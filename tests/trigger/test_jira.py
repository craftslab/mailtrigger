# -*- coding: utf-8 -*-

from mailtrigger.trigger.jira import Jira
from mailtrigger.trigger.trigger import TriggerException


def test_jira():
    jira = None

    try:
        jira = Jira(None)
    except TriggerException as err:
        assert str(err) == 'invalid jira configuration'

    config = {
        'debug': True,
        'filter': {
            'from': [
                'name@example.com'
            ],
            'subject': '[trigger]'
        },
        'host': 'localhost',
        'port': 8082
    }

    try:
        jira = Jira(config)
    except TriggerException as err:
        assert str(err) == 'invalid jira configuration'

    assert len(Jira.help()) == 0

    msg, status = jira.run(None)
    assert msg == ''
    assert status is False

    event = {
        'content': '',
        'date': '',
        'from': 'name@example.com',
        'subject': '',
        'to': ''
    }

    msg, status = jira.run(event)
    assert msg == ''
    assert status is False

    event = {
        'content': '',
        'date': '',
        'from': 'name@example.com',
        'subject': '[trigger]',
        'to': ''
    }

    msg, status = jira.run(event)
    assert msg == ''
    assert status is False
