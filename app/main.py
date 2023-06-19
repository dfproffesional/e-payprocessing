from fastapi import FastAPI
from middleware import ErrorHandler

from router import icl_router

app = FastAPI()
app.include_router(icl_router)
app.add_middleware(ErrorHandler)

@app.get('/')
def message():
    return "Hello World, default message"