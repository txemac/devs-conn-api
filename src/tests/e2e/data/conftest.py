import pytest


@pytest.fixture
def mock_twitter_api_client(mocker):
    return mocker.patch('data.twitter_api_client._twitter_api_client')


@pytest.fixture
def mock_twitter_get_friends(mocker):
    return mocker.patch('data.twitter_api_client._get_friends')


@pytest.fixture
def mock_github_api_client(mocker):
    return mocker.patch('data.github_api_client._github_api_client')
