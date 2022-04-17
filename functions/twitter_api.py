import tweepy

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


def build_tweet(body, media_folder):
    """Return a valid tweet."""
    pass


def send_tweet(api, tweet):
    """Send the tweet once built."""
    media = api.media_upload(tweet.path_picture)
    post_result = api.update_status(
        status=tweet['body'], media_ids=[
            media.media_id])

    print('We successfully tweeted')
