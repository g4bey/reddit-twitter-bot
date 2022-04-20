"""Load utilities."""

import logging


def init_logger(conf):
    """Initialise the logging system.

    the conf dictionnary should have:
        file_level
        console_level
    as attributes.
    """
    logging.basicConfig(filename=conf['file'], encoding='utf-8',
                        level=conf['file_level'], filemode='a',
                        format='%(name)s - %(levelname)s - %(message)s')

    console = logging.StreamHandler()
    console.setLevel(conf['console_level'])
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
