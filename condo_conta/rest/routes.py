from fastapi import APIRouter

from condo_conta.rest.api.v1 import healthcheck


v1 = APIRouter()

v1.include_router(healthcheck.router, tags=["healthcheck"])
