# --- Importar as bibliotecas --- #
from PIL import Image
import streamlit as st

# --- Configurações iniciais da página --- #
st.set_page_config(
    page_title='Curso Intensivo de Python',
    page_icon=Image.open('./assets/logo/logo.png'),
    layout='wide'
)

# --- Carregar o estilo das fontes --- #
with open('./assets/css/style.css', 'r') as css:
    st.html(f'<style>{css.read()}</style>')

# --- Colocar o banner do curso --- #
st.image('./assets/imagens/guis_python_pyside2/banner/banner.png')

# --- Colunas para as caixas com as aulas (linha 1)--- #
colunas = st.columns(4, vertical_alignment='center')
with colunas[0]:
    with st.container(border=True):
        st.image('./assets/imagens/guis_python_pyside2/capa/capa.png')
        st.write('Capítulo 01 - Introdução à GUIs')
        acessar = st.button(
            label='Acessar',
            use_container_width=True,
            key='aula_01'
        )
        if acessar:
            st.switch_page('./pages/guis_python_pyside2/aula_01_guis_python_pyside2.py')
with colunas[1]:
    with st.container(border=True):
        st.image('./assets/imagens/guis_python_pyside2/capa/capa.png')
        st.write('Capítulo 02 - Seu primeiro App')
        acessar = st.button(
            label='Acessar',
            use_container_width=True,
            key='aula_02'
        )
        if acessar:
            st.switch_page('./pages/guis_python_pyside2/aula_02_guis_python_pyside2.py')
