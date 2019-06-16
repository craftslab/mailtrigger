# -*- coding: utf-8 -*-

import json
import os

from mailtrigger.main import _format
from mailtrigger.main import _emit
from mailtrigger.main import _help
from mailtrigger.main import _trigger
from mailtrigger.main import _unpack
from mailtrigger.main import _filter
from mailtrigger.main import _retrieve
from mailtrigger.main import _job
from mailtrigger.main import _scheduler

DATA = './test_data.json'


def test_main():
    def _load(name):
        with open(name, 'r') as f:
            data = json.load(f)
        return data

    data = _load(os.path.join(os.path.dirname(__file__), DATA))

    assert _format(data, '') is not None

    try:
        _emit(data, None, None)
        _help(data, None, None)
        _trigger([data], None, None)
    except AttributeError as _:
        assert True

    assert len(_unpack([data])) != 0
    assert len(_filter([data])) != 0

    try:
        _retrieve(None)
        _job([None, None, None])
        _scheduler(None, None, None, None)
    except AttributeError as _:
        assert True
