import os

from loguru import logger

from settings import BASE_DIR

logger.add(
    os.path.join(BASE_DIR, 'logs', 'data', 'logs.log'),
    level='DEBUG',
    rotation='1 MB',
    compression='zip',
    backtrace=True,
)
