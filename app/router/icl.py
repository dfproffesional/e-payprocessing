from fastapi import APIRouter

from service.v1.icl import (
    reader
)

app = APIRouter()
app.prefix = "/v1/icl"

app.get(path="/read")(reader.index)