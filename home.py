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

# --- Curso Intensivo de Python --- #
with st.container(border=True):
    colunas = st.columns(2)
    with colunas[0]:
        st.image('./assets/imagens/curso_intensivo_python/capa/capa.png')
    with colunas[1]:
        st.html('<p class="fonte_titulos"><b>Curso Intensivo de Python</b></p>')
        st.html('<p class="fonte_descricao">Se você está no começo da sua carreira de programador, ou só quer dar uma revisada, '
                 'essas aulas são feitas para você! Aqui você terá acesso as aulas de Python desde o '
                 'básico até o avançado.</p>')
        acessar = st.button(
            label='Acessar',
            use_container_width=True,
            key='curso_intensivo_python'
        )
        if acessar:
            st.switch_page('./pages/curso_intensivo_python/menu_curso_intensivo_python.py')

# --- IA com Scikit-learn, Keras e Tensorflow --- #
with st.container(border=True):
    colunas = st.columns(2)
    with colunas[0]:
        st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/capa/capa.png')
    with colunas[1]:
        st.html('<p class="fonte_titulos"><b>IA com Scikit-learn, Keras e Tensorflow</b></p>')
        st.html('<p class="fonte_descricao">Se você está quer aprender como montar os seus modelos de IA '
                'e também compreender como os algoritmos funcionam, essas aulas ajudam você nesta '
                'tarefa. Aqui você aprenderá desde o básico de IA até o avançado, sem enrolação '
                'e de modo fácil e didático.</p>')
        acessar = st.button(
            label='Acessar',
            use_container_width=True,
            key='ia_scikit_learn_keras_tensorflow'
        )
        if acessar:
            st.switch_page('./pages/ia_scikit_learn_keras_tensorflow/menu_ia_scikit_learn_keras_tensorflow.py')

# --- Redes Neurais do Zero --- #
with st.container(border=True):
    colunas = st.columns(2)
    with colunas[0]:
        st.image('./assets/imagens/redes_neurais_zero/capa/capa.png')
    with colunas[1]:
        st.html('<p class="fonte_titulos"><b>Redes Neurais do Zero</b></p>')
        st.html('<p class="fonte_descricao">Se você quer aprender como as redes neurais funcionam e '
                'criar uma com suas próprias mãos, então esse curso é para você! Aqui você aprenderá '
                'como criar uma rede neural do zero, sem complicação. Com esse material você conseguirá '
                'dominar as redes neurais e o mundo da IA.</p>')
        acessar = st.button(
            label='Acessar',
            use_container_width=True,
            key='redes_neurais_zero'
        )
        if acessar:
            st.switch_page('./pages/redes_neurais_zero/menu_redes_neurais_zero.py')


# --- Inteligência artificial e ciências de dados para finanças --- #
# with st.container(border=True):
#     colunas = st.columns(2)
#     with colunas[0]:
#         st.image('./assets/imagens/inteligencia_artificial_financas/capa/capa.png')
#     with colunas[1]:
#         st.html('<p class="fonte_titulos"><b>Inteligência Artificial e Ciência de Dados para Finanças</b></p>')
#         st.html('<p class="fonte_descricao">Se você quer aprender a como utilizar IA e ciência de dados '
#                 'para o mundo financeiro, essas aulas são par você. Aqui você aprenderá a como utilizar '
#                 'os dados e o poder das IAs para melhorar os seus investimentos e compreender melhor como '
#                 'esse mundo funciona.</p>')
#         acessar = st.button(
#             label='Acessar',
#             use_container_width=True,
#             key='inteligencia_artificial_financas'
#         )
#
# # --- Criptografia com Python --- #
# with st.container(border=True):
#     colunas = st.columns(2)
#     with colunas[0]:
#         st.image('./assets/imagens/criptografia_python/capa/capa.png')
#     with colunas[1]:
#         st.html('<p class="fonte_titulos"><b>Criptografia com Python</b></p>')
#         st.html('<p class="fonte_descricao">Se você gosta de criptografia ou pretende deixar seus '
#                 'arquivos mais seguros, essas aulas são perfeitas para você! Aqui você aprenderá a '
#                 'criar algoritmos de criptografia sofisticados, bem como decriptografar mensagens.</p>')
#         acessar = st.button(
#             label='Acessar',
#             use_container_width=True,
#             key='criptografia_python'
#         )
#
# # --- PySide2 --- #
# with st.container(border=True):
#     colunas = st.columns(2)
#     with colunas[0]:
#         st.image('./assets/imagens/pyside2/capa/capa.png')
#     with colunas[1]:
#         st.html('<p class="fonte_titulos"><b>GUIs com Python e PySide2</b></p>')
#         st.html('<p class="fonte_descricao">Se você desenvolveu um aplicativo mas não sabe como '
#                 'dar "cara" a ele, você está no lugar certo! Nessas aulas veremos como criar uma '
#                 'interface gráfica para o seu programa, ajudando a distribuí-lo e tornar mais acessível '
#                 'o seu projeto.</p>')
#         acessar = st.button(
#             label='Acessar',
#             use_container_width=True,
#             key='pyside2'
#         )
