from datetime import date
from typing import TypedDict, List

from app.domain.repositories.trip_repository import TripRepository
from app.domain.repositories.favorite_place_repository import FavoritePlaceRepository


class TripOut(TypedDict):
    id: str
    destination: str
    start_date: date
    end_date: date
    travelers: int
    status: str


class FavoritePlaceOut(TypedDict):
    id: str
    name: str
    country: str


class DashboardOut(TypedDict):
    upcoming_trips: List[TripOut]
    favorite_places: List[FavoritePlaceOut]


class GetDashboardUseCase:
    def __init__(self, trip_repo: TripRepository, fav_repo: FavoritePlaceRepository) -> None:
        self._trip_repo = trip_repo
        self._fav_repo = fav_repo

    def execute(self, user_id: str) -> DashboardOut:
        trips = self._trip_repo.list_upcoming_trips(user_id)
        favs = self._fav_repo.list_favorites(user_id)

        return {
            "upcoming_trips": [
                {
                    "id": t.id,
                    "destination": t.destination,
                    "start_date": t.start_date,
                    "end_date": t.end_date,
                    "travelers": t.travelers,
                    "status": t.status,
                }
                for t in trips
            ],
            "favorite_places": [{"id": f.id, "name": f.name, "country": f.country} for f in favs],
        }