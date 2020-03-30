import pytest
from _pytest.fixtures import SubRequest
from .tester import Tester
from ..constants import HOST, store_tmp

# not all params
store_tester = Tester(HOST, 'stores', store_tmp)

@pytest.fixture
def create_store(request: SubRequest):
    param = getattr(request, 'param', None)
    response = store_tester.create_obj(param[0])
    return response


@pytest.fixture
def find_store_by_id(request: SubRequest):
    param = getattr(request, 'param', None)
    response = product_store.find_obj_by_id(param[0])
    return response

@pytest.fixture
def find_store_by_name(request: SubRequest):
    param = getattr(request, 'param', None)
    response = store_tester.find_obj_by_name(param[0])
    return response
