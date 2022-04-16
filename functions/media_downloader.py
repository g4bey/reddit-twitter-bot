from urllib.parse import urlparse
import requests
from ffmpeg import input, output

# DOWNLOADING MEDIAS
# ------------------------------------
# download an image from an url.
def download_image(link, folder):
    pass
# download multiple image from a list
def download_multiple_image(links, folder):
    for image in links:
        download_image(links, folder)
# download 
def download_video(links, audio, folder):
    pass
# download a media
def stream_download(url, folder, title, extension='mp4'):
    video_stream = requests.get(url, stream=True)
    
    with open(f"{folder}/{title}.{extension}", 'wb') as media:
        for chunk in video_stream.iter_content(chunk_size = 1024):
            media.write(chunk)

# FETCHING LINKS
# ------------------------------------
# explore reddit gallery and return links to media
def gallery_explorer(sumission, max=4):
    response = []
    images = sumission.media_metadata.items()
    
    for i, image in enumerate(images): 
        if i < 4: 
            response.append(image[1]['s']['u'])
        
    return response
def video_explorer(submission, max=512):
    response = {}
    for resolution in [360, 480, 720]:
        r = requests.get(f"{submission['url']}/DASH_{resolution}.mp4")
        if r.ok: response[resolution] = r.url

    return response
# explore reddit audio and return links to the right stream.
def audio_explorer(submission):
    r = requests.get(f"{submission['url']}/DASH_audio.mp4")
    if r.ok: return r.url
    else: return None
    

# ROOTING
# ------------------------------------
# returns links to the media.
def media_rooter(submission):
    hostame = urlparse(submission['url']).hostname
    path = urlparse(submission['url']).hostname
    
    if hostame and hostame.endswith('v.redd.it'):
        return {
            'type': 'video',
            'audio': audio_explorer(submission),
            'video': video_explorer(submission)
        }
    elif hostame and hostame.endswith('i.redd.it'):
        return {
            'type': 'image',
            'link': submission['url']
        }
    elif hostame and hostame.endswith('i.imgur.com'):
        return {
            'type': 'image',
            'link': submission['url']
        }
    elif path and path.startswith('/gallery'):
        return {
            'type': 'gallery',
            'links': gallery_explorer(submission)
        }
    else:
        return {
            'type': 'unsupported',
            'error': f"{hostame} is unsupported"
        }
# download the media(s)
def media_downloader(metadata, media_folder):
    media_type = metadata['type']
    
    if media_type == 'image': 
        return download_image(metadata['link'], media_folder)
    elif media_type == 'gallery':
        return download_multiple_image(metadata['links'], media_folder)
    elif media_type == 'video':
        return download_video(metadata['video'], metadata['audio'], media_folder)