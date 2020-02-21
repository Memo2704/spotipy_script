from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
Base = declarative_base()


def engine_creation():
    db_string = 'postgresql://admin:password@localhost:5432/spotify_db'
    engine = create_engine(db_string)
    return engine


class Tracks(Base):
    __tablename__ = 'tracks'

    id = Column(Integer, primary_key=True)
    name = Column(String)


def base_metadata():
    create_base = Base.metadata.create_all(engine_creation())
    return create_base


