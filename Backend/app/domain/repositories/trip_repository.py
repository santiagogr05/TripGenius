from abc import ABC, abstractmethod
from typing import List
from app.domain.entities.trip import Trip


class TripRepository(ABC):
    @abstractmethod
    def list_upcoming_trips(self, user_id: str) -> List[Trip]:
        raise NotImplementedError