# -*- coding: utf-8 -*-

from mailtrigger.banner import BANNER


def test_banner():
    assert BANNER is not None and len(BANNER) != 0
