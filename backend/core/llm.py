from llama_index.llms.ollama import Ollama
from llama_index.core import Settings
from llama_index.core.embeddings import resolve_embed_model
from llama_index.core.memory import ChatMemoryBuffer
from config import OLLAMA_MODEL, OLLAMA_HOST, EMBED_MODEL, CHUNK_SIZE, CHUNK_OVERLAP

class LLMManager:
    def __init__(self):
        # 初始化 Ollama LLM
        self.llm = Ollama(
            model=OLLAMA_MODEL,
            base_url=OLLAMA_HOST,
            temperature=0.1
        )
        
        # 初始化嵌入模型
        self.embed_model = resolve_embed_model(f"local:{EMBED_MODEL}")
        
        # 配置全局设置
        Settings.llm = self.llm
        Settings.embed_model = self.embed_model
        Settings.chunk_size = CHUNK_SIZE
        Settings.chunk_overlap = CHUNK_OVERLAP
        
        # 初始化聊天记忆
        self.memory = ChatMemoryBuffer.from_defaults(token_limit=2048)
    
    def generate_response(self, prompt: str, context: str = None) -> str:
        try:
            full_prompt = f"基于以下内容回答问题:\n\n{context}\n\n问题: {prompt}" if context else prompt
            self.memory.put(full_prompt)
            response = self.llm.complete(full_prompt)
            self.memory.put(response.text)
            return response.text
        except Exception as e:
            raise Exception(f"LLM响应失败: {str(e)}")