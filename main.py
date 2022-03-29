from settings import *
from functions import *
from creds import *
import tweepy
import praw

# ------------------------------------

# This is queue. We only fetch top posts hence why we will only save the last 400 ids.
previous_post_list = [0] * 400 


reddit_api = log_on_reddit_api(REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT)

# ------------------------------------

# maximum possible index
i_max = len(subreddit_list) - 1

# 542 % 5 = 2...  543 % 5 = 3...  544 % 5 = 4...  545 % 5 = 0
# using the modulo provides the index a natural rotation.
try:
    current_i = fetch_state(fSTATE) % (i_max)
except (FileNotFoundError, TypeError):
    create_state_file(fSTATE)   
    current_i = 0

subreddit = reddit_api.subreddit(subreddit_list[current_i])



# program
# program
# program

increment_state(fSTATE)
