from typing import List
from typing import Union

from github import Github
from github import GithubException

import secrets

_github_api_client = None


def _get_github_api_client():
    """
    Singleton to get a mongoDB client.

    :return MongoClient: client
    """
    global _github_api_client
    if _github_api_client is None:
        _github_api_client = Github(
            login_or_token=secrets.GITHUB_USER,
            password=secrets.GITHUB_PASSWORD,
        )
    return _github_api_client


def get_organisations(
        username: str,
) -> Union[List[str], str]:
    """
    Get list of organisations from user.

    :param str username: username
    :return NamedUser: GitHub user
    """
    try:
        user = _get_github_api_client().get_user(login=username)
        orgs = user.get_orgs()
        result = [x.login for x in orgs]
        return result
    except GithubException:
        return f"{username} is no a valid user in github"
