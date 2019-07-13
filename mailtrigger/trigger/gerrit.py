# -*- coding: utf-8 -*-

import os

from .trigger import Trigger, TriggerException

PREFIX = '@gerrit '

HELP = (
    PREFIX + 'help',
    PREFIX + 'list',
    PREFIX + 'check <host>',
    PREFIX + 'restart <host>',
    PREFIX + 'start <host>',
    PREFIX + 'stop <host>',
    PREFIX + 'abandon <host> <changeid>',
    PREFIX + 'restore <host> <changeid>',
    PREFIX + 'review <host> <changeid>',
    PREFIX + 'submit <host> <changeid>'
)

LIST = (
    'localhost'
)

PORT = '29418'


class Dispatcher(object):
    def __init__(self):
        self._dispatcher = {
            'help': self._help,
            'list': self._list,
            'check': self._check,
            'restart': self._restart,
            'start': self._start,
            'stop': self._stop,
            'abandon': self._abandon,
            'restore': self._restore,
            'review': self._review,
            'submit': self._submit
        }

    @staticmethod
    def _help(self, _):
        return os.linesep.join(HELP)

    @staticmethod
    def _list(self, _):
        return os.linesep.join(LIST)

    @staticmethod
    def _check(self, msg):
        return 'Unsupported'

    @staticmethod
    def _restart(self, msg):
        return 'Unsupported'

    @staticmethod
    def _start(self, msg):
        return 'Unsupported'

    @staticmethod
    def _stop(self, msg):
        return 'Unsupported'

    @staticmethod
    def _abandon(self, msg):
        return 'Unsupported'

    @staticmethod
    def _restore(self, msg):
        return 'Unsupported'

    @staticmethod
    def _review(self, msg):
        return 'Unsupported'

    @staticmethod
    def _submit(self, msg):
        return 'Unsupported'

    def run(self, msg):
        return self._dispatcher[msg.split()[0]](msg)


class Gerrit(Trigger):
    def __init__(self, config):
        if config is None:
            raise TriggerException('invalid gerrit configuration')
        self._debug = config.get('debug', False)
        self._dispatcher = Dispatcher()
        self._filter = config.get('filter', [])
        self._server = config.get('server', [])

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

    def _run(self, content):
        lines = content.split('\n')
        msg = []
        for item in lines:
            if len(item.strip()) == 0 or item.startswith(PREFIX) is False:
                continue
            buf = item.split()
            if len(buf) < 2:
                msg.append('Invalid %s' % item)
                continue
            ret = self._dispatcher.run(buf[1:])
            msg.append(os.linesep.join([
                'Run: %s' % item,
                'Return: %s' % ret
            ]))
        return msg, True

    @staticmethod
    def help():
        return os.linesep.join(HELP)

    def run(self, event):
        if self._check(event) is False:
            return '', False
        return self._run(event['content'])
