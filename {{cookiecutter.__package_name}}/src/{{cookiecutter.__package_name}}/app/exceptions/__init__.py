"""
Exception registration module.

This module provides a centralized way to add all exception handlers to the FastAPI app instance.

"""

from fastapi import FastAPI

import {{cookiecutter.__package_name}}.app.exceptions.custom_handlers as ch


def add_exception_handlers(app: FastAPI) -> None:
    """
    Add all custom exception handlers to the FastAPI app.

    Arguments:
        app (FastAPI): The FastAPI application instance.

    """
    app.add_exception_handler(ch.HTTPException, ch.http_exception_handler)  # type: ignore
    app.add_exception_handler(ch.RequestValidationError, ch.validation_exception_handler)  # type: ignore
    app.add_exception_handler(Exception, ch.general_exception_handler)
