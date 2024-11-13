from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Enum
import enum

Base = declarative_base()

class PerevalStatus(enum.Enum):
    new = "new"
    pending = "pending"
    accepted = "accepted"
    rejected = "rejected"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    fam = Column(String)
    name = Column(String)
    otc = Column(String)
    phone = Column(String)


class Coords(Base):
    __tablename__ = "coords"

    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    height = Column(Float)


class Level(Base):
    __tablename__ = "levels"

    id = Column(Integer, primary_key=True, index=True)
    winter = Column(String)
    summer = Column(String)
    autumn = Column(String)
    spring = Column(String)


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(String)
    title = Column(String)
    pereval_id = Column(Integer, ForeignKey("perevals.id"))
    pereval = relationship("Pereval", back_populates="images")


class Pereval(Base):
    __tablename__ = "perevals"

    id = Column(Integer, primary_key=True, index=True)
    beauty_title = Column(String)
    title = Column(String)
    other_titles = Column(String)
    connect = Column(String)
    add_time = Column(String)
    status = Column(Enum(PerevalStatus), default=PerevalStatus.new)

    user_id = Column(Integer, ForeignKey("users.id"))
    coords_id = Column(Integer, ForeignKey("coords.id"))
    level_id = Column(Integer, ForeignKey("levels.id"))

    user = relationship("User")
    coords = relationship("Coords")
    level = relationship("Level")
    images = relationship("Image", back_populates="pereval")