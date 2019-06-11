# -*- coding: utf-8 -*-

from apscheduler.schedulers.blocking import BlockingScheduler


class SchedulerException(Exception):
    def __init__(self, info):
        super().__init__(self)
        self._info = info

    def __str__(self):
        return self._info


class Scheduler(object):
    def __init__(self, _):
        self._sched = BlockingScheduler()

    def add(self, job):
        self._sched.add_job(job, 'interval', seconds=3)

    def start(self):
        self._sched.start()
