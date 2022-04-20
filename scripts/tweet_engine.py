"""Handle tweeting for each category."""

import logging

if __name__ == "__main__":
    from media_rooting import get_media_category_for_twitter
    from downloader import download_from_url 
else:
    from .media_rooting import get_media_category_for_twitter
    from .downloader import download_from_url


def tweet_image(api, submission, body, folder):
    """Tweet an image from a reddit submission."""
    category = get_media_category_for_twitter(submission)
    media_path = download_from_url(submission.url, folder, 'img')
    media = api.media_upload(filename=media_path, media_category=category)
    tweet =  f"{body}\n\nCredit: {submission.url}"
    
    try:
        api.update_status(status=tweet, media_ids=[media.media_id])
        return True
    except Exception as e:
        logging.error('Tweeting failed.') # To-do: handle expression more precisely.
        return False
    
    
def tweet_video(submission):
    """Tweet a video from a reddit submission."""
    category = get_media_category_for_twitter(submission)
    
    pass

def tweet_gallery(submission):
    """Tweet a gallery from a reddit submission."""
    category = get_media_category_for_twitter(submission)
    
    pass