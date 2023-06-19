from fastapi import APIRouter

from service.v1 import (
    reader
)

app = APIRouter()
app.prefix = "/api/v1"

app.get(path="/read")(reader.index)