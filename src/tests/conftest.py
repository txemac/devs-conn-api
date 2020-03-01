import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy_utils import create_database
from sqlalchemy_utils import database_exists
from sqlalchemy_utils import drop_database
from starlette.testclient import TestClient

from app.main import app
from data import Base
from data import get_db
from data.schemas import OrganisationPost
from data.schemas import UserPost


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


url = f'{os.getenv("DATABASE_URL")}_test'
_db_conn = create_engine(url)


def get_test_db_conn():
    assert _db_conn is not None
    return _db_conn


def get_test_db():
    sess = Session(bind=_db_conn)

    try:
        yield sess
    finally:
        sess.close()


@pytest.fixture(scope="session", autouse=True)
def database():
    if database_exists(url):
        drop_database(url)
    create_database(url)
    Base.metadata.create_all(_db_conn)
    app.dependency_overrides[get_db] = get_test_db
    yield
    drop_database(url)


@pytest.yield_fixture
def session():
    db_session = Session(bind=_db_conn)

    yield db_session
    for tbl in reversed(Base.metadata.sorted_tables):
        _db_conn.execute(tbl.delete())
    db_session.close()


@pytest.fixture
def new_user():
    return UserPost(name='txemac')


@pytest.fixture
def new_organisation():
    return OrganisationPost(name='organisation_1')
