from dotenv import load_dotenv
import os
import base64
import requests
import json

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token(client_id, client_secret):
    auth_string = f'{client_id}:{client_secret}'    
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes), 'utf-8')

    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': f'Basic {auth_base64}',
        'Content-Type': 'application/x-www-form-urlencoded' 
    }
    data = {
        'grant_type': 'client_credentials'
    }

    res = requests.post(url, headers=headers, data=data)
    jsron_result = json.loads(res.content)
    token = jsron_result['access_token']

    return token

def get_auth_header(token):
    return {
        'Authorization': f'Bearer {token}'
    }

def get_playlist_tracks(token, playlist_id):
    url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
    headers = get_auth_header(token)
    res = requests.get(url, headers=headers)
    json_result = json.loads(res.content)
    tracks_json = json_result['items']

    tracks = []
    for track in tracks_json:
        tracks.append(track['track']['name'])

    return tracks

if __name__ == '__main__':
    token = get_token(client_id, client_secret)
    tracks = get_playlist_tracks(token, '48Zqp7HCEBIiEYj3HTC45U')
