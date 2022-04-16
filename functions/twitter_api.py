import tweepy

# TWITTER RELATED FUNCTIONS
# ------------------------------------
# log on the twitter api.
def log_on_twitter_api(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    return tweepy.API(auth, wait_on_rate_limit=True)

# verify that the twitter api credentials are up to date.
def verify_twitter_credentials(api):
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
        return False
    return True
# build the tweet as a dictionarry.
def build_tweet():
    pass
# send the tweet once built
def send_tweet(api, tweet):
    media = api.media_upload(tweet.path_picture)
    post_result = api.update_status(status=tweet.body, media_ids=[media.media_id])

    print('We successfully tweeted')