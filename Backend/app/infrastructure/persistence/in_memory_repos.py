from datetime import date
from typing import List

from app.domain.entities.trip import Trip
from app.domain.entities.favorite_place import FavoritePlace
from app.domain.repositories.trip_repository import TripRepository
from app.domain.repositories.favorite_place_repository import FavoritePlaceRepository


class InMemoryTripRepository(TripRepository):
    def __init__(self) -> None:
        self._trips: List[Trip] = [
            Trip(
                id="trip_paris_001",
                user_id="user_123",
                destination="Paris, France",
                start_date=date(2024, 10, 12),
                end_date=date(2024, 10, 18),
                travelers=2,
                status="AI_PLANNING",
            ),
            Trip(
                id="trip_tokyo_001",
                user_id="user_123",
                destination="Tokyo, Japan",
                start_date=date(2024, 12, 5),
                end_date=date(2024, 12, 15),
                travelers=1,
                status="READY",
            ),
            # Otro usuario, para comprobar filtrado
            Trip(
                id="trip_other_001",
                user_id="user_999",
                destination="Rome, Italy",
                start_date=date(2024, 11, 1),
                end_date=date(2024, 11, 6),
                travelers=2,
                status="DRAFT",
            ),
        ]

    def list_upcoming_trips(self, user_id: str) -> List[Trip]:
        return [t for t in self._trips if t.user_id == user_id]


class InMemoryFavoritePlaceRepository(FavoritePlaceRepository):
    def __init__(self) -> None:
        self._favorites: List[FavoritePlace] = [
            FavoritePlace(id="fav_bali_001", user_id="user_123", name="Bali", country="Indonesia"),
            FavoritePlace(id="fav_zermatt_001", user_id="user_123", name="Zermatt", country="Switzerland"),
            FavoritePlace(id="fav_other_001", user_id="user_999", name="Cairo", country="Egypt"),
        ]

    def list_favorites(self, user_id: str) -> List[FavoritePlace]:
        return [p for p in self._favorites if p.user_id == user_id]