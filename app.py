# Q&A Chatbot
# from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI

# from langchain.llms import OpenAI
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()


def get_openai_response(question):
    llm = ChatOpenAI(
        openai_api_key=os.getenv("OPEN_API_KEY"),
        model_name="gpt-3.5-turbo",
        temperature=0.5,
    )
    response = llm.invoke(question)  # Updated function call
    return response


st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input = st.text_input("Input: ", key="input")
response = get_openai_response(input)

submit = st.button("Ask the question")

if submit:
    st.subheader("The Response is:")
    st.write(response)
