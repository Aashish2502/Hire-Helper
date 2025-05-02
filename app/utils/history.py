
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import  create_history_aware_retriever, create_retrieval_chain
import streamlit as st
from langchain.chains.combine_documents import create_stuff_documents_chain

contextualize_q_system_prompt = (
    "Given a caht history and the latest question"
    "which might reference context in the chat history,"
    "formulate a standalone question whcih can be understood "
    "without the chat history. Do NOT answer the question"
    "just reformulate it if needed and otherwise return it as is"
)

system_prompt = (
    "You are an assistant to the HR of the company. "
    "Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you "
    "don't know. If you didn't understand the question, "
    "ask the HR if he/she can repharse it, and then answer"
    "\n\n"
    "{context}"
)

contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", contextualize_q_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}")
    ]
)

qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human","{input}")
    ]
)


def history_aware(llm, get_session_history, retriever):
    history_aware_retriever = create_history_aware_retriever(llm,retriever, contextualize_q_prompt)
    qa_chain = create_stuff_documents_chain(llm, qa_prompt)
    retriever_chain = create_retrieval_chain(history_aware_retriever, qa_chain)
    conversational_rag = RunnableWithMessageHistory(
        retriever_chain, get_session_history,
        input_messages_key="input",
        history_messages_key="chat_history",
        output_messages_key="answer",
    )
    return conversational_rag

    

