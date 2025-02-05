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
        layout="wide",
        initial_sidebar_state="collapsed"  # 默认折叠左侧边栏
    )
    
    st.title("ChatPDF 📚")
    
    # 只使用两列，并调整比例，PDF区域窄一点，对话区域宽一点
    pdf_col, chat_col = st.columns([2, 1.5])
    
    # 使用 sidebar 来放置文件上传组件
    with st.sidebar:
        file_path = render_file_uploader()
    
    with pdf_col:
        if file_path and os.path.exists(file_path):
            try:
                with open(file_path, "rb") as pdf_file:
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