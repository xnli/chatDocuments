import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
VECTOR_STORE_DIR = os.path.join(DATA_DIR, 'vector_store')
UPLOAD_DIR = os.path.join(DATA_DIR, 'uploads')

# 创建必要的目录
for dir_path in [DATA_DIR, VECTOR_STORE_DIR, UPLOAD_DIR]:
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

# LLM配置
OLLAMA_HOST = "http://localhost:11434"
OLLAMA_MODEL = "mistral"
EMBED_MODEL = "/root/autodl-tmp/hf/BAAI/bge-small-en-v1.5"  # 新增
# 文档处理配置
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200