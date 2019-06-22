# -*- coding: utf-8 -*-

from mailtrigger.trigger.jenkins import Jenkins
from mailtrigger.trigger.trigger import TriggerException


def test_jenkins():
    try:
        _ = Jenkins(None)
    except TriggerException as err:
        assert str(err) == 'invalid jenkins configuration'

    assert len(Jenkins.help()) != 0
