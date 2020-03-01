from datetime import datetime

import pytest
from pydantic import ValidationError

from data.schemas import OrganisationDB
from data.schemas import OrganisationPost
from data.schemas import RealtimeDB
from data.schemas import RealtimeGet
from data.schemas import RealtimeOut
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
    assert RealtimeGet(user_1='txemac', user_2='jobandtalent') is not None


@pytest.mark.parametrize('name1', [None, '', 'a' * 151])
@pytest.mark.parametrize('name2', [None, '', 'a' * 151])
def test_realtime_get_name_worng(name1, name2):
    with pytest.raises(ValidationError):
        RealtimeGet(
            user_1=name1,
            user_2=name2,
        )


@pytest.mark.parametrize('connected', [True, False])
def test_realtime_post_ok(connected):
    assert RealtimePost(
        user_1='txemac',
        user_2='jobandtalent',
        connected=connected,
        organisations=['organisation_1']) is not None


@pytest.mark.parametrize('connected', [True, False])
def test_realtime_db_ok(connected):
    assert RealtimeDB(
        id=1,
        user_1='txemac',
        user_2='jobandtalent',
        connected=connected,
        organisations=['organisation_1'],
        registered_at=datetime.now()) is not None


@pytest.mark.parametrize('name1', [None, '', 'a' * 151])
@pytest.mark.parametrize('name2', [None, '', 'a' * 151])
@pytest.mark.parametrize('connected', [None, 123, 'hola'])
def test_realtime_post_wrong(name1, name2, connected):
    with pytest.raises(ValidationError):
        RealtimePost(
            user_1=name1,
            user_2=name2,
            connected=connected,
            organisations=['organisation_1'])


@pytest.mark.parametrize('name1', [None, '', 'a' * 151])
@pytest.mark.parametrize('name2', [None, '', 'a' * 151])
@pytest.mark.parametrize('connected', [None, 123, 'hola'])
def test_realtime_db_wrong(name1, name2, connected):
    with pytest.raises(ValidationError):
        assert RealtimeDB(
            id=1,
            user_1=name1,
            user_2=name2,
            connected=connected,
            organisations=['organisation_1'],
            registered_at=datetime.now())


@pytest.mark.parametrize('connected', [True, False])
@pytest.mark.parametrize('organisations', [['organisation_!'], None])
def test_realtime_out_ok(connected, organisations):
    assert RealtimeOut(
        registered_at=datetime.now(),
        connected=connected,
        organisations=organisations,
    ) is not None


@pytest.mark.parametrize('connected', [None, 123, 'hola'])
def test_realtime_out_wrong(connected):
    with pytest.raises(ValidationError):
        assert RealtimeOut(
            registered_at=datetime.now(),
            connected=connected,
            organisations=['organisation_!']
        )
