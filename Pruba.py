import streamlit as st
from openai import openai

class Pagina1:
  def__init__(self)
    self.client=OpenAI(api_key = secrets.OpenAIAPI.openai_api_key)
      
      prompt = "Simula ser Harvey Specter"
      
      if "trip_adviser_messages" not in st.session_state:
      st.session_state["Harvey_Specter"] = ["role": "system", "content": prompt]
    
    def communicate():
      messages = st.session_state["Harvey_Specter"]
      user_message = {"role": "user", "content": st.session_state["user_input"]}
      messages.append(user_message)
      response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
      bot_message = response.choices[0].message
      messages.append(bot_message)


    st.session_state["user_input"] = ""
    st.title ("Desarrollador AI")
    st.write ("Utilizando la API chatGPT, este chatbot ofrece capacidades conversacionales avanzadas.")
  
    user_input = st.text_input("por favor ingrese un mensaje aquí.", key = "user_input", on_change=communicate)

    if st.session_state["Harvey_Specter"]:
    messages = st.session_state["messages"]


    for message in reversed(messages[1:]):
        if isinstance(message, dict):
            speaker = "😎" if message["role"] == "user" else "🤖"
            st.write (speaker + ": " + message["content"])
        else:
            st.write("🤖: " + message.content)


class Pagina2:
  def__init__(self):
    self.client=OpenAI(api_key=secret_keys.openai_api_key)
      
      prompt2 = "Simula ser Mike Ross"
      
      if "trip_adviser_messages" not in st.session_state:
      st.session_state["Mike_Ross"] = ["role": "system", "content": prompt2]
    
    def communicate():
      messages = st.session_state["Mike_Ross"]
      user_message = {"role": "user", "content": st.session_state["user_input"]}
      messages.append(user_message)
      response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
      bot_message = response.choices[0].message
      messages.append(bot_message)


    st.session_state["user_input"] = ""
    st.title ("Desarrollador AI")
    st.write ("Utilizando la API chatGPT, este chatbot ofrece capacidades conversacionales avanzadas.")
  
    user_input = st.text_input("por favor ingrese un mensaje aquí.", key = "user_input", on_change=communicate)

    if st.session_state["Mike_Ross"]:
    messages = st.session_state["messages"]


    for message in reversed(messages[1:]):
        if isinstance(message, dict):
            speaker = "😎" if message["role"] == "user" else "🤖"
            st.write (speaker + ": " + message["content"])
        else:
            st.write("🤖: " + message.content)

def main():
    siderbar = st.siderbar

    page = siderbar.radio("Seleccione", ["PRUBA 1", "PRUBA 2"])

    if page == "PRUBA1"
      Pagina1()
    else
      Pagina2()

if __name__ == "__main__":
  main()
