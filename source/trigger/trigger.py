# -*- coding: utf-8 -*-

import abc


class Trigger(object):
    __metaclass__ = abc.ABCMeta

    @staticmethod
    @abc.abstractmethod
    def help():
        return None

    @staticmethod
    @abc.abstractmethod
    def parse(event):
        return True

    @abc.abstractmethod
    def send(self, event):
        return None
