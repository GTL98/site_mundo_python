# --- Importar as bibliotecas --- #
from PIL import Image
import streamlit as st
from carregar_css import carregar_css

# --- Configurações iniciais da página --- #
st.set_page_config(
    page_title='PySide6 Maestria - Aula 02',
    page_icon=Image.open('./assets/logo/logo.png'),
    layout='wide'
)

# --- Carregar o CSS --- #
carregar_css()

# --- Colocar o título da aula --- #
st.html('<h1 class="fonte_titulo_aula">Aula 2: Menus, Toolbars e Status Bar – Aplicações Profissionais!</h1>')

# --- Vídeo --- #
with st.expander('Se quiser acompanhar com o vídeo, acesse aqui! 👇'):
    st.video('https://youtu.be/WeeeHe_VLw8')

# --- Código da aula --- #
st.subheader('Se quiser acessar o código completo da aula, clique [aqui](https://github.com/GTL98/canal_mundo_python/blob/main/Maestria%20em%20PySide6%3A%20O%20Guia%20Definitivo/Aula%2002/aula_02.py)')
st.divider()

# --- Introdução --- #
st.subheader('E fala, devs! Tudo bem com vocês? Espero que sim!')
st.html('<h1 class="fonte_titulo_aula">Introdução</h1>')
st.html('''<p class="fonte_texto">Bem-vindos à segunda etapa da nossa jornada com o PySide6! Se na primeira 
aula nós demos os nossos primeiros passos criando uma janela bem simples usando apenas um QLabel, agora é 
hora de elevar o nível e começar a construir as coisas como os profissionais. Nesta etapa, vamos abandonar 
as janelas improvisadas e abraçar a estrutura definitiva usada nos maiores softwares de desktop do 
mercado.</p>''')
st.html('''<p class="fonte_texto">Para criar aplicativos completos, com aqueles menus de navegação no topo, 
barras de ferramentas cheias de ícones e barras de status no rodapé, nós precisamos de um alicerce 
construído especificamente para isso. É aqui que entra a estrela de hoje: a QMainWindow. Diferente de um 
widget comum que apenas exibe um conteúdo solto, a QMainWindow é uma classe superpoderosa que já vem com 
um layout pré-montado, reservando áreas específicas da tela para cada ferramenta que vamos 
adicionar.</p>''')
st.html('''<p class="fonte_texto">Além disso, para dominar essa nova estrutura, nós vamos dar um passo 
importantíssimo e muito elegante no Python: o uso da Programação Orientada a Objetos (POO). Nós vamos 
criar a nossa própria classe de janela e fazer com que ela "herde" todas as funcionalidades nativas do 
PySide6. Dessa forma, pegamos uma interface profissional em branco e a personalizamos exatamente do nosso 
jeito, mantendo o código incrivelmente limpo e organizado!</p>''')
st.subheader('Então sem mais delongas, bora para a aula!')
st.divider()

# --- Criar a classe principal --- #
st.html('<h1 class="fonte_titulo_aula">Criar a classe principal</h1>')
st.html('''<p class="fonte_texto">Quando migramos de scripts simples para aplicações profissionais, 
precisamos de um alicerce robusto. É exatamente aqui que entra a teoria por trás da 
<span class="texto_python">QMainWindow</span>. Diferente de um widget comum (que é essencialmente apenas 
uma "caixa" em branco na tela), a <span class="texto_python">QMainWindow</span> é uma estrutura 
arquitetural completa e complexa. Ela já possui áreas invisíveis pré-definidas e otimizadas pelo próprio 
framework exclusivamente para receber menus no topo, barras de ferramentas flutuantes (ToolBars) e barras 
de status no rodapé. Adotar essa classe como o "chassi" principal do nosso projeto é o que garante aquele 
layout padronizado e responsivo que os usuários já esperam encontrar em qualquer software de ponta.</p>''')
st.html('''<p class="fonte_texto">Para manipular essa estrutura com maestria, nós aplicamos um dos conceitos 
mais poderosos do Python: a Programação Orientada a Objetos (POO), focando especialmente na Herança. Ao 
criarmos a nossa própria classe e passarmos a <span class="texto_python">QMainWindow</span> entre 
parênteses como molde, estamos determinando que a nossa nova janela herde, instantaneamente, todas as 
características físicas e comportamentais da janela padrão do PySide6. A peça central de toda essa mecânica 
é o comando <span class="funcoes_python">super</span><span class="texto_python">().__init__()</span>. Ele 
atua como um gatilho essencial que invoca o construtor genético da classe "mãe", garantindo que toda a 
engenharia pesada do Qt seja inicializada e montada nos bastidores antes mesmo de começarmos a personalizar 
nossa tela (como títulos e tamanhos) utilizando o referencial <span class="self_python">self</span>.</p>''')
st.html('''<p class="fonte_texto">Além disso, a forma como devolvemos o controle para o sistema operacional 
ao final do script muda levemente, mas com um impacto teórico enorme. O nosso já conhecido loop de eventos, 
gerado pelo <span class="texto_python">app.exec()</span>, passa a operar encapsulado pelo 
<span class="texto_python">sys.exit()</span>. Essa combinação cria uma ponte de comunicação cirúrgica entre 
o seu aplicativo e o sistema (Windows, macOS ou Linux). Quando o usuário fecha o programa, quebrando o 
loop, um código de status é gerado. O <span class="texto_python">sys.exit()</span> intercepta esse código 
e avisa ao computador que a execução foi encerrada de maneira limpa e controlada, forçando a liberação 
imediata da memória e extinguindo qualquer risco do seu programa se transformar em um "processo fantasma" 
travado no gerenciador de tarefas:</p>''')
st.code('''# --- Importar os módulos --- #
import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel,
                               QMenuBar, QToolBar, QStatusBar)


class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        # --- Configurações fundamentais da janela principal --- #
        self.setWindowTitle('Sistema Profissional PySide6')
        self.resize(1024, 768)


if __name__ == '__main__':
    # --- Inicialização da infraestrutura do Qt --- #
    app = QApplication()

    # --- Instanciação da interface principal --- #
    janela = JanelaPrincipal()
    janela.show()

    # --- Início do loop de eventos --- #
    sys.exit(app.exec())''', line_numbers=True)
