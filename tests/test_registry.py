# -*- coding: utf-8 -*-

import json
import os

from mailtrigger.registry import Registry

CONFIG = '../mailtrigger/config/trigger.json'


def test_registry():
    def _load(name):
        with open(name, 'r') as f:
            data = json.load(f)
        return data

    registry = Registry()
    assert registry is not None

    config = _load(os.path.join(os.path.dirname(__file__), CONFIG))
    config['debug'] = True

    registry.fill(config)
    assert True

    assert len(registry.list()) != 0

    assert registry.query(registry.list()[0]) is not None
