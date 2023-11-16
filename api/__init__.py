import logging
import sys
from api.exception_handler import attach_exception_handlers
from api.route import router
from api.logging_handler import format_record, InterceptHandler
from fastapi import FastAPI
from llama_cpp import Llama
from loguru import logger


def create_app() -> FastAPI:
    # 1. 建立 FastAPI 物件
    app = FastAPI(version='0.1.0')

    # 2. 載入模型
    model_path = r'weights/Taiwan-LLM-7B-v2.0-chat-Q5_1.gguf'
    llm = Llama(model_path=model_path)
    app.state.llm = llm

    # 3. 設定日誌格式
    # 格式
    logger.configure(handlers=[{
        "sink": sys.stdout,
        "level": logging.DEBUG,
        "format": format_record
    }])

    # Uvicorn
    logging.getLogger().handlers = [InterceptHandler()]
    logging.getLogger("uvicorn.access").handlers = [InterceptHandler()]

    # 新增儲存位置
    logger.add("logs/run.log",
               rotation="500MB",
               encoding="utf-8",
               enqueue=True,
               retention="15 days")
    
    # 4. 註冊路由
    app.include_router(router, prefix='/api')

    # 5. 註冊全局例外
    app = attach_exception_handlers(app)

    return app
