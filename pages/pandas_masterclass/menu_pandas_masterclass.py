# --- Importar as bibliotecas --- #
from PIL import Image
import streamlit as st
from carregar_css import carregar_css


# --- Configurações iniciais da página --- #
st.set_page_config(
    page_title='Pandas Masterclass',
    page_icon=Image.open('./assets/logo/logo.png'),
    layout='wide'
)

# --- Carregar o CSS --- #
carregar_css()

# --- Colocar o banner do curso --- #
st.image('./assets/imagens/pandas_masterclass/capa/capa.png', width='stretch')

# --- Colunas para as caixas com as aulas (linha 1) --- #
colunas = st.columns(4, vertical_alignment='center', border=True)
with colunas[0]:
    st.image('./assets/imagens/pandas_masterclass/aula_01/capa_aula_01.png')
    st.write('Aula 01: Criando seu Primeiro DataFrame 🚀')
    acessar = st.button(
        label='Acessar',
        width='stretch',
        key='aula_01'
    )
    if acessar:
        st.switch_page('./pages/pandas_masterclass/aula_01_pandas_masterclass.py')

with colunas[1]:
    st.image('./assets/imagens/pandas_masterclass/aula_02/capa_aula_02.png')
    st.write('Aula 02: Domine a Importação de Dados - CSV, Excel, Parquet e URLs! 📂🚀')
    acessar = st.button(
        label='Acessar',
        width='stretch',
        key='aula_02'
    )
    if acessar:
        st.switch_page('./pages/pandas_masterclass/aula_02_pandas_masterclass.py')

with colunas[2]:
    st.image('./assets/imagens/pandas_masterclass/aula_03/capa_aula_03.png')
    st.write('Aula 03: Explorando Dados - Conheça Seu Dataset Como um Detetive! 🔍📊')
    acessar = st.button(
        label='Acessar',
        width='stretch',
        key='aula_03'
    )
    if acessar:
        st.switch_page('./pages/pandas_masterclass/aula_03_pandas_masterclass.py')

with colunas[3]:
    st.image('./assets/imagens/pandas_masterclass/aula_04/capa_aula_04.png')
    st.write('Aula 04: Seleção de Dados - Extraia Exatamente o Que Precisa! 🎯🔍')
    st.subheader('Em breve')
    # acessar = st.button(
    #     label='Acessar',
    #     width='stretch',
    #     key='aula_04'
    # )
    # if acessar:
    #     pass

# --- Colunas para as caixas com as aulas (linha 2) --- #
colunas = st.columns(4, vertical_alignment='center', border=True)
with colunas[0]:
    st.image('./assets/imagens/pandas_masterclass/aula_05/capa_aula_05.png')
    st.write('Aula 05: Limpando Dados - Valores Nulos, Duplicatas e Padronização! 🧹🧼')
    st.subheader('Em breve')
    # acessar = st.button(
    #     label='Acessar',
    #     width='stretch',
    #     key='aula_05'
    # )
    # if acessar:
    #     pass

with colunas[1]:
    st.image('./assets/imagens/pandas_masterclass/aula_06/capa_aula_06.png')
    st.write('Aula 06: Conversão de Tipos e Strings – Limpeza Profissional! 🔤🔄')
    st.subheader('Em breve')
    # acessar = st.button(
    #     label='Acessar',
    #     width='stretch',
    #     key='aula_06'
    # )
    # if acessar:
    #     pass

with colunas[2]:
    st.image('./assets/imagens/pandas_masterclass/aula_07/capa_aula_07.png')
    st.write('Aula 07: Groupby e Agregações – Resumindo Dados como Especialista! 📊🔍')
    st.subheader('Em breve')
    # acessar = st.button(
    #     label='Acessar',
    #     width='stretch',
    #     key='aula_07'
    # )
    # if acessar:
    #     pass

with colunas[3]:
    st.image('./assets/imagens/pandas_masterclass/aula_08/capa_aula_08.png')
    st.write('Aula 08: Transformação de Dados – pivot_table, melt, stack e unstack! 🔄📊')
    st.subheader('Em breve')
    # acessar = st.button(
    #     label='Acessar',
    #     width='stretch',
    #     key='aula_08'
    # )
    # if acessar:
    #     pass