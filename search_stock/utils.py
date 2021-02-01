import requests

def search_symbol(param="TSLA"):
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    return r.json()