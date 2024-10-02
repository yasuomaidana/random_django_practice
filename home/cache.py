import cachetools
import requests


@cachetools.cached(cache=cachetools.TTLCache(maxsize=100, ttl=3600))  # Adjust maxsize and ttl as needed
def fetch_website(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.text