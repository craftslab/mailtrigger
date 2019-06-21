# -*- coding: utf-8 -*-

from .trigger.gerrit import Gerrit
from .trigger.help import Help
from .trigger.jenkins import Jenkins
from .trigger.jira import Jira

REGISTRY = [
    {
        'class': Gerrit,
        'config': {},
        'name': Gerrit.__name__.lower()
    },
    {
        'class': Help,
        'config': {},
        'name': Help.__name__.lower()
    },
    {
        'class': Jenkins,
        'config': {},
        'name': Jenkins.__name__.lower()
    },
    {
        'class': Jira,
        'config': {},
        'name': Jira.__name__.lower()
    }
]


class Registry(object):
    def __init__(self):
        self._registry = REGISTRY

    def _set_debug(self, data):
        for index in range(len(self._registry)):
            self._registry[index]['config']['debug'] = data

    def _set_trigger(self, name, data):
        for index in range(len(self._registry)):
            if name == self._registry[index]['name']:
                buf = self._registry[index]['config'].get('debug', False)
                self._registry[index]['config'] = data
                self._registry[index]['config']['debug'] = buf

    def fill(self, config):
        for key, val in config.items():
            if key == 'debug':
                self._set_debug(val)
            else:
                self._set_trigger(key, val)

    def list(self):
        return [r['name'] for r in self._registry]

    def query(self, name):
        trigger = None
        for item in self._registry:
            if item['name'] == name:
                trigger = item
                break
        return trigger
