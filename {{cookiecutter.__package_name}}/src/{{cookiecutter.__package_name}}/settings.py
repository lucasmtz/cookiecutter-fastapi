"""
Configure settings for the FastAPI application.

This module contains configurations related to the FastAPI application, such as API settings, database settings, and any
other relevant configurations.

"""

import os

from dotenv import load_dotenv
from {{cookiecutter.__package_name}} import __version__
from {{cookiecutter.__package_name}}.logger import get_logger

logger = get_logger(__name__)

load_dotenv()


VERSION = __version__
ENVIRONMENT = os.getenv("ENVIRONMENT", "dev")
BASE_URL = os.getenv("BASE_URL", "/{{cookiecutter.__package_name_hyphen}}")

logger.info("Application environment: %s", ENVIRONMENT)
