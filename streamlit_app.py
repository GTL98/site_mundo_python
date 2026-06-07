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
            st.Page('./pages/pandas_masterclass/aula_03_pandas_masterclass.py', title='Aula 03:  Conheça Seu Dataset Como um Detetive!')
        ],
    },
    position='top'
)
pg.run()