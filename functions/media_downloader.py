from urllib.parse import urlparse
from requests import get
from ffmpeg import input, output

# DOWNLOADING MEDIAS
# ------------------------------------
# download an image from an url.
def download_image(link, media_folder):
    pass
# download multiple image from a list
def download_multiple_image(links, media_folder):
    pass
# download 
def download_video(video, audio, media_folder):
    pass

# FETCHING LINKS
# ------------------------------------
# explore reddit gallery and return links to media
def gallery_explorer(sumission, max=4):
    # access post.media_metadata.items():
    # return all the link in a dict.
    pass
# explore reddit video and return links to the right stream.
def video_explorer(submission, max=512):
    # access audio stream. 
    # access video stream (trying 360, 480 & 720)
    # return all the link in a dict.
    pass

# ROOTING
# ------------------------------------
# returns links to the media.
def media_rooter(submission):
    hostame = urlparse(submission['url']).hostname
    path = urlparse(submission['url']).hostname
    
    if hostame and hostame.endswith('v.redd.it'):
        return {
            'type': 'video',
            'audio': 'tbd',
            'video': video_explorer(submission)
        }
    elif hostame and hostame.endswith('i.redd.it'):
        return {
            'type': 'image',
            'link': hostame
        }
    elif hostame and hostame.endswith('i.imgur.com'):
        return {
            'type': 'image',
            'link': hostame
        }
    elif path and path.startswith('/gallery'):
        return {
            'type': 'gallery',
            'link': gallery_explorer(submission)
        }
    else:
        return {
            'type': 'unsupported',
            'error': f"{hostame} is unsupported"
        }
# download the media(s)
def media_downloader(metadata, media_folder):
    media_type = metadata['type']
    link = metadata['link']
    
    if media_type == 'image': 
        return download_image(links, media_folder)
    elif media_type == 'gallery':
        return download_multiple_image(links, media_folder)
    elif media_type == 'video':
        return download_video(links, media_folder)