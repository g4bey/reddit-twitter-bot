"""Publish content from reddit to twitter."""

import settings as conf
from scripts import *
import creds
from random import choice
from pickle import dump
from pickle import load
from os import path
from os import listdir


# Create the file if it doesn't exist
# Load the list using pickle.
if path.exists(conf.saved_previous_posts):
    with open(conf.saved_previous_posts, 'rb') as file:
        previous_posts = load(file)
else:
    previous_posts = []


submissions = []


# initialiation logging.
init_logger(conf.logger)

# log on the apis.
# read the documentation for dict keys.
twitter = log_on_twitter_api(**creds.twitter)
reddit = log_on_reddit_api(**creds.reddit)


# pick and select a random subreddit.
random_subreddit = choice(list(conf.subreddits.keys()))
subreddit = reddit.subreddit(random_subreddit)


# set up the body of the tweet
tweet_body = conf.subreddits[random_subreddit]
if not tweet_body:
    tweet_body = conf.default_tweet

previous_posts = []  # debug

# fetch the submissions we're going to look through.
# excludeds stickied, unsupported media
# and previously posted media.
for submission in subreddit.hot(limit=conf.fetch_limit):
    if not submission.stickied:
        if submission.id not in (previous_posts or previous_posts):
            media_type = get_media_type_for_reddit(submission)
            if media_type:
                submission.type = media_type
                submissions.append(submission)

# media = download_from_url(submission.url, conf.media_folder, 'img')

tweet = False
for submission in submissions:
    
    args = [
        twitter, 
        submission,
        tweet_body,
        conf.media_folder
    ]
    
    if submission.type == 'image':
        tweet = tweet_image(*args)
        
    if submission.type == 'gallery':
       # tweet = tweet_gallery(*args)
       pass

    if submission.type == 'video':
        # tweet = tweet_video(*args)
        pass

    previous_posts.append(submission)
    if tweet:
        break
    break
    


# update the previous_post list.
# emptying it so the size stays constant.
# this is less to load in ram.
while len(previous_posts) > 400:
    previous_posts.pop()


# save the previous_posts list on the disk
with open(conf.saved_previous_posts, 'wb') as file:
    dump(previous_posts, file)


# note: we're going to download videos as well need.
