import pytest
from _pytest.fixtures import SubRequest
from .tester import Tester
from ..constants import HOST, product_tmp

# not all params
product_tester = Tester(HOST, 'products', product_tmp)

@pytest.fixture
def create_product(request: SubRequest):
    param = getattr(request, 'param', None)
    response = product_tester.create_obj(param[0])
    return response


@pytest.fixture
def find_product_by_id(request: SubRequest):
    param = getattr(request, 'param', None)
    response = product_tester.find_obj_by_id(param[0])
    return response

@pytest.fixture
def find_product_by_name(request: SubRequest):
    param = getattr(request, 'param', None)
    response = product_tester.find_obj_by_name(param[0])
    return response
