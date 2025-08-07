import streamlit as st
import pandas as pd
import psycopg2

# Título do app
st.header("Teste")

# Conexão com o banco
@st.cache_resource
def connect_to_db():
    return psycopg2.connect(
        host="localhost",
        database="farmaceutica",
        user="postgres",
        password="1234",
        port=5432
    )

# Carregando dados
@st.cache_data
def load_data():
    conn = connect_to_db()
    df_clientes = pd.read_sql("SELECT * FROM clientes;", conn)
    df_produtos = pd.read_sql("SELECT * FROM produtos;", conn)
    conn.close()
    return df_clientes, df_produtos

# Exibir dados
st.title("📦 Dados do Banco de Dados da Farmacêutica")

try:
    df_clientes, df_produtos = load_data()

    st.subheader("👥 Tabela de Clientes")
    st.dataframe(df_clientes)

    st.subheader("💊 Tabela de Produtos")
    st.dataframe(df_produtos)

except Exception as e:
    st.error(f"Erro ao carregar dados: {e}")