st.html('''<p class="fonte_texto">Vamos destrinchar esse código inicial detalhadamente. Logo de cara, 
você notará que a nossa lista de importações cresceu bastante. No ecossistema do PySide6, as coisas 
são muito bem organizadas em módulos distintos, e já deixamos tudo importado para usarmos no decorrer da 
aula:</p>''')
st.html('''<ul class="fonte_texto">
    <li><span class="texto_python">QtCore</span>: Traz o coração lógico do framework (como o 
    <span class="texto_python">Qt</span> para as flags de alinhamento e 
    <span class="texto_python">QSize</span> para manipulação de tamanhos).</li>
    <li><span class="texto_python">QtGui</span>: Lida com elementos visuais que não são necessariamente 
    janelas ou botões, como as nossas ações (<span class="texto_python">QAction</span>), ícones (
    <span class="texto_python">QIcon</span>) e os mapeamentos de atalhos de teclado (
    <span class="texto_python">QKeySequence</span>).</li>
    <li><span class="texto_python">QtWidgets</span>: Onde moram os componentes físicos da interface, como 
    a nossa nova <span class="texto_python">QMainWindow</span>, barras de menu, barras de ferramentas e a 
    barra de status.</li>
</ul>''')
st.html('''<p class="fonte_texto">A grande revolução do nosso código está na linha 
<span class="palavras_reservadas">class </span><span class="classe_python">JanelaPrincipal</span>
<span class="texto_python">(QMainWindow)</span>. Aqui estamos dizendo ao interpretador: "Crie uma nova 
janela chamada <span class="texto_python">JanelaPrincipal</span>, mas use a 
<span class="texto_python">QMainWindow</span> como molde original!". Ao fazermos isso, iniciamos o 
conceito de herança que discutimos agorinha. E para garantir que a nossa nova janela puxe todas as 
configurações desse molde, nós chamamos o construtor da classe mãe através do comando mágico 
<span class="funcoes_python">super</span><span class="texto_python">().__init__()</span>. Graças a ele, 
não precisamos reescrever as centenas de regras de como uma janela funciona por baixo dos panos; nós 
simplesmente herdamos o trabalho pesado e focamos apenas no nosso design.</p>''')
st.html('''<p class="fonte_texto">Como já estamos dentro da nossa própria classe, não usamos mais 
variáveis soltas para alterar o título e o tamanho. Utilizamos o <span class="self_python">self</span>, 
que é a forma do Python dizer "aplique isso a mim mesmo" ou "esteja vinculado à própria janela". Com 
<span class="self_python">self</span><span class="texto_python">.setWindowTitle()</span> e 
<span class="self_python">self</span><span class="texto_python">.resize()</span>, deixamos nossa janela 
com o título profissional e com uma resolução muito mais ampla (1024x768), pronta para receber os novos 
widgets.</p>''')
st.html('''<p class="fonte_texto">Por fim, repare no bloco final do nosso script, onde o aplicativo ganha 
vida. A lógica é quase idêntica à da primeira aula: instanciamos a 
<span class="texto_python">QApplication</span>, criamos a nossa 
<span class="texto_python">JanelaPrincipal</span> e pedimos para ela aparecer com o 
<span class="texto_python">.show()</span>. No entanto, como vimos na teoria, implementamos o encerramento 
seguro na última linha: <span class="texto_python">sys.exit(app.exec())</span>. O aplicativo entra em loop 
normalmente, mas quando o <b>X</b> é pressionado, ele manda o recado correto de finalização para o seu 
computador, provando que o seu código agora roda em padrão profissional.</p>''')
st.divider()

# --- Adicionar o widget central --- #
st.html('<h1 class="fonte_titulo_aula">Adicionar o widget central</h1>')
st.html('''<p class="fonte_texto">Agora que já temos o nosso "chassi" profissional montado com a 
<span class="texto_python">QMainWindow</span>, precisamos dar a ele um coração. Na teoria de design de 
interfaces do Qt, a <span class="texto_python">QMainWindow</span> é uma estrutura incrivelmente organizada, 
mas ela possui uma regra de ouro inquebrável: ela exige a definição de um Widget Central. Pense na 
janela principal como um grande teatro; os menus e as barras de ferramentas são as bilheterias e as 
coxias, mas o Widget Central é o palco principal. É ali que a verdadeira magia do seu aplicativo acontece, 
seja uma área de edição de texto (como no Word), uma tela de desenho (como no Photoshop) ou uma tabela 
de dados. Se você ignorar essa regra e não definir um widget central, o framework pode apresentar 
comportamentos imprevisíveis na hora de redimensionar a tela.</p>''')
st.html('''<p class="fonte_texto">Para tornar esse "palco" visualmente agradável, o PySide6 nos oferece 
um recurso espetacular chamado <b>QSS (Qt Style Sheets)</b>. Se você já tem alguma familiaridade com 
desenvolvimento web, se sentirá em casa, pois o QSS é praticamente o irmão gêmeo do CSS (Cascading 
Style Sheets). Ele permite que você separe completamente a lógica do seu programa da parte estética. Em 
vez de criar dezenas de linhas de código complexas só para mudar a cor de uma letra, você passa uma 
simples string (um texto) contendo comandos diretos de estilo. Isso possibilita alterar o tamanho da 
fonte, o peso (negrito), aplicar cores em formato hexadecimal e arredondar bordas, transformando aquela 
interface padrão "cinza e sem graça" do sistema operacional em um design moderno e atrativo.</p>''')
st.html('''<p class="fonte_texto">Além do estilo puro e simples, o posicionamento dos elementos é crucial 
para uma boa experiência do usuário. O Qt resolve a organização espacial utilizando <i>Flags</i> 
(sinalizadores) de alinhamento. Em vez de tentarmos adivinhar as coordenadas exatas da tela (X e Y) para 
colocar um texto bem no meio, o núcleo do framework (<span class="texto_python">QtCore</span>) nos 
fornece constantes prontas, como as famosas <span class="texto_python">AlignmentFlags</span>. Quando 
combinamos essas constantes com o nosso widget central, garantimos que o conteúdo se adapte e permaneça 
perfeitamente centralizado e responsivo, não importa o quanto o usuário estique ou encolha a janela do 
aplicativo:</p>''')
st.code("""...(continuação do código)
class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        # --- Configurações fundamentais da janela principal --- #
        self.setWindowTitle('Sistema Profissional PySide6')
        self.resize(1024, 768)

        # --- Criação e configuração do widget central --- #
        self.widget_central = QLabel('Área de trabalho principal')
        self.widget_central.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget_central.setStyleSheet('''font-size: 24pt;
font-weight: bold;
color: #6fa3d6''')

        # --- Definição obrigatório do widget central no QMainWindow --- #
        self.setCentralWidget(self.widget_central)
(continuação do código)...""", line_numbers=True)
st.html('''<p class="fonte_texto">Vamos mergulhar nas novidades do nosso código e entender cada 
engrenagem dessa atualização. Dentro do método  <span class="funcoes_python">__init__</span> da nossa 
<span class="texto_python">JanelaPrincipal</span>, logo após definirmos o título e o tamanho, iniciamos a 
construção do nosso palco principal com a linha 
<span class="self_python">self</span><span class="texto_python">.widget_central = QLabel(</span>
<span class="variaveis">'Área de trabalho principal'</span><span class="texto_python">)</span>. Note que, 
mais uma vez, estamos usando um <span class="texto_python">QLabel</span> para exibir texto, mas agora ele 
está amarrado ao <span class="self_python">self</span>, tornando-se uma propriedade oficial da nossa 
janela.''')
st.html('''<p class="fonte_texto">A linha seguinte, <span class="self_python">self</span>
<span class="texto_python">.widget_central.setAlignment(Qt.AlignmentFlag.AlignCenter)</span>, é onde a 
mágica do posicionamento acontece. Nós acessamos o módulo <span class="texto_python">Qt</span> (que 
importamos lá no topo do código, vindo do <span class="texto_python">QtCore</span>) e buscamos a diretriz 
<span class="texto_python">AlignCenter</span>. Esse comando diz ao PySide6: "Pegue esse texto e trave ele 
exatamente no centro do widget, tanto na vertical (eixo Y) quanto na horizontal (eixo X)". Assim, temos um 
layout perfeitamente responsivo desde o primeiro segundo.''')
st.html("""<p class="fonte_texto">Logo abaixo, entramos na estilização com o método 
<span class="texto_python">.setStyleSheet()</span>. Repare que utilizamos novamente as três aspas simples (
<span class="variaveis">'''</span>) para escrever uma string de múltiplas linhas. Passamos três comandos 
clássicos de QSS/CSS: <span class="texto_python">font-size: 24pt</span> para deixar a letra bem grande e 
legível, <span class="texto_python">font-weight: bold</span> para aplicar o negrito, e 
<span class="texto_python">color: #6fa3d6</span> que aplica um tom de azul muito elegante usando o código 
hexadecimal. Cada comando é separado por um ponto e vírgula, exatamente como faríamos na construção de um 
site na web.""")
st.html('''<p class="fonte_texto">Por fim, e sem sombra de dúvidas o passo mais crítico desta etapa, temos 
a linha <span class="self_python">self</span>
<span class="texto_python">.setCentralWidget(self.widget_central)</span>. É através do método 
<span class="texto_python">setCentralWidget()</span> (que nós herdamos gentilmente da 
<span class="texto_python">QMainWindow</span>) que nós formalizamos o nosso "casamento". Estamos 
comunicando à janela principal que aquela <span class="texto_python">QLabel</span> lindamente estilizada 
que acabamos de criar não é apenas um widget qualquer perdido na memória, mas sim a dona do palco 
principal. Sem essa declaração obrigatória, o seu texto não teria um lugar definido para existir e a 
janela ficaria em branco.''')
st.divider()

