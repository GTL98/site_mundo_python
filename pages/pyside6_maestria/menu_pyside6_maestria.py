# --- Importar as bibliotecas --- #
from PIL import Image
import streamlit as st
from carregar_css import carregar_css

# --- Configurações iniciais da página --- #
st.set_page_config(
    page_title='PySide6 Maestria',
    page_icon=Image.open('./assets/logo/logo.png'),
    layout='wide'
)

# --- Carregar o CSS --- #
carregar_css()

# --- Colocar o banner do curso --- #
st.image('./assets/imagens/pyside6_maestria/capa/capa.png', width='stretch')

# --- Colunas para as caixas com as aulas (linha 1) --- #
colunas = st.columns(4, vertical_alignment='center', border=True)
with colunas[0]:
    st.image('./assets/imagens/pyside6_maestria/aula_01/capa_aula_01.png')
    st.write('Aula 01: Primeiros Passos - Ciclo de Vida da QApplication! 🚀')
    acessar = st.button(
        label='Acessar',
        width='stretch',
        key='aula_01'
    )
    if acessar:
        st.switch_page('./pages/pyside6_maestria/aula_01_pyside6_maestria.py')

with colunas[1]:
    st.image('./assets/imagens/pyside6_maestria/aula_02/capa_aula_02.png')
    st.write('Aula 02: Menus, Toolbars e Status Bar – Aplicações Profissionais! 🛠️')
    acessar = st.button(
        label='Acessar',
        width='stretch',
        key='aula_02'
    )
    if acessar:
        st.switch_page('./pages/pyside6_maestria/aula_02_pyside6_maestria.py')

with colunas[2]:
    st.image('./assets/imagens/pyside6_maestria/aula_03/capa_aula_03.png')
    st.write('Aula 03: Widgets de Entrada – QLineEdit, Radio, CheckBox e Validação! 🖱️✅')
    st.subheader('Em breve')
#     acessar = st.button(
#         label='Acessar',
#         width='stretch',
#         key='aula_03'
#     )
#     if acessar:
#         st.switch_page('./pages/pyside6_maestria/aula_03_pyside6_maestria.py')

with colunas[3]:
    st.image('./assets/imagens/pyside6_maestria/aula_04/capa_aula_04.png')
    st.write('Aula 04: Layouts Profissionais – QHBoxLayout, QVBoxLayout e Espaçadores! 📐🖥️')
    st.subheader('Em breve')
#     acessar = st.button(
#         label='Acessar',
#         width='stretch',
#         key='aula_04'
#     )
#     if acessar:
#         st.switch_page('./pages/pyside6_maestria/aula_04_pyside6_maestria.py')