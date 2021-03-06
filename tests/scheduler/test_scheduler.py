# -*- coding: utf-8 -*-

import logging
import time

from datetime import datetime
from mailtrigger.scheduler.scheduler import Scheduler, SchedulerException


def test_exception():
    exception = SchedulerException('exception')
    assert str(exception) == 'exception'


def test_add():
    config = {
        'debug': True,
        'interval': 30
    }

    sched = Scheduler(config)
    assert sched is not None

    sched._sched = None

    try:
        sched.add(None, None, None)
    except SchedulerException as e:
        assert str(e) == 'required to create scheduler'

    try:
        sched.run()
    except SchedulerException as e:
        assert str(e) == 'required to create scheduler'

    try:
        sched.stop()
    except SchedulerException as e:
        assert str(e) == 'required to create scheduler'


def test_job():
    config = {
        'debug': True,
        'interval': 30
    }

    sched = Scheduler(config)
    assert sched is not None

    def _func(_):
        log = logging.getLogger('test_scheduler')
        log.debug(datetime.now())

    args = []
    try:
        sched.add(_func, args, '_func')
    except SchedulerException as e:
        assert str(e) == 'required to create scheduler'

    try:
        sched.run()
    except SchedulerException as e:
        assert str(e) == 'required to create scheduler'

    time.sleep(1)

    try:
        sched.stop()
    except SchedulerException as e:
        assert str(e) == 'required to create scheduler'

    assert True
