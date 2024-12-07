import os
from dotenv import load_dotenv
# from langchain_ollama import OllamaLLM
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
# Langsmith tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT')

# Create a Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the question asked"),
        ("user", "Question:{question}")
    ]
)

# Design Web App
st.title("Langchain Chatbot with OLlama")
input_text=st.text_input("What is your question?")

# Ollama 3.2 model call with explicit format
"""
LangChainDeprecationWarning: The class `Ollama` was deprecated in LangChain 0.3.1 
and will be removed in 1.0.0. An updated version of the class exists in 
the :class:`~langchain-ollama package and should be used instead. 
To use it run `pip install -U :class:`~langchain-ollama` and 
import as `from :class:`~langchain_ollama import OllamaLLM``.
  llm = Ollama(model="gemma2:2b") # format="json"
"""
llm = Ollama(model="gemma2:2b") # format="json" # 
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

# Handle user input
if input_text.strip():
    st.write(chain.invoke({"question":input_text}))
