from datetime import datetime
from typing import Optional

from pydantic import BaseModel, PositiveInt


class BalloonModel(BaseModel):

    uid: Optional[PositiveInt]
    firm: str
    paint_code: str
    color: str
    volume: int
    weight: PositiveInt
    acceptance_date: Optional[datetime]

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class ProjectsModel(BaseModel):

    uid: PositiveInt
    name: str
    created_at: datetime

    class Config:
        orm_mode = True
