import time

class PerformanceOptimized:
    def __init__(self):
        self.data = []

    def add_data(self, item):
        self.data.append(item)

    def calculate_average(self):
        if not self.data:
            return 0
        return sum(self.data) / len(self.data)

    def time_execution(self, func, *args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return result

    def optimized_processing(self):
        self.data = list(range(10000))
        avg = self.time_execution(self.calculate_average)
        print(f"Average: {avg}")

# Example usage:
# processor = PerformanceOptimized()
# processor.optimized_processing()