"""Settings for the application."""

media_folder = 'media'
submission_per_fetch = 15

subreddits = {
    'aww': '',
    'cats': ''
}

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
    'file_level': 10,
    'console_level': 10
}
