import pytest

@pytest.mark.one
def test_method1():
    x = 10
    y = 20
    assert x == y
@pytest.mark.two
def test_method2():
    a = 20
    b = 15
    assert a == b+5
