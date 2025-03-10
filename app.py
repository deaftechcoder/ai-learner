# import necessary libraries
from google import genai
import os
import streamlit as st
from dotenv import load_dotenv

# load this environment variable 
load_dotenv()

# initialize env var from .env
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Check if the api key is working properly
if not GEMINI_API_KEY:
    print("gemini key api is not set")
    exit()

client = genai.Client(api_key=GEMINI_API_KEY)
st.header("Gemini API Chatbot")
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

prompt = st.text_input("Enter your prompt",key='user_input')
if st.button(label="Submit"):
    try:
        response = client.models.generate_content(
        model='gemini-2.0-flash', contents=prompt
        )

        st.session_state.chat_history.append({'role':'user', 'content':prompt})
        st.session_state.chat_history.append({'role':'model', 'content':response.text})
        
        st.write(response.text)
    except ValueError as e:
        st.write(f"Error occured {e}")

st.sidebar.subheader("Chat History")
if st.session_state.chat_history:
    for message in st.session_state.chat_history:
        st.sidebar.write(f"{message['role']}: {message['content']}")


