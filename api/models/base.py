from api.enums.status_code import StatusCode
from api.enums.status_msg import StatusMsg
from pydantic import BaseModel
from typing import Optional, Any


class BaseResponse(BaseModel):

    code: Optional[int] = StatusCode.SUCCESS.value  # 執行代碼
    msg: Optional[str] = StatusMsg.SUCCESS.value  # 回應訊息
    data: Optional[Any] = None  # 回應資料
