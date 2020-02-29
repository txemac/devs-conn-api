from typing import List

from twitter import Api
from twitter import TwitterError

import secrets

_twitter_api_client = None


def _get_twitter_api_client():
    """
    Singleton to get a mongoDB client.

    :return MongoClient: client
    """
    global _twitter_api_client
    if _twitter_api_client is None:
        _twitter_api_client = Api(
            consumer_key=secrets.TWITTER_CONSUMER_KEY,
            consumer_secret=secrets.TWITTER_CONSUMER_SECRET,
            access_token_key=secrets.TWITTER_ACCESS_TOKEN_KEY,
            access_token_secret=secrets.TWITTER_ACCESS_TOKEN_SECRET,
        )
    return _twitter_api_client


def _get_friends(
        username: str
) -> List[str]:
    """
    Get a list of screen_name of friends from a user.

    :param str username: username
    :return List: friends
    """
    return [u.screen_name for u in _get_twitter_api_client().GetFriends(screen_name=username)]


def is_valid_user(
        username: str
) -> bool:
    """
    Check if the username is a valid user.

    :param str username: username
    :return bool: is valid
    """
    try:
        _get_twitter_api_client().GetUser(screen_name=username)
    except TwitterError:
        return False
    return True


def is_friends(
        username_1: str,
        username_2: str,
) -> bool:
    """
    Return True if username 1 follows username 2 on twitter, and 2 follows 1.

    :return bool: friends
    """
    if username_2 in _get_friends(username=username_1) and \
            username_1 in _get_friends(username=username_2):
        return True
    return False
