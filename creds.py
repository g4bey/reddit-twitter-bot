"""Credentials."""

import os

twitter = {
    "consumer_key": os.getenv('consumer_key'),
    "consumer_secret": os.getenv('consumer_secret'),
    "access_token": os.getenv('access_token'),
    "access_token_secret": os.getenv('access_token_secret')
}

reddit = {
    "client_id": os.getenv('client_id'),
    "client_secret": os.getenv('client_secret'),
    "user_agent": os.getenv('user_agent')
}
