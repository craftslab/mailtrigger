# -*- coding: utf-8 -*-

import smtplib
import time

from mailtrigger.mailer.sender import Sender, SenderException


class DummyServer(object):
    def __init__(self):
        pass

    def quit(self):
        return

    def sendmail(self, from_addr, to_addrs, msg):
        return


def test_smtp():
    config = {
        'debug': True,
        'pop3': {
            'host': 'pop.example.com',
            'pass': 'pass',
            'port': 995,
            'ssl': True,
            "timeout": 10,
            'user': 'user'
        }
    }

    sender = None

    try:
        sender = Sender(config)
    except SenderException as e:
        assert str(e) == 'missing smtp configuration'
    assert sender is None


def test_sender():
    config = {
        'debug': True,
        'pop3': {
            'host': 'pop.example.com',
            'pass': 'pass',
            'port': 995,
            'ssl': True,
            "timeout": 10,
            'user': 'user'
        },
        'smtp': {
            'host': 'smtp.example.com',
            'pass': 'pass',
            'port': 465,
            'ssl': True,
            "timeout": 10,
            'user': 'user'
        }
    }

    data = {
        'content': '@help',
        'date': time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())),
        'from': 'name@example.com',
        'subject': '[trigger]',
        'to': 'name@example.com'
    }

    msg = {
        'content': '\n'.join((
            'pytest',
            '%s' % ('-'*80),
            '> From: %s' % data['from'],
            '> To: %s' % data['to'],
            '> Subject: %s' % data['subject'],
            '> Date: %s' % data['date'],
            '> Content: %s' % data['content'])),
        'date': time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())),
        'from': data['to'],
        'subject': 'Re: %s' % data['subject'],
        'to': data['from']
    }

    sender = None

    try:
        sender = Sender(config)
    except SenderException as e:
        assert str(e) == 'missing smtp configuration'
    assert sender is not None

    try:
        sender.connect()
    except SenderException as e:
        assert str(e) == 'failed to connect smtp server'
    finally:
        sender._server = DummyServer()

    try:
        sender.send(msg)
    except SenderException as e:
        assert str(e) == 'required to connect smtp server'

    try:
        sender.disconnect()
    except (OSError, smtplib.SMTPException) as _:
        assert True


def test_server():
    config = {
        'debug': True,
        'pop3': {
            'host': 'pop.example.com',
            'pass': 'pass',
            'port': 995,
            'ssl': True,
            "timeout": 10,
            'user': 'user'
        },
        'smtp': {
            'host': 'smtp.example.com',
            'pass': 'pass',
            'port': 465,
            'ssl': True,
            "timeout": 10,
            'user': 'user'
        }
    }

    sender = None

    try:
        sender = Sender(config)
    except SenderException as e:
        assert str(e) == 'missing smtp configuration'
    assert sender is not None

    sender._server = None

    try:
        sender.send(None)
    except SenderException as e:
        assert str(e) == 'required to connect smtp server'

    try:
        sender.disconnect()
    except (OSError, smtplib.SMTPException) as _:
        assert True
