# -*- coding: utf-8 -*-

from mailtrigger.trigger.jenkins import Jenkins
from mailtrigger.trigger.trigger import TriggerException


def test_jenkins():
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

    jenkins = None

    try:
        jenkins = Jenkins(config)
    except TriggerException as err:
        assert str(err) == 'invalid jenkins configuration'

    assert len(Jenkins.help()) != 0

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
