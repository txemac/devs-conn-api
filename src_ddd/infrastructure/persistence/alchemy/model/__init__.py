import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(os.getenv('DATABASE_URL'))
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)


def add(obj):
    session.add(obj)
    try:
        session.commit()
    except Exception:
        session.rollback()
        raise


from infrastructure.persistence.alchemy.model.dev import Dev
from infrastructure.persistence.alchemy.model.register import Register
