 # Arquivo principal para rodar o dashboard 
import streamlit as st
from components import login
from pages import controle_demanda, dashboard, relatorio_pdf

# Configuração da página
st.set_page_config(page_title="Dashboard de Demandas", layout="wide")

# Autenticação do usuário
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    login.login_page()
else:
    # Barra lateral para navegação
    menu = st.sidebar.selectbox("Menu", ["Controle de Demandas", "Dashboard de Produtividade", "Relatórios em PDF", "Sair"])

    if menu == "Controle de Demandas":
        controle_demanda.registrar_demanda()
    elif menu == "Dashboard de Produtividade":
        dashboard.visualizar_dashboard()
    elif menu == "Relatórios em PDF":
        relatorio_pdf.gerar_relatorio()
    elif menu == "Sair":
        st.session_state.autenticado = False
        st.experimental_rerun()