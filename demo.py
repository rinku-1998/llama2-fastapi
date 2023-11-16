from llama_cpp import Llama

MAX_TOKENS = 512

def run() -> dict:
    """執行預測下一句

    Returns:
        dict: 預測結果
    """

    # 1. 載入模型
    model_path = r'weights/Taiwan-LLM-7B-v2.0-chat-Q5_1.gguf'
    llm = Llama(model_path=model_path)

    # 2. 預測下一句
    text = '你好'
    output = llm(text, max_tokens=512)
    print(output)

    return output


if __name__ == '__main__':
    result = run()
