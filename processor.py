import json
import os
from constants import CONFIG_PATH
from logger import logger

class DataProcessor:
    def __init__(self, data):
        self.data = data
        logger.info('DataProcessor initialized')

    def process_data(self):
        logger.info('Starting data processing')
        # Implementation of data processing logic
        processed = {key: self.data[key] for key in self.data if key != 'exclude'}
        logger.info('Data processing finished')
        return processed

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.data, file)
        logger.info(f'Data saved to {filename}')

if __name__ == '__main__':
    sample_data = {'value1': 100, 'value2': 200, 'exclude': 300}
    processor = DataProcessor(sample_data)
    processed_data = processor.process_data()
    processor.save_to_file(os.path.join(CONFIG_PATH, 'output.json'))
