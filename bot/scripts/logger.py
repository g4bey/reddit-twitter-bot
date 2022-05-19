"""Set-up the logger for the project"""

from os import path, makedirs
import logging


def create_if_missing(folder: str) -> None:
    """Create folder if non-existent"""

    if not path.exists(folder):
        makedirs(folder)


def init_logger(conf: dict) -> None:
    """Initialise the logging system."""

    log_folder = conf['file'] or 'logs'
    name = conf['name']
    file_level = conf['file_level']
    console_level = conf['console_level']

    create_if_missing(log_folder)

    logger = logging.getLogger()

    logger.setLevel(file_level)

    files = logging.FileHandler(
        filename=f'{log_folder}/{name}.log',
        encoding='utf-8',
        mode='w'
    )

    files.setFormatter(logging.Formatter(
        '%(asctime)s:%(levelname)s:%(name)s: %(message)s')
    )

    logger.addHandler(files)

    console = logging.StreamHandler()

    console.setLevel(console_level)

    console.setFormatter(logging.Formatter(
        '%(asctime)s:%(levelname)s:%(name)s: %(message)s')
    )

    logger.addHandler(console)
