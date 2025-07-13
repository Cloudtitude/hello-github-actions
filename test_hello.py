import pytest
from hello import greet

def test_greeting():
    assert greet("Jose") == "Hello, Jose!"
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"
    assert greet("") == "Hello, !"
    assert greet("123") == "Hello, 123!"