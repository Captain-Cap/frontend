import os
from dataclasses import dataclass


@dataclass
class Config:

    app_host: str
    app_port: int
    url: str


config = Config(
    app_host=os.environ['APP_HOST'],
    app_port=int(os.environ['APP_PORT']),
    url=os.environ['BACKEND_URL'],
)
