# --- Importar as bibliotecas --- #
from PIL import Image
import streamlit as st
from carregar_css import carregar_css

# --- Configurações iniciais da página --- #
st.set_page_config(
    page_title='Mundo Python',
    page_icon=Image.open('./assets/logo/logo.png'),
    layout='wide'
)

# --- Carregar o CSS --- #
carregar_css()

# --- Colocar o banner do site --- #
st.image('./assets/banner/banner_escrito.png')

# --- Introdução do site --- #
st.html('<p class="fonte_intro">Bem-vindo ao Mundo Python! Aqui você aprenderá desde o começo a linguagem de programação '
        'Python, desenvolverá projetos em diversas áreas e criará um portifólio muito bem consolidado!</p>')

# --- KivyMD Multiplataforma --- #
with st.container(border=True):
    colunas = st.columns(2, vertical_alignment='center')
    with colunas[0]:
        st.image('./assets/imagens/kivymd_multiplataforma/capa/capa.png')
    with colunas[1]:
        st.html('<p class="fonte_titulos"><b>KivyMD Multiplataforma: Do Zero ao App Multiplataforma</b></p>')
        st.html('<p class="fonte_descricao">Se você acha que o Python não consegue criar aplicativos mobile, '
                'então esse curso é para você! Aqui veremos como podemos criar aplicativos mobile '
                'profissionais somente com Python, de modo simples e fácil de aprender. '
                'Então cola com a gente e veja o poder que o Python tem!')
        acessar = st.button(
            label='Acessar',
            width='stretch',
            key='kivymd_multiplataforma'
        )
        if acessar:
            st.switch_page('./pages/kivymd_multiplataforma/menu_kivymd_multiplataforma.py')

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

# --- PySide6 Maestria --- #
with st.container(border=True):
    colunas = st.columns(2, vertical_alignment='center')
    with colunas[0]:
        st.image('./assets/imagens/pyside6_maestria/capa/capa.png')
    with colunas[1]:
        st.html('<p class="fonte_titulos"><b>Maestria em PySide6: O Guia Definitivo</b></p>')
        st.html('<p class="fonte_descricao">Se você quer dar uma cara ao seu programa, esse curso '
                'é para você! Aqui você aprenderá a criar aplicativos desktop profissionais '
                'com o PySide6 de modo simples e fácil, e claro, totalmente em Python!')
        acessar = st.button(
            label='Acessar',
            width='stretch',
            key='pyside6_maestria'
        )
        if acessar:
            st.switch_page('./pages/pyside6_maestria/menu_pyside6_maestria.py')

# --- Python para Excel --- #
with st.container(border=True):
    colunas = st.columns(2, vertical_alignment='center')
    with colunas[0]:
        st.image('./assets/imagens/python_excel/capa/capa.png')
    with colunas[1]:
        st.html('<p class="fonte_titulos"><b>Curso Completo de Python para Excel: Do Zero ao Especialista</b></p>')
        st.html('<p class="fonte_descricao">Se você trabalha com Excel e não aguenta mais fazer tarefas '
                'repetitivas, este é o curso ideal para você! Aqui você verá como automatizar planilhas '
                'enormes com poucas linhas em Python; e o melhor de tudo: de um jeito bem fácil '
                'de aprender!')
        acessar = st.button(
            label='Acessar',
            width='stretch',
            key='python_excel'
        )
        if acessar:
            st.switch_page('./pages/python_excel/menu_python_excel.py')

# --- Streamlit Fullstack --- #
with st.container(border=True):
    colunas = st.columns(2, vertical_alignment='center')
    with colunas[0]:
        st.image('./assets/imagens/streamlit_fullstack/capa/capa.png')
    with colunas[1]:
        st.html('<p class="fonte_titulos"><b>Streamlit Full-Stack: Crie Aplicações Web Completas com Python</b></p>')
        st.html('<p class="fonte_descricao">Se você quer criar sites profissionais de modo rápido e simples, '
                'este curso é para você! Aqui veremos como criar dashboards completos e sites topo de linha '
                'com Streamlit. E o melhor: totalmente em Python!')
        acessar = st.button(
            label='Acessar',
            width='stretch',
            key='streamlit_fullstack'
        )
        if acessar:
            st.switch_page('./pages/streamlit_fullstack/menu_streamlit_fullstack.py')
