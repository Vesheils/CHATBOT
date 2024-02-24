import streamlit as st
from openai import openai

class Pagina1:
    def __init__(self):
        self.client = openai(api_key=secret_keys.openai_api_key)
        prompt = "Simula ser Harvey Specter"
        if "Harvey_Specter" not in st.session_state:
            st.session_state["Harvey_Specter"] = [{"role": "system", "content": prompt}]
    
    def communicate(self):
        messages = st.session_state["Harvey_Specter"]
        user_message = {"role": "user", "content": st.session_state["user_input"]}
        messages.append(user_message)
        response = self.client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
        bot_message = response.choices[0].message
        messages.append(bot_message)

    def run(self):
        st.session_state["user_input"] = ""
        st.title("Desarrollador AI")
        st.write("Utilizando la API chatGPT, este chatbot ofrece capacidades conversacionales avanzadas.")
    
        user_input = st.text_input("Por favor ingrese un mensaje aquí.", key="user_input", on_change=self.communicate)

        if st.session_state["Harvey_Specter"]:
            messages = st.session_state["Harvey_Specter"]

        for message in reversed(messages[1:]):
            if isinstance(message, dict):
                speaker = "😎" if message["role"] == "user" else "🤖"
                st.write(speaker + ": " + message["content"])
            else:
                st.write("🤖: " + message.content)

class Pagina2:
    def __init__(self):
        self.client = openai(api_key=secret_keys.openai_api_key)
        prompt2 = "Simula ser Mike Ross"
        if "Mike_Ross" not in st.session_state:
            st.session_state["Mike_Ross"] = [{"role": "system", "content": prompt2}]
    
    def communicate(self):
        messages = st.session_state["Mike_Ross"]
        user_message = {"role": "user", "content": st.session_state["user_input"]}
        messages.append(user_message)
        response = self.client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
        bot_message = response.choices[0].message
        messages.append(bot_message)

    def run(self):
        st.session_state["user_input"] = ""
        st.title("Desarrollador AI")
        st.write("Utilizando la API chatGPT, este chatbot ofrece capacidades conversacionales avanzadas.")
    
        user_input = st.text_input("Por favor ingrese un mensaje aquí.", key="user_input", on_change=self.communicate)

        if st.session_state["Mike_Ross"]:
            messages = st.session_state["Mike_Ross"]

        for message in reversed(messages[1:]):
            if isinstance(message, dict):
                speaker = "😎" if message["role"] == "user" else "🤖"
                st.write(speaker + ": " + message["content"])
            else:
                st.write("🤖: " + message.content)

def main():
    sidebar = st.sidebar

    page = sidebar.radio("Seleccione", ["PRUEBA 1", "PRUEBA 2"])

    if page == "PRUEBA 1":
        Pagina1().run()
    else:
        Pagina2().run()

if __name__ == "__main__":
    main()
