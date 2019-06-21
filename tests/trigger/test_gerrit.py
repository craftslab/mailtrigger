# -*- coding: utf-8 -*-

from mailtrigger.trigger.gerrit import Gerrit


def test_gerrit():
    gerrit = Gerrit(None)
    assert gerrit is not None

    _, ret = gerrit.run(None)
    assert ret is True
