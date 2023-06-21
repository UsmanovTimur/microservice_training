from datetime import datetime
from functools import wraps
from uuid import uuid4

from utils.logger import get_logger

__all__ = ('tracert',)

LOGGER = get_logger(__name__)


def tracert(func):
    """Декоратор подмешивающий uuid к запросу"""

    @wraps(func)
    async def wrapper(*args, trace_id="", **kwargs):
        if trace_id is None or trace_id == "":
            trace_id = uuid4()
        LOGGER.info(f'Request {trace_id} start')
        resp = await func(*args, trace_id=trace_id, **kwargs)
        LOGGER.info(f'Request {trace_id} close')
        return resp

    return wrapper
