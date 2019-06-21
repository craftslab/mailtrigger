# -*- coding: utf-8 -*-

from .trigger import Trigger

HELP = ('@jenkins build <host>:<port> JOB [--parameter <PARAMETER> | -p <PARAMETER>]',
        '@jenkins help',
        '@jenkins list',
        '@jenkins list <host>:<port>',
        '@jenkins query <host>:<port> JOB',
        '@jenkins rebuild <host>:<port> JOB',
        '@jenkins stop <host>:<port> JOB',
        '@jenkins verify <host>:<port> JOB')


class Jenkins(Trigger):
    def __init__(self, config):
        self._config = config

    def run(self, data):
        return None, True
