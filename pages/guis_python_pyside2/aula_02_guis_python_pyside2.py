# --- Importar as bibliotecas --- #
from PIL import Image
import streamlit as st

# --- Configurações iniciais da página --- #
st.set_page_config(
    page_title='Capítulo 01 - Introdução à GUIs',
    page_icon=Image.open('./assets/logo/logo.png'),
    layout='wide'
)

# --- Carregar o estilo das fontes --- #
with open('./assets/css/style.css', 'r') as css:
    st.html(f'<style>{css.read()}</style>')

# --- Colocar o banner do capítulo --- #
st.image('./assets/imagens/guis_python_pyside2/aula_02/aula_02.png')

# --- Instalar a biblioteca PySide2 --- #
st.html('<h1 class="fonte_titulo_aula">Instalar a biblioteca PySide2</h1>')
st.html('<p class="fonte_texto">Antes de começarmos a escrever o código para o nosso App, devemos instalar '
        'a biblioteca PySide2 em nosso computador. Para isso, utilize o seguinte comando:</p>')
st.code('pip install PySide2', line_numbers=True)
st.html('<p class="fonte_texto">Com a biblioteca devidamente instalada, podemos começar a nossa aula.</p>')

# --- Dica inicial --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Dica inicial</h1>')
st.html('<p class="fonte_texto">Vamos criar nosso primeiro aplicativo! Para começar, crie um novo arquivo '
        'Python, você pode chamá-lo como quiser (por exemplo, <b>meu_app.py</b>) e salvá-lo em algum lugar '
        'acessível. Escreveremos nosso aplicativo simples neste arquivo.</p>')

# --- Criando o seu App --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Criando o seu App</h1>')
st.html('<p class="fonte_texto">O código-fonte do seu primeiro aplicativo é mostrado abaixo. Digite-o '
        'literalmente e tome cuidado para não cometer erros. Se você errar, o Python informará o que há '
        'de errado:</p>')
st.code('''# --- Importar as bibliotecas --- #
import sys  # necessário apenas para acesso aos argumementos da linha de comando
from PySide2.QtWidgets import QApplication, QWidget

# --- Você precisa de uma (e apenas uma) instância de QApplication por aplicativo --- #
# --- Passe sys.argv para permitir argumentos de linha de comando para seu aplicativo --- #
# --- Se você sabe que não usará argumentos de linha de comando, QApplication([]) também funciona --- #
app = QApplication(sys.argv)

# --- Crie um widget Qt, que será a nossa janela --- #
janela = QWidget()
janela.show()  # IMPORTANTE!!!!! As janelas ficam ocultas por padrão

# --- Iniciar o loop de eventos --- #
app.exec_()''', line_numbers=True)
st.html('<p class="fonte_texto">Agora você verá sua janela. O Qt cria automaticamente uma janela com as '
        'decorações normais da janela e você pode arrastá-la e redimensioná-la como qualquer janela:</p>')
colunas = st.columns((1, 1, 2, 1, 1))
with colunas[2]:
    st.image('./assets/imagens/guis_python_pyside2/aula_02/figura_01.png',
             caption='Figura 1: Janela do App.')
st.html('<p class="fonte_texto">O que você verá dependerá da plataforma em que você está executando '
        'este exemplo.</p>')

# --- Percorrendo o código --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Percorrendo o código</h1>')
st.html('<p class="fonte_texto">Vamos percorrer o código linha por linha para entendermos exatamente o que '
        'está acontecendo. Primeiro, importamos as classes PySide2 necessárias para o aplicativo. Aqui '
        'estamos importando <b>QApplication</b>, o manipulador de aplicativos e <b>QWidget</b>, um widget '
        'GUI vazio básico, ambos do módulo <b>QtWidgets</b>:</p>')
st.code('from PySide2.QtWidgets import QApplication, QWidget', line_numbers=True)
st.html('<p class="fonte_texto">Os principais módulos do Qt são <b>QtWidgets</b>, <b>QtGui<b> e '
        '<b>QtCore</b>. A seguir criamos uma instância de QApplication, passando sys.arg, que é uma lista '
        'Python contendo os argumentos da linha de comando passados para a aplicação:</p>')
st.code('app = QApplication(sys.argv)', line_numbers=True)
st.html('<p class="fonte_texto">Se você sabe que não usará argumentos de linha de comando para controlar '
        'o Qt, poderá passar uma lista vazia, por exemplo:</p>')
st.code('app = QApplication([])', line_numbers=True)
st.html('<p class="fonte_texto">A seguir, criamos uma instância de um <b>QWidget</b> usando <b>janela</b> '
        'como nome da variável:</p>')
st.code('''janela = QWidget()
janela.show()''', line_numbers=True)
st.html('<p class="fonte_texto">No Qt, <b>todos</b> os widgets de nível superior são janelas, ou seja, '
        'eles não têm um pai e não estão aninhados em outro widget ou layout. Isso significa que você pode '
        'criar tecnicamente uma janela usando qualquer widget que desejar. Mas o que é uma janela?</p>')
