"""This contains a function that fetchs data from provided
   urls in a concurrency(multithreading) manner
"""
import os
import threading
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
    print(f'ID of process running fetch_url: {os.getpid()}')
    print(f'Name of thread: {threading.current_thread().name}')
    response = requests.get(url)
    return len(response.content)  # Return content size


def main():
    """Main function"""
    print(f'ID of main process: {os.getpid()}')
    print(f'Name of main thread: {threading.main_thread().name}\n')
    start_time = time.time()
    threads = {}

    # results = [fetch_url(url) for url in URLS] 
    # creates the threads
    for i in range(len(URLS)):
        threads[f'thread{i}'] = threading.Thread(target=fetch_url, args=(URLS[i],), name=f'thread{i}')

    # starts the threads
    for name, thread in threads.items():
        thread.start()
        print(f'{name} is started')
    print()

    # wait until all threads are executed
    for thread in threads.values():
        thread.join()
    
    # checks if all threads are done
    for thread in threads.values():
        print(f'Is {thread.name} still running: {thread.is_alive()}')
    print()
    end_time = time.time()
    print("Concurrent Execution Time:", end_time - start_time)


if __name__ == "__main__":
    main()
