# -*- coding: utf-8 -*-

from mailtrigger.trigger.jira import Jira


def test_jira():
    jira = Jira ()
    assert jira is not None

    _, ret = jira.send('help')
    assert ret is True