# --- Criar ações (QAction) --- #
st.html('<h1 class="fonte_titulo_aula">Criar ações (<span class="texto_python">QAction</span>)</h1>')
st.html('''<p class="fonte_texto">Um dos grandes segredos dos softwares profissionais é a inteligência na 
hora de reaproveitar comandos. Pense bem: quando você quer criar um novo arquivo em um programa como o 
Word ou o próprio PyCharm, você pode clicar no menu "Arquivo > Novo", clicar no ícone de "Novo" na barra 
de ferramentas ou simplesmente apertar o atalho "Ctrl+N" no teclado. Todas essas três interações fazem 
exatamente a mesma coisa! Em vez de escrevermos o código de criar um arquivo três vezes diferentes, o 
PySide6 nos entrega a poderosa classe <span class="texto_python">QAction</span> (Ação). Uma 
<span class="texto_python">QAction</span> é um pacote centralizado que guarda o nome do comando, o ícone, 
o atalho de teclado e o que deve acontecer quando ele for acionado. Depois de criarmos essa ação, podemos 
simplesmente "espalhá-la" pelos menus e barras de ferramentas.''')
st.html('''<p class="fonte_texto">Para deixar essa experiência ainda mais profissional e multiplataforma, 
entramos no mundo do <span class="texto_python">QKeySequence</span>. Quando desenvolvemos um software, não 
sabemos se o nosso usuário estará usando Windows, Linux ou macOS. Se você "cravar" (hardcode) um atalho 
como "Ctrl+N", isso funcionará no Windows, mas no Mac o padrão é "Command+N". Para resolver esse 
problema de forma elegante, o Qt possui os <span class="texto_python">StandardKeys</span> (Teclas Padrão). 
O framework identifica automaticamente em qual sistema operacional o seu programa está rodando e aplica o 
atalho nativo correto para aquela ação, tirando toda essa dor de cabeça das suas costas.''')
st.html('''<p class="fonte_texto">Por fim, precisamos entender como a interface se comunica com a lógica 
do Python. No PySide6, isso é feito através do padrão de "Sinais e Slots" (Signals and Slots). Toda vez 
que uma <span class="texto_python">QAction</span> é ativada (seja por clique ou teclado), ela emite um 
"sinal" sonoro invisível chamado <span class="texto_python">triggered</span> (acionado). Nós utilizamos o 
método <span class="texto_python">.connect()</span> para ligar esse sinal a um "slot", que nada mais é do 
que uma função comum do Python que fará o trabalho pesado. É assim que o clique de um mouse se transforma 
em código real executado:''')
st.code('''...(continuação do código)
class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        
        ...(continuação do código)

        # --- Definição de ações compartilhadas (QAction) --- #
        self.acao_novo = QAction(QIcon.fromTheme('document-new'), '&Novo', self)
        self.acao_novo.setShortcut(QKeySequence.StandardKey.New)
        self.acao_novo.setStatusTip('Criar um novo projeto no sistema')
        self.acao_novo.triggered.connect(self.executar_novo)

        self.acao_abrir = QAction('&Abrir...', self)
        self.acao_abrir.setShortcut(QKeySequence.StandardKey.Open)
        self.acao_abrir.setStatusTip('Abrir um arquivo existente')

        self.acao_sair = QAction('&Sair', self)
        self.acao_sair.setShortcut('Ctrl+Q')
        self.acao_sair.setStatusTip('Encerrar a aplicação')
        self.acao_sair.triggered.connect(self.close)

    def executar_novo(self):
        # --- Slot de exemplo para demonstrar a resposta ao evento --- #
        self.widget_central.setText('Iniciando um novo projeto...')
(continuação do código)...''', line_numbers=True)
st.html('''<p class="fonte_texto">Vamos dissecar a criação das nossas ações para entender cada detalhe. 
Começando pela nossa primeira ação, <span class="self_python">self</span>
<span class="texto_python">.acao_novo = QAction(...)</span>, passamos três parâmetros geniais. O primeiro é 
<span class="texto_python">QIcon.fromTheme(</span><span class="variaveis">'document-new'</span>
<span class="texto_python">)</span>, que busca um ícone padrão de "novo documento" diretamente do sistema 
operacional do usuário. O segundo é a string <span class="variaveis">'&Novo'</span>. Percebeu o "E 
comercial" (<b>&</b>) ali? Ele não aparece na tela final! Ele serve para dizer ao PySide6 que a letra "N" 
será um atalho de acesso rápido quando os menus estiverem abertos (a famosa letra sublinhada nos menus). 
O terceiro parâmetro é o <span class="self_python">self</span>, indicando que essa ação pertence à nossa 
janela principal.''')
st.html('''<p class="fonte_texto">Na linha seguinte, usamos o 
<span class="texto_python">setShortcut()</span> alimentado com a mágica do 
<span class="texto_python">QKeySequence.StandardKey.New</span>. Como vimos na teoria, isso delega ao 
framework a responsabilidade de descobrir qual é o melhor atalho ("Ctrl+N" ou "Cmd+N") dependendo do 
computador de quem está usando o programa. Já na nossa ação de "Sair", para fins didáticos, mostramos que 
você também pode forçar um atalho personalizado usando uma simples string, como fizemos em 
<span class="self_python">self</span><span class="texto_python">.acao_sair.setShortcut(</span>
<span class="variaveis">'Ctrl+Q'</span><span class="texto_python">)</span>.''')
st.html('''<p class="fonte_texto">O método <span class="texto_python">setStatusTip()</span> é um charme à 
parte. Ele define o texto de ajuda que aparecerá na Barra de Status (que criaremos mais à frente) toda vez 
que o usuário repousar o mouse sobre o botão correspondente a essa ação. É aquele detalhe de usabilidade 
que separa os programas amadores dos profissionais.''')
st.html('''<p class="fonte_texto">Agora, o momento mais importante: as conexões! Na linha 
<span class="self_python">self</span><span class="texto_python">.acao_novo.triggered.connect(</span>
<span class="self_python">self</span><span class="texto_python">.executar_novo)</span>, nós estamos 
mapeando a ação para a nossa função personalizada. Atenção total aqui: observe que passamos 
<span class="self_python">self</span><span class="texto_python">.executar_novo</span> <b>SEM</b> os 
parênteses no final! Se você colocar os parênteses, o Python executará a função logo que o aplicativo 
abrir, e não é isso que queremos. Queremos apenas "apontar" para a função, para que ela só seja executada 
no momento do clique.''')
st.html('''<p class="fonte_texto">A ação de sair tem um atalho incrível: 
<span class="self_python">self</span><span class="texto_python">.acao_sair.triggered.connect(</span>
<span class="self_python">self</span><span class="texto_python">.close)</span>. O método 
<span class="texto_python">.close</span> já existe nativamente dentro da 
<span class="texto_python">QMainWindow</span> que herdamos, então não precisamos escrever uma função só 
para fechar o aplicativo. Já estava tudo pronto!''')
st.html('''<p class="fonte_texto">Por fim, criamos o nosso "slot", o método 
<span class="palavras_reservadas">def </span><span class="funcao_python">executar_novo</span>
<span class="texto_python">(</span><span class="self_python">self</span><span class="texto_python">)</span>. 
Nele, usamos o comando <span class="texto_python">.setText()</span> no nosso 
<span class="texto_python">widget_central</span>. O que isso faz na prática? Toda vez que o usuário 
apertar o atalho "Ctrl+N", o texto grandão que estava no meio da tela ("Área de trabalho principal") 
mudará instantaneamente para "Iniciando um novo projeto...".''')
st.html('''<p class="fonte_texto"><b>Um detalhe visual:</b> Se você rodar o código agora, não verá 
nenhum botão de menu na tela ainda. Mas o programa já está escutando. Se você apertar "Ctrl+N", o texto da 
tela mudará, e se apertar "Ctrl+Q", a janela fechará. As ações já estão vivas, só precisamos 
colocá-las em uma prateleira visual, que é exatamente o nosso próximo passo!''')
st.divider()

