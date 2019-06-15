#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time

from mailtrigger.argument import Argument
from mailtrigger.banner import BANNER
from mailtrigger.logger.logger import Logger
from mailtrigger.mailer.receiver import Receiver, ReceiverException
from mailtrigger.mailer.sender import Sender, SenderException
from mailtrigger.registry import REGISTRY
from mailtrigger.scheduler.scheduler import Scheduler, SchedulerException
from mailtrigger.trigger.trigger import TriggerException

MAILER = 'mailtrigger/config/mailer.json'
SCHEDULER = 'mailtrigger/config/scheduler.json'
TRIGGER = 'mailtrigger/config/trigger.json'


def _format(data, content):
    return {
        'content': '\n'.join((
            content,
            '%s' % ('-'*80),
            '> From: %s' % data['from'],
            '> To: %s' % data['to'],
            '> Subject: %s' % data['subject'],
            '> Date: %s' % data['date'],
            '>',
            '> Content: %s' % data['content'])),
        'date': time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())),
        'from': data['to'],
        'subject': 'Re: %s' % data['subject'],
        'to': data['from']
    }


def _emit(data, sender, triggers):
    """TODO"""


def _help(data, sender, triggers):
    buf = []
    for item in triggers:
        buf.append('@%s help' % item)
    sender.send(_format(data, os.linesep.join(buf)))


def _trigger(data, sender, triggers):
    for item in data:
        t = item.split()[0].lstrip('@').strip()
        if t == 'help':
            _help(data, sender, triggers)
        else:
            _emit(item, sender, triggers)


def _unpack(data):
    buf = []
    lines = data['content'].splitlines()

    for item in lines:
        if len(item.strip()) != 0:
            data['content'] = item.strip()
            buf.append(data)

    return buf


def _retrieve(receiver):
    return receiver.retrieve()


def _job(args):
    receiver, sender, triggers = args
    data = _retrieve(receiver)
    if data is not None and len(data) != 0:
        data = _unpack(data)
        _trigger(data, sender, triggers)


def _scheduler(sched, receiver, sender, triggers):
    sched.add(_job, [receiver, sender, triggers], '_job')

    while True:
        sched.run()
        time.sleep(1)


def main():
    print(BANNER)

    argument = Argument()
    args = argument.parse()

    triggers = args.trigger.split(',')
    buf = list(set(triggers) - set([r['name'] for r in REGISTRY]))
    if len(buf) != 0:
        Logger.error('invalid trigger %s' % ','.join(buf))
        return -1

    try:
        sched = Scheduler(os.path.join(os.path.dirname(__file__), SCHEDULER))
    except SchedulerException as e:
        Logger.error(str(e))
        return -2

    receiver = None
    sender = None

    try:
        receiver = Receiver(os.path.join(os.path.dirname(__file__), MAILER))
        receiver.connect()
        sender = Sender(os.path.join(os.path.dirname(__file__), MAILER))
        sender.connect()
    except (ReceiverException, SenderException) as e:
        Logger.error(str(e))
        sender.disconnect()
        receiver.disconnect()
        sched.stop()
        return -3

    ret = 0

    try:
        _scheduler(sched, receiver, sender, triggers)
    except (SchedulerException, ReceiverException, SenderException, TriggerException) as e:
        Logger.error(str(e))
        ret = -4
    finally:
        sender.disconnect()
        receiver.disconnect()
        sched.stop()

    return ret


if __name__ == '__main__':
    sys.exit(main())
