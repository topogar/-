import pytest
from _pytest.fixtures import SubRequest
from .tester import Tester
from ..constants import HOST, category_tmp

# not all params
category_tester = Tester(HOST, 'categories', category_tmp)

@pytest.fixture
def create_category(request: SubRequest):
    param = getattr(request, 'param', None)
    response = category_tester.create_obj(param[0])
    return response


@pytest.fixture
def find_category_by_id(request: SubRequest):
    param = getattr(request, 'param', None)
    response = category_tester.find_obj_by_id(param[0])
    return response

@pytest.fixture
def find_category_by_name(request: SubRequest):
    param = getattr(request, 'param', None)
    response = category_tester.find_obj_by_name(param[0])
    return response
