"""Main entry point for the {{cookiecutter.project_name}} application."""

from fastapi import Depends, FastAPI

from {{cookiecutter.__package_name}}.app.exceptions import add_exception_handlers
from {{cookiecutter.__package_name}}.app.middlewares.logging_middleware import LoggingMiddleware
from {{cookiecutter.__package_name}}.app.routers import api_router
from {{cookiecutter.__package_name}}.settings import get_settings

app_settings = get_settings()

# Initialize the FastAPI app
app = FastAPI(
    title=app_settings.APP_NAME,
    version=app_settings.VERSION,
    description="{{cookiecutter.project_name}} API allows you to interact with the {{cookiecutter.project_name}} app.",
)

# Add middleware
app.add_middleware(LoggingMiddleware)

# Add exception handlers
add_exception_handlers(app)

# Include the main API router
app.include_router(
    api_router,
    dependencies=[Depends(get_settings)],
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("{{cookiecutter.__package_name}}.app.main:app", host="127.0.0.1", port=8800, reload=True)
