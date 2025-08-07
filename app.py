import streamlit as st
import pandas as pd
import plotly as pl
import psycopg2

# estabelecer conexão com o banco de dados

conn = psycopg2.connectect(
    host="localhost",
    port="5435",
    dbname="nome_do_banco",
    user="seu_usuario",
    password="sua_senha"
)

#teste com git