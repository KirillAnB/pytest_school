
import pytest

def main_print():
    print("activate test")
    yield
    print("deactivate test")

def awesome_func(param):
    if not isinstance(param, int):
        raise TypeError
    print(param)

