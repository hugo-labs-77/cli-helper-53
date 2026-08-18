import time
import requests
from requests.exceptions import RequestException

class NetworkOperation:
    def __init__(self, max_retries=3, backoff_factor=1):
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor

    def retry_request(self, url):
        attempts = 0
        while attempts < self.max_retries:
            try:
                response = requests.get(url)
                response.raise_for_status()  # Raise an error for bad responses
                return response.json()  # Assuming response is JSON
            except RequestException as e:
                attempts += 1
                if attempts == self.max_retries:
                    print(f'Failed after {attempts} attempts: {e}')
                    raise
                else:
                    wait_time = self.backoff_factor * (2 ** (attempts - 1))
                    print(f'Retrying in {wait_time} seconds...')
                    time.sleep(wait_time)
        return None  # Optional: Safeguard return

# Example usage
if __name__ == '__main__':
    net_ops = NetworkOperation(max_retries=5, backoff_factor=1)
    try:
        result = net_ops.retry_request('https://api.example.com/data')
        print(result)
    except Exception as e:
        print(f'Error occurred: {e}')