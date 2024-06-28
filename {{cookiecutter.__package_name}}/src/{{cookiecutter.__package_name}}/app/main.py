"""
Implement the main entry point of the FastAPI application.

This module initializes the FastAPI application instance, imports routers, and sets up middleware and exception handlers
as needed.

To run the app, execute the following command in the terminal: uvicorn {{cookiecutter.__package_name}}.app.main:app
--reload

"""

from fastapi import FastAPI
from {{cookiecutter.__package_name}}.app.exceptions import add_exception_handlers
from {{cookiecutter.__package_name}}.app.middleware.logging_middleware import LoggingMiddleware
from {{cookiecutter.__package_name}}.logger import get_logger
from {{cookiecutter.__package_name}}.settings import BASE_URL, ENVIRONMENT, VERSION

logger = get_logger(__name__)

app = FastAPI(
    title="{{cookiecutter.__title}} API",
    version=VERSION,
    openapi_url=f"{BASE_URL}/openapi.json",
    docs_url=f"{BASE_URL}/docs",
    redoc_url=f"{BASE_URL}/redoc",
)

SHOW_DOCS_ENV = ("local", "dev", "staging")

if ENVIRONMENT not in SHOW_DOCS_ENV:
    app.openapi_url = None

# Add routers
# First, import the routers: from {{cookiecutter.__package_name}}.app.routers import ...
# Then, add the routers to the app: app.include_router(...)

# Add middleware
app.add_middleware(LoggingMiddleware)

# Add exception handlers
add_exception_handlers(app)


@app.get(BASE_URL, tags=["home"])
async def homepage() -> dict:
    """
    Homepage for the {{cookiecutter.__title}} API.

    Returns:
        The homepage message.

    """
    logger.info("Root endpoint called.")
    return {app.title: app.version}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8800, reload=True)
