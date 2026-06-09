# --- Importar as bibliotecas --- #
from PIL import Image
import streamlit as st


# --- Configurações iniciais da página --- #
st.set_page_config(
    page_title='Python para Excel',
    page_icon=Image.open('./assets/logo/logo.png'),
    layout='wide'
)

# --- Carregar o CSS --- #
with open('./assets/css/style.css', 'r') as css:
    st.html(f'<style>{css.read()}</style>')

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
