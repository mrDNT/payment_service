import requests
from uuid import UUID
from app.check_info import payment_info

def test_get_payment_info(url):
    res = requests.get(url).json()
    assert (res == payment_info)

def test_create_paycheck(url):
    res = requests.get(url).json()
    assert (res.status_code == 500)

if __name__ == '__main__':
    URL = 'http://127.0.0.1:5000/api/payment/'
    test_get_payment_info(URL)
    UUID = 'd2e2c4be-ec86-42f1-a2e4-cd7697c90c3f'
    test_create_paycheck(URL)
