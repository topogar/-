import pytest
import requests
import json
from .constants import HOST

def test_empty_status():
    ''' clear db and check api status'''
    requests.delete(HOST + 'services')
    requests.delete(HOST + 'products')
    requests.delete(HOST + 'stores')
    requests.delete(HOST + 'categories')

    response = requests.get(HOST+'healthcheck')
    assert response.status_code == 200

def test_is_empty():
    ''' check that db is empty'''
    response = requests.get(HOST+'products').content
    assert json.loads(response)['total'] == 0
