import streamlit as st
from modules.chatbot import HRChatbot

st.set_page_config(page_title="Multilingual HR Support Bot")

st.title("Multilingual HR & Employee Support Chatbot")

# Initialize the chatbot instance in session state
if 'chatbot' not in st.session_state:
    st.session_state.chatbot = HRChatbot()

# Initialize chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Function to get user input
def user_input():
    return st.text_input("Ask your HR question here (any language):", key="input")

#  Function to display chat history
def display_chat():
    for chat in st.session_state.chat_history:
        if chat['role'] == 'user':
            st.markdown(f"**You:** {chat['content']}")
        else:
            st.markdown(f"**Bot:** {chat['content']}")

# To get the user's query
query = user_input()                                        
if query:
    with st.spinner("Bot is typing..."):
        answer = st.session_state.chatbot.chat(query)
        st.session_state.chat_history.append({"role": "user", "content": query})
        st.session_state.chat_history.append({"role": "assistant", "content": answer})

st.markdown("---")
display_chat()
