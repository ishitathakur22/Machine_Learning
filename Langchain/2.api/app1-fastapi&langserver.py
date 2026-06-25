
#---------------------------------------------------------
#          THIS IS YOUR BACKEND API 
#-client.py frontend
#---------------------------------------------------------


from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set API keys
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

#create FastAPI application
app=FastAPI(
    title='langchain server',
    version="1.0",
    description='A simple API server'
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)

# Create OpenAI model object
model= ChatOpenAI()

# Create Ollama model object
llm = Ollama(model="llama2")

prompt1 = ChatPromptTemplate.from_template( "Write me an essay about {topic} with 100 words" )
prompt2 = ChatPromptTemplate.from_template( "Write me a poem about {topic} for a 5 year old child with 100 words" )

add_routes(
    app,
    prompt1|model,
    path="/essay"
)

add_routes(
    app,
    prompt2|llm,
    path="/poem"
)


if __name__=="__main__":
    uvicorn.run(
        app,
        host="localhost",
        port=8000)
