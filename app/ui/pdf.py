import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import os

def render_pdf_viewer(pdf_file):
    try:
        # 检查文件对象
        if pdf_file is None:
            st.error("文件对象为空")
            return
            
        # 读取文件内容
        pdf_content = pdf_file.read()
        
        # 检查内容
        if not pdf_content:
            st.error("PDF内容为空")
            return
            
        st.write(f"文件大小: {len(pdf_content)} bytes")  # 调试信息
        
        # 使用文档中的参数显示 PDF
        pdf_viewer(
            input=pdf_content,
            width="100%",
            height=800
        )
        
    except Exception as e:
        st.error(f"PDF显示失败: {str(e)}")
        st.write("错误类型:", type(e))  # 显示错误类型