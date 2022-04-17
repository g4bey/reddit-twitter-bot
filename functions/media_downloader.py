"""Handle every function related to medias."""

from urllib.parse import urlparse
import requests
from ffmpeg import input, output, run
from os import remove, path


def stream_download(url, name):
    """Download a file from an url, in chunk."""
    video_stream = requests.get(url, stream=True)

    with open(name, 'wb') as media:
        for chunk in video_stream.iter_content(chunk_size=1024):
            media.write(chunk)


def gallery_explorer(sumission, max=4):
    """Explore reddit gallery and return links to media."""
    response = []
    images = sumission.media_metadata.items()

    for i, image in enumerate(images):
        if i < 4:
            response.append(image[1]['s']['u'])

    return response


def video_explorer(submission, max=512):
    """Explore reddit videos and return all fallback links."""
    response = {}
    for resolution in [360, 480, 720]:
        r = requests.get(f"{submission['url']}/DASH_{resolution}.mp4")
        if r.ok:
            response[resolution] = r.url

    return response


def audio_explorer(submission):
    """Explore reddit audio and return links to the right stream."""
    r = requests.get(f"{submission['url']}/DASH_audio.mp4")
    if r.ok:
        return r.url


def media_rooter(submission):
    """Return links to the media."""
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


def download_image(metadata, folder, name):
    """Download an image in chunks."""
    stream_download(metadata['link'],
                    f"{folder}/{name}.{metadata['link'][-3:]}")


def download_video(metadata, folder):
    """Download and sort the videos."""
    audio_path = f"{folder}/file_audio.mp3"
    audio = metadata['audio']

    if audio:
        stream_download(audio, audio_path)
        audio_stream = input(audio_path)

        max_size = 0
        stored_max_path = ''
        for key, video in metadata['video'].items():
            video_path = f"{folder}/{key}.mp4"
            temps_video_path = f"{folder}/{key}_temp.mp4"

            if audio:
                stream_download(video, temps_video_path)
                video_stream = input(temps_video_path)
                output(audio_stream, video_stream, video_path).run(quiet=True)
                remove(temps_video_path)
            else:
                video_path = f"{folder}/{key}.mp4"
                stream_download(video, video_path)

            max_size, stored_max_path = keep_largest_file(
                max_size, stored_max_path, video_path)
        else:
            if audio:
                remove(audio_path)


def keep_largest_file(max_size, stored_max, potential_max):
    """Only keep the largest of stored_max and potential_max."""
    file_size = path.getsize(potential_max)
    if not stored_max:
        stored_max = potential_max
        max_size = file_size
    elif file_size >= max_size:
        max_size = file_size
        remove(stored_max)
        stored_max = potential_max

    return max_size, stored_max


def media_downloader(metadata, folder):
    """Download the media(s) depending on their type."""
    media_type = metadata['type']

    if media_type == 'image':
        download_image(metadata, folder, 'img')

    elif media_type == 'gallery':
        for i, link in enumerate(metadata['links']):
            download_image(link, folder, f"img{i}")

    elif media_type == 'video':
        download_video(metadata, folder)
