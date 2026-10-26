import pytest


@pytest.fixture(scope="class")
def setup():
    print("i will be executing first")
    yield
    print("i will be executing last ")


@pytest.fixture()
def data_load():
    print("userprofile data is being created")
    return ["rahul", "shetty", "rahulshettyacademy.com"]


@pytest.fixture(params=[ ("chrome", " rahul") , ("firefox", "shetty" ), ("IE", "ss") ] )
def cross_browser(request):
    return request.param



