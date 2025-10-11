# --- Importar as bibliotecas --- #
from PIL import Image
import streamlit as st

# --- Configurações iniciais da página --- #
st.set_page_config(
    page_title='IA com Scikit-Learn, Keras e Tensorflow',
    page_icon=Image.open('./assets/logo/logo.png'),
    layout='wide'
)

# --- Carregar o estilo das fontes --- #
with open('./assets/css/style.css', 'r') as css:
    st.html(f'<style>{css.read()}</style>')

# --- Colocar o banner do curso --- #
st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/banner/banner.png')

# --- Colunas para as caixas com as aulas (linha 1)--- #
colunas = st.columns(4, vertical_alignment='center')
with colunas[0]:
    with st.container(border=True):
        st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/capa/capa.png')
        st.write('Capítulo 01 - O cenário do aprendizado de máquina')
        acessar = st.button(
            label='Acessar',
            use_container_width=True,
            key='aula_01'
        )
        if acessar:
            st.switch_page('./pages/ia_scikit_learn_keras_tensorflow/aula_01_ia_scikit_learn_keras_tensorflow.py')