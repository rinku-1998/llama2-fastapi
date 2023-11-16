from enum import Enum


class StatusMsg(Enum):

    # 0 成功
    SUCCESS = '成功'

    # [-1, -10] HTTP請求
    REQUEST_RESOLVE_FAILED = 'Request 解析失敗'
    REQUEST_MISSING_REQUIRED_PARAMETER = 'Request 缺少必要參數'
    REQUEST_INVALID_URL = '無效的 URL'
    REQUEST_UNSUPPORTED_HTTP_METHOD = 'HttpMethod 格式錯誤'

    # [-200, -299] 代碼檔
    CODE_NOT_EXIST = '代碼檔代碼不存在'

    # [-300, -399] 資源存取
    ITEM_UNHANDLED_EXCEPTION = '資源存取時發生意外'
    ITEM_ALREADY_EXIST = '資源已存在'
    ITEM_NOT_EXIST = '資源不存在'
    ITEM_MODIFIED_FAILED = '資源異動失敗'

    # [-900, -998] 檔案上傳
    UPLOAD_FILE_FAILED = '上傳檔案失敗'
    UPLOAD_EMPTY_FILE = '檔案不可為空'
    UPLOAD_FILE_EXCEED_LIMIT = '上傳檔案超過限制大小'
    UPLOAD_UNSUPPORTED_EXTENSION = '不支援此類型檔案'
    UPLOAD_FILE_NOT_EXIST = '檔案不存在'
    UPLOAD_FILE_CONTENT_ERROR = '檔案格式異常'
    UPLOAD_UNKNOWN_EXTENSION = '未知的副檔名'
    UPLOAD_COMPRESS_FILE_ERROR = '壓縮圖片失敗'
    UPLOAD_WRONG_FILENAME_PATTERN = '檔案名稱格式錯誤'

    # -999 全域錯誤
    UNDEFINED_EXCEPTION = '未被定義的錯誤'
