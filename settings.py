"""Settings for the application."""

media_folder = 'media'
submission_per_fetch = 15

default_tweet = 'Your hourly dose of cute has arrived!'

excluded_flair = ['Advise', 'Human']

subreddits = {
    'cats': ''
}

fetch_limit = 20

banned_post = []


"""
Levels:
    + CRITICAL: 50
    + ERROR: 40
    + WARNING: 30
    + INFO: 20
    + DEBUG: 10
    + NOTSET: 0
"""
logger = {
    'file': 'default-log.log',
    'file_level': 30,
    'console_level': 10
}
