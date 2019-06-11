# -*- coding: utf-8 -*-

from .trigger import Trigger


class Jira(Trigger):
    @staticmethod
    def help():
        return ('Jira Trigger'
                ''
                'TBD')

    @staticmethod
    def parse(event):
        return False

    def send(self, event):
        return None
