def assert_dicts(original, expected):
    """
    Assert that check that the dict body contains all keys in expected.
    And the values are the same.
    If a value in expected contains "*" the value in body can be any value.
    If a value is a dict, check the dict inside.
    If a value is a list, check the list inside.

    :param Dict original: original dict
    :param Dict expected: expected dict
    """
    for key in expected.keys():
        assert key in original.keys(), key
        if type(original[key]) == dict:
            assert type(expected[key]) == dict
            assert_dicts(original=original[key], expected=expected[key])
        elif type(original[key]) == list:
            assert type(expected[key]) == list
            assert_lists(original=original[key], expected=expected[key])
        elif not expected[key] == '*' and original[key] is not None:
            assert original[key] == expected[key], key


def assert_lists(original, expected):
    """
    Assert that check to lists. Check the len of both list and the content.

    :param List original: original list
    :param List expected: expected list
    """
    assert len(original) == len(expected), len(original)
    for i in range(len(original)):
        if type(original[i]) == dict:
            assert type(expected[i]) == dict, type(expected[i])
            assert_dicts(original=original[i], expected=expected[i])
        elif type(original[i]) == list:
            assert type(expected[i]) == list, type(expected[i])
            assert_lists(original=original[i], expected=expected[i])
        elif not expected[i] == '*':
            assert original[i] == expected[i], original[i]
