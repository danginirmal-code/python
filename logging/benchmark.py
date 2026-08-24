import logging
import time
from logging.handlers import RotatingFileHandler

def benchmark_logging_performance():
    logger = logging.getLogger('performance_logger')
    logger.setLevel(logging.DEBUG)

    # File handler
    file_handler = logging.FileHandler('performance_file.log')
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)

    start_time = time.time()
    for i in range(10000):
        logger.debug('This is a debug message')
    end_time = time.time()
    print('File handler logging time: {} seconds'.format(end_time - start_time))
    logger.removeHandler(file_handler)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)

    start_time = time.time()
    for i in range(10000):
        logger.debug('This is a debug message')
    end_time = time.time()
    print('Console handler logging time: {} seconds'.format(end_time - start_time))
    logger.removeHandler(console_handler)

    # Rotating file handler
    rotating_handler = RotatingFileHandler('performance_rotating.log', maxBytes=2000, backupCount=5)
    rotating_handler.setLevel(logging.DEBUG)
    logger.addHandler(rotating_handler)

    start_time = time.time()
    for i in range(10000):
        logger.debug('This is a debug message')
    end_time = time.time()
    print('Rotating file handler logging time: {} seconds'.format(end_time - start_time))
    logger.removeHandler(rotating_handler)

# Test the function
benchmark_logging_performance()