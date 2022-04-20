"""Handle tweeting for each category."""

import logging
from ffmpeg import input
from ffmpeg import output
from time import sleep


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
    category = get_media_category_for_twitter('mp4')
    audio_path =  download_from_url(f"{submission.url}/DASH_audio.mp4", folder, 'audio')
    
    # prepare the content for the tweet.
    tweet_body = create_tweet_body(submission, body)
    
    if audio_path:
        audio_stream = input(audio_path)

    for resolution in ['720', '480', '360', '240', '144']:
        video_path = download_from_url(f"{submission.url}/DASH_{resolution}.mp4", folder, 'video_m')

        # if not video path, we look for lower resolution.
        if video_path:
            
            video_stream = input(video_path)
            if(audio_path):
                video_stream = input(video_path)
                media_path = f"{folder}/video.mp4" # new path.
                output(audio_stream, video_stream, media_path).run(quiet=True, overwrite_output=True)
            else: 
                media_path = video_path 
            media = api.media_upload(filename=media_path, media_category=category)
            
            # gotta for twitter to process the media
            if not wait_for_processing(api, media.media_id):
                return 0
            else: 
                logging.info('tweeting')
                return tweet(api, tweet_body, [media.media_id])



def tweet_gallery(api, submission, body, folder):
    """Tweet a gallery from a reddit submission."""
    category = get_media_category_for_twitter('gallery')
    media_metadata = submission.media_metadata.items()
    media_ids = []
    
    # prepare the content for the tweet.
    tweet_body = create_tweet_body(submission, body)
    
    # Select the firt fouth image.
    for i, image in enumerate(media_metadata):
        if i < 4:
            image_url = image[1]['p'][0]['u']
            image_url = image_url.split("?")[0].replace("preview", "i")
            media_path = download_from_url(image_url, folder, f"img{i+1}")
            media = api.media_upload(filename=media_path, media_category=category)
            media_ids.append(media.media_id)
        else: break
    return tweet(api, tweet_body, media_ids)



def wait_for_processing(api, media_id):
    """Wait for videos de be processed."""
    while True:
        r = api.get_media_upload_status(media_id)
        print('processing')
        state = r.processing_info['state']
        logging.info(f"media upload status: {state}")
        if state == 'failed':
            logging.error(r.processing_info['error'])
            return 0
        if state == 'succeeded':
            return 1
        else:
            print('sleeping')
            logging.info('Sleeping for 10 seconds.')
            sleep(10)
