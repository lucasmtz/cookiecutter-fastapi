"""Router for health check endpoints, including info and status."""

from fastapi import APIRouter, Depends, status

from {{cookiecutter.__package_name}}.app.schemas.health import InfoResponse, StatusResponse
from {{cookiecutter.__package_name}}.settings import Settings, get_settings

router = APIRouter()


@router.get(
    "/info",
    response_model=InfoResponse,
    status_code=status.HTTP_200_OK,
    description="Retrieve application information, including name, version, and environment.",
    responses={
        status.HTTP_200_OK: {"description": "Successful response", "model": InfoResponse},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"description": "Internal server error"},
    },
    tags=["health"],
)
async def get_info(settings: Settings = Depends(get_settings)) -> InfoResponse:
    """
    Endpoint to retrieve application information.

    Arguments:
        settings (Settings): Application settings provided by dependency injection.

    Returns:
        InfoResponse: An object containing application information.

    """
    return InfoResponse(
        app_name=settings.APP_NAME,
        version=settings.VERSION,
        environment=settings.ENVIRONMENT,
    )


@router.get(
    "/status",
    response_model=StatusResponse,
    status_code=status.HTTP_200_OK,
    description="Check the status of the application.",
    responses={
        status.HTTP_200_OK: {"description": "Application is running", "model": StatusResponse},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"description": "Internal server error"},
    },
    tags=["health"],
)
async def get_status() -> StatusResponse:
    """
    Endpoint to check the status of the application.

    Returns:
        StatusResponse: An object indicating the application status.

    """
    return StatusResponse(status="running")
