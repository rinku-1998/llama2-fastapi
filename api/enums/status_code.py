from enum import Enum


class StatusCode(Enum):

    # 0 成功
    SUCCESS = 0  # 成功

    # [-1, -10] HTTP請求
    REQUEST_RESOLVE_FAILED = -1  # Request 解析失敗
    REQUEST_MISSING_REQUIRED_PARAMETER = -2  # Request 缺少必要參數
    REQUEST_INVALID_URL = -3  # 無效的 URL
    REQUEST_UNSUPPORTED_HTTP_METHOD = -4  # HttpMethod 格式錯誤

    # [-200, -299] 代碼檔
    CODE_NOT_EXIST = -200  # 代碼檔代碼不存在

    # [-300, -399] 資源存取
    ITEM_UNHANDLED_EXCEPTION = -300  # 資源存取時發生意外
    ITEM_ALREADY_EXIST = -301  # 資源已存在
    ITEM_NOT_EXIST = -302  # 資源不存在
    ITEM_MODIFIED_FAILED = -303  # 資源異動失敗

    # [-900, -998] 檔案上傳
    UPLOAD_FILE_FAILED = -900  # 上傳檔案失敗
    UPLOAD_EMPTY_FILE = -901  # 檔案不可為空
    UPLOAD_FILE_EXCEED_LIMIT = -902  # 上傳檔案超過限制大小
    UPLOAD_UNSUPPORTED_EXTENSION = -903  # 不支援此類型檔案
    UPLOAD_FILE_NOT_EXIST = -904  # 檔案不存在
    UPLOAD_FILE_CONTENT_ERROR = -905  # 檔案格式異常
    UPLOAD_UNKNOWN_EXTENSION = -906  # 未知的副檔名
    UPLOAD_COMPRESS_FILE_ERROR = -907  # 壓縮圖片失敗
    UPLOAD_WRONG_FILENAME_PATTERN = -908  # 檔案名稱格式錯誤

    # -999 全域錯誤
    UNDEFINED_EXCEPTION = -999  # 未被定義的錯誤
