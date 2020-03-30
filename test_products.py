import pytest
from .helpers.products import find_product_by_name, find_product_by_id, create_product, product_tester

@pytest.mark.parametrize('create_product', [('my_product1',)], indirect=True)
def test_create_first_product(create_product):
    assert create_product['name'] == 'my_product1'



@pytest.mark.parametrize('find_product_by_name', [('my_product1',)], indirect=True)
def test_find_first_product(find_product_by_name):
    assert find_product_by_name['total'] > 0

def test_delete_product():
    id = product_tester.create_obj('my_product2')['id']
    product_tester.delete_obj_by_id(id)
    assert product_tester.find_obj_by_id(id)['total'] == 0

def test_del_first_but_second_exists():
    id1 = product_tester.create_obj('my_product3')['id']
    id2 = product_tester.create_obj('my_product4')['id']
    product_tester.delete_obj_by_id(id1)
    assert product_tester.find_obj_by_id(id1)['total'] == 0
    assert product_tester.find_obj_by_id(id2)['total'] > 0

@pytest.mark.parametrize('find_product_by_name', [('my_product100',)], indirect=True)
def test_find_not_exist_product(find_product_by_name):
    assert find_product_by_name['total'] == 0
