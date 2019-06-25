# -*- coding: utf-8 -*-

from mailtrigger.registry import Registry, RegistryException


def test_registry():
    exception = RegistryException('exception')
    assert str(exception) == 'exception'

    config = {
        'debug': True,
        'gerrit': {
            'filter': {
                'from': [
                    'name@example.com'
                ],
                'subject': '[trigger]'
            },
            'host': 'localhost',
            'port': 8080
        },
        'helper': {
            'filter': {
                'from': [
                    'name@example.com'
                ],
                'subject': '[trigger]'
            }
        },
        'jenkins': {
            'filter': {
                'from': [
                    'name@example.com'
                ],
                'subject': '[trigger]'
            },
            'host': 'localhost',
            'port': 8081
        },
        'jira': {
            'filter': {
                'from': [
                    'name@example.com'
                ],
                'subject': '[trigger]'
            },
            'host': 'localhost',
            'port': 8082
        }
    }

    registry = Registry(config)
    assert registry is not None

    trigger = []
    try:
        trigger = registry.instantiate()
    except RegistryException as err:
        assert str(err) == 'invalid trigger configuration'
    assert len(trigger) != 0

    registry._registry = []

    try:
        _ = registry.instantiate()
    except RegistryException as err:
        assert str(err) == 'invalid trigger configuration'
