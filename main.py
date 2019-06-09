#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from source.argument import Argument
from source.mail.receiver import Receiver, ReceiverException
from source.mail.sender import Sender, SenderException
from source.trigger.trigger import Trigger


def main():
    argument = Argument()
    args = argument.parse()

    if args.trigger:
        pass


if __name__ == '__main__':
    sys.exit(main())
