import pytest


@pytest.mark.usefixtures("data_load")
class TestExample2:

    def test_edit_profile(self, data_load):
        print("executing middle")
        print(data_load)
        print(len(data_load))