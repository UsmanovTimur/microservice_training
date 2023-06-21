from datetime import datetime
from functools import wraps

from utils.logger import get_logger

__all__ = ('benchmark',)

LOGGER = get_logger(__name__)


def benchmark(func):
    """Декоратор засекающий время выполнения запроса"""

    @wraps(func)
    async def wrapper(*args, **kwargs):
        now = datetime.now()
        resp = await func(*args, **kwargs)
        LOGGER.info(f"To to request: {datetime.now() - now}")
        return resp

    return wrapper
