"""This contains a function that fetches data from URLs
   sequentially using the requests library.
"""

import time
import requests


URLS = [
    "https://www.example.com",
    "https://www.example.org",
    "https://www.example.net",
    "https://www.example.edu",
]


def fetch_url(url):
    """Fetches data from the provide urls"""
    response = requests.get(url)
    return len(response.content)  # Return content size


def main():
    """Main function"""
    start_time = time.time()
    results = [fetch_url(url) for url in URLS] 
    end_time = time.time()
    print("Sequential Execution Time:", end_time - start_time)


if __name__ == "__main__":
    main()
