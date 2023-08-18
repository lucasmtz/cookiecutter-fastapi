"""
A logger module for Python applications.

This module provides a `get_logger` function that creates and returns a configured logger. The logger is configured
differently depending on the environment:

- When running on Google Cloud Platform (as determined by the 'LOG_FORMAT' environment variable being set to 'gcp'), the
  logger is configured to use Google Cloud Logging with a custom formatter.

- In all other cases, the logger uses a RichHandler for console output, suitable for local development.

Example:
    import logger

    log = logger.get_logger(__name__)
    log.info("This is an info message.")
    log.warning("This is a warning message.")
    log.error("This is an error message.")
    log.critical("This is a critical message.")

"""

import json
import logging
import os
from typing import Any

from google.cloud import logging as cloudlogging
from google.cloud.logging.handlers import CloudLoggingHandler
from rich.logging import RichHandler


class CustomCloudFormatter(logging.Formatter):
    """A custom formatter for Google Cloud Logging."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the formatter."""
        super().__init__(*args, **kwargs)

        # The default set of attribute names in LogRecord objects
        self.default_record_attrs = set(
            logging.LogRecord(name="", level=0, pathname="", lineno=0, msg="", args=(), exc_info=None).__dict__.keys()
        )

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the specified log record and return the result.

        Arguments:
            record -- Log record.

        Returns:
            Formatted log record.

        """
        message = super().format(record)
        log_struct = {
            "message": message,
        }

        # Include extra fields, excluding default LogRecord attributes
        for key, value in record.__dict__.items():
            if key not in self.default_record_attrs and not key.startswith("_"):
                log_struct[key] = value

        return json.dumps(log_struct)


def get_logger(name: str, level: str | None = None) -> logging.Logger:
    """
    Return a logger with the specified name.

    If running on Google Cloud (as determined by the value 'gcp' of an 'LOG_FORMAT' environment variable), the logger is
    configured to use Google Cloud Logging with a custom formatter. In all other cases, the logger uses a RichHandler
    for console output.

    Args:
        name -- Name of the logger.

    Keyword Arguments::
        level -- Logging level. Defaults to 'DEBUG' if running locally, or 'INFO' if running on Google Cloud.

    Returns:
        Configured logger.

    """
    logger = logging.getLogger(name)

    # Running on Google Cloud.
    if os.getenv("LOG_FORMAT") == "gcp":
        # Set the default logging level
        if level is None:
            level = "INFO"

        # Create a Cloud Logging client
        client = cloudlogging.Client()

        # Add custom formatter
        cloud_handler = CloudLoggingHandler(client)
        cloud_handler.setFormatter(CustomCloudFormatter())
        logger.addHandler(cloud_handler)

    # Running locally.
    else:
        # Set the default logging level
        if level is None:
            level = "DEBUG"

        # Add RichHandler for console output
        rich_handler = RichHandler(rich_tracebacks=True)
        logger.addHandler(rich_handler)

    logger.setLevel(level)
    return logger
