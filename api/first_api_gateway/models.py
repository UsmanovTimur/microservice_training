from typing import Annotated, Any

from fastapi import Header
from pydantic import BaseModel
from fastapi import Request
from starlette.datastructures import Headers


class BaseRequestHeadersModel(Request):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._headers = Headers(headers={"Auth": "JWT"},
                                raw=[("Auth".encode('utf-8'), "JWT".encode('utf-8'))],
                                scope={"Auth": "JWT"})


class BaseRequestModel(Request):
    """Базовая модель запроса"""


class BaseResponseModel(BaseModel):
    """Базовая модель ответа"""
    data: Any
