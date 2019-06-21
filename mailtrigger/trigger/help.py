# -*- coding: utf-8 -*-

from .trigger import Trigger

HELP = ('TBD',
        '')


class Help(Trigger):
    def __init__(self, config):
        self._config = config

    def run(self, data):
        return None, True
