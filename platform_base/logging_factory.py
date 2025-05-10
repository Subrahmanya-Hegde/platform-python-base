import os
import logging
from logging.handlers import RotatingFileHandler

def get_logger(log_dir="logs", log_name="system", level=logging.INFO):
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger()
    logger.setLevel(level)

    formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s')

    file_handler = RotatingFileHandler(
        filename=os.path.join(log_dir, f"{log_name}.log"),
        maxBytes=10 * 1024 * 1024,
        backupCount=5
    )
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
