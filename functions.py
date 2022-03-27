import praw, tweepy, pickle


# PROGRAMME STATE RELATED FUNCTIONS
# ------------------------------------
# returns the state of the program.
def fetch_state(file) -> int:
    with open(file, 'r') as f:
        val = f.read()
        if val: return int(val)

# increment the state of the program
def increment_state(file) -> None:
    current_state = fetch_state(file)
    with open(file, 'w') as f:
        next_state = str(current_state + 1)
        f.write(next_state)

# create the file and append a 0
def create_state_file(file) -> None:
    with open(file, 'w+') as f:
        f.write(str(0))




    
# PREVIOUS POST LIST RELATED FUNCTIONS
# ------------------------------------
# verify if the thread is the previous_postList
def has_been_posted(threadId, previous_post_list) -> bool:
    if threadId in previous_post_list: 
        return True
    
    return False

# update the previous post list. we're using a queue as we only fetch top threads. 
# Given a few days, it's sure they've never been posted.
def update_post_list(threadId, previous_post_list):
    previous_post_list.pop()
    previous_post_list.append(threadId)
    return previous_post_list

# overwrite the previous_post_file with a given list. 
def update_previous_posts_file(fPREVIOUS_POSTS, previous_post_list):
    with open(fPREVIOUS_POSTS, 'wb') as file:
        pickle.dump(previous_post_list, file)





# TWITTER RELATED FUNCTIONS
# ------------------------------------
# log on the twitter api.
def log_on_twitter_api(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    return tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)

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

def fetch_submission(subreddit, previous_post_list):
    posts = []
    
    for submission in  subreddit.get_hot(limit=10):
        if submission not in previous_post_list:
            posts.append(
                [submission.id, submission.title, submission.permalink, submission.url]
            )
    
    return posts
