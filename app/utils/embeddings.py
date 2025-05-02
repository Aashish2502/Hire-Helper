import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader

def create_vector_embeddings(tmp_path):
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
        loader = PyPDFLoader(tmp_path)
        docs = loader.load()
        text_splitter=RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        final_docs = text_splitter.split_documents(docs)
        vectorDb = FAISS.from_documents(final_docs, embeddings)
        retriever = vectorDb.as_retriever()
        return (retriever)