"""Handle every function related to the twitter api."""

import tweepy
from os import listdir
from time import sleep

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
    tweet = f"""{body}\n\nCredit: {link}"""

    if len(tweet) <= 280:
        return {
            "tweet": tweet,
            "media": listdir(media_folder)
        }


def get_media_category(file):
    """Map format to media categories."""
    format = file[-3:]

    if format == 'mp4':
        return 'tweet_video'
    elif format == 'gif':
        return 'tweet_gif'

    return 'tweet_image'


def wait_for_processing(twitter_api, media_id):
    """Wait for videos de be processed."""
    while True:
        r = twitter_api.get_media_upload_status(media_id)
        state = r.processing_info['state']
        print('media upload status: ', state)
        if state == 'failed':
            print(r.processing_info['error'])
            return 0
        if state == 'succeeded':
            return 1
        else:
            sleep(10)


def send_tweet(api, tweet, media_folder):
    """Send the tweet once built."""
    media_ids = []
    for file in tweet['media']:
        category = get_media_category(file)
        media = api.media_upload(
            f"{media_folder}/{file}",
            media_category=category)
        media_ids.append(media.media_id)

        if category == 'tweet_video':
            if not wait_for_processing(api, media.media_id):
                return 0

    try:
        api.update_status(status=tweet['tweet'], media_ids=media_ids)
        print('We successfully tweeted')
    except BaseException:
        return 0
    return True
