# -*- coding: utf-8 -*-

from mailtrigger.trigger.trigger import Trigger


def test_trigger():
    trigger = Trigger()
    assert trigger is not None

    assert len(Trigger.help()) == 0

    msg, ret = trigger.run(None)
    assert msg == ''
    assert ret is True
