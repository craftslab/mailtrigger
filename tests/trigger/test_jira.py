# -*- coding: utf-8 -*-

from mailtrigger.trigger.jira import Jira
from mailtrigger.trigger.trigger import TriggerException


def test_jira():
    try:
        _ = Jira(None)
    except TriggerException as err:
        assert str(err) == 'invalid jira configuration'

    assert len(Jira.help()) == 0
