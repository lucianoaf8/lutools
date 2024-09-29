# utils/logger_config.py

import logging
import os
from logging.handlers import RotatingFileHandler
import sys
import inspect
from datetime import datetime

# Default configurations
DEFAULT_LOG_LEVEL = logging.INFO
DEFAULT_LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
DEFAULT_LOG_DIR = 'logs'
MAX_LOG_SIZE = 5 * 1024 * 1024  # 5 MB
BACKUP_COUNT = 5

def get_logger(
    name=None,
    log_level=None,
    log_file_path=None,
    log_to_console=True,
    log_to_file=True,
    file_log_level=None,
    console_log_level=None
):
    """
    Configure and return a logger.

    Args:
        name (str, optional): Name of the logger. Defaults to the calling script's base name.
        log_level (int, optional): Logging level for the logger. Defaults to DEFAULT_LOG_LEVEL.
        log_file_path (str, optional): Full path to the log file. If provided, it will be used as is.
                                       Otherwise, a log file will be created in DEFAULT_LOG_DIR with the name based on the logger's name.
        log_to_console (bool, optional): Whether to log to console. Defaults to True.
        log_to_file (bool, optional): Whether to log to file. Defaults to True.
        file_log_level (int, optional): Logging level for the file handler. Defaults to logger's level.
        console_log_level (int, optional): Logging level for the console handler. Defaults to logger's level.

    Returns:
        logging.Logger: Configured logger object.
    """
    if name is None:
        # Get the name of the calling script
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        if module and hasattr(module, '__file__'):
            name = os.path.splitext(os.path.basename(module.__file__))[0]
        else:
            name = 'root'
    
    logger = logging.getLogger(name)
    
    # Set the log level for the logger
    level = log_level if log_level is not None else DEFAULT_LOG_LEVEL
    logger.setLevel(level)

    # Avoid adding handlers multiple times if the logger already has them
    if not logger.handlers:
        # Create formatter
        formatter = logging.Formatter(DEFAULT_LOG_FORMAT, DEFAULT_DATE_FORMAT)

        # Add console handler if requested
        if log_to_console:
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(formatter)
            console_handler.setLevel(console_log_level if console_log_level is not None else level)
            logger.addHandler(console_handler)

        # Add file handler if requested
        if log_to_file:
            if log_file_path is None:
                # Determine the absolute path to the log directory based on this file's location
                current_file_path = os.path.abspath(__file__)
                current_dir = os.path.dirname(current_file_path)
                # Assuming project root is two levels up; adjust if needed
                project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))

                # Create daily log directory
                current_date = datetime.now().strftime('%Y-%m-%d')
                log_dir = os.path.join(project_root, DEFAULT_LOG_DIR, current_date)
                os.makedirs(log_dir, exist_ok=True)
                log_file = os.path.join(log_dir, f'{name}.log')
            else:
                # Use provided log_file_path
                log_file = log_file_path
                # Ensure the directory exists
                os.makedirs(os.path.dirname(log_file), exist_ok=True)

            file_handler = RotatingFileHandler(log_file, maxBytes=MAX_LOG_SIZE, backupCount=BACKUP_COUNT)
            file_handler.setFormatter(formatter)
            file_handler.setLevel(file_log_level if file_log_level is not None else level)
            logger.addHandler(file_handler)

    return logger

def set_log_level(logger, level):
    """
    Set the log level for the logger and all its handlers.

    Args:
        logger (logging.Logger): The logger to modify.
        level (int): The new log level.
    """
    logger.setLevel(level)
    for handler in logger.handlers:
        handler.setLevel(level)

# Usage example
if __name__ == "__main__":
    # Initialize logger with file logging only for errors and above
    logger = get_logger(file_log_level=logging.ERROR)
    
    # These messages won't be logged to the file (since their level is below ERROR)
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    
    # This message will be logged to the file
    logger.error("This is an error message")
    
    # Change log level dynamically
    set_log_level(logger, logging.DEBUG)
    logger.debug("This debug message will now be logged to console")
