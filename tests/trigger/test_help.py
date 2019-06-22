# -*- coding: utf-8 -*-

from mailtrigger.trigger.help import Help
from mailtrigger.trigger.trigger import TriggerException


def test_help():
    try:
        _ = Help(None)
    except TriggerException as err:
        assert str(err) == 'invalid help configuration'

    assert len(Help.help()) == 0
