import praw

# REDDIT RELATED FUNCTIONS
# ------------------------------------
# returns the api object after identifying to the reddit api.
def log_on_reddit_api(REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT):
    try:
        reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,client_secret=REDDIT_CLIENT_SECRET,user_agent=REDDIT_USER_AGENT)
        print("Authentication to reddit OK")
    except:
        print("Error during authentication to reddit")
        return False
    return reddit
# returns a list of submission from the a subreddit.
def fetch_submission(subreddit, previous_post_list, banned_post_list):
    posts = []
    
    for submission in  subreddit.hot(limit=11):
        if submission not in (previous_post_list or banned_post_list):
            posts.append(
                [submission.id, submission.url]
            )
    
    return posts