# --- Criar o menu (QMenu ou self.menuBar) --- #
st.html('<h1 class="fonte_titulo_aula">Criar o menu ('
        '<span class="texto_python">QMenu</span> ou <span class="texto_python">self.menuBar</span>)</h1>')
st.html('''<p class="fonte_texto">Na etapa anterior, nós construímos os nossos "poderes" invisíveis: as 
<span class="texto_python">QAction</span>. Vimos que elas já estavam funcionando perfeitamente através dos 
atalhos de teclado, mas um usuário comum não adivinhará que precisa apertar "Ctrl+N" para criar um 
arquivo, certo? Nós precisamos dar uma "casa" visual para essas ações. É exatamente aqui que entra um dos 
componentes mais clássicos de qualquer software de desktop: a Barra de Menus (MenuBar). Sabe aquela barra 
superior com "Arquivo", "Editar", "Exibir" e "Ajuda"? É o que construiremos agora!''')
st.html('''<p class="fonte_texto">A grande vantagem de estarmos utilizando a 
<span class="texto_python">QMainWindow</span> como a fundação do nosso projeto é que ela já possui um 
espaço exclusivo e reservado no topo da tela só para essa barra. Nós não precisamos criar um widget do 
zero, calcular o tamanho dele e tentar colar no teto da janela. O framework nos entrega um método nativo 
super inteligente que simplesmente "invoca" essa barra superior. A partir daí, nosso trabalho é apenas 
criar as "gavetas" (os menus suspensos) e colocar as nossas ações lá dentro.''')
st.html('''<p class="fonte_texto">Para organizar tudo como um verdadeiro profissional, a lógica de 
montagem segue uma hierarquia muito clara. Primeiro, acessamos a barra de menus principal. Em seguida, 
adicionamos os títulos dos menus (como "Arquivo" e "Editar"). Por fim, abrimos o menu "Arquivo" e 
adicionamos as nossas ações uma a uma. Vamos até dar um toque de design de interface (UI/UX) colocando uma 
linha divisória para separar comandos de edição do comando de fechar o aplicativo. Vejamos como essa 
mágica ganha forma no código:''')
st.code('''...(continuação do código)
class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        ...(continuação do código)

        # --- Acesso à barra de menus da janela --- #
        menu = self.menuBar()

        # --- Criação de menus principais --- #
        menu_arquivo = menu.addMenu('&Arquivo')
        menu_editar = menu.addMenu('&Editar')

        # --- Adição de ações ao menu Arquivo --- #
        menu_arquivo.addAction(self.acao_novo)
        menu_arquivo.addAction(self.acao_abrir)
        menu_arquivo.addSeparator()  # linha visual de divisória
        menu_arquivo.addAction(self.acao_sair)
    
    (continuação do código)...''', line_numbers=True)
