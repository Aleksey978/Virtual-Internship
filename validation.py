from pydantic import BaseModel
from typing import List

from models import PerevalStatus


class UserBase(BaseModel):
    email: str
    fam: str
    name: str
    otc: str
    phone: str

class CoordsBase(BaseModel):
    latitude: float
    longitude: float
    height: float

class LevelBase(BaseModel):
    winter: str
    summer: str
    autumn: str
    spring: str

class ImageBase(BaseModel):
    data: bytes
    title: str

class PerevalBase(BaseModel):
    beauty_title: str
    title: str
    other_titles: str
    connect: str
    add_time: str
    user: UserBase
    status: PerevalStatus = PerevalStatus.new
    coords: CoordsBase
    level: LevelBase
    images: List[ImageBase]


class UpdateResponse(BaseModel):
    state: int
    message: str