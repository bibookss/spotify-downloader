from spotify import get_token, get_playlist_tracks
from youtube import get_youtube_url
from downloader import download

from dotenv import load_dotenv
import os

if __name__ == '__main__':
    load_dotenv()

    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    token = get_token(client_id, client_secret)

    playlist_id = input('Enter playlist id: ')
    tracks = get_playlist_tracks(token, playlist_id)
    path = input('Enter download path: ')

    for track in tracks:
        print(f'Downloading: {track}')
        url = get_youtube_url(track)
        download(track, url, path)

    print('Download finished!')