st.html('''<p class="fonte_texto">Vamos dissecar essa nova parte do nosso quebra-cabeça! A festa começa 
na linha <span class="texto_python">menu = </span><span class="self_python">self</span>
<span class="texto_python">.menuBar()</span>. Como expliquei na teoria, o 
<span class="self_python">self</span><span class="texto_python">.menuBar()</span> é um método nativo da 
classe <span class="texto_python">QMainWindow</span> que vai até o topo da nossa tela, acorda a barra de 
menus invisível que já estava lá esperando por nós, e a entrega na nossa mão através da variável menu.''')
st.html('''<p class="fonte_texto">Com a barra de menus em mãos, começamos a criar as nossas "gavetas" 
principais com as linhas <span class="texto_python">menu_arquivo = menu.addMenu(</span>
<span class="variaveis">'&Arquivo'</span><span class="texto_python">)</span> e 
<span class="texto_python">menu_editar = menu.addMenu(</span>
<span class="variaveis">'&Editar'</span><span class="texto_python">)</span>. Lembra do símbolo "E 
comercial" (<b>&</b>) que usamos nas ações? Ele brilha aqui novamente! Ao colocar o & antes da letra "A", 
estamos dizendo ao sistema operacional que, se o usuário apertar a tecla "Alt" e depois a letra "A", o 
menu "Arquivo" vai se abrir automaticamente. É um detalhe de acessibilidade e navegação por teclado que 
deixa o seu software incrivelmente dinâmico. O menu "Editar" foi criado aqui só para você ver como é fácil 
empilhar categorias lá no topo da tela, mesmo que ainda não tenhamos ações para ele.''')
st.html('''<p class="fonte_texto">Agora, o grande momento da integração: pegar as ações que criamos no 
passo anterior e vinculá-las ao visual! Nas linhas 
<span class="texto_python">menu_arquivo.addAction(...)</span>, nós pegamos o nosso menu recém-criado e 
pedimos para ele adicionar a <span class="self_python">self</span>
<span class="texto_python">.acao_novo</span> e a <span class="self_python">self</span>
<span class="texto_python">.acao_abrir</span>. O PySide6 é tão inteligente que ele extrai tudo da 
<span class="texto_python">QAction</span> sozinho: ele pega o nome ("Novo"), coloca o ícone do lado 
esquerdo e já alinha o texto do atalho ("Ctrl+N") bonitinho do lado direito do menu suspendo. Você não 
precisa formatar nada disso na mão!''')
st.html('''<p class="fonte_texto">Para finalizar, adicionamos um charme de design muito importante com o 
<span class="texto_python">menu_arquivo.addSeparator()</span>. O que esse comando faz? Ele desenha uma 
linha horizontal suave e cinza logo abaixo do botão "Abrir...". Isso cria um respiro visual (agrupando 
funções de criação de arquivo) e isola a nossa <span class="self_python">self</span>
<span class="texto_python">.acao_sair</span> logo abaixo. É uma prática clássica de UI/UX para evitar que 
o usuário clique no botão de fechar o programa sem querer.''')
st.html('''<p class="fonte_texto">Se você executar o seu aplicativo agora, a transformação será notável. 
Lá no topo esquerdo, o menu "Arquivo" estará esperando o seu clique. E ao clicar nele, as suas ações 
estarão enfileiradas como em qualquer programa profissional do mercado!''')
st.divider()

# --- Criar a barra de ferramentas (QToolBar) --- #
st.html('<h1 class="fonte_titulo_aula">Criar a barra de ferramentas ('
        '<span class="texto_python">QToolBar</span>)</h1>')
st.html('''<p class="fonte_texto">Os menus suspensos são fantásticos para organizar absolutamente todas as 
funções do seu aplicativo, mas sejamos sinceros: clicar em "Arquivo", procurar a opção e depois clicar 
de novo não é a coisa mais rápida do mundo. Para aquelas ferramentas que o usuário usa a todo instante 
(como criar um novo documento, salvar ou desfazer uma ação) 
nós precisamos de uma via expressa. É para isso que existem as Barras de Ferramentas (ToolBars)! Elas 
formam aquele painel super visual e recheado de ícones que geralmente fica logo abaixo do menu principal, 
deixando as ações mais importantes a um clique de distância.''')
st.html('''<p class="fonte_texto">Lembra quando conversamos sobre a inteligência de usar as 
<span class="texto_python">QAction</span>? Este é o momento em que essa genialidade brilha intensamente! 
Como nós já empacotamos a lógica, o ícone e o atalho de teclado dentro das nossas ações (
<span class="texto_python">acao_novo</span>, <span class="texto_python">acao_sair</span>), nós não 
precisamos recriar esses botões do zero para a barra de ferramentas. Nós vamos simplesmente pegar essas 
mesmas ações e adicioná-las à nossa nova ToolBar. Isso não apenas poupa dezenas de linhas de código, como 
garante consistência absoluta: não importa se o usuário usa o atalho do teclado, clica no menu ou clica 
no ícone da barra de ferramentas, o resultado será rigorosamente o mesmo.''')
st.html('''<p class="fonte_texto">A cereja do bolo ao usar a classe 
<span class="texto_python">QToolBar</span> integrada à nossa 
<span class="texto_python">QMainWindow</span> é o dinamismo. Quando adicionamos uma barra de ferramentas 
usando as diretrizes de posicionamento do Qt, o framework automaticamente cria uma alça de movimentação 
(aquelas pontilhadas bem sutis no canto esquerdo da barra). Isso significa que, sem escrever uma única 
linha extra de lógica, o seu usuário poderá clicar nessa alça e arrastar a barra para a lateral direita, 
para a parte de baixo da tela, ou até mesmo destacá-la e deixá-la flutuando como uma janelinha 
independente. É um recurso absurdamente profissional que você ganha "de brinde" do PySide6:''')
st.code('''...(continuação do código)
class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        
        (continuação do código)...
        
        # --- Criação da barra de ferramentas --- #
        self.toolbar = QToolBar('Barra principal')
        self.toolbar.setIconSize(QSize(24, 24))
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolbar)

        # --- Reutilização das mesmas ações para garantir consistência --- #
        self.toolbar.addAction(self.acao_novo)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.acao_sair)

        # --- Customização do estilo da toolbar --- #
        self.toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
    
    (continuação do código)...''', line_numbers=True)
