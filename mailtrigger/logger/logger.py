# -*- coding: utf-8 -*-

import colorama
import sys


class Logger(object):
    def __init__(self):
        pass

    @staticmethod
    def debug(msg):
        sys.stderr.write(u'{debug}DEBUG:{reset} {msg}\n'.format(
            debug=colorama.Fore.GREEN + colorama.Style.BRIGHT,
            reset=colorama.Style.RESET_ALL,
            msg=msg))

    @staticmethod
    def error(msg):
        sys.stderr.write(u'{error}ERROR:{reset} {msg}\n'.format(
            error=colorama.Fore.RED + colorama.Style.BRIGHT,
            reset=colorama.Style.RESET_ALL,
            msg=msg))

    @staticmethod
    def info(msg):
        sys.stderr.write(u'{info}info:{reset} {msg}\n'.format(
            info=colorama.Fore.WHITE + colorama.Style.BRIGHT,
            reset=colorama.Style.RESET_ALL,
            msg=msg))

    @staticmethod
    def warn(msg):
        sys.stderr.write(u'{warn}WARN:{reset} {msg}\n'.format(
            warn=colorama.Fore.YELLOW + colorama.Style.BRIGHT,
            reset=colorama.Style.RESET_ALL,
            msg=msg))
