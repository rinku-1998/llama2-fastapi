from api.models.base import BaseResponse
from api.enums.status_code import StatusCode
from api.enums.status_msg import StatusMsg

from fastapi import FastAPI, Request, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


def attach_exception_handlers(app: FastAPI):

    # TODO: 未來可以從這個事件攔截 401、 402 等已經被定義好的例外
    # HTTP 例外(FastAPI 預設攔截的例外)
    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request,
                                     exception: HTTPException) -> JSONResponse:
        pass

    # Request 錯誤例外
    @app.exception_handler(RequestValidationError)
    async def request_validation_error_handler(
            request: Request,
            exception: RequestValidationError) -> JSONResponse:

        # 1. 格式化錯誤訊息
        msg = ''
        for error in exception.errors():

            location = error.get('loc')[0]
            field_name = error.get('loc')[1]

            msg += f'Request {location} 缺少 {field_name}，'

        # 2. 整理資料
        res = BaseResponse(code=StatusCode.MISSING_REQUEST_PARAM.value)
        res.msg = msg

        return JSONResponse(jsonable_encoder(res))

    # 全局例外
    @app.exception_handler(Exception)
    async def base_exception_handler(request: Request,
                                     exception: Exception) -> JSONResponse:

        res = BaseResponse(code=StatusCode.UNDEFINED_EXCEPTION.value,
                              msg=str(exception))
        return JSONResponse(jsonable_encoder(res))

    return app
