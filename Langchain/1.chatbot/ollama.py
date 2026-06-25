
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# LangSmith Tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "Question: {question}")
    ]
)

# Streamlit UI
st.title("LangChain Demo With ollama llm API")

input_text = st.text_input("Search the topic you want")

# OpenAI LLM
llm = Ollama(model="llama2")

# Output Parser
output_parser = StrOutputParser()

# Create Chain
chain = prompt | llm | output_parser

# Run when user enters text
if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)



