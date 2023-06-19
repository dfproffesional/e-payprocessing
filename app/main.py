from router import routes
from fastapi import FastAPI
from middleware import ErrorHandler

app = FastAPI()
app.include_router(routes)
app.add_middleware(ErrorHandler)

@app.get('/')
def message():
    return "Hello World, default message"