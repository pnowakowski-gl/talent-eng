from some_func import check_type

# homework#2 create positive and negative tests for main python types: int, float, bool, strings, lists, tuples, dicts
def test_check_if_int():
    assert check_type(3) == int


def test_check_if_float():
    assert check_type(3.14) == float


def test_check_if_boolen():
    assert check_type(False) == bool


def test_check_if_string():
    assert check_type("string to test") == str


def test_check_if_list():
    assert check_type(["a", "b", 1, 2]) == list


def test_check_if_dict():
    assert check_type({"a": 1, "b": 2}) == dict


def test_check_if_tuple():
    assert check_type((1,2,3)) == tuple


def test_check_if_not_dict():
    assert check_type({1,4,444}) == dict


def test_check_if_not_int():
    assert check_type("2") == int
