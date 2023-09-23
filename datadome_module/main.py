# coding: utf-8
"""Http Interceptor decorator."""

from functools import wraps
import requests
from datadome_module.config import get_configs
import logging
import time
from urllib.parse import urljoin


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
    def wrapper(*args, **kwargs):
        """."""
        settings = get_configs()
        request_object = kwargs.get("request")
        request_object.allow_traffic = False
        signals = {
            "host": request_object.headers.get("Host"),
            "client_IP": request_object.client,
            "user-agent": request_object.headers.get("User-Agent"),
        }
        try:
            base_url = settings.get("external-endpoints", "ws.protector_api")
            url = urljoin(base_url, "check_incomming_http_traffic")
            with requests.Session() as session:
                response = session.post(
                    url,
                    data=signals,
                    headers={"X-Origin": "datadome_module"},
                )
                response.raise_for_status()
                if response.status_code == 201:
                    request_object.allow_traffic = True

        except Exception as exc_info:
            LOGGER.error(str(exc_info))
            pass

        result = func(*args, **kwargs)

        return result

    return wrapper
