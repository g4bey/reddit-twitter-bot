"""Handle every function related to the twitter api."""

import tweepy
from os import listdir

# TWITTER RELATED FUNCTIONS
# ------------------------------------


def log_on_twitter_api(
        CONSUMER_KEY, CONSUMER_SECRET,
        ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
    """Log on the twitter api."""
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    return tweepy.API(auth, wait_on_rate_limit=True)


def verify_twitter_credentials(api):
    """Verify that the twitter api credentials are up to date."""
    try:
        api.verify_credentials()
        print("Authentication OK")
    except BaseException:
        print("Error during authentication")
        return False
    return True


def build_tweet(body, post_id, media_folder):
    """
    Return the tweet and path to medias.

    The url is shorttened in the process.
    """
    link = f"https://reddit.com/{post_id}"
    tweet = f"""{body}
           Credit: {link}"""

    if len(tweet) <= 280:
        return {
            "tweet": tweet,
            "media": listdir(media_folder)
        }


def send_tweet(api, tweet):
    """Send the tweet once built."""
    media = api.media_upload(tweet.path_picture)
    post_result = api.update_status(
        status=tweet['body'], media_ids=[
            media.media_id])

    print('We successfully tweeted')
