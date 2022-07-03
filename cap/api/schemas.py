from datetime import datetime
from typing import Optional

from pydantic import BaseModel, PositiveInt


class BalloonModel(BaseModel):

    uid: int
    firm: str
    paint_code: str
    color: str
    volume: int
    weight: float
    acceptance_date: datetime
    project_id: Optional[int]

    @property
    def acceptance(self) -> str:
        return self.acceptance_date.strftime('%m/%d/%Y %H:%M:%S')

    @property
    def project(self) -> int:
        uid = 0
        if self.project_id is not None:
            uid = self.project_id
        return uid

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class ProjectsModel(BaseModel):

    uid: PositiveInt
    name: str
    created_at: datetime

    class Config:
        orm_mode = True
