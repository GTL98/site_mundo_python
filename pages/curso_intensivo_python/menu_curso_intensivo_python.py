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
st.image('./assets/imagens/curso_intensivo_python/banner/banner.png')

# --- Colunas para as caixas com as aulas (linha 1)--- #
colunas = st.columns(4, vertical_alignment='center')
with colunas[0]:
    with st.container(border=True):
        st.image('./assets/imagens/curso_intensivo_python/capa/capa.png')
        st.write('Capítulo 01 - Baixar o Python')
        acessar = st.button(
            label='Acessar',
            use_container_width=True,
            key='aula_01'
        )
        if acessar:
            st.switch_page('./pages/curso_intensivo_python/aula_01_curso_intensivo_python.py')

with colunas[1]:
    with st.container(border=True):
        st.image('./assets/imagens/curso_intensivo_python/capa/capa.png')
        st.write('Capítulo 02 - Variáveis e tipos de dados simples')
        acessar = st.button(
            label='Acessar',
            use_container_width=True,
            key='aula_02'
        )
        if acessar:
            st.switch_page('./pages/curso_intensivo_python/aula_02_curso_intensivo_python.py')

with colunas[2]:
    with st.container(border=True):
        st.image('./assets/imagens/curso_intensivo_python/capa/capa.png')
        st.write('Capítulo 03 - Introdução à listas')
        acessar = st.button(
            label='Acessar',
            use_container_width=True,
            key='aula_03'
        )
        if acessar:
            st.switch_page('./pages/curso_intensivo_python/aula_03_curso_intensivo_python.py')
# with colunas[3]:
#     with st.container(border=True):
#         st.image('./assets/imagens/curso_intensivo_python/capa/capa.png')
#         st.write('Capítulo 04 - Trabalhando com listas')
#         acessar = st.button(
#             label='Acessar',
#             use_container_width=True,
#             key='aula_04'
#         )
#
# # --- Colunas para as caixas com as aulas (linha 2)--- #
# colunas = st.columns(4, vertical_alignment='center')
# with colunas[0]:
#     with st.container(border=True):
#         st.image('./assets/imagens/curso_intensivo_python/capa/capa.png')
#         st.write('Capítulo 05 - Instruções if')
#         acessar = st.button(
#             label='Acessar',
#             use_container_width=True,
#             key='aula_05'
#         )
# with colunas[1]:
#     with st.container(border=True):
#         st.image('./assets/imagens/curso_intensivo_python/capa/capa.png')
#         st.write('Capítulo 06 - Dicionários')
#         acessar = st.button(
#             label='Acessar',
#             use_container_width=True,
#             key='aula_06'
#         )
# with colunas[2]:
#     with st.container(border=True):
#         st.image('./assets/imagens/curso_intensivo_python/capa/capa.png')
#         st.write('Capítulo 07 - Entradas do usuário e loops while')
#         acessar = st.button(
#             label='Acessar',
#             use_container_width=True,
#             key='aula_07'
#         )
#
# with colunas[3]:
#     with st.container(border=True):
#         st.image('./assets/imagens/curso_intensivo_python/capa/capa.png')
#         st.write('Capítulo 08 - Funções')
#         acessar = st.button(
#             label='Acessar',
#             use_container_width=True,
#             key='aula_08'
#         )
#
# # --- Colunas para as caixas com as aulas (linha 3)--- #
# colunas = st.columns(4, vertical_alignment='center')
# with colunas[0]:
#     with st.container(border=True):
#         st.image('./assets/imagens/curso_intensivo_python/capa/capa.png')
#         st.write('Capítulo 09 - Classes')
#         acessar = st.button(
#             label='Acessar',
#             use_container_width=True,
#             key='aula_09'
#         )
# with colunas[1]:
#     with st.container(border=True):
#         st.image('./assets/imagens/curso_intensivo_python/capa/capa.png')
#         st.write('Capítulo 10 - Arquivos e exceções')
#         acessar = st.button(
#             label='Acessar',
#             use_container_width=True,
#             key='aula_10'
#         )