st.html('<ul class="fonte_texto">'
            '<li>Mantém a interface do usuário do seu aplicativo;</li>'
            '<li>Cada aplicação precisa de pelo menos uma (…mas pode ter mais) e;</li>'
            '<li>O aplicativo (por padrão) será encerrado quando a última janela for fechada.</li>'
        '</ul>')
st.html('<p class="fonte_texto">Finalmente, chamamos <b>app.exec_()</b> para iniciar o loop de eventos.</p>')

# --- O que é o loop de eventos? --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">O que é o loop de eventos?</h1>')
st.html('<p class="fonte_texto">Antes de exibir a janela na tela, existem alguns conceitos-chave a serem '
        'apresentados sobre como os aplicativos são organizados no mundo Qt. Se você já estiver '
        'familiarizado com loops de eventos, poderá pular com segurança para a próxima seção.</p>')
st.html('<p class="fonte_texto">O núcleo de todos os aplicativos Qt é a classe <b>QApplication</b>. Cada '
        'aplicativo precisa de um, e apenas um, objeto <b>QApplication</b> para funcionar. Este objeto '
        'contém o <i>loop</i> de eventos do seu aplicativo, o loop principal que governa toda a interação '
        'do usuário com a GUI.</p>')
st.html('<p class="fonte_texto">Cada interação com seu aplicativo (seja o pressionamento de uma tecla, o '
        'clique do mouse ou o movimento do mouse) gera um <i>evento</i> que é colocado na <i>fila de '
        'eventos</i>. No loop de eventos, a fila é verificada em cada iteração e se um evento em espera '
        'for encontrado, o evento e o controle são passados para o <i>manipulador de eventos</i> '
        'específico para o evento. O manipulador de eventos lida com o evento e depois passa o controle '
        'de volta ao loop de eventos para aguardar mais eventos. Há <b>apenas um loop</b> de eventos em '
        'execução por aplicativo. A classe <b>QApplication</b></p>')
st.html('<ul class="fonte_texto">'
            '<li><b>QApplication</b> contém o loop de eventos Qt;</li>'
            '<li>É necessária uma instância de <b>QApplication</b>;</li>'
            '<li>Seu aplicativo fica esperando no loop de eventos até que uma ação seja executada e;</li>'
            '<li>Existe <b>apenas um</b> loop de eventos a qualquer momento.</li>'
        '</ul>')
st.html('<p class="fonte_texto">O sublinhado existe porque <b>exec</b> era uma palavra reservada no '
        'Python 2.7. PySide2 lida com isso anexando um sublinhado ao nome usado na biblioteca C++. Você '
        'também verá métodos <b>.print_()</b> em widgets, por exemplo.</p>')

# --- QMainWindow --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">QMainWindow</h1>')
st.html('<p class="fonte_texto">Como descobrimos na última parte, no Qt qualquer widget pode ser janela. '
        'Por exemplo, se você substituir <b>QtWidget</b> por <b>QPushButton</b>. No exemplo abaixo, você '
        'obteria uma janela com um único botão:</p>')
st.code('''from PySide2.QtWidgets import QPushButton
janela = QPushButton('Me aperte!')
janela.show()''', line_numbers=True)
st.html('<p class="fonte_texto">Isso é legal, mas não é <i>muito útil</i>, é raro que você precise de uma '
        'interface do usuário (UI, em inglês, <i>User Interface</i>) que consista em apenas um único '
        'controle! Mas, como descobriremos mais tarde, a capacidade de aninhar widgets dentro de outros '
        'widgets usando layouts significa que você pode construir UIs complexas dentro de um '
        '<i>QWidget</i> vazio.</p>')
st.html('<p class="fonte_texto">Mas, o Qt já tem uma solução para você: o <b>QMainWindow</b>. Este é um '
        'widget pré-fabricado que fornece muitos recursos de janela padrão que você usará em seus '
        'aplicativos, incluindo barras de ferramentas, menus, uma barra de status, widgets encaixáveis e '
        'muito mais. Veremos esses recursos avançados mais tarde, mas, por enquanto, adicionaremos um '
        '<b>QMainWindow</b> simples e vazio ao nosso aplicativo:</p>')
st.code('''# --- Importar as bibliotecas --- #
import sys
from PySide2.QtWidgets import QApplication, QMainWindow

# --- Criar a instância do App -- #
app = QApplication(sys.argv)

# --- Criar a janela do App --- #
janela = QMainWindow()
janela.show()

# --- Iniciar o loop de eventos --- #
app.exec_()''', line_numbers=True)
st.html('<p class="fonte_texto">Agora você verá sua janela principal. Parece exatamente igual a antes! '
        'Portanto, nosso <b>QMainWindow</b> não é muito interessante no momento. Podemos consertar isso '
        'adicionando algum conteúdo. Se você deseja criar uma janela personalizada, a melhor abordagem é '
        'subclassificar <b>QMainWindow</b> e então incluir a configuração da janela no bloco '
        '<b>__init__</b>. Isso permite que o comportamento da janela seja independente. Podemos adicionar '
        'nossa própria subclasse de <b>QMainWindow</b>, chame-a de <b>TelaPrincipal</b> para manter as '
        'coisas simples:</p>')
