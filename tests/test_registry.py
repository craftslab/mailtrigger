# -*- coding: utf-8 -*-

from mailtrigger.registry import Registry, RegistryException


def test_registry():
    exception = RegistryException('exception')
    assert str(exception) == 'exception'

    config = {
        'debug': True,
        "gerrit": {
            'debug': True,
            "filter": [
                {
                    "from": "group:ldap/name",
                    "subject": "[trigger]"
                },
                {
                    "from": "group:name",
                    "subject": "[trigger]"
                },
                {
                    "from": "user:ldap/name@example.com",
                    "subject": "[trigger]"
                },
                {
                    "from": "user:name@example.com",
                    "subject": "[trigger]"
                }
            ],
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
            "filter": [
                {
                    "from": "group:ldap/name",
                    "subject": "[trigger]"
                },
                {
                    "from": "group:name",
                    "subject": "[trigger]"
                },
                {
                    "from": "user:ldap/name@example.com",
                    "subject": "[trigger]"
                },
                {
                    "from": "user:name@example.com",
                    "subject": "[trigger]"
                }
            ],
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
            "file": "output.xlsx",
            "filter": [
                {
                    "from": "group:ldap/name",
                    "subject": "[trigger]"
                },
                {
                    "from": "group:name",
                    "subject": "[trigger]"
                },
                {
                    "from": "user:ldap/name@example.com",
                    "subject": "[trigger]"
                },
                {
                    "from": "user:name@example.com",
                    "subject": "[trigger]"
                }
            ]
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
