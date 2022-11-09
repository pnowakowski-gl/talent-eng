# positive and negative tests for main python types: int, float, bool, strings, lists, tuples, dicts
def test_check_if_int():
    assert type(3) == int


def test_check_if_float():
    assert type(3.14) == float


def test_check_if_boolen():
    assert type(False) == bool


def test_check_if_string():
    assert type("string to test") == str


def test_check_if_list():
    assert type(["a", "b", 1, 2]) == list


def test_check_if_dict():
    assert type({"a": 1, "b": 2}) == dict


def test_check_if_tuple():
    assert type((1, 2, 3)) == tuple


def test_check_if_not_dict():
    assert type({1, 4, 444}) == dict


def test_check_if_not_int():
    assert type("2") == int
