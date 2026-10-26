import pytest


def test_firstprogram():
    message= "hello"
    assert  message == "Hi"

@pytest.mark.smoke
@pytest.mark.skip
def test_secondcreditcard():
    a=4
    b=6
    assert a+2 == b, "additiondo not match"