
#---------------------------------------------------------
#          THIS IS YOUR FRONTENT API
#---------------------------------------------------------

import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# LangSmith Tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

def get_openai_response(input_text):
    response = requests.post( 
    "http://localhost:8000/essay/invoke", # invoke the url with /invoke
    json={'input':{'topic':input_text}}) #json is the input
    
    return response.json()['output']['content'] # we will get the responce inside content

def get_ollama_response(input_text1):
    response=requests.post(
    "http://localhost:8000/poem/invoke",
    json={'input':{'topic':input_text1}})

    return response.json()['output'] # no content here directly responce displayed

#streamlit framework

st.title("langchain demo with openai llama2 api chains")
input_text=st.text_input("write an eassy on ")
input_text1=st.text_input("write an poem on ")

if input_text:
    st.write(get_openai_response(input_text)) #in this function we are calling the fucntion that is running in the backend 

if input_text1:
    st.write(get_ollama_response(input_text1))
