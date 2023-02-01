# 11:35
# uvicorn app.main:app --reload
# fetch('http://localhost:8000/').then(res => res.json()).then(console.log)
from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import Settings
from fastapi.middleware.cors import CORSMiddleware

# sqlalchemy
# not needed with alembic
# disable this since alembic will the one now responsible for creating tables and such
# models.Base.metadata.create_all(bind=engine) 

app = FastAPI()


# cors settings
# origins = ["https://www.google.com"] # allow only certain domain
origins = ["*"] # allow all domain to talk to your API

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include all routers
app.include_router(post.router)   
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

