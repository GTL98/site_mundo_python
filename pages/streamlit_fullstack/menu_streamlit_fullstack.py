# --- Importar as bibliotecas --- #
from PIL import Image
import streamlit as st


# --- Configurações iniciais da página --- #
st.set_page_config(
    page_title='Streamlit Fullstack',
    page_icon=Image.open('./assets/logo/logo.png'),
    layout='wide'
)

# --- Carregar o CSS --- #
with open('./assets/css/style.css', 'r') as css:
    st.html(f'<style>{css.read()}</style>')

# --- Colocar o banner do curso --- #
st.image('./assets/imagens/streamlit_fullstack/capa/capa.png', width='stretch')

# --- Colunas para as caixas com as aulas (linha 1) --- #
colunas = st.columns(4, vertical_alignment='center', border=True)
with colunas[0]:
    st.image('./assets/imagens/streamlit_fullstack/aula_01/capa_aula_01.png')
    st.write('Aula 01: Primeiros Passos – Widgets, Layout e Persistência! 🚀')
    acessar = st.button(
        label='Acessar',
        width='stretch',
        key='aula_01'
    )
    if acessar:
        st.switch_page('./pages/streamlit_fullstack/aula_01_streamlit_fullstack.py')

with colunas[1]:
    st.image('./assets/imagens/streamlit_fullstack/aula_02/capa_aula_02.png')
    st.write('Aula 02: Layouts Avançados – Colunas, Abas e Popovers! 📐🚀')
    st.subheader('Em breve')
#     acessar = st.button(
#         label='Acessar',
#         width='stretch',
#         key='aula_02'
#     )
#     if acessar:
#         st.switch_page('./pages/streamlit_fullstack/aula_02_streamlit_fullstack.py')

with colunas[2]:
    st.image('./assets/imagens/streamlit_fullstack/aula_03/capa_aula_03.png')
    st.write('Aula 03: Cache Data vs Cache Resource – Performance Pro! ⚡📊')
    st.subheader('Em breve')
#     acessar = st.button(
#         label='Acessar',
#         width='stretch',
#         key='aula_03'
#     )
#     if acessar:
#         st.switch_page('./pages/streamlit_fullstack/aula_03_streamlit_fullstack.py')

with colunas[3]:
    st.image('./assets/imagens/streamlit_fullstack/aula_04/capa_aula_04.png')
    st.write('Aula 04: Fragmentos e Atualização Assíncrona – Monitoramento em Tempo Real! ⚡🔄')
    st.subheader('Em breve')
#     acessar = st.button(
#         label='Acessar',
#         width='stretch',
#         key='aula_04'
#     )
#     if acessar:
#         st.switch_page('./pages/streamlit_fullstack/aula_04_streamlit_fullstack.py')