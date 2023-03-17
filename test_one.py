import pytest
import main
from test_2 import print_init
A = 42


@pytest.mark.skipif(A == 42,reason="because 42")
def test_add():
    a,b = 2,5
    assert a+b == 7
# @pytest.mark.skip()
def test_remove():
    a,b = 7,4
    assert a - b == 3
@pytest.mark.xfail
def test_equlity():
    a,b = 7,7
    assert a == b


def test_type_error(print_init):
    a = 'text'
    with pytest.raises(TypeError):
        main.awesome_func(a)