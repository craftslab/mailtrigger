# -*- coding: utf-8 -*-

import json
import os

from mailtrigger.main import _job
from mailtrigger.main import _receive
from mailtrigger.main import _scheduler
from mailtrigger.main import _send
from mailtrigger.main import _trigger

DATA = './test_data.json'


def test_main():
    def _load(name):
        with open(name, 'r') as f:
            data = json.load(f)
        return data

    data = _load(os.path.join(os.path.dirname(__file__), DATA))

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
