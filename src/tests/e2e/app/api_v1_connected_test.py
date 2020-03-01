from starlette.status import HTTP_200_OK

from data.database.realtime import Realtime
from data.schemas import RealtimePost
from tests.utils import assert_lists


def test_real_time_true(client, session, mock_twitter_get_friends, mock_github_get_organisations):
    count_1 = session.query(Realtime).count()
    dev1 = 'txemac'
    dev2 = 'jobandtalent'
    organisations = ['organisation_1']
    mock_twitter_get_friends.return_value = [dev1, dev2]
    mock_github_get_organisations.return_value = organisations

    response = client.get(f'/api/v1/connected/realtime/{dev1}/{dev2}')
    assert response.status_code == HTTP_200_OK
    assert response.json() == dict(connected=True, organisations=organisations)

    count_2 = session.query(Realtime).count()
    assert count_1 + 1 == count_2


def test_real_time_false(client, session, mock_twitter_get_friends, mock_github_get_organisations):
    count_1 = session.query(Realtime).count()
    dev1 = 'txemac'
    dev2 = 'jobandtalent'
    mock_twitter_get_friends.return_value = [dev1]
    mock_github_get_organisations.return_value = ['organisation_1']

    response = client.get(f'/api/v1/connected/realtime/{dev1}/{dev2}')
    assert response.status_code == HTTP_200_OK
    assert response.json() == dict(connected=False)

    count_2 = session.query(Realtime).count()
    assert count_1 + 1 == count_2


def test_register_empty(client, session):
    dev1 = 'txemac'
    dev2 = 'jobandtalent'

    response = client.get(f'/api/v1/connected/register/{dev1}/{dev2}')
    assert response.status_code == HTTP_200_OK
    assert response.json() == []


def test_register(client, session):
    dev1 = 'txemac'
    dev2 = 'jobandtalent'
    data_1 = RealtimePost(
        user_1=dev1,
        user_2=dev2,
        connected=True,
        organisations=['organisation_1'],
    )
    Realtime.create(db_session=session, data=data_1)
    data_2 = RealtimePost(
        user_1=dev2,
        user_2=dev1,
        connected=False,
    )
    Realtime.create(db_session=session, data=data_2)

    response = client.get(f'/api/v1/connected/register/{dev1}/{dev2}')
    assert response.status_code == HTTP_200_OK
    expected = [
        dict(
            registered_at='*',
            connected=data_1.connected,
            organisations=data_1.organisations,
        ),
        dict(
            registered_at='*',
            connected=data_2.connected,
        ),
    ]
    assert_lists(original=response.json(), expected=expected)
