from typing import Optional, Dict
from llama_index import VectorStoreIndex
from backend.core.document_processor import DocumentProcessor
import os
from config import VECTOR_STORE_DIR

class IndexService:
    def __init__(self):
        self.doc_processor = DocumentProcessor()
        self.index_cache: Dict[str, VectorStoreIndex] = {}
    
    def get_index(self, file_path: str) -> VectorStoreIndex:
        if file_path in self.index_cache:
            return self.index_cache[file_path]
            
        index = self.doc_processor.process_document(file_path)
        self.index_cache[file_path] = index
        return index
    
    def query_index(self, file_path: str, query: str, top_k: int = 3) -> str:
        try:
            index = self.get_index(file_path)
            retriever = index.as_retriever(similarity_top_k=top_k)
            nodes = retriever.retrieve(query)
            return "\n".join([node.text for node in nodes])
        except Exception as e:
            raise Exception(f"检索失败: {str(e)}")