import logging

def basic_logger():
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')

# # Test the function
# basic_logger()

def logger_handler():
    logger=logging.getLogger()
    logger.setLevel(logging.DEBUG)

    
    file_handler = logging.FileHandler('app.log')
    console_handler = logging.StreamHandler()

    
    file_handler.setLevel(logging.DEBUG)
    console_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
        
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')
# logger_handler()


def logger_with_custom_format():
    logger = logging.getLogger('custom_logger')
    logger.setLevel(logging.DEBUG)
    
    file_handler = logging.FileHandler('custom_app.log')
    console_handler = logging.StreamHandler()
    
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')

# Test the function
# logger_with_custom_format()


def logger_with_different_formats():
    logger = logging.getLogger('multi_format_logger')
    logger.setLevel(logging.DEBUG)
    
    file_handler = logging.FileHandler('multi_format_app.log')
    console_handler = logging.StreamHandler()
    
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)
    console_handler.setFormatter(console_formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')

# Test the function
# logger_with_different_formats()

 ###Write a Python function to create a logger that uses a rotating file handler, which creates a new log file when the current log file reaches a certain size.

from logging.handlers import RotatingFileHandler

def logger_with_rotating_file_handler():
    logger = logging.getLogger('rotating_logger')
    logger.setLevel(logging.DEBUG)
    
    rotating_handler = RotatingFileHandler('rotating_app.log', maxBytes=2000, backupCount=5)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    rotating_handler.setFormatter(formatter)
    
    logger.addHandler(rotating_handler)
    
    for i in range(100):
        logger.debug('This is debug message number {}'.format(i))

# Test the function
# logger_with_rotating_file_handler()

#Write a Python function that logs an exception stack trace to a log file when an exception occurs

def log_exception():
    logger = logging.getLogger('exception_logger')
    logger.setLevel(logging.ERROR)
    
    file_handler = logging.FileHandler('exception_app.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    
    try:
        1 / 0
    except Exception as e:
        logger.exception("An exception occurred")

# Test the function
log_exception()


##Write a Python function to create a logger that includes contextual information (e.g., function name, line number) in the log messages.

def logger_with_additional_context(user_id, session_id):
    logger = logging.getLogger('additional_context_logger')
    logger.setLevel(logging.DEBUG)
    
    file_handler = logging.FileHandler('additional_context_app.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(funcName)s - %(lineno)d - UserID: %(user_id)s - SessionID: %(session_id)s')
    file_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    
    extra = {'user_id': user_id, 'session_id': session_id}
    
    def test_func():
        logger.debug('This is a debug message', extra=extra)
        logger.info('This is an info message', extra=extra)
        logger.warning('This is a warning message', extra=extra)
        logger.error('This is an error message', extra=extra)
        logger.critical('This is a critical message', extra=extra)
    
    test_func()

# Test the function
# logger_with_additional_context('user123', 'session456')


import logging.config

def configure_logging_with_dict():
    log_config = {
        'version': 1,
        'formatters': {
            'default': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            },
            'detailed': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(funcName)s - %(lineno)d'
            }
        },
        'handlers': {
            'file': {
                'class': 'logging.FileHandler',
                'filename': 'dict_config_app.log',
                'formatter': 'detailed',
                'level': 'DEBUG'
            },
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'level': 'DEBUG'
            }
        },
        'root': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG'
        }
    }
    logging.config.dictConfig(log_config)
    logger = logging.getLogger('')
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')

# Test the function
configure_logging_with_dict()