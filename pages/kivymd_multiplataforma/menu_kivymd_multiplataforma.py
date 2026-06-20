# --- Importar as bibliotecas --- #
from PIL import Image
import streamlit as st
from carregar_css import carregar_css

# --- Configurações iniciais da página --- #
st.set_page_config(
    page_title='KivyMD Multiplataforma',
    page_icon=Image.open('./assets/logo/logo.png'),
    layout='wide'
)

# --- Carregar o CSS --- #
carregar_css()

# --- Colocar o banner do curso --- #
st.image('./assets/imagens/kivymd_multiplataforma/capa/capa.png', width='stretch')

# --- Colunas para as caixas com as aulas (linha 1) --- #
colunas = st.columns(4, vertical_alignment='center', border=True)
with colunas[0]:
    st.image('./assets/imagens/kivymd_multiplataforma/aula_01/capa_aula_01.png')
    st.write('Aula 01: Primeiros Passos - Tema, Tela e Ciclo de Vida! 📱✨')
    acessar = st.button(
        label='Acessar',
        width='stretch',
        key='aula_01'
    )
    if acessar:
        st.switch_page('./pages/kivymd_multiplataforma/aula_01_kivymd_multiplataforma.py')

with colunas[1]:
    st.image('./assets/imagens/kivymd_multiplataforma/aula_02/capa_aula_02.png')
    st.write('Aula 02: Estrutura KV – Integrando Interface e Lógica! 🧩📱')
    st.subheader('Em breve')
#     acessar = st.button(
#         label='Acessar',
#         width='stretch',
#         key='aula_02'
#     )
#     if acessar:
#         st.switch_page('./pages/kivymd_multiplataforma/aula_02_kivymd_multiplataforma.py')

with colunas[2]:
    st.image('./assets/imagens/kivymd_multiplataforma/aula_03/capa_aula_03.png')
    st.write('Aula 03: Tema Claro/Escuro com MDSwitch – Interface Adaptativa! 🌓🎨')
    st.subheader('Em breve')
#     acessar = st.button(
#         label='Acessar',
#         width='stretch',
#         key='aula_03'
#     )
#     if acessar:
#         st.switch_page('./pages/streamlit_fullstack/aula_03_streamlit_fullstack.py')

with colunas[3]:
    st.image('./assets/imagens/kivymd_multiplataforma/aula_04/capa_aula_04.png')
    st.write('Aula 04: Temas Dinâmicos – Paleta Primária, Acento e Tons ao Vivo! 🎨🔄')
    st.subheader('Em breve')
#     acessar = st.button(
#         label='Acessar',
#         width='stretch',
#         key='aula_04'
#     )
#     if acessar:
#         st.switch_page('./pages/streamlit_fullstack/aula_04_streamlit_fullstack.py')