import requests
import pytest
from uuid import UUID, uuid4
from app.check_info import payment_info

URL = 'http://127.0.0.1:5000/api/payment/'

@pytest.fixture(scope='session')
def test_get_payment_info() -> None:
    res = requests.get(f'{URL}').json()
    assert (res == payment_info)

@pytest.fixture(scope='session')
def test_create_paycheck() -> None:
    res = requests.get(f'{URL}/create/{uuid4()}').json()
    assert (res.status_code == 500)

