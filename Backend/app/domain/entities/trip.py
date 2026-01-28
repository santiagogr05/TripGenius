from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Trip:
    id: str
    user_id: str
    destination: str
    start_date: date
    end_date: date
    travelers: int
    status: str