import streamlit as st
from app.ui.upload import render_file_uploader
from app.ui.pdf import render_pdf_viewer
from app.ui.chat import render_chat_interface

def main():
    st.set_page_config(
        page_title="ChatPDF",
        layout="wide"
    )
    
    st.title("ChatPDF")
    
    # 创建三列布局
    upload_col, pdf_col, chat_col = st.columns([1, 2, 1])
    
    with upload_col:
        file_path = render_file_uploader()
    
    with pdf_col:
        if file_path:
            with open(file_path, "rb") as pdf_file:
                render_pdf_viewer(pdf_file)
    
    with chat_col:
        if file_path:
            render_chat_interface(file_path)
        else:
            st.info("请先上传PDF文件")

if __name__ == "__main__":
    main()