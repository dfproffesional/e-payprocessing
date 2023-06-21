from router import routes
from fastapi import FastAPI
from middleware import ErrorHandler
from config.database import Database
from model.file_header import FileHeader

app = FastAPI()
app.include_router(routes)
app.add_middleware(ErrorHandler)

Database().metadata.create_all(bind=Database().engine())

@app.get('/')
def message():
    return FileHeader().test()