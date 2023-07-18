import requests
from youtubesearchpython import VideosSearch

def get_youtube_url(title):
    search = VideosSearch(title, limit=1)
    result = search.result()
    url = result['result'][0]['link']
    
    return url