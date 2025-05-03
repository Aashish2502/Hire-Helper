import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()
from utils.embeddings import create_vector_embeddings
from utils.history import history_aware

os.environ["LANGSMITH_PROJECT"]='HR-Assistant'
os.environ["LANGSMITH_ENDPOINT"]="true"
os.environ["LANGSMITH_TRACING"]="https://api.smith.langchain.com"


from langchain_groq import ChatGroq
import tempfile
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory



st.title("Hire Help")
st.text("Hello there, I'm your AI Hire Helper, and would be assisting you with the profile scanning of the candidates")

st.sidebar.title("Settings")
groq_api_key = st.sidebar.text_input("Enter your GROQ Api Key", type="password")
hf_api_key = st.sidebar.text_input("Enter your HuggingFace API Key", type="password")
ls_api_key = st.sidebar.text_input("Enter your Langsmith API Key", type="password")

os.environ['HF_API_KEY'] = hf_api_key
os.environ['LANGSMITH_API_KEY'] = ls_api_key

if groq_api_key and hf_api_key and ls_api_key:
    llm = ChatGroq(model="gemma2-9b-it", api_key=groq_api_key)

    session_id = st.sidebar.text_input("Session ID", value="default_session")

    if 'store' not in st.session_state:
        st.session_state.store = {}

    resume = st.file_uploader("Upload your Resume", type="pdf")

    if resume is not None:
        # Save the uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(resume.read())
            tmp_path = tmp_file.name
        retriever = create_vector_embeddings(tmp_path)
        
        if retriever:
            user_input = st.text_input("Ask any question related to your resume!")
            

            def get_session_history(session:str)->BaseChatMessageHistory:
                if session_id not in st.session_state.store:
                    st.session_state.store[session_id] = ChatMessageHistory()
                return st.session_state.store[session_id]
            
            if user_input:
                rag_chain = history_aware(llm=llm,get_session_history= get_session_history, retriever=retriever)
                session_history = get_session_history(session_id)
                response = rag_chain.invoke(
                    {"input":user_input},
                    config={
                        "configurable": {"session_id":session_id}
                    }
                )   

                st.write(response['answer'])






