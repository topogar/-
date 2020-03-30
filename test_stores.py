import pytest
from .helpers.stores import find_store_by_name, find_store_by_id, create_store, store_tester

@pytest.mark.parametrize('create_store', [('my_store1',)], indirect=True)
def test_create_first_store(create_store):
    assert create_store['name'] == 'my_store1'



@pytest.mark.parametrize('find_store_by_name', [('my_store1',)], indirect=True)
def test_find_first_store(find_store_by_name):
    assert find_store_by_name['total'] > 0

def test_delete_product():
    id = store_tester.create_obj('my_store2')['id']
    store_tester.delete_obj_by_id(id)
    assert store_tester.find_obj_by_id(id)['total'] == 0

def test_del_first_but_second_exists():
    id1 = store_tester.create_obj('my_store3')['id']
    id2 = store_tester.create_obj('my_store4')['id']
    store_tester.delete_obj_by_id(id1)
    assert store_tester.find_obj_by_id(id1)['total'] == 0
    assert store_tester.find_obj_by_id(id2)['total'] > 0

@pytest.mark.parametrize('find_store_by_name', [('my_store100',)], indirect=True)
def test_find_not_exist_store(find_store_by_name):
    assert find_store_by_name['total'] == 0
