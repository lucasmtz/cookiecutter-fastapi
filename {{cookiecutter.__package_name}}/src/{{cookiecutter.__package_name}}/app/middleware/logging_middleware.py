"""Middleware for logging requests and responses."""

import time
from collections.abc import Callable

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
from {{cookiecutter.__package_name}}.logger import get_logger

logger = get_logger(__name__)


class LoggingMiddleware(BaseHTTPMiddleware):  # pylint: disable=too-few-public-methods
    """Middleware for logging requests and responses."""

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        """
        Dispatches the request to the next middleware or endpoint, while logging the request and response.

        Arguments:
            request -- The incoming request object.
            call_next -- The callable representing the next middleware or endpoint.

        Returns:
            The response returned by the next middleware or endpoint.

        """
        logger.info("Received request: %s %s", request.method, request.url)
        start_time = time.time()
        response: Response = await call_next(request)
        process_time = time.time() - start_time
        logger.info("Sent response: %s %s", response.status_code, request.url)
        response.headers["X-Process-Time"] = str(process_time)
        return response
