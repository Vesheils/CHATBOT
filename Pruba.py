import streamlit as st
from openai import OpenAI

class Pagina1:
    def __init__(self):
        self.client = OpenAI(api_key="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")
        prompt = "Simula ser Harvey Specter"
        if "Harvey_Specter" not in st.session_state:
            st.session_state["Harvey_Specter"] = [{"role": "system", "content": prompt}]
    
    def communicate(self):
        messages = [{"role": "system", "content": "Simula ser Harvey Specter"}]  # Inicializamos messages con el mensaje de sistema
        user_input = st.session_state.get("user_input", "")  # Obtenemos el input del usuario
        if user_input:  # Si hay input de usuario, agregamos su mensaje a messages
            messages.append({"role": "user", "content": user_input})

        response = self.client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
        bot_message = response.choices[0].message
        messages.append({"role": "system", "content": bot_message})  # Agregamos la respuesta del bot a messages

        st.session_state["Harvey_Specter"] = messages  # Actualizamos los mensajes en la sesión

    def run(self):
        st.session_state["user_input"] = ""
        st.title("Desarrollador AI")
        st.write("Utilizando la API chatGPT, este chatbot ofrece capacidades conversacionales avanzadas.")
    
        user_input = st.text_input("Por favor ingrese un mensaje aquí.", key="user_input", on_change=self.communicate)

        messages = st.session_state.get("Harvey_Specter", [])
        for message in reversed(messages):
            speaker = "😎" if message["role"] == "user" else "🤖"
            st.write(f"{speaker}: {message['content']}")

class Pagina2:
    def __init__(self):
        self.client=OpenAI(api_key = "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")
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

        messages = st.session_state.get("Mike_Ross", [])  # Obtener messages de st.session_state, si no está presente, retornar una lista vacía

        if messages:
            for message in reversed(messages[1:]):
                if isinstance(message, dict):
                    speaker = "😎" if message["role"] == "user" else "🤖"
                    st.write(speaker + ": " + message["content"])
                else:
                    st.write("🤖: " + message.content)

def main():
    sidebar = st.sidebar

    page = sidebar.radio("Seleccione", ["PRUEBA1", "PRUEBA2"])

    if page == "PRUEBA1":
        Pagina1().run()
    elif page == "PRUEBA2":
        st.session_state["Mike_Ross"] = []  # Inicializar st.session_state["Mike_Ross"] como una lista vacía
        Pagina2().run()

if __name__ == "__main__":
    main()