st.html('''<p class="fonte_texto">Vamos esmiuçar como construímos essa nova ferramenta! Tudo se inicia com 
a instância <span class="self_python">self</span><span class="texto_python">.toolbar = QToolBar(</span>
<span class="variaveis">'Barra principal'</span><span class="texto_python">)</span>. Passar esse nome 
('Barra principal') é uma boa prática porque, se o seu programa tiver várias barras e o usuário clicar com 
o botão direito para ocultar ou exibir algumas delas, é esse o nome que aparecerá no menu de 
gerenciamento.''')
st.html('''<p class="fonte_texto">Na linha seguinte, garantimos a harmonia visual usando 
<span class="self_python">self</span><span class="texto_python">.toolbar.setIconSize(QSize(</span>
<span class="numeros">24</span><span class="texto_python">, </span><span class="numeros">24</span>
<span class="texto_python">))</span>. A classe <span class="texto_python">QSize</span> (que importamos do 
<span class="texto_python">QtCore</span>) é a maneira padronizada do Qt lidar com larguras e alturas. 
Aqui, estamos forçando a barra a renderizar todos os seus ícones no tamanho quadrado de 24x24 pixels. Isso 
evita que um ícone maior desalinhe a barra inteira, mantendo a estética perfeitamente simétrica.''')
st.html('''<p class="fonte_texto">A linha 
<span class="self_python">self</span><span class="texto_python">.addToolBar(Qt.ToolBarArea.TopToolBarArea, </span>
<span class="self_python">self</span><span class="texto_python">.toolbar)</span> é onde o "casamento" com a 
<span class="texto_python">QMainWindow</span> acontece. Lembra das áreas invisíveis que a janela principal 
possui? Ao usar a <i>flag</i> <span class="texto_python">TopToolBarArea</span>, nós damos a instrução 
explícita: "Pegue a minha barra de ferramentas e encaixe ela firmemente no topo da tela, logo abaixo do 
menu". Se você quisesse que ela iniciasse do lado esquerdo, bastaria usar 
<span class="texto_python">LeftToolBarArea</span>.''')
st.html('''<p class="fonte_texto">A partir daí, o trabalho fica fácil. Com os comandos 
<span class="self_python">self</span><span class="texto_python">.toolbar.addAction(</span><span class="self_python">self</span><span class="texto_python">.acao_novo)</span> 
e <span class="self_python">self</span><span class="texto_python">.toolbar.addAction(</span><span class="self_python">self</span><span class="texto_python">.acao_sair)</span>, 
nós simplesmente chamamos de volta as ações que já havíamos configurado. No meio delas, colocamos um 
<span class="self_python">self</span><span class="texto_python">.toolbar.addSeparator()</span>. Assim como 
fizemos no menu, esse separador cria uma linha vertical elegante entre os botões, ótima para organizar 
grupos de funções lógicas (separando criação de encerramento, por exemplo).''')
st.html('''<p class="fonte_texto">Para fechar o visual com maestria, usamos um comando de estilo 
sensacional: 
<span class="self_python">self</span><span class="texto_python">.toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)</span>. 
Por padrão, uma ToolBar geralmente exibe apenas os ícones para economizar espaço. No entanto, passando essa 
constante específica do Qt, nós instruímos a barra a extrair também o nome da nossa ação e colocá-lo logo 
ao lado direito do ícone. Fica um visual muito descritivo e amigável para usuários iniciantes no seu 
sistema! Experimente rodar o código e não se esqueça de clicar nas pontilhadas e arrastar sua barra pela 
tela para ver a magia acontecendo!''')
st.divider()

# --- Criar a barra de status (self.statusBar) --- #
st.html('<h1 class="fonte_titulo_aula">Criar a barra de status ('
        '<span class="self_python">self</span><span class="texto_python">.statusBar</span>)</h1>')
st.html('''<p class="fonte_texto">Para fecharmos o esqueleto da nossa 
<span class="texto_python">QMainWindow</span> com chave de ouro, precisamos olhar para a base de tudo: o 
rodapé do nosso aplicativo. Já dominamos o topo com os menus e barras de ferramentas, e já garantimos o 
espetáculo no centro com o widget principal. Mas como o nosso programa se comunica com o usuário de forma 
contínua e silenciosa? A resposta está na Barra de Status (Status Bar)! Ela é a ferramenta definitiva para 
o que chamamos de "feedback não intrusivo". Em vez de jogar uma janela de aviso (pop-up) na cara do 
usuário toda vez que ele salvar um arquivo (o que é super irritante), nós usamos o rodapé para dar um 
"sinal de fumaça" sutil de que a ação deu certo.''')
st.html('''<p class="fonte_texto">No ecossistema do Qt, a Barra de Status possui uma dualidade brilhante: 
ela consegue lidar tanto com o efêmero quanto com o permanente. De um lado, ela pode exibir mensagens 
temporárias que somem sozinhas após alguns segundos (como "Carregando...", "Salvo com sucesso" ou 
"Pronto para uso"). Do outro, ela possui uma área dedicada para widgets permanentes, que ficam fixados no 
canto direito da tela, imunes às mensagens temporárias. É o lugar perfeito para colocar um contador de 
palavras, um controle de zoom ou, como faremos aqui, a versão atual do sistema.''')
st.html('''<p class="fonte_texto">Além disso, a criação da Barra de Status ativa automaticamente um 
superpoder que deixamos adormecido algumas etapas atrás. Lembra quando criamos as nossas 
<span class="texto_python">QAction</span> e configuramos o método 
<span class="texto_python">setStatusTip()</span> com textos explicativos? Pois bem, o framework é tão 
inteligente que essas duas partes conversam sozinhas. Assim que a sua barra de status nascer, toda vez que 
o usuário repousar o mouse sobre um botão na barra de ferramentas ou no menu, a explicação daquele botão 
aparecerá magicamente no rodapé, sem que você precise escrever um único 
<span class="palavras_reservadas">if</span> ou função de detecção de mouse:''')
st.code('''...(continuação do código)
class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        
        ...(continuação do código)
        
        # --- Inicialização da barra de status --- #
        self.status = self.statusBar()

        # --- Exibição de uma mensagem temporária de inicialização --- #
        self.status.showMessage('Pronto para uso', 5000)  # dura 5 segundos

        # --- Adição de um widget permanente (ex: contator de caracteres ou versão do app) --- #
        self.label_versao = QLabel('Versão: 1.2.0 | Engine: PySide6 v6.10')
        self.status.addPermanentWidget(self.label_versao)
    
    (continuação do código)...''', line_numbers=True)
st.html('''<p class="fonte_texto">Vamos entender a simplicidade e a elegância dessa implementação. Assim 
como fizemos com a barra de menus, nós não precisamos instanciar um objeto complexo do zero. Na linha 
<span class="self_python">self</span><span class="texto_python">.status = </span><span class="self_python">self</span><span class="texto_python">.statusBar()</span>, 
nós apenas utilizamos o método nativo da nossa <span class="texto_python">QMainWindow</span> para "acordar" 
a barra de status que já existe por baixo dos panos e a atribuímos à nossa variável 
<span class="self_python">self</span><span class="texto_python">.status</span>. Só de fazer isso, se você 
passar o mouse sobre os botões "Novo" ou "Sair", já verá as dicas aparecendo lá embaixo.''')
st.html('''<p class="fonte_texto">Para dar boas-vindas ao nosso usuário, utilizamos a função 
<span class="self_python">self</span><span class="texto_python">.status.showMessage(</span><span class="variaveis">'Pronto para uso'</span><span class="texto_python">, </span><span class="numeros">5000</span><span class="texto_python">)</span>. 
O primeiro parâmetro é a string com o texto que queremos exibir. O pulo do gato está no segundo parâmetro: 
ele representa o tempo de vida dessa mensagem em milissegundos. Ao colocarmos 
<span class="numeros">5000</span>, estamos instruindo o PySide6 a mostrar o texto por exatamente 5 
segundos e depois apagá-lo automaticamente, limpando a tela sem que precisemos criar lógicas complexas de 
contagem de tempo.''')
st.html('''<p class="fonte_texto">Por fim, nós criamos uma informação que não pode sumir nunca: a versão 
do nosso sistema. Primeiro, criamos uma simples <span class="texto_python">QLabel</span> de texto chamada 
<span class="self_python">self</span><span class="texto_python">.label_versao</span>. Em seguida, passamos 
essa label para o comando poderoso 
<span class="self_python">self</span><span class="texto_python">.status.addPermanentWidget(</span><span class="self_python">self</span><span class="texto_python">.label_versao)</span>.''')
st.html('''<p class="fonte_texto">O que esse método faz de tão especial? Ele pega a nossa label e a 
"ancora" de forma definitiva no extremo direito da barra de status. Isso é sensacional porque o lado 
esquerdo da barra fica totalmente livre para exibir as mensagens temporárias (como o 'Pronto para uso' 
ou as dicas de hover do mouse), enquanto o lado direito mantém a sua informação de versão ali, firme e 
forte, sem que um texto atropele o outro. É assim que garantimos um layout funcional e perfeitamente 
equilibrado!''')
st.divider()

