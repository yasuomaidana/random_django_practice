import requests
from django.shortcuts import render

from home.cache import fetch_website


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