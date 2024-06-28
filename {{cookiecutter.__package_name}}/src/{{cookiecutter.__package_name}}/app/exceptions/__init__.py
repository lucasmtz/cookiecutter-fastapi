"""
Exception registration module.

This module provides a centralized way to add all exception handlers to the FastAPI app instance.

"""

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from {{cookiecutter.__package_name}}.app.exceptions.custom_handlers import pydantic_validation_error_handler


def add_exception_handlers(app: FastAPI) -> None:
    """
    Add all custom exception handlers to the FastAPI app.

    Arguments:
        app -- FastAPI app instance.

    """
    app.add_exception_handler(RequestValidationError, pydantic_validation_error_handler)  # type: ignore
