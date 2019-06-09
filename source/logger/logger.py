# -*- coding: utf-8 -*-

import colorama
import json
import os
import sys

CONFIG = '../config/config.json'


class Logger(object):
    def __init__(self):
        pass

    @staticmethod
    def debug(msg):
        def _load(name):
            with open(name, 'r') as f:
                data = json.load(f)
            return data.get('debug', False)
        debug = _load(os.path.join(os.path.dirname(__file__), CONFIG))
        if debug is False:
            return
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
