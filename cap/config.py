import os
from dataclasses import dataclass


@dataclass
class Config:

    app_host: str
    app_port: int


config = Config(
    os.environ['APP_HOST'],
    int(os.environ['APP_PORT']),
)
