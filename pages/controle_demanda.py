# Página para controle de demanda
import streamlit as st
import sqlite3
from datetime import datetime

# Conexão com o banco de dados SQLite
conn = sqlite3.connect('data\demandas.db')
c = conn.cursor()

# Criação da tabela de demandas (se não existir)
c.execute('''
    CREATE TABLE IF NOT EXISTS demandas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        funcionario TEXT,
        descricao TEXT,
        data TEXT
    )
''')
conn.commit()

def registrar_demanda():
    st.title("Registrar Demanda")

    funcionario = st.text_input("Nome do Funcionário")
    descricao = st.text_area("Descrição da Demanda")
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if st.button("Registrar Demanda"):
        if funcionario and descricao:
            c.execute("INSERT INTO demandas (funcionario, descricao, data) VALUES (?, ?, ?)",
                      (funcionario, descricao, data))
            conn.commit()
            st.success("Demanda registrada com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos.")

    # Exibição das demandas registradas
    st.subheader("Demandas Registradas")
    demandas = c.execute("SELECT funcionario, descricao, data FROM demandas ORDER BY data DESC").fetchall()

    for demanda in demandas:
        st.write(f"**Funcionário:** {demanda[0]} | **Demanda:** {demanda[1]} | **Data:** {demanda[2]}")
