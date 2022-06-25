from cap.api.balloons import BalloonApi
from cap.api.projects import ProjectsApi
from cap.config import config


class ApiClient:

    def __init__(self, url: str) -> None:
        self.balloons = BalloonApi(url)
        self.projects = ProjectsApi(url)


client = ApiClient(config.url)
