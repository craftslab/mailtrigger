# -*- coding: utf-8 -*-

from mailtrigger.registry import Registry, RegistryException


def test_registry():
    exception = RegistryException('exception')
    assert str(exception) == 'exception'

    trigger_config = {
        'debug': True,
        "gerrit": {
            'debug': True,
            "server": [
                {
                    "host": "localhost",
                    "pass": "pass",
                    "port": 8080,
                    "user": "user"
                }
            ]
        },
        "jenkins": {
            'debug': True,
            "server": [
                {
                    "host": "localhost",
                    "pass": "pass",
                    "port": 8081,
                    "user": "user"
                }
            ]
        },
        "printer": {
            'debug': True,
            "file": "output.xlsx"
        }
    }

    registry = Registry(trigger_config)
    assert registry is not None

    trigger = []
    try:
        trigger = registry.instantiate()
    except RegistryException as e:
        assert str(e) == 'invalid trigger configuration'
    assert len(trigger) != 0

    registry._registry = []

    try:
        _ = registry.instantiate()
    except RegistryException as e:
        assert str(e) == 'invalid trigger configuration'
