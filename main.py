#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from mailtrigger.argument import Argument
from mailtrigger.banner import BANNER


def main():
    print(BANNER)

    argument = Argument()
    args = argument.parse()

    if args.trigger:
        pass


if __name__ == '__main__':
    sys.exit(main())
