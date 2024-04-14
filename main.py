from fastapi import FastAPI
from routers import Eos

app = FastAPI()
app.include_router(Eos.router)
