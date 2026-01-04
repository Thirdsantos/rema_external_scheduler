"""
Application package for the external_rema project.

This package follows a simple layered architecture:
- config: environment configuration and settings
- database: SQLAlchemy engine and DB-related utilities
- schemas: Pydantic models (request/response DTOs)
- routers: FastAPI route definitions (API layer)
- services: business logic / use cases
- repositories: data access and persistence logic
"""


