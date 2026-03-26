import logging
import os
from datetime import datetime

# create log file name
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

# project root directory
ROOT_DIR = os.getcwd()

# logs folder path
LOG_DIR = os.path.join(ROOT_DIR, "logs")

# create logs directory
os.makedirs(LOG_DIR, exist_ok=True)

# full log file path
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

