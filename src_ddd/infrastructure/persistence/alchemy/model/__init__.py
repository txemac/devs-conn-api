from config.persistence import database_settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(database_settings.SQLALCHEMY_DATABASE_URI)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)


def add(obj):
    session.add(obj)
    try:
        session.commit()
    except:
        session.rollback()
        raise
