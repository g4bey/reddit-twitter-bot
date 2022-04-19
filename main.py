"""Publish content from reddit to twitter."""

import logging
import settings as conf
from random import choice
from scripts import init_logger

# initialiation logging.
init_logger(conf.logger)


# picks a random subreddit.
subreddit = choice(list(conf.subreddits.keys()))
logging.debug('test')