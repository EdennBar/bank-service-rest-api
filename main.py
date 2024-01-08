from fastapi import FastAPI

from core.database import Base, engine

from app.routers import user
from app.routers import bank
from app.routers import trans
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


app.include_router(user.router)
app.include_router(bank.router)
app.include_router(trans.router)

Base.metadata.create_all(engine)


origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)