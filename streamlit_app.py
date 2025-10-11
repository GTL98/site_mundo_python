# --- Importar o Streamlit --- #
import streamlit as st

# --- Menu separado com as páginas --- #
pg = st.navigation(
    {
        'Página Inicial': [st.Page('./home.py', title='Página Inicial')],
        'Curso Intensivo de Python': [
            st.Page('./pages/curso_intensivo_python/menu_curso_intensivo_python.py', title='Aulas'),
            st.Page('./pages/curso_intensivo_python/aula_01_curso_intensivo_python.py', title='Capítulo 01 - Baixar o Python'),
            st.Page('./pages/curso_intensivo_python/aula_02_curso_intensivo_python.py', title='Capítulo 02 - Variáveis e tipos de dados simples'),
            st.Page('./pages/curso_intensivo_python/aula_03_curso_intensivo_python.py', title='Capítulo 03 - Introdução à listas')
        ],
        'IA com Scikit-Learn, Keras e Tensorflow': [
            st.Page('./pages/ia_scikit_learn_keras_tensorflow/menu_ia_scikit_learn_keras_tensorflow.py', title='Aulas'),
            st.Page('./pages/ia_scikit_learn_keras_tensorflow/aula_01_ia_scikit_learn_keras_tensorflow.py', title='Capítulo 01 - O cenário do aprendizado de máquina'),
        ]
    },
    position='top'
)
pg.run()