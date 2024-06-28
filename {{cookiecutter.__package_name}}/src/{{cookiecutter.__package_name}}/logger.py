"""
A logger module for Python applications.

Provides a `get_logger` function for setting up a logger with appropriate handlers based on the environment (local or
cloud).

Usage:
    from {{cookiecutter.__package_name}}.logger import get_logger
    logger = get_logger(__name__)

"""

import json
import logging
import os
from typing import Any

from google.cloud import logging as cloudlogging
from google.cloud.logging.handlers import CloudLoggingHandler
from rich.logging import RichHandler


class CustomCloudFormatter(logging.Formatter):
    """Custom formatter for Google Cloud Logging."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the formatter."""
        super().__init__(*args, **kwargs)
        self.default_record_attrs = set(
            logging.LogRecord(name="", level=0, pathname="", lineno=0, msg="", args=(), exc_info=None).__dict__.keys()
        )

    def format(self, record: logging.LogRecord) -> str:
        """Format the specified log record and return the result."""
        message = super().format(record)
        log_struct = {"message": message}

        for key, value in record.__dict__.items():
            if key not in self.default_record_attrs and not key.startswith("_"):
                log_struct[key] = value

        return json.dumps(log_struct)


def get_logger(name: str, level: str | int | None = None) -> logging.Logger:
    """
    Return a logger configured based on the environment.

    Arguments:
         name: Name of the logger.

     Keyword Arguments:
         level: Logging level. Defaults to 'DEBUG' locally or 'INFO' in cloud environments.

     Returns:
         logging.Logger: Configured logger.

    """
    logger = logging.getLogger(name)

    if os.getenv("ENVIRONMENT", "").lower() in ("prod", "staging"):
        if level is None:
            level = "INFO"
        client = cloudlogging.Client()
        cloud_handler = CloudLoggingHandler(client)
        cloud_handler.setFormatter(CustomCloudFormatter())
        logger.addHandler(cloud_handler)
    else:
        if level is None:
            level = "DEBUG"
        rich_handler = RichHandler(rich_tracebacks=True)
        logger.addHandler(rich_handler)

    logger.setLevel(level)
    return logger
