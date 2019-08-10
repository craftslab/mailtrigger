# -*- coding: utf-8 -*-

import poplib

from mailtrigger.mailer.receiver import Receiver, ReceiverException

MESSAGE = [
    b'Date: Jan, 01 Jan 1970 00:00:00 +0800',
    b'From: name@example.com',
    b'To: name <name@example.com>',
    b'Subject: [trigger]: subject',
    b'MIME-Version: 1.0',
    b'Content-Type: multipart/alternative; boundary="5d0f15d3_54f6eed9_ca0"',
    b'',
    b'--5d0f15d3_54f6eed9_ca0',
    b'Content-Type: text/plain; charset="utf-8"',
    b'Content-Transfer-Encoding: 7bit',
    b'Content-Disposition: inline',
    b'',
    b'content',
    b'',
    b'--5d0f15d3_54f6eed9_ca0',
    b'Content-Type: text/html; charset="utf-8"',
    b'Content-Transfer-Encoding: quoted-printable',
    b'Content-Disposition: inline',
    b'',
    b'<div>',
    b' content',
    b'</div>',
    b'--5d0f15d3_54f6eed9_ca0--'
]


class DummyServer(object):
    def __init__(self):
        global MESSAGE
        self._count = 0
        self._lines = MESSAGE
        self._mails = ['1']
        self._octets = None
        self._resp = None
        self._size = 0

    def list(self):
        return self._resp, self._mails, self._octets

    def quit(self):
        return

    def retr(self, num):
        return self._resp, self._lines, self._octets

    def stat(self):
        return self._count, self._size


def test_pop3():
    config = {
        'debug': True,
        'smtp': {
            'host': 'smtp.example.com',
            'pass': 'pass',
            'port': 465,
            'ssl': True,
            "timeout": 10,
            'user': 'user'
        }
    }

    receiver = None

    try:
        receiver = Receiver(config)
    except ReceiverException as err:
        assert str(err) == 'missing pop3 configuration'
    assert receiver is None


def test_receiver():
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

    receiver = None

    try:
        receiver = Receiver(config)
    except ReceiverException as err:
        assert str(err) == 'missing pop3 configuration'
    assert receiver is not None

    try:
        receiver.connect()
    except ReceiverException as err:
        assert str(err) == 'failed to connect pop3 server'
    finally:
        receiver._server = DummyServer()

    count = None
    size = None

    try:
        count, size = receiver.stat()
    except ReceiverException as err:
        assert str(err) == 'required to connect pop3 server'

    assert count is not None
    assert size is not None

    buf = None

    try:
        buf = receiver.receive(1)
    except ReceiverException as err:
        assert str(err) == 'required to connect pop3 server'

    if buf is None or type(buf) is str or type(buf) is list:
        assert True

    try:
        receiver.disconnect()
    except (OSError, poplib.error_proto) as _:
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

    receiver = None

    try:
        receiver = Receiver(config)
    except ReceiverException as err:
        assert str(err) == 'missing pop3 configuration'
    assert receiver is not None

    receiver._server = None

    try:
        _, _ = receiver.stat()
    except ReceiverException as err:
        assert str(err) == 'required to connect pop3 server'

    try:
        _ = receiver.receive(1)
    except ReceiverException as err:
        assert str(err) == 'required to connect pop3 server'

    assert receiver.disconnect() is None
