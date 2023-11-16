from api.models.base import BaseResponse
from fastapi import APIRouter, Request

router = APIRouter(prefix='/v1')


@router.post('/predict', response_model=BaseResponse)
def predict(request: Request, text: str, max_tokens: int = 32):

    # 1. 取得模型
    llm = request.app.state.llm

    # 2. 預測下一句
    output = llm(text, max_tokens=max_tokens)

    # 3. 設定回傳資料
    res = BaseResponse()
    res.data = output

    return res
