import httpx

from cap.api.schemas import ProjectsModel


class ProjectsApi:

    def __init__(self, url: str) -> None:
        self.url = url

    def get_all(self) -> list[ProjectsModel]:
        response = httpx.get(f'{self.url}/api/v1/projects/')
        response.raise_for_status()
        return [ProjectsModel(**project) for project in response.json()]
