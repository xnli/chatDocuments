from typing import Optional, List
import faiss
from llama_index.core.vector_stores import FaissVectorStore  # 更新导入路径
from llama_index.core import VectorStoreIndex, Document  # 更新导入路径
from pathlib import Path
import numpy as np
from config import VECTOR_STORE_DIR
import os
import pickle

class VectorStore:
    def __init__(self):
        self.index_map = {}  # 文件路径 -> FAISS索引的映射
        self.dimension = 768  # 默认向量维度，使用标准embedding大小
        
    def create_store(self, file_path: str) -> FaissVectorStore:
        """
        为文档创建向量存储
        """
        try:
            # 创建FAISS索引
            faiss_index = faiss.IndexFlatL2(self.dimension)
            vector_store = FaissVectorStore(faiss_index)
            
            # 保存到内存映射
            self.index_map[file_path] = vector_store
            
            # 保存到磁盘
            self._save_to_disk(file_path, vector_store)
            
            return vector_store
            
        except Exception as e:
            raise Exception(f"创建向量存储失败: {str(e)}")

    def get_store(self, file_path: str) -> Optional[FaissVectorStore]:
        """
        获取文档的向量存储
        """
        # 检查内存中是否存在
        if file_path in self.index_map:
            return self.index_map[file_path]
            
        # 尝试从磁盘加载
        loaded_store = self._load_from_disk(file_path)
        if loaded_store:
            self.index_map[file_path] = loaded_store
            return loaded_store
            
        return None

    def search(self, file_path: str, query_embedding: np.ndarray, top_k: int = 3) -> List[int]:
        """
        搜索最相似的向量
        """
        try:
            store = self.get_store(file_path)
            if not store:
                store = self.create_store(file_path)
            
            # 执行向量搜索
            D, I = store.index.search(query_embedding.reshape(1, -1), top_k)
            return I[0].tolist()
            
        except Exception as e:
            raise Exception(f"向量搜索失败: {str(e)}")

    def _save_to_disk(self, file_path: str, vector_store: FaissVectorStore) -> None:
        """
        将向量存储保存到磁盘
        """
        try:
            # 创建保存目录
            if not os.path.exists(VECTOR_STORE_DIR):
                os.makedirs(VECTOR_STORE_DIR)
            
            # 构造保存路径
            save_path = os.path.join(
                VECTOR_STORE_DIR, 
                f"{Path(file_path).stem}_vector_store.pkl"
            )
            
            # 保存向量存储
            with open(save_path, 'wb') as f:
                pickle.dump(vector_store, f)
                
        except Exception as e:
            raise Exception(f"保存向量存储失败: {str(e)}")

    def _load_from_disk(self, file_path: str) -> Optional[FaissVectorStore]:
        """
        从磁盘加载向量存储
        """
        try:
            # 构造加载路径
            load_path = os.path.join(
                VECTOR_STORE_DIR,
                f"{Path(file_path).stem}_vector_store.pkl"
            )
            
            # 检查文件是否存在
            if not os.path.exists(load_path):
                return None
            
            # 加载向量存储
            with open(load_path, 'rb') as f:
                return pickle.load(f)
                
        except Exception as e:
            raise Exception(f"加载向量存储失败: {str(e)}")

    def delete_store(self, file_path: str) -> None:
        """
        删除向量存储
        """
        try:
            # 从内存中删除
            if file_path in self.index_map:
                del self.index_map[file_path]
            
            # 从磁盘删除
            store_path = os.path.join(
                VECTOR_STORE_DIR,
                f"{Path(file_path).stem}_vector_store.pkl"
            )
            if os.path.exists(store_path):
                os.remove(store_path)
                
        except Exception as e:
            raise Exception(f"删除向量存储失败: {str(e)}")

    def clear(self) -> None:
        """
        清理所有向量存储
        """
        try:
            # 清理内存
            self.index_map.clear()
            
            # 清理磁盘
            if os.path.exists(VECTOR_STORE_DIR):
                for file in os.listdir(VECTOR_STORE_DIR):
                    if file.endswith('_vector_store.pkl'):
                        os.remove(os.path.join(VECTOR_STORE_DIR, file))
                        
        except Exception as e:
            raise Exception(f"清理向量存储失败: {str(e)}")