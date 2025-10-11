# --- Importar as bibliotecas --- #
from PIL import Image
import streamlit as st

# --- Configurações iniciais da página --- #
st.set_page_config(
    page_title='Capítulo 01 - Baixar o Python',
    page_icon=Image.open('./assets/logo/logo.png'),
    layout='wide'
)

# --- Carregar o estilo das fontes --- #
with open('./assets/css/style.css', 'r') as css:
    st.html(f'<style>{css.read()}</style>')

# --- Colocar o banner do capítulo --- #
st.image('./assets/imagens/curso_intensivo_python/aula_01/aula_01.png')

# --- Corpo da página --- #
st.html('<p class="fonte_texto">Nesse capítulo você aprenderá a como baixar o Python e como é a sua IDLE.</p>')
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Site do Python</h1>')
st.html('<p class="fonte_texto">Para baixar o Python, basta acessar esse '
        '<a href="https://www.python.org/">site</a>. Após isso, vá na aba <b>Downloads</b> e '
        'escolha o seu sistema operacional:</p>')
st.image('./assets/imagens/curso_intensivo_python/aula_01/figura_01.png')
st.html('<p class="fonte_texto">No momento da montagem dessa aula, a versão mais atual do Python é a 3.13.1. Ao longo da sua '
        'vida de desenvolvedor, você utilizará bibliotecas (código que outras pessoas fizeram e você '
        'pode usar) que podem não estarem compatíveis com a versão mais atualizada do Python. Recomento '
        'que baixe a versão 3.9.13. Para achá-la na página de download, basta apertar os botões '
        '<b>CTRL+F</b> e digitar a versão:</p>')
st.image('./assets/imagens/curso_intensivo_python/aula_01/figura_02.png')
st.html('<p class="fonte_texto">Basta clicar no hiperlink e você será redirecionado à página de download '
        'dessa versão. No final da página estão os arquivos para baixar:</p>')
st.image('./assets/imagens/curso_intensivo_python/aula_01/figura_03.png')
st.html('<p class="fonte_texto">O site do Python informa na coluna <b><i>Description</b></i> qual é o arquivo recomendado'
        ' para você baixar. Baixado o arquivo, agora é só instalar:</p>')
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Instalar o Python</h1>')
st.image('./assets/imagens/curso_intensivo_python/aula_01/figura_04.png')
st.html('<p class="fonte_texto">Lembre-se de marcar a caixa com o texto <b>Add Python 3.9 to PATH</b>. '
        'Essa opção é crucial para baixar as bibliotecas para os seus projetos. Sem essa opção marcada '
        'você terá de fazer o download dessas bibliotecas manualmente. Clique na primeira opção '
        '(<b>Install Now</b>) e espere terminar a instalação.</p>')
st.html('<p class="fonte_texto">Com o Python instalado em seu computador, basta você ir na barra de '
        'pesquisa do seu computador e digitar <b>Python</b>:</p>')
st.image('./assets/imagens/curso_intensivo_python/aula_01/figura_05.png')
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Conhecendo a IDLE</h1>')
st.html('<p class="fonte_texto">Para acessar a janela de escrita de código (ILDE), clique no programa '
        'que contenha a palavra <b>IDLE</b>. Ao clicar você verá uma janela semelhante a essa:</p>')
st.image('./assets/imagens/curso_intensivo_python/aula_01/figura_06.png')
st.html('<p class="fonte_texto">Essa tela é uma IDLE (<i><b>I</b>ntegrated <b>D</b>evelopment and '
        '<b>L</b>earning <b>E</b>nvironment</i>, ou Ambiente Integrado de Desenvolvimento e Aprendizagem). '
        'Aqui é que conseguimos fazer os códigos, nada muito complexo. Vejamos um exemplo:</p>')
st.image('./assets/imagens/curso_intensivo_python/aula_01/figura_07.png')
st.html('<p class="fonte_texto">Basta digitar o comando desejado e apertar a tecla <b>ENTER</b> '
        'que a "magia" acontece!</p>')
st.html('<p class="fonte_texto">Trabalhar nessa IDLE não é vantajoso, pois você não pode modificar o '
        'código que já foi executado e conforme os códigos crescem, fica mais complicado gerenciar tudo '
        'nessa tela. Para contornar essa situação, vamos escrever o mesmo código só que no editor de código '
        'do Python. Para isso, pressione as teclas <b>CTRL+N</b> na IDLE. Você deverá ter uma tela '
        'como essa:</p>')
st.image('./assets/imagens/curso_intensivo_python/aula_01/figura_08.png')
st.html('<p class="fonte_texto">Trabalhar nessa IDLE não é vantajoso, pois você não pode modificar o '
        'código que já foi executado e conforme os códigos crescem, fica mais complicado gerenciar tudo '
        'nessa tela. Para contornar essa situação, vamos escrever o mesmo código só que no editor de código '
        'do Python. Para isso, pressione as teclas <b>CTRL+N</b> na IDLE. Você deverá ter uma tela '
        'como essa:</p>')
st.html('<p class="fonte_texto">Agora sim! Aqui é o lugar de escrever o código, editá-lo e executá-lo. '
        'Vamos escrever o mesmo código que escrevemos na IDLE. Com o código escrito, basta salvar o '
        'arquivo com um nome que referencie o que p código faz (nesse caso vamos salvá-lo como '
        '<i>ola_mundo.py</i>). Com o arquivo devidamente salvo, basta apertar a tecla <b>F5</b> '
        'que o Python executará o código:</p>')
st.image('./assets/imagens/curso_intensivo_python/aula_01/figura_09.png')
st.html('<p class="fonte_texto">Como você pode perceber, o resultado do código é retornado na IDLE. '
        'Aqui nós podemos ver de onde vem essa execução, do arquivo <i>ola_mundo.py</i>. Se você quiser '
        'mudar a saída ou adicionar qualquer outra coisa no código, é só alterar o arquivo.</p>')
st.html('<p class="fonte_texto">Nas nossas aulas, usaremos o editor de código padrão do Python, mas '
        'sinta-se à vontade para escolher o seu editor de código preferido.</p>')
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Resumo</h1>')
st.html('<p class="fonte_texto">Nessa aula você aprendeu a como baixar qualquer versão do Python através '
        'do site oficial. Aprendeu também como instalar de modo correto o Python. Por fim, aprendeu como '
        'criar códigos no editor de texto padrão do Python, além de executar o código presente nele.</p>')