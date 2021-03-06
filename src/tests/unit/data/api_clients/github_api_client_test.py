import pytest

from data.api_clients import github_api_client


@pytest.fixture
def mock_github_api_client(mocker):
    return mocker.patch('data.api_clients.github_api_client._github_api_client')


def test_get_organisations_ok(mock_github_api_client):
    mock_github_api_client.get_orgs.side_effect = []
    assert github_api_client.get_organisations(username='txemac') == []
