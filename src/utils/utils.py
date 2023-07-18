from bs4 import BeautifulSoup

def get_auth_header(token):
    return {
        'Authorization': f'Bearer {token}'
    }

def html_page(page):
    return BeautifulSoup(page.text, 'html.parser')