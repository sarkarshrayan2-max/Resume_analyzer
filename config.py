import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


def get_api_key():
    return st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")


def get_llm():
    return ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
        api_key=get_api_key()
    )