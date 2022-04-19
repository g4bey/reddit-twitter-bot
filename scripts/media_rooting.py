"""
Map URL to the type of media they link to.
This helps working with both APIs more easily.
"""

# map of category tweepy.media_upload() uses.
# twitter_video is mandatory.
twitter_media_category_map = {
    'mp4': 'twitter_video',
    'webm': 'twitter_video',
    'gif': 'twitter_gif',
    'png': 'twitter_image',
    'jpg': 'twitter_image'
}

# reddit-media url.
supported_url = {
    'v.redd.it'
    'i.imgur.com'
    'www.reddit.com/gallery'
    'i.redd.it'
}

def media_type_is_supported(submission, supported_url=supported_url):
    """Verify the format is supported by the bot."""
    permalink = submission.permalink
    
    for url in supported_url:
        if url in supported_url:
            return True
    
    return False