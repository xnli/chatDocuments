from llama_index.llms import Ollama
from config import OLLAMA_MODEL, OLLAMA_HOST

class LLMManager:
    def __init__(self):
        self.llm = Ollama(
            model=OLLAMA_MODEL,
            base_url=OLLAMA_HOST
        )
    
    def generate_response(self, prompt: str, context: str = None) -> str:
        try:
            if context:
                full_prompt = f"基于以下内容回答问题:\n\n{context}\n\n问题: {prompt}"
            else:
                full_prompt = prompt
                
            response = self.llm.complete(full_prompt)
            return response.text
            
        except Exception as e:
            raise Exception(f"LLM响应失败: {str(e)}")