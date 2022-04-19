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
    'i.redd.it': "image"
}


def get_media_type_for_reddit(submission, media_map=reddit_media_map):
    """Verify the format is supported and return its category."""
    url = submission.url

    for media, media_type in media_map.items():
        if media in url:
            return media_type

    return False
