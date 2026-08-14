import time
import random

class RetryException(Exception):
    pass

# Retry configurations
RETRY_COUNT = 3  # Number of retries
RETRY_DELAY = 2  # Delay between retries in seconds


def retry_on_failure(func):
    """Decorator to retry a network operation on failure."""
    def wrapper(*args, **kwargs):
        for attempt in range(RETRY_COUNT):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if attempt < RETRY_COUNT - 1:
                    time.sleep(RETRY_DELAY)
                    print(f'Attempt {attempt + 1} failed: {e}. Retrying...')
                else:
                    print('Max retries reached. Operation failed.')
                    raise RetryException(f'Operation failed after {RETRY_COUNT} attempts') from e
    return wrapper


@retry_on_failure
def mock_network_call():
    """Simulates a network call that may fail."""
    if random.choice([True, False]):
        raise ConnectionError('Network error occurred')
    return 'Success'

if __name__ == '__main__':
    try:
        result = mock_network_call()
        print(result)
    except RetryException as e:
        print(e)