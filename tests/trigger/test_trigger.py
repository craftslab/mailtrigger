# -*- coding: utf-8 -*-

from mailtrigger.trigger.trigger import Trigger, TriggerException


def test_trigger():
    exception = TriggerException('exception')
    assert str(exception) == 'exception'

    trigger = Trigger()
    assert trigger is not None

    assert len(Trigger.help()) == 0

    msg, ret = trigger.run(None)
    assert msg == ''
    assert ret is True
