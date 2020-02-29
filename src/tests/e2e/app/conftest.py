import pytest


@pytest.fixture
def mock_twitter_get_friends(mocker):
    return mocker.patch('data.twitter_api_client.get_friends')


@pytest.fixture
def mock_github_get_organisations(mocker):
    return mocker.patch('data.github_api_client.get_organisations')
