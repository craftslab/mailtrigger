# -*- coding: utf-8 -*-

from .trigger import Trigger


class Gerrit(Trigger):
    @staticmethod
    def help():
        return 'TBD'

    @staticmethod
    def parse(event):
        return False

    def send(self, event):
        return None
