import pytest
import requests
from bs4 import BeautifulSoup
from .constants import HOST

def test_status():
    status = requests.get(HOST).status_code
    assert status == 200

def test_is_smth_good():
    content = requests.get(HOST).content
    page = BeautifulSoup(content, 'lxml')
    assert len(page.findAll('h2')) == 2 and len(page.findAll('h3')) == 6
