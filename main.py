import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_restful.timing import add_timing_middleware

from api.router import router as api_router
from core.config import settings
# from core.db.base import *  # noqa

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
add_timing_middleware(app)

app.include_router(api_router)


@app.get("/_ah/warmup")
def warmup():
    return "Success"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
