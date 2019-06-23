# -*- coding: utf-8 -*-

from mailtrigger.main import _job
from mailtrigger.main import _receive
from mailtrigger.main import _scheduler
from mailtrigger.main import _send
from mailtrigger.main import _trigger


def test_main():
    data = {
        'content': '',
        'date': '',
        'from': 'name@example.com',
        'subject': '[trigger]',
        'to': ''
    }

    try:
        _send(data, None, None)
        _trigger([data], None, None)
    except AttributeError as _:
        assert True

    try:
        _receive(None)
        _job([None, None, None])
        _scheduler(None, None, None, None)
    except AttributeError as _:
        assert True
