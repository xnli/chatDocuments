import streamlit as st
from backend.services.chat_service import ChatService
from streamlit_float import *

def render_chat_interface(file_path: str):
    # 初始化浮动功能
    float_init()
    
    st.subheader("对话区")
    
    # 初始化会话状态
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "chat_service" not in st.session_state:
        st.session_state.chat_service = ChatService()
    
    # 创建消息显示区域的容器
    messages_container = st.container()
    
    # 创建输入区域的容器
    input_container = st.container()
    
    # 在消息容器中显示历史消息
    with messages_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    
    # 在输入容器中添加聊天输入框
    with input_container:
        # 用户输入
        if prompt := st.chat_input("输入问题"):
            # 添加用户消息
            with messages_container:
                with st.chat_message("user"):
                    st.markdown(prompt)
                st.session_state.messages.append({"role": "user", "content": prompt})
                
                # 获取回答
                try:
                    response = st.session_state.chat_service.get_response(file_path, prompt)
                    # 添加助手消息
                    with st.chat_message("assistant"):
                        st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                except Exception as e:
                    st.error(f"获取回答失败: {str(e)}")
    
    # 将输入容器固定在底部
    input_container.float("bottom: 0")