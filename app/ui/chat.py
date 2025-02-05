import streamlit as st
from backend.services.chat_service import ChatService

def render_chat_interface(file_path: str):
    st.subheader("对话区")
    
    # 初始化会话状态
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
        # 先添加用户消息并立即显示
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # 获取并显示助手回答
        try:
            with st.chat_message("assistant"):
                response = st.session_state.chat_service.get_response(file_path, prompt)
                st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
        except Exception as e:
            st.error(f"获取回答失败: {str(e)}")