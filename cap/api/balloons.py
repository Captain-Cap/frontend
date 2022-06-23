import httpx
import orjson

from cap.api.schemas import BalloonModel


class BalloonApi:

    def __init__(self, url: str) -> None:
        self.url = url

    def get_all(self) -> list[BalloonModel]:
        response = httpx.get(f'{self.url}/api/v1/balloons/')
        response.raise_for_status()
        return [BalloonModel(**balloon) for balloon in response.json()]

    def add(self, balloon: BalloonModel) -> BalloonModel:
        json_balloon = orjson.dumps(balloon.dict())
        headers = {
            'Content-Type': 'application/json',
        }
        respose = httpx.post(f'{self.url}/api/v1/balloons/', data=json_balloon, headers=headers)
        respose.raise_for_status()

        balloon = respose.json()
        return BalloonModel(**balloon)

    def delete(self, uid) -> None:
        response = httpx.delete(f'{self.url}/api/v1/balloons/{uid}')
        response.raise_for_status()
