from fastapi import APIRouter

from service.v1 import (
    reader
)

app = APIRouter()
app.prefix = "/v1"

app.get(path="/read")(reader.index)