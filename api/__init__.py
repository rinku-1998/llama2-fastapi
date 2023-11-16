from api.exception_handler import attach_exception_handlers
from api.route import router
from fastapi import FastAPI
from llama_cpp import Llama


def create_app() -> FastAPI:
    # 1. 建立 FastAPI 物件
    app = FastAPI(version='0.1.0')

    # 2. 載入模型
    model_path = r'weights/Taiwan-LLM-7B-v2.0-chat-Q5_1.gguf'
    llm = Llama(model_path=model_path)
    app.state.llm = llm

    # 3. 註冊路由
    app.include_router(router, prefix='/api')

    # 4. 註冊全局例外
    app = attach_exception_handlers(app)

    return app
