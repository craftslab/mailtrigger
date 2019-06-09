#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from source.argument import Argument
from source.banner import BANNER


def main():
    print(BANNER)

    argument = Argument()
    args = argument.parse()

    if args.trigger:
        pass


if __name__ == '__main__':
    sys.exit(main())
