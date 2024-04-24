from fastapi import FastAPI

from app.endpoints.payment_router import appointment_router

app = FastAPI(title='Payment service', openapi_url="/api/payment/openapi.json", docs_url="/api/payment/docs")

app.include_router(appointment_router, prefix='/api/payment')

if __name__ == '__main__':
    import uvicorn
    import os
    try:
        PORT = int(os.environ['PORT'])
    except KeyError as keyerr:
        PORT = 5000
    uvicorn.run(app, host='0.0.0.0', port=PORT)