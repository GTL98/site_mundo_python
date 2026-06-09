# --- Importar as bibliotecas --- #
from PIL import Image
import streamlit as st

# --- Configurações iniciais da página --- #
st.set_page_config(
    page_title='Mundo Python',
    page_icon=Image.open('./assets/logo/logo.png'),
    layout='wide',
    initial_sidebar_state='collapsed'
)

# --- Carregar o estilo das fontes --- #
with open('./assets/css/style.css', 'r') as css:
    st.html(f'<style>{css.read()}</style>')

# --- Colocar o banner do site --- #
st.image('./assets/banner/banner_escrito.png')

# --- Introdução do site --- #
st.html('<p class="fonte_intro">Bem-vindo ao Mundo Python! Aqui você aprenderá desde o começo a linguagem de programação '
        'Python, desenvolverá projetos em diversas áreas e criará um portifólio muito bem consolidado!</p>')

# --- Pandas Masterclass --- #
with st.container(border=True):
    colunas = st.columns(2, vertical_alignment='center')
    with colunas[0]:
        st.image('./assets/imagens/pandas_masterclass/capa/capa.png')
    with colunas[1]:
        st.html('<p class="fonte_titulos"><b>Pandas Masterclass: Do Zero ao Herói dos Dados</b></p>')
        st.html('<p class="fonte_descricao">Se você quer aprender a como dominar os dados e criar relatórios '
                'com tabelas profissionais, esse é o curso certo para você! Aqui você aprenderá a como '
                'utilizar todo o poder do Pandas para criar excelentes análises e como compartilhar '
                'de modo profissional os seus insights!')
        acessar = st.button(
            label='Acessar',
            width='stretch',
            key='pandas_masterclass'
        )
        if acessar:
            st.switch_page('./pages/pandas_masterclass/menu_pandas_masterclass.py')

# --- Python para Excel --- #
with st.container(border=True):
    colunas = st.columns(2, vertical_alignment='center')
    with colunas[0]:
        st.image('./assets/imagens/python_excel/capa/capa.png')
    with colunas[1]:
        st.html('<p class="fonte_titulos"><b>Curso Completo de Python para Excel: Do Zero ao Especialista</b></p>')
        st.html('<p class="fonte_descricao">Se você trabalha com Excel e não aguenta mais fazer tarefas '
                'repetitivas, este é o curso ideal para você! Aqui você verá como automatizar planilhas '
                'enormes com poucas linhas em Python; e o melhor de tudo: de um keito bem fácil '
                'de aprender!')
        acessar = st.button(
            label='Acessar',
            width='stretch',
            key='python_excel'
        )
        if acessar:
            st.switch_page('./pages/python_excel/menu_python_excel.py')
