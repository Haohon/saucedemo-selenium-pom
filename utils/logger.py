import logging
import sys

def get_logger():
    logger = logging.getLogger("SauceDemo")
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

        # Console Handler (Terminal)
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        # File Handler (saved to automation.log)
        file_handler = logging.FileHandler("automation.log", mode='w') # 'w' clears old logs
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger