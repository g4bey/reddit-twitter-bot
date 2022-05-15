"""Download files from links."""


from requests import get
import logging


def download_from_url(url, folder, name):
    """Download content from URL in chunkks of 8kb. Return 0 if failed."""
    media_stream = get(url, stream=True)  # requests.get
    file_path = f"{folder}/{name}.{url[-3:]}"

    try:
        with open(file_path, 'wb') as file:
            for chunk in media_stream.iter_content(chunk_size=1024 * 64):
                file.write(chunk)
            logging.info(file_path + ' has been downloaded.')
            return file_path
    except Exception:  # To-do: handle expression more precisely.
        logging.error('Downloading the media failed.')
        return 0
