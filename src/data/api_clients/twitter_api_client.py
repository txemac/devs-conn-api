from typing import List
from typing import Union

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


def get_friends(
        username: str
) -> Union[str, List[str]]:
    """
    Get a list of friends from a user.

    :param str username: username
    :return list: friends or error
    """
    try:
        return [u.screen_name for u in _get_twitter_api_client().GetFriends(screen_name=username)]
    except TwitterError:
        return f"{username} is no a valid user in twitter"
