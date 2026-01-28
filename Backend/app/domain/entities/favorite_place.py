from dataclasses import dataclass


@dataclass(frozen=True)
class FavoritePlace:
    id: str
    user_id: str
    name: str
    country: str