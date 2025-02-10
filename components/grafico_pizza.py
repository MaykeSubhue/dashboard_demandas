# Página com gráficos interativos
import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

def visualizar_dashboard():
    st.title("Dashboard de Produtividade")

    # Conexão com o banco de dados SQLite
    conn = sqlite3.connect('data\demandas.db')
    c = conn.cursor()

    # Consulta das demandas registradas
    demandas = c.execute("SELECT funcionario, COUNT(*) as total_demandas FROM demandas GROUP BY funcionario").fetchall()

    if demandas:
        # Transformar os dados em um DataFrame para o Plotly
        df = pd.DataFrame(demandas, columns=['Funcionário', 'Total de Demandas'])

        # Gráfico de Pizza com Plotly
        fig = px.pie(df, names='Funcionário', values='Total de Demandas', title='Produtividade por Funcionário')
        st.plotly_chart(fig)
    else:
        st.info("Nenhuma demanda registrada até o momento.")
