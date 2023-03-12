import pytest


@pytest.mark.run_this_please
def test_pow():
    a,b = 2,3
    assert a**b == 8