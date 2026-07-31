import time
import logging

logging.basicConfig(level=logging.INFO)

class PerformanceOptimizer:
    def __init__(self):
        self.execution_times = []

    def time_execution(self, func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            self.execution_times.append(execution_time)
            logging.info(f'Execution time for {func.__name__}: {execution_time:.4f} seconds')
            return result
        return wrapper

    @staticmethod
    def get_average_time():
        if not self.execution_times:
            return 0
        return sum(self.execution_times) / len(self.execution_times)

@PerformanceOptimizer().time_execution
def sample_function(n):
    total = sum(range(n))
    return total

if __name__ == '__main__':
    for i in range(1, 6):
        sample_function(10000000)
    optimizer = PerformanceOptimizer()
    avg_time = optimizer.get_average_time()
    logging.info(f'Average execution time: {avg_time:.4f} seconds')