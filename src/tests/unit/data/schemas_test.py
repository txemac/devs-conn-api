from datetime import datetime

import pytest
from pydantic import ValidationError

from data.schemas import OrganisationDB
from data.schemas import OrganisationPost
from data.schemas import RealtimeDB
from data.schemas import RealtimeGet
from data.schemas import RealtimePost
from data.schemas import UserDB
from data.schemas import UserPost


def test_user_post_ok():
    assert UserPost(name='name') is not None


@pytest.mark.parametrize('name', [None, '', 'a' * 151])
def test_user_post_name_wrong(name):
    with pytest.raises(ValidationError):
        UserPost(name=name)


def test_user_db_ok():
    assert UserDB(id=1, name='name', registered_at=datetime.now()) is not None


def test_organisation_post_ok():
    assert OrganisationPost(name='name') is not None


@pytest.mark.parametrize('name', [None, '', 'a' * 151])
def test_organisation_post_name_wrong(name):
    with pytest.raises(ValidationError):
        OrganisationPost(name=name)


def test_organisation_db_ok():
    assert OrganisationDB(id=1, name='name', registered_at=datetime.now()) is not None


def test_realtime_get_ok():
    assert RealtimeGet(user_1_id=1, user_2_id=2) is not None


@pytest.mark.parametrize('connected', [True, False])
def test_realtime_post_ok(connected):
    assert RealtimePost(
        user_1='txemac',
        user_2='fever',
        connected=connected,
        organisations=['organisation_1']) is not None


@pytest.mark.parametrize('connected', [True, False])
def test_realtime_db_ok(connected):
    assert RealtimeDB(
        id=1,
        user_1='txemac',
        user_2='fever',
        connected=connected,
        organisations=['organisation_1'],
        registered_at=datetime.now()) is not None
