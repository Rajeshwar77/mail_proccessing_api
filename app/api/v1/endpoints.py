from fastapi import APIRouter
from .rules.endpoints import router as rule_router

router = APIRouter()

router.include_router(
    rule_router, prefix="/rule", tags=["Rules"]
)