"""Тестовый гейтвей для проксирования в другие службы"""
from decorators.benchmark_decorator import benchmark
from decorators.tracert_decorator import tracert
from pydantic import BaseModel
from models import BaseRequestModel, BaseRequestHeadersModel
from fastapi import FastAPI, Request

app = FastAPI()


class RequestModel(BaseRequestModel, BaseRequestHeadersModel):
    pass


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.get("/redirect", response_model=Item)
@tracert
@benchmark
async def redirect_gate(request: Request):
    return {1: 1}
