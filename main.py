"""Publish content from reddit to twitter."""

import settings as conf
from scripts import *
import creds
from random import choice



previous_posts = []  # temporary
submissions = []


# initialiation logging.
init_logger(conf.logger)

# log on the apis.
# read the documentation for dict keys.
twitter = log_on_twitter_api(**creds.twitter)
reddit = log_on_reddit_api(**creds.reddit)


# pick and select a random subreddit.
random_subreddit = choice(list(conf.subreddits.keys()))
subreddit = reddit.subreddit(random_subreddit)



# fetch the submissions we're going to look through.
# excludeds stickied, unsupported media
# and previously posted media.
for submission in subreddit.hot(limit=conf.fetch_limit):
    if not submission.stickied and media_type_is_supported(submission):
        if submission.id not in (previous_posts or previous_posts):
                submissions.append(submission)

print(submissions)