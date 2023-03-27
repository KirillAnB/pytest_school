import pytest
import main

a = 'text1'

@pytest.fixture()
def printer():
    print("connection to db")
    yield
    print("connection closed")
@pytest.mark.parametrize('a',[3,4,5])
@pytest.mark.parametrize('b',[5,4,3])
def test_add(printer, a, b):
    assert a+b == 7
# @pytest.mark.skip()

@pytest.mark.parametrize('a',[1,2,3,4,5,6,7,8])
def test_remove(printer, a):
    b = 4
    assert a - b == 3
@pytest.mark.mirror
@pytest.mark.smoke
def test_equlity():
    a,b = 7,7
    assert a == b

@pytest.mark.skipif(a == 'text', reason="var is a str")
def test_type_error():
    a = 'text'
    with pytest.raises(TypeError):
        main.awesome_func(a)
