# -*- coding: utf-8 -*-

import os
import pprint

from datetime import datetime
from mailtrigger.scheduler.scheduler import Scheduler, SchedulerException

CONFIG = '../../mailtrigger/config/scheduler.json'


def test_scheduler():
    def _tick():
        pprint.pprint(datetime.now())
    try:
        sched = Scheduler(os.path.join(os.path.dirname(__file__), CONFIG))
        sched.add(_tick)
        sched.start()
    except SchedulerException as err:
        pprint.pprint(str(err))
    assert True
