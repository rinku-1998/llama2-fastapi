from huggingface_hub import hf_hub_download

# 模型下載參數
REPO_ID = 'audreyt/Taiwan-LLM-7B-v2.0-chat-GGUF'
FILENAME = 'Taiwan-LLM-7B-v2.0-chat-Q5_1.gguf'


def download_model() -> str:
    """下載模型

    Returns:
        str: 模型下載路徑
    """

    # 1. 下載模型
    model_path = hf_hub_download(repo_id=REPO_ID, filename=FILENAME)
    print(f'Model weight saved in {model_path}.')

    return model_path


if __name__ == '__main__':

    download_model()
