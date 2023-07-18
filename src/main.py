from spotify import get_token, get_playlist_tracks
from youtube import yotube_search

from dotenv import load_dotenv
import os

if __name__ == '__main__':
    load_dotenv()

    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")

    token = get_token(client_id, client_secret)
    tracks = get_playlist_tracks(token, '48Zqp7HCEBIiEYj3HTC45U')

    yotube_search('never gonna give you up')