# -*- coding: utf-8 -*-

import json
import logging
import os
import time

from datetime import datetime
from mailtrigger.scheduler.scheduler import Scheduler, SchedulerException

CONFIG = '../../mailtrigger/config/scheduler.json'


def test_scheduler():
    def _load(name):
        with open(name, 'r') as f:
            data = json.load(f)
        return data

    log = logging.getLogger('test_scheduler')

    config = _load(os.path.join(os.path.dirname(__file__), CONFIG))
    config['debug'] = True

    sched = Scheduler(config)
    assert sched is not None

    def _func(_):
        log.debug(datetime.now())

    args = []
    try:
        sched.add(_func, args, '_func')
    except SchedulerException as _:
        assert False

    try:
        sched.run()
    except SchedulerException as _:
        assert False

    time.sleep(1)

    try:
        sched.stop()
    except SchedulerException as _:
        assert False

    assert True
