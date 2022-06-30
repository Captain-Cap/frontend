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

    def get_by_id(self, uid: int) -> BalloonModel:
        response = httpx.get(f'{self.url}/api/v1/balloons/{uid}')
        response.raise_for_status()
        payload = response.json()

        return BalloonModel(**payload)

    def add(self, balloon: BalloonModel) -> BalloonModel:
        json_balloon = orjson.dumps(balloon.dict())
        headers = {
            'Content-Type': 'application/json',
        }
        respose = httpx.post(f'{self.url}/api/v1/balloons/', content=json_balloon, headers=headers)
        respose.raise_for_status()

        payload = respose.json()
        return BalloonModel(**payload)

    def delete(self, uid) -> None:
        response = httpx.delete(f'{self.url}/api/v1/balloons/{uid}')
        response.raise_for_status()

    def update(self, balloon: BalloonModel) -> None:
        json_balloon = orjson.dumps(balloon.dict())
        headers = {
            'Content-Type': 'application/json',
        }
        response = httpx.put(f'{self.url}/api/v1/balloons/', content=json_balloon, headers=headers)
        response.raise_for_status()

    def get_balloons_by_name_project(self, name) -> list[BalloonModel]:
        response = httpx.get(f'{self.url}/api/v1/balloons/{name}')
        response.raise_for_status()
        return [BalloonModel(**balloon) for balloon in response.json()]
