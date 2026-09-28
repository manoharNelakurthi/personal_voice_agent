import streamlit as st
from app.voice_agent import VoiceAgent
from app.memory import ConversationMemory


st.set_page_config(page_title="Personal Voice Agent", layout="wide")

st.title("🎤 Personal Voice Assistant")

if "agent" not in st.session_state:
    st.session_state.agent = VoiceAgent()

if "memory" not in st.session_state:
    st.session_state.memory = st.session_state.agent.memory

# Sidebar
with st.sidebar:
    st.header("Controls")
    mode = st.radio("Select mode:", ["Chat", "History", "Statistics"])
    if st.button("🗑️ Clear History"):
        st.session_state.memory.clear_history()
        st.success("History cleared!")

# Main content
if mode == "Chat":
    st.subheader("💬 Chat with Assistant")
    user_input = st.text_input("You:", placeholder="Type your message here...")
    if user_input:
        with st.spinner("Generating response..."):
            response = st.session_state.agent.respond_text(user_input)
        st.success(f"**Assistant:** {response}")

elif mode == "History":
    st.subheader("📜 Conversation History")
    conversations = st.session_state.memory.get_all_conversations()
    if conversations:
        for i, conv in enumerate(conversations, 1):
            with st.expander(f"Conversation {i} - {conv['timestamp']}"):
                st.write(f"**You:** {conv['user']}")
                st.write(f"**Assistant:** {conv['assistant']}")
    else:
        st.info("No conversations yet.")

elif mode == "Statistics":
    st.subheader("📊 Statistics")
    conversations = st.session_state.memory.get_all_conversations()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Conversations", len(conversations))
    with col2:
        st.metric("Session Conversations", st.session_state.agent.conversation_count)
    with col3:
        st.metric("Unique Users", 1)

    if conversations:
        st.subheader("Recent Conversations")
        recent = conversations[-5:]
        for conv in reversed(recent):
            st.write(f"**{conv['timestamp']}**")
            st.write(f"You: {conv['user']}")
            st.write(f"Assistant: {conv['assistant']}")
            st.divider()
