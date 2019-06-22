# -*- coding: utf-8 -*-

from mailtrigger.trigger.gerrit import Gerrit
from mailtrigger.trigger.trigger import TriggerException


def test_gerrit():
    try:
        _ = Gerrit(None)
    except TriggerException as err:
        assert str(err) == 'invalid gerrit configuration'

    assert len(Gerrit.help()) != 0
