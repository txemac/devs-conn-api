from github import NamedUser

from data import github_api_client


def test_is_valid_user_true(mock_github_api_client):
    mock_github_api_client.get_user.return_value = NamedUser
    assert github_api_client.get_user(username='txemac') is not None
