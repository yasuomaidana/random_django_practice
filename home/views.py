import requests
from django.shortcuts import render

from home.cache import fetch_website, fetch_and_cache_website


# Create your views here.
def home(request):
    try:
        website_content = fetch_website("https://www.example.com")
    except requests.RequestException as e:
        # Handle exceptions gracefully
        website_content = f"Error fetching website: {e}"

    context = {
        'title':'Caching using cachetools decorator',
        'website_content': website_content
    }

    return render(request, 'home.html', context)

# def cache_alternative(request):
#     url = 'https://example.com'  # You can dynamically pass the URL as well
#     cached_json = fetch_and_cache_website(request, url)
#     # website_content = cached_json.get('content', 'No content available')  # Safely get the content
#     # print(cached_json)
#     # context = {
#     #     'title':'Caching using cachetools decorator',
#     #     'website_content': website_content
#     # }
#     # return render(request, 'home.html', context)
#     return cached_json

def cache_alternative(request):
    url = 'https://example.com'  # You can dynamically pass the URL as well
    return fetch_and_cache_website(request, url)