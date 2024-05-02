from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_env

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


# prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assist. Please respond to the user queries")
        ("user", "Question:{question}")
    ]
)

# streamlit framework
st.title('Langchain Demo with OpenAI')
input_text = st.text_input("Search for the topic you want")


# OpenAI LLM
llm = ChatOpenAI(model='gpt-3.5-turbo')
output_parser = StrOutputParser()
chain = prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({'question':input_text}))