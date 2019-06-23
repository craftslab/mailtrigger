# -*- coding: utf-8 -*-

from mailtrigger.trigger.jenkins import Jenkins
from mailtrigger.trigger.trigger import TriggerException


def test_jenkins():
    jenkins = None

    try:
        jenkins = Jenkins(None)
    except TriggerException as err:
        assert str(err) == 'invalid jenkins configuration'

    config = {
        'debug': True,
        'filter': {
            'from': [
                'name@example.com'
            ],
            'subject': '[trigger]'
        },
        'host': 'localhost',
        'port': 8081
    }

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
