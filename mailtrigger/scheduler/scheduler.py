# -*- coding: utf-8 -*-

import json

from apscheduler.schedulers.background import BackgroundScheduler
from ..logger.logger import Logger


class SchedulerException(Exception):
    def __init__(self, info):
        super().__init__(self)
        self._info = info

    def __str__(self):
        return self._info


class Scheduler(object):
    def __init__(self, config):
        def _load(name):
            with open(name, 'r') as f:
                data = json.load(f)
            return data.get('job', None), data.get('scheduler', None)
        self._logger = Logger()
        self._job, self._scheduler = _load(config)
        if self._job is None or self._scheduler is None:
            raise SchedulerException('missing job or scheduler configuration in %s' % config)
        self._sched = BackgroundScheduler(self._scheduler)

    def add(self, job, id):
        if self._sched is None:
            raise SchedulerException('required to create scheduler')
        self._sched.add_job(job, 'interval', seconds=self._job['interval'], id=id)

    def remove(self, id):
        if self._sched is None:
            raise SchedulerException('required to create scheduler')
        self._sched.remove_job(id)

    def start(self):
        if self._sched is None:
            raise SchedulerException('required to create scheduler')
        self._sched.start()

    def stop(self):
        if self._sched is None:
            raise SchedulerException('required to create scheduler')
        self._sched.shutdown()
