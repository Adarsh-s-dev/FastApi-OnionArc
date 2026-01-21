from fastapi import FastAPI

from Api.router import router

app = FastAPI()
app.include_router(router)
