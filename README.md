# llama2-fastapi

## 環境
- python 3.11.2
- huggingface-hub 0.19.2
- llama_cpp_python 0.2.18
- fastapi 0.104.1


## 安裝
```shell
pip install huggingface-hub llama_cpp_python fastapi uvicorn loguru
```

## 使用方法
-  預測下一個句子

    ```shell
    python3 demo.py
    ```

- 啟動預測服務 API

    ```shell
    # 方法1
    python start_api.py

    # 方法2
    uvicorn start_api:app --host 0.0.0.0 --port 8000
    ```