"""
Custom handlers for exceptions.

This module contains handlers for custom and third-party exceptions like Pydantic's RequestValidationError.

"""

from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from {{cookiecutter.__package_name}}.logger import get_logger

logger = get_logger(__name__)


async def pydantic_validation_error_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    """
    Handle Pydantic validation errors.

    Arguments:
        request -- Incoming request that led to the error.
        exc -- The validation error raised.

    Returns:
        JSONResponse -- The response containing the error details.

    """
    # Log the validation error
    error_details = exc.errors()
    logger.error("Validation error for %s: %s", request.url.path, error_details)

    # Return the default FastAPI response
    return JSONResponse(
        status_code=422,
        content={"detail": error_details, "body": exc.body},
    )
