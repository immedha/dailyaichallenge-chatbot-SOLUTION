import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Here we load the OpenAI API key from the environment variable and set it
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("API key not found. Please set the OPENAI_API_KEY in the .env file.")

# Create an Open AI client object and set the API key
client = OpenAI(api_key=api_key)

# Initialize an object to store the message history (in the session state)
if "messages" not in st.session_state:
    st.session_state.messages = []


# TODO: Here we will set up all the Streamlit display elements. 
# (1) Create a title for the streamlit page, 
# (2) display the previous message history using streamlit's chat_message() and markdown() functions, and 
# (3) display an input element for the user's message using streamlit's chat_input() function
st.title("Daily AI Challenge: Simple Chatbot With Memory 🤖")
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

input_el = st.chat_input("What is up?")

# Here we handle the user submitting the message and getting the AI response.
# If the user submitted a message, input_el will not be None and instead will store the string they inputted
if input_el:
    # Display the user's message
    st.chat_message("user").markdown(input_el)
    # Append it to the session state
    st.session_state.messages.append({"role": "user", "content": input_el})

    # Generate the AI response
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a very smart show-off chatbot. Keep that personality while answering the user's queries or responding to their message."}
        ] + st.session_state.messages
    )
    ai_reply = response.choices[0].message.content
    # Display the AI response
    with st.chat_message("assistant"):
        st.markdown(ai_reply)

    # append it to the session state
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
