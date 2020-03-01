import pytest

from app.utils import get_connections


@pytest.mark.parametrize('dev1, dev2, twitter_user_1, twitter_user_2, github_user_1, github_user_2, connected, orgs',
                         [('txemac', 'jobandtalent', ['jobandtalent'], ['txemac'], ['org1'], ['org1'], True, ['org1']),
                          ('txemac', 'jobandtalent', ['jobandtalent'], ['txemac'], ['org1'], ['org2'], False, []),
                          ('txemac', 'jobandtalent', ['jobandtalent'], ['other'], ['org1'], ['org1'], False, ['org1']),
                          ('txemac', 'jobandtalent', ['other'], ['txemac'], ['org1'], ['org1'], False, ['org1']),
                          ('txemac', 'jobandtalent', ['jobandtalent'], ['txemac'], ['org1'], [], False, []),
                          ('txemac', 'jobandtalent', ['jobandtalent'], ['txemac'], [], ['org1'], False, [])])
def test_get_connections(dev1, dev2, twitter_user_1, twitter_user_2, github_user_1, github_user_2, connected, orgs):
    assert get_connections(
        dev1=dev1,
        dev2=dev2,
        twitter_user_1=twitter_user_1,
        twitter_user_2=twitter_user_2,
        github_user_1=github_user_1,
        github_user_2=github_user_2,
    ) == (connected, orgs)
