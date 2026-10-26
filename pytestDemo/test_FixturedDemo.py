import pytest


@pytest.mark.usefixtures("setup")
class TestExample :

    def test_fixture_demo(self):
        print("i will be executing steps in fixturedemo method")

    def test_fixture_demo1(self):
        print("i will be executing steps in fixturedemo1 method")

    def test_fixture_demo2(self):
        print("i will be executing steps in fixturedemo2 method")

    def test_fixture_demo3(self):
        print("i will be executing steps in fixturedemo3 method")

