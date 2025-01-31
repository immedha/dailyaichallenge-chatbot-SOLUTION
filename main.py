"""
Streamlit is a python framework that allows you to maintain a simple UI for your application with no effort.
We will be using it to create a simple chatbot interface: displaying the previous messages and allowing the user to input a new message.

You need to learn just a couple of things first to use it: 
(1) what is session state: https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state
(2) How to use the chat_message() and markdown() functions for displaying the assistant/user messages in a chatbot interface: https://docs.streamlit.io/develop/api-reference/chat/st.chat_message
(3) How to get user input (chat_input() function): https://docs.streamlit.io/develop/api-reference/chat/st.chat_input

NOTE: To run your streamlit app, run the coommand `streamlit run main.py` in your terminal.
"""

import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Here we load the OpenAI API key from the environment variable and set it
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("API key not found. Please set the OPENAI_API_KEY in the .env file.")

# TODO: Create an Open AI client object and set the API key

# TODO: Initialize an object to store the message history (in the session state)

# TODO: Here we will set up all the Streamlit display elements. 
# (1) Create a title for the streamlit page, 
# (2) display the previous message history using streamlit's chat_message() and markdown() functions, and 
# (3) display an input element for the user's message using streamlit's chat_input() function

# TODO: Here we will handle the user submitting the message and getting the AI response.
# You need to check if the user submitted something in the input element and if so, 
# (1) display the user's message using markdown()
# (2) append the user's message to the session state
# (3) generate the AI response using the Open AI API (make sure to include the entire message history so the AI has a memory of the conversation)
# (4) display the AI response using markdown() and append it to the session state

# NOTE: We do steps 1 and 4 even though we are already appending it to the session state, because streamlit will only update the display 
# automatically on the NEXT re-render.