st.code('''# --- Criar uma classe que herda QMainWindow para personalizar a janela principal do seu aplicativo --- #
class TelaPrincipal(QMainWindow):
    """Classe que cria a tela principal do App."""
    def __init__(self):
        """Função responsável por inicializara classe."""
        # --- Herdar a classe QMainWindow --- #
        super().__init__()  # 1
   
        # --- Colocar o nome da janela --- #
        self.setWindowTitle('Meu App')

        # --- Criar um botão --- #
        botao = QPushButton('Me aperte!')

        # --- Deixar o widget centralizado --- #
        self.setCentralWidget(botao)  # 2

# --- Criar a instância do App --- #
app = QApplication(sys.argv)

# --- Criar a janela do App --- #
janela = TelaPrincipal()
janela.show()

# --- Executar o loop de eventos --- #
app.exec_()''', line_numbers=True)
st.html('<ol class="fonte_texto" type="1">'
            '<li>Devemos sempre chamar o método <b>__init__</b> da classe <b>super()</b> e;</li>'
            '<li>Use <b>.setCentralWidget</b> para colocar um widget no <b>QMainWindow</b>.</li>'
        '</ol>')
st.html('<p class="fonte_texto">Em nosso bloco <b>__init__</b> usamos primeiro <b>.setWindowTitle()</b>'
        ' para alterar o título de nossa janela principal. Em seguida, adicionamos nosso primeiro widget, '
        'um <b>QPushButton</b>, no meio da janela. Este é um dos widgets básicos disponíveis no Qt. Ao '
        'criar o botão você pode passar o texto que deseja que o botão exiba.</p>')
st.html('<p class="fonte_texto">Finalmente, chamamos <b>.setCentralWidget()</b> na janela. Esta é uma '
        'função específica do <b>QMainWindow</b> que permite que você defina o widget que vai no meio da '
        'janela.</p>')
st.html('<p class="fonte_texto">Agora você verá sua janela novamente, mas desta vez com o widget '
        '<b>QPushButton</b> no meio. Pressionar o botão não fará nada, resolveremos isso a seguir:</p>')
colunas = st.columns(5)
with colunas[2]:
    st.image('./assets/imagens/guis_python_pyside2/aula_02/figura_02.png',
             caption='Figura 2: Botão do App.')
st.html('<p class="fonte_texto">Com fome de widgets? Abordaremos mais widgets em detalhes em breve, mas se '
        'você estiver impaciente e quiser avançar, pode dar uma olhada na '
        '<a href="https://doc.qt.io/archives/qt-5.15/widget-classes.html">documentação do QWidget</a>. '
        'Experimente adicionar diferentes widgets à sua janela!</p>')
# --- Dimensionando janelas e widgets --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Dimensionando janelas e widgets</h1>')
st.html('<p class="fonte_texto">A janela atualmente pode ser redimensionada livremente, se você pegar '
        'qualquer canto com o mouse, poderá arrastá-la e redimensioná-la para o tamanho que desejar. '
        'Embora seja bom permitir que os usuários redimensionem seus aplicativos, às vezes você pode '
        'querer impor restrições aos tamanhos mínimos ou máximos ou bloquear uma janela em um tamanho '
        'fixo.</p>')
st.html('<p class="fonte_texto">No Qt, os tamanhos são definidos usando um objeto <b>QSize</b>. Aceita '
        'parâmetros de largura e altura nessa ordem. Por exemplo, o seguinte criará uma janela de tamanho '
        'fixo de 400x300 pixels. Importe o módulo <b>QSize</b> no começo do código e adiciona o seguinte '
        'código ao final da função <b>__init__</b>:</p>')
st.code('''from PySide2.QtCore import QSize


class TelaPrincipal(QMainWindow):
  def __init__(self):
    .
    .
    .
    self.setFixedSize(QSize(400, 300))

app = QApplication(sys.argv)
.
.
.''', line_numbers=True)
st.html('<p class="fonte_texto">Você verá uma janela de tamanho fixo, tente redimensioná-la, não '
        'funcionará. Assim como <b>.setFixedSize()</b> você também pode chamar <b>.setMinimumSize()</b>'
        ' e <b>.setMaximumSize()</b> para definir os tamanhos mínimo e máximo respectivamente. '
        'Experimente você mesmo! Você pode usar esses métodos de tamanho em <i>qualquer</i> widget.</p>')