import streamlit as st
import pandas as pd
import plotly as pl
import psycopg2

# estabelecer conexão com o banco de dados

st.header("Teste")

conn = psycopg2.connect(
    host="localhost",
    port="5433",
    dbname="farmaceutica",
    user="postgres",
    password="1234"
)

#consulta docmentation https://www.postgresql.org/docs/current/index.html

