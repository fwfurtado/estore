import uvicorn

from fastapi import FastAPI


def build_app() -> FastAPI:
    app = FastAPI()

    return app


app = build_app()

if __name__ == '__main__':
    uvicorn.run(
        'estore.main:app',
        host='0.0.0.0',
        port=5000,
        debug=True,
        reload=True,
        access_log=False
    )
