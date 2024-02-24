import streamlit as st
from openai import OpenAI
import secret_keys

client = OpenAI(api_key = secret_keys.openai_api_key)


if "messages" not in st.session_state:
    st.session_state["messages"] = [
  {"role": "system", "content": "Piensa como un Desarrollador"}
]


def communicate():
    messages = st.session_state["messages"]
    user_message = {"role": "user", "content": st.session_state["user_input"]}
    messages.append(user_message)


    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=messages
    )
    bot_message = response.choices[0].message
    messages.append(bot_message)


    st.session_state["user_input"] = ""

