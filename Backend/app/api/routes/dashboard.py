from fastapi import APIRouter, Depends

from app.application.use_cases.get_dashboard import GetDashboardUseCase, DashboardOut
from app.core.dependencies import get_dashboard_use_case

router = APIRouter(prefix="/api", tags=["dashboard"])


def get_current_user_id() -> str:
    # Mock temporal del usuario logueado
    return "user_123"


@router.get("/dashboard")
def get_dashboard(use_case: GetDashboardUseCase = Depends(get_dashboard_use_case)) -> DashboardOut:
    user_id = get_current_user_id()
    return use_case.execute(user_id)