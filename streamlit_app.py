# --- Importar o Streamlit --- #
import streamlit as st

# --- Menu separado com as páginas --- #
pg = st.navigation(
    {
        'Página Inicial': [st.Page('home.py', title='Página Inicial')],
        'KivyMD Multiplataforma': [
            st.Page('./pages/kivymd_multiplataforma/menu_kivymd_multiplataforma.py', title='Aulas'),
            st.Page('./pages/kivymd_multiplataforma/aula_01_kivymd_multiplataforma.py', title='Aula 01: Tema, Tela e Ciclo de Vida!'),
            st.Page('./pages/kivymd_multiplataforma/aula_02_kivymd_multiplataforma.py', title='Aula 02: Estrutura KV – Integrando Interface e Lógica!')
        ],
        'Pandas Masterclass':[
            st.Page('./pages/pandas_masterclass/menu_pandas_masterclass.py', title='Aulas'),
            st.Page('./pages/pandas_masterclass/aula_01_pandas_masterclass.py', title='Aula 01: Criando seu Primeiro DataFrame'),
            st.Page('./pages/pandas_masterclass/aula_02_pandas_masterclass.py', title='Aula 02: Domine a Importação de Dados'),
            st.Page('./pages/pandas_masterclass/aula_03_pandas_masterclass.py', title='Aula 03: Explorando Dados')
        ],
        'PySide6 Maestria': [
            st.Page('./pages/pyside6_maestria/menu_pyside6_maestria.py', title='Aulas'),
            st.Page('./pages/pyside6_maestria/aula_01_pyside6_maestria.py', title='Aula 01: Ciclo de Vida da QApplication')
        ],
        'Python para Excel': [
            st.Page('./pages/python_excel/menu_python_excel.py', title='Aulas'),
            st.Page('./pages/python_excel/aula_01_python_excel.py', title='Aula 01: Criando seu Primeiro Arquivo Excel com openpyxl'),
            st.Page('./pages/python_excel/aula_02_python_excel.py', title='Aula 02: Múltiplas Abas, Iteração Inteligente e Tratamento de Dados'),
            st.Page('./pages/python_excel/aula_03_python_excel.py', title='Aula 03: Estilização Profissional – Cores, Fontes, Bordas e Formatação')
        ],
        'Streamlit Full-Stack': [
            st.Page('./pages/streamlit_fullstack/menu_streamlit_fullstack.py', title='Aulas'),
            st.Page('./pages/streamlit_fullstack/aula_01_streamlit_fullstack.py', title='Aula 01: Widgets, Layout e Persistência'),
            st.Page('./pages/streamlit_fullstack/aula_02_streamlit_fullstack.py', title='Aula 02: Layouts Avançados – Colunas, Abas e Popovers')
        ]
    },
    position='sidebar'
)
pg.run()