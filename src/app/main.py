from typing import Dict

import uvicorn
from fastapi import FastAPI

from app.api_v1_connected import api_v1_connected
from data.database import Base
from data.database import engine

Base.metadata.create_all(bind=engine)


def create_app() -> FastAPI:
    api = FastAPI(
        title='Devs connection API'
    )

    api.include_router(api_v1_connected, prefix='/api/v1/connected', tags=['events'])

    return api


app = create_app()


@app.get('/_health', status_code=200)
def get_health() -> Dict:
    return dict(status='OK')


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
