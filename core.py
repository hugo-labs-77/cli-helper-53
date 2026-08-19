import time

class PerformanceOptimizer:
    def __init__(self):
        self.execution_time = 0

    def timed_execution(self, func):
        """Decorator to time a function's execution."""
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            self.execution_time = end_time - start_time
            print(f"Execution time: {self.execution_time:.4f} seconds")
            return result
        return wrapper

    @timed_execution
    def process_data(self, data):
        """Simulated processing of data with a time delay."""
        time.sleep(2)  # Simulating time-consuming computation
        return [d * 2 for d in data]  # Example data processing step

if __name__ == '__main__':
    optimizer = PerformanceOptimizer()
    result = optimizer.process_data([1, 2, 3, 4])
    print(f"Processed data: {result}")