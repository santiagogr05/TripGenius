from functools import lru_cache

from app.application.use_cases.get_dashboard import GetDashboardUseCase
from app.infrastructure.persistence.in_memory_repos import (
    InMemoryTripRepository,
    InMemoryFavoritePlaceRepository,
)


@lru_cache
def get_dashboard_use_case() -> GetDashboardUseCase:
    trip_repo = InMemoryTripRepository()
    fav_repo = InMemoryFavoritePlaceRepository()
    return GetDashboardUseCase(trip_repo=trip_repo, fav_repo=fav_repo)