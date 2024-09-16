"""Schemas for health check endpoints."""

from pydantic import BaseModel


class InfoResponse(BaseModel):
    """Response schema for the /info endpoint."""

    app_name: str
    version: str
    environment: str


class StatusResponse(BaseModel):
    """Response schema for the /status endpoint."""

    status: str
