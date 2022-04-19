"""Provide functions to connect to respective APIS"""

from tweepy import OAuthHandler
from tweepy import API
from praw import Reddit
from prawcore.exceptions import PrawcoreException
import logging


def log_on_twitter_api(
        consumer_key, consumer_secret,
        access_token, access_token_secret):
    """Log on the twitter api."""
    auth = OAuthHandler(consumer_key, consumer_secret, 
                               access_token, access_token_secret)

    return API(auth, wait_on_rate_limit=True)


def verify_twitter_credentials(api):
    """Verify that the twitter api credentials are up to date."""
    try:
        api.verify_credentials()
        logging.info('Connection to twitter: OK')
    except BaseException:
        logging.warning(f"Connection to twitter: FAILED")
        return False
    return True


def log_on_reddit_api(
        client_id,
        client_secret,
        user_agent):
    """Returns the api object after identifying to the reddit api."""
    reddit = Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent)
    try:
        test_connection(reddit)
        logging.info('Connection to reddit: OK')
    except PrawcoreException:
        logging.warning(f"Connection to reddit: FAILED")
        return False
    return reddit


def test_connection(reddit_api):
    """Make request for basic error management."""
    submission = reddit_api.submission(id="39zje0").title
