import requests
import os
from requests.auth import HTTPBasicAuth
from django.conf import settings

def fetch_movies(page=1):
    url = f"https://demo.credy.in/api/v1/maya/movies/?page={page}"
    auth = HTTPBasicAuth(os.getenv('MOVIE_API_USER'), os.getenv('MOVIE_API_PASS'))
    retries = 3
    for _ in range(retries):
        response = requests.get(url, auth=auth)
        if response.status_code == 200:
            return response.json()
    return None