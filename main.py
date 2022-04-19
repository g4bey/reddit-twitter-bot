from settings import *
from functions.files_manager import *
from functions.media_downloader import *
from functions.reddit_api import *
from functions.twitter_api import *
from creds import *


reddit_api = log_on_reddit_api(
    REDDIT_CLIENT_ID,
    REDDIT_CLIENT_SECRET,
    REDDIT_USER_AGENT)
twitter_api = log_on_twitter_api(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET)

if not reddit_api or not twitter_api:
    exit('Could not connect to APIs.')


i_max = len(subreddit_list) - 1  # maximum possible index


try:
    # modulo provides a natural rotation.
    current_i = fetch_state(fSTATE) % (i_max)
except (FileNotFoundError, TypeError):
    create_state_file(fSTATE)
    current_i = 0
    
try:
    previous_post_list = load_previous_posts_file(fPREVIOUS_POSTS)
except (FileNotFoundError):
    update_previous_posts_file(fPREVIOUS_POSTS, [])
    previous_post_list = []

subreddit_name = subreddit_list[current_i][0]
subreddit = reddit_api.subreddit(subreddit_name)
submissions = fetch_submission(
    subreddit,
    previous_post_list,
    banned_post_list,
    submission_to_fetch)



for submission in submissions:
    empty_folder(fMEDIA_FOLDER)
    metadata = media_rooter(submission)
        
    if metadata['type'] == 'unsuported':
        break
    
    media_downloader(metadata, fMEDIA_FOLDER)

    body = subreddit_list[current_i][1]
    if not body:
        body = default_tweet_body

    tweet = build_tweet(body, submission['id'], fMEDIA_FOLDER)
    previous_post_list = update_post_list(submission['id'], previous_post_list)
    if send_tweet(twitter_api, tweet, fMEDIA_FOLDER):
        update_previous_posts_file(fPREVIOUS_POSTS, previous_post_list)
        break

increment_state(fSTATE)
