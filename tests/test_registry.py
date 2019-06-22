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

    config = _load(os.path.join(os.path.dirname(__file__), CONFIG))
    config['debug'] = True

    registry = Registry(config)
    assert registry is not None

    trigger = registry.instantiate()
    assert len(trigger) != 0
