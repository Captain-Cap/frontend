from datetime import datetime
from typing import Optional

from pydantic import BaseModel


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

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class ProjectsModel(BaseModel):

    uid: int
    name: str
    created_at: datetime

    class Config:
        orm_mode = True
