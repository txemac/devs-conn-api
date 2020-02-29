from unittest.mock import Mock

import pytest
from twitter import TwitterError

from data import twitter_api_client


@pytest.fixture
def mock_twitter_api_client(mocker):
    return mocker.patch('data.twitter_api_client._twitter_api_client')


def test_get_friends_ok(mock_twitter_api_client):
    user = Mock()
    user.screen_name = 'fever'
    mock_twitter_api_client.GetFriends.return_value = [user]
    assert twitter_api_client.get_friends(username='txemac') == ['fever']


def test_get_friends_error(mock_twitter_api_client):
    mock_twitter_api_client.GetFriends.side_effect = TwitterError
    assert twitter_api_client.get_friends(username='txemac') == "txemac is no a valid user in twitter"
