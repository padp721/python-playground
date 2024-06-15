import logging
import os
import shutil

from unit_testing.logging import config


def test_get_logger():
    assert isinstance(config.get_logger(), logging.Logger)


def test_setup_logging():
    log_file = 'tests/logs/app.log'
    log_dir = log_file.split('/')
    del log_dir[-1]
    log_dir = '/'.join(log_dir)

    if os.path.exists(log_dir):
        shutil.rmtree(log_dir)

    config.setup_logging(
        logger_level=logging.DEBUG,
        logger_file=log_file
    )
    logger = config.get_logger()
    assert logger.level == logging.DEBUG
