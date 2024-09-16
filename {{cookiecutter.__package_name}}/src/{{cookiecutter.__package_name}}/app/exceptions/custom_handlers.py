"""
Custom exception handlers.

This module contains handlers for custom and third-party exceptions like Pydantic's RequestValidationError and
Starlette's HTTPException.

"""

import traceback

from fastapi import Request
from fastapi.exceptions import RequestValidationError, HTTPException
from fastapi.responses import JSONResponse

from {{cookiecutter.__package_name}}.logger import get_logger

logger = get_logger(__name__)


async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    """
    Handle HTTP exceptions raised by Starlette.

    Arguments:
        request (Request): The incoming request that led to the error.
        exc (HTTPException): The HTTP exception raised.

    Returns:
        JSONResponse: The response containing the error details.

    """
    logger.error(
        "HTTPException: %s for %s %s",
        exc.detail,
        request.method,
        request.url.path,
    )
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )


async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    """
    Handle Pydantic validation errors.

    Arguments:
        request (Request): The incoming request that led to the error.
        exc (RequestValidationError): The validation error raised.

    Returns:
        JSONResponse: The response containing the error details.

    """
    error_details = exc.errors()
    logger.error(
        "Validation error for %s %s: %s",
        request.method,
        request.url.path,
        error_details,
    )
    return JSONResponse(
        status_code=422,
        content={"detail": error_details},
    )


async def general_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """
    Handle all other exceptions.

    Arguments:
        request (Request): The incoming request that led to the error.
        exc (Exception): The exception raised.

    Returns:
        JSONResponse: The response containing the error details.

    """
    error_trace = traceback.format_exc()
    logger.error(
        "Unhandled exception for %s %s: %s",
        request.method,
        request.url.path,
        str(exc),
    )
    logger.debug("Traceback: %s", error_trace)

    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"},
    )
