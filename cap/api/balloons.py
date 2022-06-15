import os

import httpx
import orjson

from cap.model.schemas import BalloonModel


class BalloonApi:

    def __init__(self):
        self.backend_url = os.environ['BACKEND_URL']
        self.url = '/api/v1/balloons/'

    def get_all(self) -> list[BalloonModel]:
        response = httpx.get(self.backend_url + self.url)
        response.raise_for_status()

        return [BalloonModel(
            uid=balloon['uid'],
            firm=balloon['firm'],
            paint_code=balloon['paint_code'],
            color=balloon['color'],
            volume=balloon['volume'],
            weight=balloon['weight'],
            acceptance_date=balloon['acceptance_date'],
        ) for balloon in response.json()
        ]

    def add(self, balloon: BalloonModel) -> None:
        json_balloon = orjson.dumps(BalloonModel.from_orm(balloon).dict())
        headers = {
            'Content-Type': 'application/json',
        }
        httpx.post(self.backend_url + self.url, data=json_balloon, headers=headers)
