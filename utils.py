import time
import requests
from requests.exceptions import RequestException

def retry_request(url, max_retries=3, backoff_factor=1):
    """
    Perform a GET request with retry logic.

    Parameters:
    - url: API endpoint to send the GET request to
    - max_retries: Maximum number of retry attempts
    - backoff_factor: Factor for exponential backoff delay
    """
    attempt = 0
    while attempt < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return JSON response if successful
        except RequestException as e:
            attempt += 1
            if attempt == max_retries:
                raise Exception(f'Failed after {max_retries} attempts: {e}')
            wait_time = backoff_factor * (2 ** (attempt - 1))
            time.sleep(wait_time)  # Wait before next retry

# Example usage (commented out) to avoid execution when imported:
# if __name__ == '__main__':
#     try:
#         data = retry_request('https://api.example.com/data')
#         print(data)
#     except Exception as e:
#         print(e)