from fastapi import APIRouter, HTTPException
from uuid import UUID
import requests

from app.check_info import paycheck_body,payment_info
appointment_router = APIRouter(prefix='/payment', tags=['Payment'])


@appointment_router.get('/')
def get_payment_info():
    try:
        return payment_info
    except KeyError:
        raise HTTPException(400)

@appointment_router.get('/create/{id}')
def create_paycheck(id: UUID):
    try:
        paycheck = paycheck_body(info = requests)
        return paycheck
    except ValueError:
        raise HTTPException(400)
    except ConnectionError:
        raise HTTPException(502)