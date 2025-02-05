from llama_index.core import VectorStoreIndex  # 更新导入路径
from llama_index.core.readers import SimpleDirectoryReader  # 更新导入路径
from llama_index.core.text_splitter import TokenTextSplitter  # 更新导入路径
from config import CHUNK_SIZE, CHUNK_OVERLAP

class DocumentProcessor:
    def __init__(self):
        self.text_splitter = TokenTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )
    
    def process_document(self, file_path: str) -> VectorStoreIndex:
        try:
            documents = SimpleDirectoryReader(
                input_files=[file_path]
            ).load_data()
            
            index = VectorStoreIndex.from_documents(
                documents,
                text_splitter=self.text_splitter
            )
            return index
            
        except Exception as e:
            raise Exception(f"文档处理失败: {str(e)}")