import os
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


class BalloonApi:
    BACKEND_URL = os.environ['BACKEND_URL']
    url = '/api/v1/balloons/'

    def get_all(self) -> list[Balloon]:
        response = httpx.get(self.BACKEND_URL + self.url)
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
