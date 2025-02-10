 # Página para geração de relatórios
import streamlit as st
import sqlite3
from fpdf import FPDF
from datetime import datetime
import os

def gerar_relatorio():
    st.title("Gerar Relatório em PDF")

    # Conexão com o banco de dados SQLite
    conn = sqlite3.connect('data\demandas.db')
    c = conn.cursor()

    # Consulta das demandas do mês atual
    mes_atual = datetime.now().strftime("%Y-%m")
    demandas = c.execute("SELECT funcionario, descricao, data FROM demandas WHERE data LIKE ?", (f'{mes_atual}%',)).fetchall()

    if demandas:
        if st.button("Gerar Relatório em PDF"):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            pdf.cell(200, 10, txt=f"Relatório de Demandas - {mes_atual}", ln=True, align='C')
            pdf.ln(10)

            for demanda in demandas:
                pdf.multi_cell(0, 10, f"Funcionário: {demanda[0]}\nDemanda: {demanda[1]}\nData: {demanda[2]}\n", border=1)
                pdf.ln(2)

            # Verifica se a pasta de relatórios existe, senão cria
            if not os.path.exists('relatorios'):
                os.makedirs('relatorios')

            caminho_arquivo = f'relatorios\relatorio_{mes_atual}.pdf'
            pdf.output(caminho_arquivo)

            st.success(f"Relatório gerado com sucesso em: {caminho_arquivo}")
            with open(caminho_arquivo, "rb") as file:
                st.download_button(label="Baixar Relatório PDF", data=file, file_name=f"relatorio_{mes_atual}.pdf", mime="application/pdf")
    else:
        st.info("Nenhuma demanda registrada para o mês atual.")
