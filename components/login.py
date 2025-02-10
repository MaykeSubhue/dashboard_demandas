# Tudo do Login
import streamlit as st
import bcrypt

# Simulação de um banco de dados de usuários (em um projeto real, use um banco de dados)
usuarios = {
    "admin": bcrypt.hashpw("senha123".encode('utf-8'), bcrypt.gensalt()),
    "usuario1": bcrypt.hashpw("123456".encode('utf-8'), bcrypt.gensalt())
}

def login_page():
    st.title("Login - Dashboard de Demandas")

    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if usuario in usuarios and bcrypt.checkpw(senha.encode('utf-8'), usuarios[usuario]):
            st.session_state.autenticado = True
            st.success("Login realizado com sucesso!")
            st.experimental_rerun()
        else:
            st.error("Usuário ou senha inválidos.")
