from sqlalchemy import create_engine # import create_engine from sqlalchemy
from sqlalchemy.orm import sessionmaker # import sessionmaker from sqlalchemy.orm
from sqlalchemy.orm import DeclarativeBase # import DeclarativeBase from sqlalchemy.orm

from app.core.config import settings # import settings from app.core.config


# create database url:
DATABASE_URL = (
    f"postgresql://"
    f"{settings.POSTGRES_USER}:"
    f"{settings.POSTGRES_PASSWORD}@"
    f"{settings.POSTGRES_HOST}:"
    f"{settings.POSTGRES_PORT}/"
    f"{settings.POSTGRES_DB}"
)


# create engine:
engine = create_engine(
    DATABASE_URL,
    echo=False
)

# create session local:
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


# create base class:
class Base(DeclarativeBase):
    pass


# create get_db function:
def get_db():

    db = SessionLocal() # create session

    try:
        yield db # yield session

    finally:
        db.close() # close session