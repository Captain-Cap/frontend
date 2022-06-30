from datetime import datetime

from pydantic import BaseModel, PositiveInt


class BalloonModel(BaseModel):

    uid: int
    firm: str
    paint_code: str
    color: str
    volume: int
    weight: float
    acceptance_date: datetime
    project: str

    @property
    def acceptance(self) -> str:
        return self.acceptance_date.strftime('%m/%d/%Y %H:%M:%S')

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class ProjectsModel(BaseModel):

    uid: PositiveInt
    name: str
    created_at: datetime

    class Config:
        orm_mode = True
