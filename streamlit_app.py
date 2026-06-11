# --- Importar o Streamlit --- #
import streamlit as st

# --- Menu separado com as páginas --- #
pg = st.navigation(
    {
        'Página Inicial': [st.Page('home.py', title='Página Inicial')],
        'Pandas Masterclass':[
            st.Page('./pages/pandas_masterclass/menu_pandas_masterclass.py', title='Aulas'),
            st.Page('./pages/pandas_masterclass/aula_01_pandas_masterclass.py', title='Aula 01: Criando seu Primeiro DataFrame'),
            st.Page('./pages/pandas_masterclass/aula_02_pandas_masterclass.py', title='Aula 02: Domine a Importação de Dados'),
            st.Page('./pages/pandas_masterclass/aula_03_pandas_masterclass.py', title='Aula 03: Explorando Dados')
        ],
        'Python para Excel': [
            st.Page('./pages/python_excel/menu_python_excel.py', title='Aulas'),
            st.Page('./pages/python_excel/aula_01_python_excel.py', title='Aula 01: Criando seu Primeiro Arquivo Excel com openpyxl')
        ],
        'Streamlit Full-Stack': [
            st.Page('./pages/streamlit_fullstack/menu_streamlit_fullstack.py', title='Aulas'),
            st.Page('./pages/streamlit_fullstack/aula_01_streamlit_fullstack.py', title='Aula 01: Widgets, Layout e Persistência')
        ]
    },
    position='top'
)
pg.run()