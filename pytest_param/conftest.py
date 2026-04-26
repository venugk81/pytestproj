import pytest

@pytest.fixture(scope="function")
def user_data(request):
    return request.param


