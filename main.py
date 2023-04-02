
import pytest

def main_print():
    print("activate test")
    yield
    print("deactivate test")

def awesome_func(param):
    if not isinstance(param, str):
        raise TypeError
    print(param)
def crud(username):
    print(f"Creating user {username} ")
    if isinstance(username, str):
        return True
    else:
        return False
