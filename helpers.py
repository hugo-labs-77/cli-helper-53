import functools
import time


def timeit(func):
    """Decorator to time a function's execution."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} executed in {execution_time:.5f} seconds")
        return result
    return wrapper

@timeit
def perform_heavy_computation(n):
    """Simulate a heavy computation task."""
    total = 0
    for i in range(n):
        total += i * i
    return total

@timeit
def load_data():
    """Simulated data loading function."""
    time.sleep(2)  # Simulate a delay in loading data
    return [1, 2, 3, 4, 5]

if __name__ == '__main__':
    print(perform_heavy_computation(10000))
    print(load_data())