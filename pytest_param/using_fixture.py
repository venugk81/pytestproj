import pytest

@pytest.fixture(params=[1, 2, 3])
def number(request):
    return request.param

def test_square(number):
    assert number * number >= 1


@pytest.fixture(params=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
def num2list(request):
    return request.param

def test_list(num2list):
    print("num2list: ", num2list)
    print(f"min: {min(num2list)}, max: {max(num2list)}, sum: {sum(num2list)} avg: {sum(num2list)/len(num2list)}")
