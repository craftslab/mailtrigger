# -*- coding: utf-8 -*-

from mailtrigger.logger.logger import Logger


def test_logger(capsys):
    logger = Logger()

    logger.debug('debug')
    captured = capsys.readouterr()
    assert 'debug\n' in captured.err

    logger.error('error')
    captured = capsys.readouterr()
    assert 'error\n' in captured.err

    logger.info('info')
    captured = capsys.readouterr()
    assert 'info\n' in captured.err

    logger.warn('warn')
    captured = capsys.readouterr()
    assert 'warn\n' in captured.err
