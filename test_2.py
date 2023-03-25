import pytest

@pytest.fixture()
def print_init():
    print("Init testing")
    yield
    print("Deactivate testing")

def test_pow(print_init):
    a,b = 2,3
    assert a**b == 8