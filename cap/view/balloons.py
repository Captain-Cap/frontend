from dataclasses import dataclass
from datetime import datetime

import httpx


@dataclass
class Balloon:
    firm: str
    paint_code: str
    color: str
    volume: int
    weight: int
    acceptance_date: datetime


class Balloons:
    url = 'http://127.0.0.1:5000/api/v1/balloons/'

    def get_balloons(self) -> list[Balloon]:
        response = httpx.get(self.url)
        response.raise_for_status()

        return [Balloon(
            firm=balloon['firm'],
            paint_code=balloon['paint_code'],
            color=balloon['color'],
            volume=balloon['volume'],
            weight=balloon['weight'],
            acceptance_date=balloon['acceptance_date'],
        ) for balloon in response.json()
        ]
