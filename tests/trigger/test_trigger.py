# -*- coding: utf-8 -*-

from mailtrigger.trigger.trigger import Trigger


def test_trigger():
    trigger = Trigger()
    assert trigger is not None

    assert trigger.help() is None
    assert trigger.send(None) is None
