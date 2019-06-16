# -*- coding: utf-8 -*-

from mailtrigger.registry import Registry


def test_registry():
    registry = Registry()
    assert (registry is not None)
