# -*- coding: utf-8 -*-

import os
import pprint
import time

from datetime import datetime
from mailtrigger.scheduler.scheduler import Scheduler, SchedulerException

CONFIG = '../../mailtrigger/config/scheduler.json'


def test_scheduler():
    def _job():
        print(datetime.now())
    try:
        sched = Scheduler(os.path.join(os.path.dirname(__file__), CONFIG))
        sched.add(_job, '_job')
        sched.start()
        time.sleep(6)
        sched.remove('_job')
        sched.stop()
    except SchedulerException as err:
        pprint.pprint(str(err))
    assert True
