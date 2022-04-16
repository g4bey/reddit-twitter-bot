from settings import *
from functions.files_manager import *
from functions.media_downloader import *
from functions.reddit_api import *
from functions.twitter_api import *
from creds import *

# ------------------------------------

def tweet_first(submissions, media_folder, tweet_body):
    for submission in submissions:
        empty_folder(media_folder)
        
        metadata = media_rooter(submission)
        media_downloader(metadata, media_folder)

        tweet = build_tweet(tweet_body, media_folder)
        send_tweet(twitter_api, tweet)

# ------------------------------------

# This is queue. We only fetch top posts hence why we will only save the last 400 ids.
previous_post_list = [0] * 400 

reddit_api = log_on_reddit_api(REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT)
twitter_api = log_on_twitter_api(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

if not reddit_api or not twitter_api:
    exit('Could not connect to APIs.')

# ------------------------------------

i_max = len(subreddit_list) - 1 # maximum possible index

# using the modulo provides the index a natural rotation.
try: current_i = fetch_state(fSTATE) % (i_max)
except (FileNotFoundError, TypeError):
    create_state_file(fSTATE)   
    current_i = 0

subreddit_name = subreddit_list[current_i][0]
subreddit = reddit_api.subreddit(subreddit_name)
submissions = fetch_submission(subreddit, previous_post_list, banned_post_list, 3)

tweet_first(submissions, fMEDIA_FOLDER, subreddit_list[fSTATE])

increment_state(fSTATE)
