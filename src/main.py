from spotify import get_token, get_playlist_tracks, display_playlist_tracks
from youtube import get_youtube_url
from downloader import download
import argparse


from dotenv import load_dotenv
import os
import sys

if __name__ == '__main__':
    load_dotenv()

    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    token = get_token(client_id, client_secret)

    parser = argparse.ArgumentParser(description='A Spotify playlist downloader.')
    
    parser.add_argument('-ls', action='store_true', help='List the tracks in the playlist.')
    parser.add_argument('-d', action='store_true', help='Download the given playlist.')

    parser.add_argument('--playlist', help='Playlist to download', required=True)
    parser.add_argument('--path', help='Downlaod path', default='.')

    args = parser.parse_args()

    playlist = args.playlist
    path = args.path

    tracks = get_playlist_tracks(token, playlist)

    if args.ls:
        display_playlist_tracks(tracks)
        exit()

    if args.d:
        print('Downloading playlist...')
        for track in tracks:
            print(f'Downloading: {track}')
            url = get_youtube_url(track)
            download(track, url, path)

            print('Download finished!')
    
    if not args.ls and not args.d:
            sys.exit('Usage: python3 main.py [-ls] [-d] <playlist_id> <path>')