# --- Melhorar o aplicativo --- #
st.html('<h1 class="fonte_titulo_aula">Melhorar o aplicativo</h1>')
st.html('''<p class="fonte_texto">Chegamos à versão final e polida do nosso aplicativo da Aula 02! Até 
aqui, nós construímos a estrutura bruta: erguemos as paredes com a 
<span class="texto_python">QMainWindow</span>, colocamos as ferramentas nas prateleiras com os Menus e as 
ToolBars, e criamos o nosso canal de comunicação no rodapé com a Barra de Status. Agora, é o momento de 
darmos aquele "tapa no visual" e aplicarmos os refinamentos técnicos que transformam um projeto didático 
em um software com cara e comportamento de mercado.''')
st.html('''<p class="fonte_texto">Nesta etapa final, o foco é aprimorar a experiência do usuário (UX) e o 
design da interface (UI). Você notará que pequenas mudanças (como a reestruturação da forma como 
aplicamos as cores e bordas, o bloqueio de movimentos indesejados nas barras e o ajuste fino nas mensagens 
que o aplicativo nos devolve) fazem uma diferença colossal na percepção de qualidade do programa. Além 
disso, começamos a preparar o terreno para o futuro do nosso curso, revelando detalhes que vão acompanhar 
o nosso projeto prático principal:''')
st.code("""# --- Importar os módulos --- #
import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel,
                               QMenuBar, QToolBar, QStatusBar)


class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        # --- Configurações fundamentais da janela principal --- #
        self.setWindowTitle('Sistema Profissional PySide6')
        self.resize(1024, 768)

        # --- Criação e configuração do widget central --- #
        self.widget_central = QLabel('Área de trabalho principal')
        self.widget_central.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget_central.setStyleSheet('''
        QLabel {
            font-size: 20pt;
            color: #34495e;
            background-color: #ecf0f1;
            border: 5px dashed #bdc3c7;
            border-radius: 10px;
            margin: 20px
        }''')

        # --- Definição obrigatório do widget central no QMainWindow --- #
        self.setCentralWidget(self.widget_central)

        # --- Definição de ações compartilhadas (QAction) --- #
        self.acao_novo = QAction(QIcon.fromTheme('document-new'), '&Novo Arquivo', self)
        self.acao_novo.setShortcut(QKeySequence.StandardKey.New)
        self.acao_novo.setStatusTip('Criar um novo arquivo em branco')
        self.acao_novo.triggered.connect(self.slot_novo_arquivo)

        self.acao_abrir = QAction('&Abrir...', self)
        self.acao_abrir.setShortcut(QKeySequence.StandardKey.Open)
        self.acao_abrir.setStatusTip('Abrir um arquivo existente')

        self.acao_sair = QAction('&Sair da Aplicação', self)
        self.acao_sair.setShortcut('Ctrl+Q')
        self.acao_sair.setStatusTip('Fechar o sistema com segurança')
        self.acao_sair.triggered.connect(self.close)

        # --- Acesso à barra de menus da janela --- #
        menu = self.menuBar()

        # --- Criação de menus principais --- #
        menu_arquivo = menu.addMenu('&Arquivo')
        menu_editar = menu.addMenu('&Editar')

        # --- Adição de ações ao menu Arquivo --- #
        menu_arquivo.addAction(self.acao_novo)
        menu_arquivo.addAction(self.acao_abrir)
        menu_arquivo.addSeparator()  # linha visual de divisória
        menu_arquivo.addAction(self.acao_sair)

        # --- Criação da barra de ferramentas --- #
        self.toolbar = QToolBar('Barra principal')
        self.toolbar.setIconSize(QSize(16, 16))
        self.toolbar.setMovable(False)
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolbar)

        # --- Reutilização das mesmas ações para garantir consistência --- #
        self.toolbar.addAction(self.acao_novo)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.acao_sair)

        # --- Customização do estilo da toolbar --- #
        self.toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        # --- Inicialização da barra de status --- #
        self.status = self.statusBar()

        # --- Exibição de uma mensagem temporária de inicialização --- #
        self.status.showMessage('Sistema Horizon pronto para operação', 5000)  # dura 5 segundos

        # --- Adição de um widget permanente (ex: contator de caracteres ou versão do app) --- #
        self.label_versao = QLabel('Versão: 1.2.0 | Engine: PySide6 v6.10')
        self.status.addPermanentWidget(self.label_versao)

    def slot_novo_arquivo(self):
        '''Resposta à ação de criar um novo arquivo.'''
        self.widget_central.setText('Ação "Novo Arquivo" executada!')
        self.status.showMessage('Novo arquivo criado.', 300)


if __name__ == '__main__':
    # --- Inicialização da infraestrutura do Qt --- #
    app = QApplication()

    # --- Instanciação da interface principal --- #
    janela = JanelaPrincipal()
    janela.show()

    # --- Início do loop de eventos --- #
    sys.exit(app.exec())""", line_numbers=True)
