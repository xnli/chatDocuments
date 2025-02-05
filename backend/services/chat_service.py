from backend.core.llm import LLMManager
from backend.services.index_service import IndexService

class ChatService:
    def __init__(self):
        self.llm = LLMManager()
        self.index_service = IndexService()
    
    def get_response(self, file_path: str, question: str) -> str:
        try:
            # 获取相关上下文
            context = self.index_service.query_index(file_path, question)
            
            # 生成回答
            return self.llm.generate_response(question, context)
        except Exception as e:
            raise Exception(f"回答生成失败: {str(e)}")