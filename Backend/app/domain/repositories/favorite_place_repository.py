from abc import ABC, abstractmethod
from typing import List
from app.domain.entities.favorite_place import FavoritePlace


class FavoritePlaceRepository(ABC):
    @abstractmethod
    def list_favorites(self, user_id: str) -> List[FavoritePlace]:
        raise NotImplementedError