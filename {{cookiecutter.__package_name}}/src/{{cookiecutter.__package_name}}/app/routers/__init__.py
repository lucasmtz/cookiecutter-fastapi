"""
Initialize the routers package.

This package contains all the route definitions for the API.

"""

from fastapi import APIRouter

from {{cookiecutter.__package_name}}.app.routers.health_router import router as health_router

# Import other routers here as needed

# Create a main API router to include all routers
api_router = APIRouter()
api_router.include_router(health_router, prefix="", tags=["health"])
# Include other routers
