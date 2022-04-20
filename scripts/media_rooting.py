"""
Map URL to the type of media they link to.

This helps working with both APIs more easily.
"""

# map of category tweepy.media_upload() uses.
# twitter_video is mandatory.
twitter_media_category_map = {
    'mp4': 'tweet_video',
    'gif': 'tweet_gif',
    'png': 'tweet_image',
    'jpg': 'tweet_image',
    'gallery': 'tweet_image'
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


def get_media_category_for_twitter(format,
                                   media_map=twitter_media_category_map):
    """Return the category of supported medias for twitter/upload."""

    if media_map[format]:
        return media_map[format]

    return False
