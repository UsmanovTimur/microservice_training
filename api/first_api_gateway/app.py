"""Тестовый гейтвей для проксирования в другие службы"""
from decorators.benchmark_decorator import benchmark
from decorators.tracert_decorator import tracert
from fastapi import FastAPI

app = FastAPI()


@app.get("/redirect")
@tracert
@benchmark
async def redirect_gate(a: str, trace_id: str = ""):
    return {1: 1}
