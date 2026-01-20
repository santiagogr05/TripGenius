
from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="My FastAPI App",
    version="0.1.0",
)

app.include_router(router)


@app.get("/")
def health_check():
    return {"status": "ok"}
