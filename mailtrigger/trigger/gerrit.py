# -*- coding: utf-8 -*-

from .trigger import Trigger

HELP = ('@gerrit help',
        '@gerrit list',
        '@gerrit restart <host>',
        '@gerrit start <host>',
        '@gerrit stop <host>',
        '@gerrit verify <host>',
        '',
        '',
        '@gerrit review <host>:<port>',
        '  [--project <PROJECT> | -p <PROJECT>]',
        '  [--branch <BRANCH> | -b <BRANCH>]',
        '  [--message <MESSAGE> | -m <MESSAGE>]',
        '  [--notify <NOTIFYHANDLING> | -n <NOTIFYHANDLING>]',
        '  [--submit | -s]',
        '  [--abandon | --restore]',
        '  [--rebase]',
        '  [--move <BRANCH>]',
        '  [--publish]',
        '  [--json | -j]',
        '  [--delete]',
        '  [--verified <N>] [--code-review <N>]',
        '  [--label Label-Name=<N>]',
        '  [--tag TAG]',
        '  {COMMIT | CHANGEID,PATCHSET}')


class Gerrit(Trigger):
    def __init__(self, config):
        self._config = config

    def run(self, data):
        return None, True
