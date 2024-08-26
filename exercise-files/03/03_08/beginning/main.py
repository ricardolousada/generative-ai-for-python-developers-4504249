import streamlit as st
from handlers import generate_chat_completion
import openai
from dotenv import load_dotenv

# Constants
PERSONA = "You are a skilled stant-up comediant with a quick with and charismatic presence, known for their clever storytelling ability."
MODEL_ENGINE = "gpt-3.5-turbo"
MESSAGE_SYSTEM = "You are a skilled standup commediant with a kanck for telling 1-2 sentence funny stories"
messages = [{"role": "system", "content": MESSAGE_SYSTEM}]

load_dotenv()
client = openai.OpenAI()

def to_dict(obj):
    return {
        "content": obj.content,
        "role": obj.role,
    }

def generate_chat_completion(user_input=""):
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.5,
        #max_tokens=150,
    )
    message = response.choices[0].message
    messages.append(to_dict(message))
    return message.content
    

# Streamlit App
st.title("😁 Funny chatbot")  # Add a title

# User input
with st.form("user_form", clear_on_submit=True):
    user_input = st.text_input("Type something")
    submit_button = st.form_submit_button(label="Send")

# Press Enter to generate response from chatbot

if submit_button:
    # generate chat completion
    with st.spinner("generating response...wait for it"):
        completion = generate_chat_completion(user_input)
        st.write(completion)
