import requests

def yotube_search(title):
    title = title.replace(' ', '+')
    url = f'https://www.youtube.com/results?search_query={title}'
    
    res = requests.get(url)
    