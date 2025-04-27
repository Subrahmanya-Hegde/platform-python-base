import asyncio
from typing import Callable, Any

async def run_in_executor(func: Callable, *args, **kwargs) -> Any:
    """
    Runs a blocking function in a separate thread, non-blocking the main event loop.

    :param func: The blocking function to run.
    :param args: Positional arguments for the function.
    :param kwargs: Keyword arguments for the function.
    :return: Result of the function call.
    """
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, func, *args, **kwargs)

async def async_sleep(seconds: float) -> None:
    """
    Async sleep utility (better than time.sleep for async code).

    :param seconds: Number of seconds to sleep.
    """
    await asyncio.sleep(seconds)
