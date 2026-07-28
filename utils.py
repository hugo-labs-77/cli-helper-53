import time
import requests
from requests.exceptions import RequestException

def retry_request(func, retries=3, delay=2, *args, **kwargs):
    """Retries a network operation with exponential backoff."""
    for i in range(retries):
        try:
            return func(*args, **kwargs)
        except RequestException as e:
            if i < retries - 1:
                time.sleep(delay ** i)  # Exponential backoff
                continue
            else:
                raise e  # Raise last exception after retries


# Example usage:

if __name__ == '__main__':
    try:
        response = retry_request(requests.get, url='https://httpbin.org/get')
        print(response.json())
    except RequestException as e:
        print(f'Failed after retries: {e}')