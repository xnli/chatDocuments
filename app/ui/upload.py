import streamlit as st
from config import UPLOAD_DIR
import os

def render_file_uploader():
    st.subheader("文件上传")
    
    uploaded_file = st.file_uploader(
        "选择PDF文件",
        type=['pdf'],
        key="pdf_uploader"
    )
    
    if uploaded_file:
        try:
            file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success(f"文件上传成功: {uploaded_file.name}")
            return file_path
        except Exception as e:
            st.error(f"文件上传失败: {str(e)}")
    return None