import httpx
import orjson

from cap.api.schemas import ProjectsModel


class ProjectsApi:

    def __init__(self, url: str) -> None:
        self.url = url

    def get_all(self) -> list[ProjectsModel]:
        response = httpx.get(f'{self.url}/api/v1/projects/')
        response.raise_for_status()
        return [ProjectsModel(**project) for project in response.json()]

    def get_by_id(self, uid: int) -> ProjectsModel:
        response = httpx.get(f'{self.url}/api/v1/projects/{uid}')
        response.raise_for_status()
        return ProjectsModel(**response.json())

    def update(self, project: ProjectsModel):
        json_project = orjson.dumps(project.dict())
        headers = {
            'Content-Type': 'application/json',
        }
        response = httpx.put(f'{self.url}/api/v1/projects/', content=json_project, headers=headers)
        response.raise_for_status()
