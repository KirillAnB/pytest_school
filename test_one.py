import pytest


def test_add():
    a,b = 2,5
    assert a+b == 7
@pytest.mark.skip()
def test_remove():
    a,b = 7,4
    assert a - b == 3