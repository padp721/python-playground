import logging
import os
import sys

LOG_FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s : %(message)s")


def get_console_handler() -> logging.StreamHandler:
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(LOG_FORMATTER)
    return console_handler


def get_file_handler(log_file_location: str) -> logging.FileHandler:
    log_dir = log_file_location.split('/')
    del log_dir[-1]
    log_dir = '/'.join(log_dir)

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    file_handler = logging.FileHandler(
        filename=log_file_location,
        mode='a',
        encoding='utf8'
    )
    file_handler.setFormatter(LOG_FORMATTER)
    return file_handler


def setup_logging(
        logger_name: str = 'unit_testing',
        logger_level=logging.NOTSET,
        logger_file: str = ''
):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logger_level)
    logger.addHandler(get_console_handler())
    if logger_file != '':
        logger.addHandler(get_file_handler(logger_file))


def get_logger(logger_name: str = 'unit_testing') -> logging.Logger:
    return logging.getLogger(logger_name)
