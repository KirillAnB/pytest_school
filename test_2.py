import pytest
from temp_fixtures import db_connector

@pytest.fixture()
def print_init():
    print("Init testing")
    yield
    print("Deactivate testing")

def test_pow(db_connector):
    a,b = 2,3
    assert a**b == 8