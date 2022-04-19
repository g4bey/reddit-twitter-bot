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
reddit_media_map = {
    'v.redd.it': "video",
    'i.imgur.com': "image",
    'www.reddit.com/gallery': "gallery",
    'i.redd.it' : "image"
}

def media_type_is_supported(submission, media_map=reddit_media_map):
    """Verify the format is supported by the bot."""
    url = submission.url
    
    for media in media_map.keys():
        if media in url:
            return True
    
    return False



