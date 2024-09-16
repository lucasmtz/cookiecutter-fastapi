"""Application configuration for the {{cookiecutter.project_name}} application."""

import os
from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings

from {{cookiecutter.__package_name}} import __version__
from {{cookiecutter.__package_name}}.logger import get_logger


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # General settings
    APP_NAME: str = "{{cookiecutter.project_name}}"
    VERSION: str = __version__

    ENVIRONMENT: Literal["development", "production", "staging"] = Field(default="development", alias="ENVIRONMENT")

    # Logging settings
    LOG_LEVEL: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = Field(default="DEBUG", alias="LOG_LEVEL")

    # Database settings (example)
    # DATABASE_URL: str = Field(..., alias="DATABASE_URL")  # Required field

    # Other settings can be added here
    # e.g., API keys, third-party service URLs, etc.

    model_config = {
        "case_sensitive": True,
        "env_file": ".env" if os.getenv("ENVIRONMENT", "development") == "development" else None,
        "env_file_encoding": "utf-8",
        "extra": "ignore",
    }


# Use lru_cache to cache the settings instance
@lru_cache
def get_settings() -> Settings:
    """
    Get the application settings.

    Returns:
        The application settings.

    """
    settings = Settings()
    logger = get_logger(__name__)
    logger.info("Loaded application settings: %s", settings)

    return settings
