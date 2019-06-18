# -*- coding: utf-8 -*-

from mailtrigger.trigger.gerrit import Gerrit


def test_gerrit():
    gerrit = Gerrit()
    assert gerrit is not None

    _, ret = gerrit.send('help')
    assert ret is True
