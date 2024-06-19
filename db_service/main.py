import sys
from contextlib import asynccontextmanager

from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

from routers.router import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(
    lifespan=lifespan,
    root_path="/db_service"
)

origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080"
]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origin=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"]
# )

app.include_router(router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )