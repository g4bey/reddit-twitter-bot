"""Handle every function related to te reddit api."""

import praw
from prawcore.exceptions import PrawcoreException

# REDDIT RELATED FUNCTIONS
# ------------------------------------


def log_on_reddit_api(
        REDDIT_CLIENT_ID,
        REDDIT_CLIENT_SECRET,
        REDDIT_USER_AGENT):
    """Returns the api object after identifying to the reddit api."""
    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT)
    try:
        test_connection(reddit)
        print("Authentication to reddit OK")
    except PrawcoreException:
        print("Error during authentication to reddit")
        return False
    return reddit


def fetch_submission(
        subreddit,
        previous_post_list,
        banned_post_list,
        limit=10):
    """Returns a list of submission from the a subreddit."""
    posts = []
    try:
        for submission in subreddit.hot(limit=limit):
            if submission.stickied == False:
                if submission not in (previous_post_list or banned_post_list):
                    try: 
                        media_metadata = submission.media_metadata.items()
                    except AttributeError:
                        media_metadata = {}
                    posts.append(
                        {
                            'id': submission.id,
                            'url': submission.url,
                            'permalink': submission.permalink,
                            'media_metadata': media_metadata
                        }
                    )
    except PrawcoreException as e:
        print(e)

    return posts


def test_connection(reddit_api):
    """Make request for basic error management."""
    submission = reddit_api.submission(id="39zje0").title
