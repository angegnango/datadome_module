# coding: utf-8
"""Http Interceptor decorator."""

from functools import wraps
import requests
import logging
import time


LOGGER = logging.getLogger(__name__)


def timeit(func):
    """."""

    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        """."""
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        LOGGER.info(
            f"Function {func.__name__} {kwargs} Took {total_time:.4f} seconds"
        )
        return result

    return timeit_wrapper


@timeit
def check_http_traffic(func):
    """."""

    @wraps(func)
    async def wrapper(*args, **kwargs):
        """."""
        request_object = kwargs.get("request")
        request_object.allow_traffic = False
        signals = {
            "host": request_object.client[0],
            "user_agent": request_object.headers.get("User-Agent")
        }
        try:
            url = "http://localhost:8000/check_incomming_http_traffic"
            with requests.Session() as session:
                response = session.post(
                    url,
                    json=signals,
                    headers={"X-Origin": "datadome_module", "Content-Type":"application/json"},
                )
                response.raise_for_status()
                if response.status_code == 201:
                    request_object.allow_traffic = True

        except Exception as exc_info:
            LOGGER.error(str(exc_info))
            pass

        result = await func(*args, **kwargs)

        return result

    return wrapper
