import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from streamlit_float import *
import streamlit as st
from ui.upload import render_file_uploader
from ui.pdf import render_pdf_viewer
from ui.chat import render_chat_interface

def main():
    st.set_page_config(
        page_title="ChatPDF",
        layout="wide"
    )
    
    st.title("ChatPDF")
    
    # 创建三列布局
    upload_col, pdf_col, chat_col = st.columns([1, 3, 1])
    
    with upload_col:
        file_path = render_file_uploader()
    
    with pdf_col:
        if file_path and os.path.exists(file_path):
            try:
                with open(file_path, "rb") as pdf_file:
                    st.write(f"正在打开文件: {file_path}")  # 调试信息
                    render_pdf_viewer(pdf_file)
            except Exception as e:
                st.error(f"文件打开失败: {str(e)}")
    
    with chat_col:
        if file_path:
            render_chat_interface(file_path)
        else:
            st.info("请先上传PDF文件")

if __name__ == "__main__":
    main()