import cachetools
import requests
from django.core.cache import cache
from django.http import JsonResponse


@cachetools.cached(cache=cachetools.TTLCache(maxsize=100, ttl=3600))  # Adjust maxsize and ttl as needed
def fetch_website(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.text


def fetch_and_cache_website(request, url):
    # Check if the content is already in the cache
    cache_key = f"website_cache_{url}"
    cached_content = cache.get(cache_key)

    if cached_content:
        # If content is cached, return it
        return JsonResponse({
            'source': 'cache',
            'content': cached_content,
        })

    # If not cached, fetch the content
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for bad HTTP responses
        website_content = response.text

        # Store the fetched content in the cache (set timeout to 1 hour)
        cache.set(cache_key, website_content, timeout=3600)

        return JsonResponse({
            'source': 'fetched',
            'content': website_content,
        })
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)