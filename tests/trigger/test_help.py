# -*- coding: utf-8 -*-

from mailtrigger.trigger.help import Help


def test_help():
    help = Help(None)
    assert help is not None

    _, ret = help.run(None)
    assert ret is True