st.html('''<p class="fonte_texto">Vamos focar exclusivamente no que mudou nesta última versão! A primeira 
grande alteração está no <span class="texto_python">setStyleSheet</span> do nosso 
<span class="texto_python">widget_central</span>. Antes, tínhamos apenas três linhas soltas. Agora, 
estruturamos o código exatamente como se faz em CSS profissional, abrindo um bloco 
<span class="texto_python">QLabel { ... }</span>. Adicionamos um 
<span class="texto_python">background-color</span> cinza claro (
<span class="texto_python">#ecf0f1</span>), criamos uma borda tracejada (
<span class="texto_python">dashed</span>) bem destacada com 
<span class="texto_python">border: 5px</span>, arredondamos as pontas com 
<span class="texto_python">border-radius: 10px</span> e colocamos um respiro de 
<span class="texto_python">margin: 20px</span> para que a borda não grude nas extremidades da janela. O 
visual ficou incrivelmente mais elegante!''')
st.html('''<p class="fonte_texto">Fizemos também ajustes cirúrgicos nos textos das nossas ações. Trocamos 
"Novo" por "Novo Arquivo" e "Sair" por "Sair da Aplicação", além de refinar as 
<span class="texto_python">StatusTips</span> (as dicas que aparecem no rodapé) para deixá-las mais 
descritivas, como "Fechar o sistema com segurança". Pequenos detalhes textuais importam muito na hora do 
usuário navegar.''')
st.html('''<p class="fonte_texto">Na nossa Barra de Ferramentas (
<span class="self_python">self</span><span class="texto_python">.toolbar</span>), aplicamos duas mudanças 
pontuais, mas muito relevantes:''')
st.html('''<ul class="fonte_texto">
    <li><span class="self_python">self</span><span class="texto_python">.toolbar.setIconSize(QSize(</span><span class="numeros">16</span><span class="texto_python">, </span><span class="numeros">16</span><span class="texto_python">))</span>: 
    Reduzimos os ícones de 24 para 16 pixels. Isso deixa a barra mais compacta e profissional, sobrando 
    mais espaço de tela para o conteúdo principal do aplicativo.</li>
    <li><span class="self_python">self</span><span class="texto_python">.toolbar.setMovable(</span><span class="palavras_reservadas">False</span><span class="texto_python">)</span>: 
    Lembra daquela alça pontilhada que permitia arrastar a barra para qualquer canto? Ao definir 
    <span class="texto_python">setMovable(</span><span class="palavras_reservadas">False</span><span class="texto_python">)</span>, 
    nós desativamos essa função! Assim, a barra fica "travada" no topo. Isso é muito útil quando você não 
    quer que o usuário desconfigure o layout do seu programa acidentalmente.</li>
</ul>''')
st.html('''<p class="fonte_texto">Outro detalhe bem legal é que introduzimos o nome do nosso grande 
projeto final na mensagem de inicialização da barra de status: 
<span class="variaveis">'Sistema Horizon pronto para operação'</span>. É bom já ir se acostumando com esse 
nome, pois ele será a estrela do nosso curso!''')
st.html('''<p class="fonte_texto">Por fim, e não menos importante, demos um upgrade no nosso "slot" (a 
função que é ativada quando clicamos em Novo Arquivo). Mudamos o nome da função para 
<span class="texto_python">slot_novo_arquivo</span> (para deixar ainda mais óbvio que ela é uma resposta a 
um sinal). E, dentro dela, adicionamos a linha 
<span class="self_python">self</span><span class="texto_python">.status.showMessage(</span><span class="variaveis">'Novo arquivo criado.'</span><span class="texto_python">, </span><span class="numeros">3000</span><span class="texto_python">)</span>. 
O que isso faz? Toda vez que o usuário criar um novo arquivo, além do texto no centro da tela mudar, a 
barra de status exibirá essa mensagem de confirmação por 3 segundos (3000 milissegundos). É o feedback 
visual perfeito e não intrusivo do qual falamos na teoria!''')
st.divider()

# --- Resumo --- #
st.html('<h1 class="fonte_titulo_aula">Resumo</h1>')
st.html('''<p class="fonte_texto">Nesta segunda aula, demos um salto gigantesco, saindo de janelas 
improvisadas para construir a estrutura definitiva de softwares comerciais utilizando a poderosa 
<span class="texto_python">QMainWindow</span>. Diferente de um widget comum, essa classe atua como um 
"chassi" profissional, possuindo áreas nativas e otimizadas para acomodar menus superiores, barras de 
ferramentas e um rodapé. Aprendemos que toda janela principal exige um "palco", o qual definimos através 
do <span class="texto_python">setCentralWidget()</span>, e elevamos o nível do design da nossa interface 
aplicando estilos visuais com QSS (Qt Style Sheets), manipulando fontes, cores hexadecimais e bordas 
arredondadas exatamente como faríamos no desenvolvimento web moderno.''')
st.html('''<p class="fonte_texto">O grande trunfo de produtividade e engenharia de software dessa etapa 
foi o domínio das <span class="texto_python">QAction</span>. Em vez de reescrever o mesmo código repetidas 
vezes, nós empacotamos nossos comandos (vinculando ícones, textos descritivos e atalhos de teclado 
inteligentes e multiplataforma via <span class="texto_python">QKeySequence</span>) em ações centralizadas. 
Em seguida, distribuímos essas ações de forma muito elegante, criando menus suspensos na Barra de Menus (<span class="texto_python">menuBar</span>) e botões de acesso ultrarrápido na Barra de Ferramentas (<span class="texto_python">QToolBar</span>). Isso nos garantiu uma consistência absoluta na navegação, 
quer o usuário clique na tela ou prefira utilizar o teclado.''')
st.html('''<p class="fonte_texto">Para amarrar todo esse esqueleto com perfeição, ativamos a Barra de 
Status (<span class="texto_python">statusBar</span>) na parte inferior do aplicativo. Descobrimos como 
ela é vital para fornecer um feedback limpo e não intrusivo, sendo capaz de exibir tanto mensagens 
temporárias de sucesso quanto widgets de informações permanentes, como a versão do nosso aguardado 
"Sistema Horizon". Tudo isso ganhou vida real no momento em que conectamos os eventos de clique dos 
usuários aos nossos métodos personalizados através do 
<span class="texto_python">triggered.connect()</span>, provando que agora sabemos exatamente como unir 
um design visual deslumbrante à lógica implacável do Python!''')
st.divider()

# --- Conclusão --- #
st.html('<h1 class="fonte_titulo_aula">Conclusão</h1>')
st.html('''<p class="fonte_texto">Chegar ao final desta segunda aula marca um verdadeiro divisor de águas 
na nossa jornada de desenvolvimento com o PySide6! Nós deixamos o campo dos testes básicos e entramos 
definitivamente na arena profissional. Ao adotarmos a arquitetura da 
<span class="texto_python">QMainWindow</span>, você percebeu como é simples e ao mesmo tempo poderoso 
implementar os mesmos padrões visuais exigidos pelo mercado de software atual. Menus bem estruturados, 
barras de ferramentas interativas e rodapés informativos não são mais mistérios; eles agora são recursos 
que você domina para entregar uma experiência de uso rica, elegante e incrivelmente intuitiva.''')
st.html('''<p class="fonte_texto">Mas a verdadeira beleza do que construímos hoje reside na inteligência 
por trás dessa interface. Com a genialidade das <span class="texto_python">QAction</span> e o padrão de 
Sinais e Slots, você aprendeu a centralizar os comandos do seu programa. Criar atalhos dinâmicos que se 
adaptam a qualquer sistema operacional e conectar cliques a funções reais em Python prova que o seu 
aplicativo deixou de ser apenas uma vitrine visual e se tornou um motor interativo pronto para executar 
ações de verdade. É exatamente sobre essa base robusta que o nosso aguardado Sistema Horizon começará a 
tomar forma!''')
st.html('''<p class="fonte_texto">A regra fundamental agora é: coloque a mão na massa e pratique sem 
medo! Explore o código, altere o QSS para aplicar as suas cores e fontes favoritas, crie novas "gavetas" 
nos menus e adicione botões inéditos na sua barra de ferramentas para ver como o framework reage. A 
familiaridade prática com esses componentes é o que afiará as suas habilidades.''')
st.subheader('No mais é isso, nos vemos na próxima aula! Até lá, fiquem com Deus e fui!')