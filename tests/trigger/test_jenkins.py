# -*- coding: utf-8 -*-

from mailtrigger.trigger.jenkins import Jenkins


def test_jenkins():
    jenkins = Jenkins(None)
    assert jenkins is not None

    _, ret = jenkins.run(None)
    assert ret is True
