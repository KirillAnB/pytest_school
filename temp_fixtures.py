import pytest


@pytest.fixture
def db_connector():
    print("Db connetcion setup")
    yield
    print("DB connection teardown")

@pytest.fixture()
def data_for_test():
    data = [1, None, 42]
    return data


