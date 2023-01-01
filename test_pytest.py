import pytest

from YD import put_directory, get_directory, path1
class TestFunction():
    def test_put_directory(self):
    etalon = 201
    result = put_directory(path1)
    assert result.status_code == etalon

    def test_get_direktory(self):
    etalon = 200
    result = get_directory(path1)
    assert etalon == result.status_code

test = TestFunction
test.test_put_directory()
test.test_get_direktory()






