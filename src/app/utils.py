from typing import List


def get_connections(
        dev1: str,
        dev2: str,
        twitter_user_1: List[str],
        twitter_user_2: List[str],
        github_user_1: List[str],
        github_user_2: List[str],
) -> (bool, List[str]):
    """
    Get response with info of connections.

    :param dev1: dev1
    :param dev2: dev2
    :param twitter_user_1: list friends user 1
    :param twitter_user_2: list friends user 2
    :param github_user_1: list organisations user 1
    :param github_user_2: list organisations user 2
    :return tuple: connected and organisations
    """
    organisations = list(set(github_user_1) & set(github_user_2))

    connected_twitter = dev2 in twitter_user_1 and dev1 in twitter_user_2
    connected_github = len(organisations) > 0

    return connected_twitter and connected_github, organisations
