"""Publish content from reddit to twitter."""

import logging
from random import choice
import creds
from scripts import *
import settings as conf



# initialiation logging.
init_logger(conf.logger)

#log on the apis.
# read the documentation for dict keys.
log_on_twitter_api(**creds.twitter)
log_on_reddit_api(**creds.reddit)


# picks a random subreddit.
subreddit = choice(list(conf.subreddits.keys()))
logging.debug('test')