import time
import functools
from typing import Callable

def retry(exceptions: tuple = (Exception,), tries: int = 3, delay: float = 1.0, backoff: float = 2.0):
    """
    Decorator for retrying a function if exceptions occur.

    :param exceptions: Tuple of exception classes to catch.
    :param tries: Total number of attempts.
    :param delay: Initial delay between retries (in seconds).
    :param backoff: Backoff multiplier (e.g., 2.0 doubles the delay each retry).
    """
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    time.sleep
