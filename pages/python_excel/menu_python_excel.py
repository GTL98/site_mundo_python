# --- Importar as bibliotecas --- #
from PIL import Image
import streamlit as st
from carregar_css import carregar_css

# --- Configurações iniciais da página --- #
st.set_page_config(
    page_title='Python para Excel',
    page_icon=Image.open('./assets/logo/logo.png'),
    layout='wide'
)

# --- Carregar o CSS --- #
carregar_css()

# --- Colocar o banner do curso --- #
st.image('./assets/imagens/python_excel/capa/capa.png', width='stretch')

# --- Colunas para as caixas com as aulas (linha 1) --- #
colunas = st.columns(4, vertical_alignment='center', border=True)
with colunas[0]:
    st.image('./assets/imagens/python_excel/aula_01/capa_aula_01.png')
    st.write('Aula 01: Criando seu Primeiro Arquivo Excel com openpyxl! 📊🐍')
    acessar = st.button(
        label='Acessar',
        width='stretch',
        key='aula_01'
    )
    if acessar:
        st.switch_page('./pages/python_excel/aula_01_python_excel.py')

with colunas[1]:
    st.image('./assets/imagens/python_excel/aula_02/capa_aula_02.png')
    st.write('Aula 02: Múltiplas Abas, Iteração Inteligente e Tratamento de Dados! 📑🔍')
    acessar = st.button(
        label='Acessar',
        width='stretch',
        key='aula_02'
    )
    if acessar:
        st.switch_page('./pages/python_excel/aula_02_python_excel.py')

with colunas[2]:
    st.image('./assets/imagens/python_excel/aula_03/capa_aula_03.png')
    st.write('Aula 03: Estilização Profissional – Cores, Fontes, Bordas e Formatação! 🎨📊')
    acessar = st.button(
        label='Acessar',
        width='stretch',
        key='aula_03'
    )
    if acessar:
        st.switch_page('./pages/python_excel/aula_03_python_excel.py')
