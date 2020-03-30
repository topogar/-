import pytest
from .helpers.categories import find_category_by_name, find_category_by_id, create_category, category_tester

category_tester.delete_obj_by_id(200)
@pytest.mark.parametrize('create_category', [('my_category1',)], indirect=True)
def test_create_first_category(create_category):
    assert create_category['name'] == 'my_category1'



@pytest.mark.parametrize('find_category_by_name', [('my_category1',)], indirect=True)
def test_find_first_category(find_category_by_name):
    assert find_category_by_name['total'] > 0

def test_delete_category():
    id = category_tester.create_obj('my_category2')['id']
    category_tester.delete_obj_by_id(id)
    assert category_tester.find_obj_by_id(id)['total'] == 0

def test_del_first_but_second_exists():
    id1 = category_tester.create_obj('my_category3')['id']
    id2 = category_tester.create_obj('my_category4')['id']
    category_tester.delete_obj_by_id(id1)
    assert category_tester.find_obj_by_id(id1)['total'] == 0
    assert category_tester.find_obj_by_id(id2)['total'] > 0

@pytest.mark.parametrize('find_category_by_name', [('my_category100',)], indirect=True)
def test_find_not_exist_category(find_category_by_name):
    assert find_category_by_name['total'] == 0


def test_delete_all():
    category_tester.delete_all_obj()
