import logging
from datetime import datetime

logging.basicConfig(
    level=logging.DEBUG,
    filename=f"logs/{datetime.now()}.log",
    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
)
