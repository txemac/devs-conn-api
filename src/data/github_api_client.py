from typing import Union

from github import Github
from github import UnknownObjectException
from github.NamedUser import NamedUser

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


def get_user(
        username: str,
) -> Union[NamedUser, None]:
    """
    Get user.

    :param str username: username
    :return NamedUser: GitHub user
    """
    try:
        return _get_github_api_client().get_user(login=username)
    except UnknownObjectException:
        return None
