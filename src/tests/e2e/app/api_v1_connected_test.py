from starlette.status import HTTP_200_OK

from data.models.realtime import Realtime


def test_real_time_true(client, session, mock_twitter_get_friends, mock_github_get_organisations):
    count_1 = session.query(Realtime).count()
    dev1 = 'txemac'
    dev2 = 'fever'
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
    dev2 = 'fever'
    mock_twitter_get_friends.return_value = [dev1]
    mock_github_get_organisations.return_value = ['organisation_1']

    response = client.get(f'/api/v1/connected/realtime/{dev1}/{dev2}')

    assert response.status_code == HTTP_200_OK
    assert response.json() == dict(connected=False)

    count_2 = session.query(Realtime).count()
    assert count_1 + 1 == count_2
