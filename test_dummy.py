def test_always_passes():
    assert True is True

# not a test
def somef():
    assert True is True


def test_tuple():
    assert (1, 2, 3) == (3, 2, 1)[::-1]