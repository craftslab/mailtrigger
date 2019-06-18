# -*- coding: utf-8 -*-

from .trigger import Trigger

HELP = ('Jira Trigger'
        ''
        'TBD')


class Jira(Trigger):
    def __init__(self):
        pass

    def send(self, event):
        if event == 'help':
            return HELP, True

        return None, False
