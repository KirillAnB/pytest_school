import pytest
import main


a = 'text'

def test_add():
    a,b = 2,5
    assert a+b == 7
# @pytest.mark.skip()
def test_remove():
    a,b = 7,4
    assert a - b == 3
@pytest.mark.xfail
def test_equlity():
    a,b = 7,8
    assert a == b

@pytest.mark.skipif(a=='text', reason='A is the text')
def test_type_error():
    a = 'text'
    with pytest.raises(TypeError):
        main.awesome_func(a)
