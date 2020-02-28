from typing import Dict

from fastapi import FastAPI

app = FastAPI(title='Events API')


@app.get('/_health', status_code=200)
def get_health() -> Dict:
    return dict(status='OK')
