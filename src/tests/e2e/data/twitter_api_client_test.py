import pytest
from twitter import TwitterError

from data import twitter_api_client


@pytest.mark.parametrize('return_get_user, expected',
                         [('txemac', True),
                          (TwitterError, False)])
def test_is_valid_user_true(mock_twitter_api_client, return_get_user, expected):
    mock_twitter_api_client.GetUser.side_effect = return_get_user
    assert twitter_api_client.is_valid_user(username='txemac') is expected


@pytest.mark.parametrize('return_get_friends, expected',
                         [(['txemac', 'fever'], True),
                          (['txemac'], False)])
def test_is_user_friends_ok(mock_twitter_get_friends, return_get_friends, expected):
    mock_twitter_get_friends.return_value = return_get_friends
    assert twitter_api_client.is_friends(username_1='txemac', username_2='fever') is expected
