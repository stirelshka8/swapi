from sqlalchemy import Column, Integer, String
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base


DB_HOST = 'admlab.ddns.net'
DB_PORT = 5432
DB_DIALECT = 'postgresql'
DB_DRIVER = 'asyncpg'
DB_USER = 'test'
DB_PASSWORD = '5512'
DB_NAME = 'test'


db_url = URL.create(
    drivername='+'.join([DB_DIALECT, DB_DRIVER]),
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME
)


engine = create_async_engine(db_url, echo=True)
Base = declarative_base()
Session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class People(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    birth_year = Column(String(length=300))
    eye_color = Column(String(length=300))
    films = Column(String(length=600))
    gender = Column(String(length=300))
    hair_color = Column(String(length=300))
    height = Column(String(length=30))
    homeworld = Column(String(length=300))
    mass = Column(String(length=300))
    name = Column(String(length=300))
    skin_color = Column(String(length=300))
    species = Column(String(length=600))
    starships = Column(String(length=600))
    vehicles = Column(String(length=600))
