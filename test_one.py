import pytest
import main

a = 'text1'


def test_add():
    a,b = 2,5
    assert a+b == 7
# @pytest.mark.skip()
def test_remove():
    a,b = 7,4
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
