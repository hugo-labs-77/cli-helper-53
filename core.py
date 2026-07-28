import time

class PerformanceOptimizer:
    def __init__(self):
        self.execution_times = []

    def time_function(self, func):
        """Decorator to time a function's execution."""
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            self.execution_times.append(execution_time)
            return result
        return wrapper

    def get_average_time(self):
        """Returns the average execution time of decorated functions."""
        if not self.execution_times:
            return 0
        return sum(self.execution_times) / len(self.execution_times)

optimizer = PerformanceOptimizer()

@optimizer.time_function
def sample_function():
    time.sleep(0.1)  # Simulate a delay

if __name__ == '__main__':
    for _ in range(5):
        sample_function()
    print(f'Average execution time: {optimizer.get_average_time()} seconds')