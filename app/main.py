from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

Instrumentator(
    excluded_handlers=["/metrics"],
).instrument(app).expose(app=app, endpoint="/metrics")

@app.get("/health")
def health():
    response = {
        'status': 'up'
    }
    return response
