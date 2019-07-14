# -*- coding: utf-8 -*-

import os

from .trigger import Trigger, TriggerException

PREFIX = '@jenkins '

HELP = (
    PREFIX + 'help',
    PREFIX + 'list',
    PREFIX + 'list <host>:<port>',
    PREFIX + 'version <host>:<port>',
    PREFIX + 'build <host>:<port> <job>',
    PREFIX + 'check <host>:<port> <job>',
    PREFIX + 'query <host>:<port> <job>',
    PREFIX + 'rebuild <host>:<port> <job>',
    PREFIX + 'stop <host>:<port> <job>'
)


class Jenkins(Trigger):
    def __init__(self, config):
        if config is None:
            raise TriggerException('invalid jenkins configuration')
        self._debug = config.get('debug', False)
        self._filter = config.get('filter', None)

    def _check(self, event):
        def _check_helper(data, event):
            if event is None:
                return False
            sender = data.get('from', None)
            if sender is None or event['from'] != sender:
                return False
            subject = data.get('subject', '').strip()
            if len(subject) == 0 or event['subject'].startswith(subject) is False:
                return False
            return True
        ret = False
        for item in self._filter:
            if _check_helper(item, event) is True:
                ret = True
                break
        return ret

    @staticmethod
    def help():
        return os.linesep.join(HELP)

    def run(self, event):
        if self._check(event) is False:
            return '', False
        return '', False
