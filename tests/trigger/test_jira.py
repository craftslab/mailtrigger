# -*- coding: utf-8 -*-

from mailtrigger.trigger.jira import Jira


def test_jira():
    jira = Jira (None)
    assert jira is not None

    _, ret = jira.run(None)
    assert ret is True
