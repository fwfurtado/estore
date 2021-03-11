import uvicorn

from estore.endpoints import product, customer
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


def build_app() -> FastAPI:
    app = FastAPI()

    app.include_router(product.admin, tags=["admin"])
    app.include_router(customer.router, tags=["customer"])

    return app


app = build_app()

@app.exception_handler(Exception)
def global_error_handler(request: Request, error: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": f"Sorry! Occurs an unespected error: {error.args}", }
    )


if __name__ == '__main__':
    uvicorn.run(
        'estore.main:app',
        host='0.0.0.0',
        port=5000,
        debug=True,
        reload=True,
        access_log=False
    )
