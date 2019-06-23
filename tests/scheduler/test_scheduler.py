# -*- coding: utf-8 -*-

import logging
import time

from datetime import datetime
from mailtrigger.scheduler.scheduler import Scheduler, SchedulerException


def test_scheduler():
    exception = SchedulerException('exception')
    assert str(exception) == 'exception'

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
    except SchedulerException as err:
        assert str(err) == 'required to create scheduler'

    try:
        sched.run()
    except SchedulerException as err:
        assert str(err) == 'required to create scheduler'

    time.sleep(1)

    try:
        sched.stop()
    except SchedulerException as err:
        assert str(err) == 'required to create scheduler'

    assert True
