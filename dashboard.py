import streamlit as st
import mysql.connector
import pandas as pd


st.set_page_config(layout="wide")
# Função para recuperar todos os dados do banco de dados
def get_dados_completos():
    db_endpoint = "institutoscheffelt.clazmf0mr7c4.sa-east-1.rds.amazonaws.com"
    db_port = 3306
    db_user = "admin"
    db_password = "Eduardo13*"
    db_name = "questoes"

    conn = mysql.connector.connect(
        host=db_endpoint,
        port=db_port,
        user=db_user,
        password=db_password,
        database=db_name
    )
    cursor = conn.cursor()
    cursor.execute("SELECT Materia, Assunto, Orgao, Cargo, Prova, Ano, Banca, TipoQuestao, NivelDificuldade, Enunciado, Questao, Resposta FROM DadosGerais JOIN Questoes ON DadosGerais.ID = Questoes.DadosGerais_ID JOIN Respostas ON Questoes.ID = Respostas.Questao_ID")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

# Configuração do aplicativo Streamlit
st.title("Visualização de Dados do Banco de Dados")

# Recupere apenas os dados relevantes, sem números de ID ou chaves estrangeiras
dados_relevantes = get_dados_completos()

# Crie um DataFrame do Pandas com os dados e nomes de colunas
colunas = ["Materia", "Assunto", "Orgao", "Cargo", "Prova", "Ano", "Banca", "TipoQuestao", "NivelDificuldade", "Enunciado", "Questao", "Resposta"]
df = pd.DataFrame(dados_relevantes, columns=colunas)

# Exiba a tabela no Streamlit
st.header("Dados Relevantes:")
st.dataframe(df)