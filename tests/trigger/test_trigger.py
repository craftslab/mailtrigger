# -*- coding: utf-8 -*-

from mailtrigger.trigger.trigger import Trigger


def test_trigger():
    trigger = Trigger(None)
    assert trigger is not None

    msg, ret = trigger.run(None)
    assert msg is None
    assert ret is False
