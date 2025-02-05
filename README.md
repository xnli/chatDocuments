# ChatDocuments

一个基于 LlamaIndex 和 Streamlit 构建的 PDF 智能问答系统。可以上传 PDF 文档,并与文档内容进行对话交互。

## 功能特性

- 支持 PDF 文档上传和在线预览
- 基于 LlamaIndex 的文档索引和检索
- 使用 Ollama 作为 LLM 模型后端
- 支持文档分段和向量检索
- 交互式对话界面

## 技术栈

- Streamlit: Web 界面框架
- LlamaIndex: 文档索引和检索
- Ollama: LLM 模型服务
- FAISS: 向量检索引擎
- streamlit-pdf-viewer: PDF 在线预览组件
- streamlit-float: 界面浮动组件

## 安装部署

1. 安装依赖

```bash
pip install -r requirements.txt
```

2. 配置 Ollama 服务

确保 Ollama 服务运行在 http://localhost:11434

3. 修改配置文件 config.py

```python
OLLAMA_HOST = "http://localhost:11434"  # Ollama 服务地址
OLLAMA_MODEL = "mistral"  # 使用的模型名称
EMBED_MODEL = "路径/到/嵌入模型"  # 嵌入模型路径
```

4. 运行应用

```bash
streamlit run app/main.py
```

## 项目结构

```
.
├── app/
│   ├── ui/                # 前端界面组件
│   │   ├── chat.py       # 对话界面
│   │   ├── pdf.py        # PDF预览
│   │   └── upload.py     # 文件上传
│   └── main.py           # 主程序入口
├── backend/
│   ├── core/             # 核心功能模块
│   │   ├── llm.py       # LLM模型管理
│   │   └── document_processor.py  # 文档处理
│   └── services/         # 服务层
│       ├── chat_service.py    # 对话服务
│       └── index_service.py   # 索引服务
├── data/                 # 数据目录
│   ├── uploads/         # 上传文件存储
│   └── vector_store/    # 向量存储
├── config.py            # 配置文件
└── requirements.txt     # 依赖包列表
```

## 使用说明

1. 启动应用后，通过左侧栏上传 PDF 文档
2. 文档上传成功后，中间区域会显示 PDF 预览
3. 右侧对话区域可以针对文档内容进行提问
4. 系统会自动检索相关内容并生成回答

## 注意事项

- 支持的文件格式: PDF
- 文件大小限制: 200MB
- 需要预先安装并启动 Ollama 服务
- 确保有足够的磁盘空间存储向量索引
