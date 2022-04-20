"""Handle tweeting for each category."""

import logging

if __name__ == "__main__":
    from media_rooting import get_media_category_for_twitter
    from downloader import download_from_url
else:
    from .media_rooting import get_media_category_for_twitter
    from .downloader import download_from_url


def tweet(api, tweet, media_ids):
    """Send a tweet whith its respective media."""
    try:
        api.update_status(status=tweet, media_ids=media_ids)
        return True
    except Exception as e:
        # To-do: handle expression more precisely.
        logging.error('Tweeting failed.')
        return False


def create_tweet_body(submission, body):
    """Return the body of the tweet."""
    return f"{body}\n\nCredit: https://reddit.com/{submission.id}"


def tweet_image(api, submission, body, folder):
    """Tweet an image from a reddit submission."""
    category = get_media_category_for_twitter(submission.url[-3:])
    media_path = download_from_url(submission.url, folder, 'img')

    # prepare the content for the tweet.
    media = api.media_upload(filename=media_path, media_category=category)
    tweet_body = create_tweet_body(submission, body)

    # try tweeting. 0 if failed.
    return tweet(api, tweet_body, [media.media_id_string])


def tweet_video(api, submission, body, folder):
    """Tweet a video from a reddit submission."""
    category = get_media_category_for_twitter(submission)

    pass


def tweet_gallery(api, submission, body, folder):
    """Tweet a gallery from a reddit submission."""
    category = get_media_category_for_twitter('gallery')
    media_metadata = submission.media_metadata.items()
    media_ids = []
    
    tweet_body = create_tweet_body(submission, body)
    
    for i, image in enumerate(media_metadata):
        if i < 4:
            image_url = image[1]['p'][0]['u']
            image_url = image_url.split("?")[0].replace("preview", "i")
            media_path = download_from_url(image_url, folder, f"img{i+1}")
            media = api.media_upload(filename=media_path, media_category=category)
            media_ids.append(media.media_id)
        else: break
    return tweet(api, tweet_body, media_ids)
