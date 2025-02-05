import streamlit as st
from backend.services.chat_service import ChatService

def render_chat_interface(file_path: str):
    st.subheader("对话区")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "chat_service" not in st.session_state:
        st.session_state.chat_service = ChatService()
    
    # 显示历史消息
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # 用户输入
    if prompt := st.chat_input("输入问题"):
        # 添加用户消息
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # 获取回答
        try:
            response = st.session_state.chat_service.get_response(file_path, prompt)
            # 添加助手消息
            st.session_state.messages.append({"role": "assistant", "content": response})
        except Exception as e:
            st.error(f"获取回答失败: {str(e)}")