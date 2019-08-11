# -*- coding: utf-8 -*-

from mailtrigger.auther.auther import Auther, AutherException


def test_init():
    try:
        _ = Auther(None)
    except AutherException as e:
        assert str(e) == 'invalid auther configuration'


def test_auther():
    auther_config = {
        'debug': True,
        "group": {
            "default": [
                "name@example.com"
            ],
            "ldap/name": "true"
        },
        "message": {
            "subject": "[trigger]"
        },
        "provider": {
            "ldap": {
                "base": "base",
                "host": "localhost",
                "pass": "pass",
                "port": 389,
                "user": "user"
            }
        }
    }

    auther = Auther(auther_config)
    msg, status = auther.auth(None)
    assert len(msg) != 0
    assert status is False

    auther_config = {
        'debug': True,
        "message": {
            "subject": "[trigger]"
        },
        "provider": {
            "ldap": {
                "base": "base",
                "host": "localhost",
                "pass": "pass",
                "port": 389,
                "user": "user"
            }
        }
    }

    event = {
        'content': '',
        'date': '',
        'from': 'foo@example.com',
        "subject": '',
        'to': ''
    }

    auther = Auther(auther_config)
    msg, status = auther.auth(event)
    assert len(msg) != 0
    assert status is False

    auther_config = {
        'debug': True,
        "group": {
            "default": [
                "name@example.com"
            ],
            "ldap/name": "true"
        },
        "message": {
            "subject": "[trigger]"
        },
        "provider": {
            "ldap": {
                "base": "base",
                "host": "localhost",
                "pass": "pass",
                "port": 389,
                "user": "user"
            }
        }
    }

    event = {
        'content': '',
        'date': '',
        'from': 'foo@example.com',
        "subject": '',
        'to': ''
    }

    auther = Auther(auther_config)
    msg, status = auther.auth(event)
    assert len(msg) != 0
    assert status is False

    auther_config = {
        'debug': True,
        "group": {
            "default": [
                "name@example.com"
            ],
            "ldap/name": "true"
        },
        "provider": {
            "ldap": {
                "base": "base",
                "host": "localhost",
                "pass": "pass",
                "port": 389,
                "user": "user"
            }
        }
    }

    event = {
        'content': '',
        'date': '',
        'from': 'name@example.com',
        "subject": '',
        'to': ''
    }

    auther = Auther(auther_config)
    msg, status = auther.auth(event)
    assert len(msg) != 0
    assert status is False

    auther_config = {
        'debug': True,
        "group": {
            "default": [
                "name@example.com"
            ],
            "ldap/name": "true"
        },
        "message": {
            "subject": "[trigger]"
        },
        "provider": {
            "ldap": {
                "base": "base",
                "host": "localhost",
                "pass": "pass",
                "port": 389,
                "user": "user"
            }
        }
    }

    event = {
        'content': '',
        'date': '',
        'from': 'name@example.com',
        "subject": 'none',
        'to': ''
    }

    auther = Auther(auther_config)
    msg, status = auther.auth(event)
    assert len(msg) != 0
    assert status is False

    auther_config = {
        'debug': True,
        "group": {
            "default": [
                "name@example.com"
            ],
            "ldap/name": "true"
        },
        "message": {
            "subject": "[trigger]"
        },
        "provider": {
            "ldap": {
                "base": "base",
                "host": "localhost",
                "pass": "pass",
                "port": 389,
                "user": "user"
            }
        }
    }

    event = {
        'content': '',
        'date': '',
        'from': 'name@example.com',
        "subject": '[trigger]',
        'to': ''
    }

    auther = Auther(auther_config)
    msg, status = auther.auth(event)
    assert len(msg) != 0
    assert status is True
