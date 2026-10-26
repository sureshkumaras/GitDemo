import pytest

@pytest.mark.smoke
def test_firstprogram(setup):
    print("Hello1")

@pytest.mark.xfail
def test_secondgreetcreditcard():
    print("Hello2")


def test_cross_browser(cross_browser):
    print(cross_browser[1])
