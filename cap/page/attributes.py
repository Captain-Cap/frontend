from cap.api.client import client
from cap.api.schemas import BalloonModel, ProjectsModel


class Attributes:

    def __init__(self) -> None:
        self.balloon = Balloon()
        self.project = Project()


class Balloon:

    def __init__(self) -> None:
        self.balloons = client.balloons.get_all()

    def all(self, status: bool) -> list[tuple[BalloonModel, str]]:
        all_free = [balloon for balloon in self.balloons if not balloon.project_id]
        all_in_project = [balloon for balloon in self.balloons if balloon.project_id]
        return self._model(all_free) if status else self._model(all_in_project)

    def color_from(self, balloons: list[BalloonModel]) -> list[str]:
        color = []
        for balloon in balloons:
            if balloon.color not in color:
                color.append(balloon.color)
        return color

    def by_color(self, models, color: str) -> list[tuple[BalloonModel, str]]:
        entity = []
        if color == 'No color':
            entity = models
        else:
            entity = [entity for entity in models if entity[0].color == color]
        return entity

    def _model(self, balloons: list[BalloonModel]) -> list[tuple[BalloonModel, str]]:
        project_map = attributes.project.project_map()
        models = []
        for balloon in balloons:
            project = project_map[balloon.project_id] if balloon.project_id else None
            project_name = project.name if project else 'No project'
            models.append((balloon, project_name))
        return models


class Project:

    def __init__(self) -> None:
        self.projects = client.projects.get_all()

    def all(self) -> list[ProjectsModel]:
        return self.projects

    def project_map(self) -> dict[int, ProjectsModel]:
        return {project.uid: project for project in self.projects}


attributes = Attributes()
