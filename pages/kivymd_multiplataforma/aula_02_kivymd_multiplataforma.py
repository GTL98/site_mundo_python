# --- Importar as bibliotecas --- #
from PIL import Image
import streamlit as st
from carregar_css import carregar_css

# --- Configurações iniciais da página --- #
st.set_page_config(
    page_title='KivyMD Multiplataforma - Aula 02',
    page_icon=Image.open('./assets/logo/logo.png'),
    layout='wide'
)

# --- Carregar o CSS --- #
carregar_css()

# --- Colocar o título da aula --- #
st.html('<h1 class="fonte_titulo_aula">Aula 02: Estrutura KV – Integrando Interface e Lógica!</h1>')

# --- Vídeo --- #
with st.expander('Se quiser acompanhar com o vídeo, acesse aqui! 👇'):
    st.video('https://youtu.be/QObpsxbMHZA')

# --- Código da aula --- #
st.subheader('Se quiser acessar o código completo da aula, clique [aqui](https://github.com/GTL98/canal_mundo_python/tree/main/Desenvolvedor%20KivyMD%3A%20Do%20Zero%20ao%20App%20Multiplataforma/Aula%2002)')
st.divider()

# --- Introdução --- #
st.subheader('E fala, devs! Tudo bem com vocês? Espero que sim!')
st.html('<h1 class="fonte_titulo_aula">Introdução</h1>')
st.html('''<p class="fonte_texto">Bem-vindos à nossa segunda aula do curso de KivyMD! Se na primeira aula 
nós montamos a base do nosso aplicativo e entendemos o ciclo de vida usando apenas o Python, hoje nós 
daremos um salto gigantesco na forma como estruturamos os nossos projetos. Aprenderemos a separar a 
parte visual (o nosso front-end) da parte lógica (o nosso back-end).</p>''')
st.html('''<p class="fonte_texto">Imagine construir uma casa onde a fiação elétrica e o encanamento ficam 
todos misturados com a pintura e os móveis da sala. Seria uma bagunça, certo? No desenvolvimento de 
aplicativos é a mesma coisa! Para evitar o famoso "código espaguete", o Kivy nos apresenta uma ferramenta 
fantástica chamada <b>Linguagem KV (KV Lang)</b>. Ela foi criada especificamente para desenhar interfaces 
gráficas de forma simples, declarativa e muito mais limpa. Hoje, entenderemos como essa linguagem se 
integra ao nosso código Python para criar aplicativos profissionais e fáceis de manter!</p>''')
st.subheader('Então sem mais delongas, bora para a aula!')
st.divider()

# --- Criar a string KV --- #
st.html('<h1 class="fonte_titulo_aula">Criar a string KV</h1>')
st.html('''<p class="fonte_texto">Antes de pularmos direto para a criação de um arquivo separado, a 
melhor forma de entender a sintaxe da linguagem KV é escrevendo ela dentro do próprio arquivo Python, 
usando uma string de múltiplas linhas.</p>''')
st.html('''<p class="fonte_texto">A teoria aqui é simples: em vez de instanciar classes e usar funções 
como <span class="texto_python">add_widget()</span> o tempo todo no Python (como fizemos na 
<a href="https://mundopython.streamlit.app/aula_01_kivymd_multiplataforma">aula 1</a>), vamos 
"desenhar" a nossa árvore de widgets usando apenas nomes e indentação (espaços). Na linguagem KV, o que 
está mais à esquerda é o "pai", e o que está recuado com espaços abaixo dele é o "filho". Em vez de usar o 
sinal de igual (<span class="texto_python">=</span>) para definir atributos, usamos os dois pontos (
<span class="texto_python">:</span>). É uma sintaxe que lembra muito o próprio Python, o que facilita 
demais o aprendizado.</p>''')
st.html('''<p class="fonte_texto">Aqui está a nossa primeira estrutura usando a linguagem KV:</p>''')
st.code("""# --- Importar os módulos --- #
from kivymd.app import MDApp
from kivy.lang import Builder

# --- Definir a interface inicial --- #
# --- O widget raiz aqui é o MDScreen --- #
KV = '''
MDScreen:
    md_bg_color: self.theme_cls.bg_normal
    
    MDLabel:
        text: "Iniciando com a Linguagem KV"
        halign: "center"
        font_style: "H4"
        theme_text_color: "Primary"
'''


class Aula02App(MDApp):
    def build(self):
        # --- O método build() deve retornar o widget raiz da aplicação --- #
        # --- Builder.load_string() processa a string KV e instancia os objetos --- #
        return Builder.load_string(KV)


if __name__ == '__main__':
    Aula02App().run()""", line_numbers=True)
st.html('''<p class="fonte_texto">Vamos esmiuçar essa estrutura para você não ter nenhuma dúvida de como 
essa mágica acontece!</p>''')
st.html('''<p class="fonte_texto">A primeira grande novidade está nas nossas importações: 
<span class="palavras_reservadas">from </span><span class="texto_python">kivy.lang </span>
<span class="palavras_reservadas">import </span><span class="texto_python">Builder</span>. O 
<span class="texto_python">Builder</span> (construtor) é o grande mestre de obras do Kivy. É ele quem 
consegue ler um texto escrito em linguagem KV, interpretar os comandos e transformá-los em botões, telas e 
textos reais no seu aplicativo. Sem ele, a nossa string seria apenas um texto inútil.</p>''')
st.html("""<p class="fonte_texto">Em seguida, criamos uma variável chamada 
<span class="texto_python">KV</span> e abrimos três aspas simples (
<span class="variaveis">'''</span>). Isso no Python permite criar uma string de várias linhas. Tudo o que 
está aqui dentro é a linguagem KV em ação.</p>""")
st.html("""<p class="fonte_texto">Repare na estrutura dessa string:</p>""")
st.html('<ol type=1 class="fonte_texto">'
        '<li>Começamos com <span class="texto_python">MDScreen:</span>. Esse é o nosso widget raiz. Ao colocar '
        'os dois pontos no final, avisamos ao interpretador que vamos configurar esse widget nas linhas '
        'seguintes.</li>'
        '<li>Logo abaixo, indentado (com um "tab" ou 4 espaços), definimos '
        '<span class="texto_python">md_bg_color: self.theme_cls.bg_normal</span>. Aqui estamos dizendo que '
        'a cor de fundo da nossa tela será a cor normal do tema do aplicativo. Note o uso dos dois pontos '
        'em vez do sinal de igual.</li>'
        '<li>Ainda dentro da tela, chamamos o <span class="texto_python">MDLabel:</span>. Como ele está '
        'indentado abaixo do <span class="texto_python">MDScreen</span>, o Kivy automaticamente entende '
        'que este texto é "filho" da tela. Nós não precisamos mais do '
        '<span class="texto_python">add_widget</span>.</li>'
        '<li>Dentro do <span class="texto_python">MDLabel</span>, com mais um nível de indentação, '
        'passamos as configurações que já conhecemos: <span class="texto_python">text</span>, '
        '<span class="texto_python">halign</span>, <span class="texto_python">font_style</span> e '
        '<span class="texto_python">theme_text_color</span>, todas separadas por dois pontos. Tudo muito '
        'visual e organizado.</li>'
        '</ol>')
st.html("""<p class="fonte_texto">Por fim, descemos para a nossa classe lógica, a 
<span class="classe_python">Aula02App</span>. Veja como o método 
<span class="funcao_python">build</span><span class="texto_python">(</span>
<span class="self_python">self</span><span class="texto_python">):</span> ficou minúsculo e limpo! A 
única coisa que ele faz agora é usar o <span class="palavras_reservadas">return </span>
<span class="texto_python">Builder.load_string(KV)</span>. Nós passamos a nossa variável de texto para o 
<span class="texto_python">Builder</span>, e ele faz todo o trabalho pesado de criar a tela, aplicar o 
fundo, gerar o texto, colocar o texto dentro da tela e entregar tudo empacotadinho e pronto para ser 
exibido.</p>""")
st.html("""<p class="fonte_texto">Execute esse código e veja que o resultado visual é idêntico ao que 
faríamos programando puramente em Python, mas agora com uma estrutura que nos prepara para criar interfaces 
infinitamente mais complexas sem perder a sanidade!</p>""")
st.divider()

# --- Incrementar a string KV --- #
st.html('<h1 class="fonte_titulo_aula">Incrementar a string KV</h1>')
st.html("""<p class="fonte_texto">Para que os elementos não fiquem todos amontoados ou perdidos na tela, 
o KivyMD utiliza os chamados <b>Layouts</b>. Pense nos layouts como caixas organizadoras transparentes. Você 
define as regras da caixa (por exemplo: "tudo o que entrar aqui deve ser empilhado de cima para baixo") 
e o framework cuida da matemática para encaixar tudo perfeitamente. Hoje veremos o 
<span class="texto_python">MDBoxLayout</span>, construir a nossa primeira barra de navegação superior e 
entender a hierarquia visual.</p>""")
st.html("""<p class="fonte_texto">Na teoria, a construção de interfaces modernas funciona como a montagem 
de uma árvore de raízes e galhos (a famosa <i>Widget Tree</i>). A nossa tela principal (
<span class="texto_python">MDScreen</span>) é o tronco. Dentro dela, colocaremos um contêiner 
organizador geral. Dentro desse contêiner, colocaremos a nossa barra superior (
<span class="texto_python">MDTopAppBar</span>) e outro contêiner menor para organizar os textos e o 
botão. Se você entender essa lógica de "caixas dentro de caixas" controladas pela indentação da 
linguagem KV, você conseguirá desenhar absolutamente qualquer tela que imaginar.</p>""")
st.html("""<p class="fonte_texto">Dá só uma olhada na evolução brutal que a nossa string KV sofreu:</p>""")
st.code("""...(continuação do código)
KV = '''
MDScreen:
    md_bg_color: self.theme_cls.bg_normal

    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: 'Aula 02: Estrutura KV'
            elevation: 4
            pos_hint: {'top': 1}
            md_bg_color: app.theme_cls.primary_color
            specific_text_color: 1, 1, 1, 1

        MDBoxLayout:
            orientation: 'vertical'
            padding: '20dp'
            spacing: '15dp'

            MDLabel:
                text: 'Entendendo a Hierarquia de Widgets'
                halign: 'center'
                font_style: 'H5'
                adaptative_height: True

            MDLabel:
                text: 'Cada nível de indentação representa um novo nível na árvore.'
                halign: 'center'
                theme_text_color: 'Secondary'
                adaptative_height: True

            MDRaisedButton:
                text: 'BOTÃO DECLARATIVO'
                pos_hint: {'center_x': 0.5}

            # --- O widget genérico atua como um espaçador flexível --- #
            Widget:
'''
(continuação do código)...""", line_numbers=True)
st.html("""<p class="fonte_texto">Vamos dissecar essa nova estrutura, detalhe por detalhe, para você não 
perder absolutamente nada do que está acontecendo nos bastidores!</p>""")
st.html("""<p class="fonte_texto">Logo abaixo do nosso <span class="texto_python">MDScreen</span>, nós 
adicionamos o nosso primeiro <span class="texto_python">MDBoxLayout</span>. O parâmetro 
<span class="texto_python">orientation: 'vertical'</span> é a regra de ouro dele: ele pegará todos os 
widgets "filhos" (que estão indentados dentro dele) e empilhá-los um embaixo do outro.</p>""")
st.html("""<p class="fonte_texto">O primeiro filho dessa caixa principal é o 
<span class="texto_python">MDTopAppBar</span>. Essa é aquela clássica barra colorida que fica no topo dos 
aplicativos mobile. Veja como a configuramos:</p>""")
st.html('<ul class="fonte_texto">'
        '<li><span class="texto_python">title</span>: O nome que aparece escrito na barra.</li>'
        '<li><span class="texto_python">elevation</span>: Define a sombra da barra. Um valor de 4 cria um '
        'efeito 3D sutil, fazendo parecer que a barra está flutuando acima da tela.</li>'
        '<li><span class="texto_python">pos_hint: {"top": 1}</span>: Esse é um dicionário de '
        'posicionamento. Ele garante que essa barra ficará grudada no topo (100% da altura) '
        'independentemente do tamanho da tela do celular.</li>'
        '<li><span class="texto_python">md_bg_color: app.theme_cls.primary_color</span>: Lembra que usamos '
        '<span class="texto_python">self</span> na cor de fundo da tela? Aqui nós usamos a palavra reservada '
        '<span class="texto_python">app</span>. No Kivy KV, <span class="texto_python">app</span> faz '
        'referência direta à sua classe Python principal (a <span class="classe_python">Aula02App</span>). '
        'Então, estamos pedindo para o Python pintar essa barra com a cor primária global do nosso '
        'aplicativo.</li>'
        '<li><span class="texto_python">specific_text_color: 1, 1, 1, 1</span>: Estamos forçando a cor '
        'do texto e dos ícones da barra a serem brancos (formato RGBA).</li>'
        '</ul>')
st.html("""<p class="fonte_texto">Logo abaixo da barra superior, nós criamos um segundo 
<span class="texto_python">MDBoxLayout</span>. Sim, uma caixa dentro de outra caixa! Por que fizemos 
isso? Porque queríamos aplicar margens específicas apenas no conteúdo, sem afetar a barra de 
navegação.</p>""")
st.html('<ul class="fonte_texto">'
        '<li><span class="texto_python">padding: "20dp"</span>: Cria uma margem de proteção "do lado de '
        'dentro" da caixa, garantindo que os textos não fiquem colados nas bordas do celular.</li>'
        '<li><span class="texto_python">spacing: "15dp"</span>: Cria um respiro (espaçamento) de 15 pixels automaticamente entre os widgets que estão dentro dessa caixa.</li>'
        '<li><span class="texto_python">pos_hint: {"top": 1}</span>: Esse é um dicionário de '
        'posicionamento. Ele garante que essa barra ficará grudada no topo (100% da altura) '
        'independentemente do tamanho da tela do celular.</li>'
        '<li><i>Nota rápida: O "dp" significa Density-independent Pixels, que garante que os tamanhos '
        'fiquem proporcionais, seja numa tela HD ou 4K.</i></li>'
        '</ul>')
st.html("""<p class="fonte_texto">Dentro dessa segunda caixa, inserimos os nossos conteúdos visuais:</p>""")
st.html('<ul class="fonte_texto">'
        '<li><span class="texto_python">MDLabel</span>: Criamos dois textos. O detalhe importante aqui é a '
        'propriedade <span class="texto_python">adaptive_height: True</span>. Se você não colocar isso, o Kivy '
        'tenta dividir a tela igualmente entre todos os widgets. Com esse parâmetro ativado, o texto diz: "Ei, '
        'me dê apenas a altura necessária para eu existir, não quero ocupar o espaço dos outros!". No segundo '
        'label, o <span class="texto_python">theme_text_color: "Secondary"</span> deixa a fonte com aquele tom '
        'acinzentado de subtítulo.</li>'
        '<li><span class="texto_python">MDRaisedButton</span>: O nosso primeiro botão interativo! O '
        '<span class="texto_python">MDRaisedButton</span> já vem com o Material Design embutido (cor '
        'primária com leve sombra). Usamos o '
        '<span class="texto_python">pos_hint: {"center_x": 0.5}</span> para centralizá-lo horizontalmente '
        '(50% do eixo X da tela).</li>'
        '</ul>')
st.html("""<p class="fonte_texto">Por fim, lá embaixo, temos um singelo 
<span class="texto_python">Widget:</span>. O <span class="texto_python">Widget</span> no Kivy é a forma 
mais crua e invisível de um elemento. Por que o colocamos ali? Lembra que os widgets tentam dividir o 
espaço da tela? Como nossos textos e botões estão configurados para ocupar apenas o mínimo de espaço 
necessário, todo o resto da tela abaixo deles ficaria "sobrando". O 
<span class="texto_python">Widget</span> em branco atua como um preenchedor ou espaçador de gravidade: 
ele absorve todo esse espaço vazio na base, empurrando o nosso botão e os textos lá para cima, deixando 
tudo elegante e organizado.</p>""")
st.html("""<p class="fonte_texto">Execute o seu código e veja que agora você já tem um aplicativo com 
barra de topo, espaçamentos profissionais e um botão estilizado. Tudo isso sem usar um único 
<span class="texto_python">add_widget</span> no Python!</p>""")
st.divider()

# --- Criar o arquivo .kv (KV Lang) --- #
st.html('<h1 class="fonte_titulo_aula">Criar o arquivo .kv (KV Lang)</h1>')
st.html("""<p class="fonte_texto">Chegou o momento de darmos o passo definitivo para a organização 
profissional do nosso projeto! Manter a interface dentro de uma variável de texto (string) no Python 
quebra um galho no começo, mas se o aplicativo crescer, esse arquivo virará um monstro indomável. A 
solução elegante é extrair todo esse código visual e colocá-lo em um arquivo próprio, com a extensão 
<span class="texto_python">.kv</span>.</p>""")
st.html("""<p class="fonte_texto">Aqui está o código que deve ser salvo no seu novo arquivo KV:</p>""")
st.code('''MDScreen:
    md_bg_color: self.theme_cls.bg_normal

    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: 'Aula 02: Estrutura KV'
            elevation: 4
            pos_hint: {'top': 1}
            md_bg_color: app.theme_cls.primary_color
            specific_text_color: 1, 1, 1, 1

        MDBoxLayout:
            orientation: 'vertical'
            padding: '20dp'
            spacing: '15dp'

            MDLabel:
                text: 'Separando a lógica da Interface'
                halign: 'center'
                font_style: 'H5'
                adaptative_height: True

            MDTextField:
                hint_text: 'Digite algo para interagir'
                mode: 'rectangle'

            MDRaisedButton:
                text: 'EXECUTAR AÇÃO'
                pos_hint: {'center_x': 0.5}
                on_release: app.acao_botao()

            # --- O widget genérico atua como um espaçador flexível --- #
            Widget:''', line_numbers=True, language='kv')
st.html("""<p class="fonte_texto">Vamos dissecar as grandes novidades que inserimos nesse arquivo visual! 
A estrutura base de caixas e topo continua a mesma, mas adicionamos dois elementos fantásticos que trazem 
a interatividade para o jogo.</p>""")
st.html("""<p class="fonte_texto">Primeiro, apresentamos o 
<span class="texto_python">MDTextField</span>. Esse é o famoso campo de entrada de dados, onde o usuário 
poderá tocar e digitar pelo teclado do celular! Nós o configuramos com duas propriedades super 
simples:</p>""")
st.html('<ul class="fonte_texto">'
        '<li><span class="texto_python">hint_text: "Digite algo para interagir"</span>: Esse é o texto '
        'de dica que fica flutuando na caixa de texto quando ela está vazia (também conhecido como '
        '<i>placeholder</i> no desenvolvimento web).</li>'
        '<li><span class="texto_python">mode: "rectangle"</span>: Por padrão, o campo de texto do '
        'Material Design é apenas uma linha sublinhada. Ao mudar o modo para retângulo, ele ganha uma '
        'borda arredondada completinha em volta dele, deixando o visual muito mais amigável e moderno.</li>'
        '</ul>')
st.html("""<p class="fonte_texto">Em seguida, fomos no nosso 
<span class="texto_python">MDRaisedButton</span> e adicionamos a linha de ouro de toda essa aula: 
<span class="texto_python">on_release: app.acao_botao()</span>. Lembra que os arquivos estão 
separados agora? Essa linha é a ponte de comunicação entre eles! O evento 
<span class="texto_python">on_release</span> significa "quando o usuário tocar no botão e soltar o dedo 
da tela". Quando isso acontecer, ele chamará o <span class="texto_python">app</span> (que é a nossa 
classe Python principal) e procurar lá dentro por uma função exata chamada 
<span class="texto_python">acao_botao()</span>.</p>""")
st.html("""<p class="fonte_texto">Agora, vejamos como o nosso arquivo Python se prepara para receber essa 
chamada:</p>""")
st.code('''# --- Importar os módulos --- #
import os
from kivymd.app import MDApp
from kivy.lang import Builder


class Aula02App(MDApp):
    def build(self):
        # --- O método build() deve retornar o widget raiz da aplicação --- #
        # --- Builder.load_file() carrega o arquivo KV e instancia os objetos --- #
        caminho_kv = os.path.join(os.path.dirname(__file__), 'interface.kv')
        return Builder.load_file(caminho_kv)

    def acao_botao(self):
        print('Botão pressionado! A lógica está no Python, a interface no KV!')


if __name__ == '__main__':
    Aula02App().run()''', line_numbers=True)
st.html("""<p class="fonte_texto">Olha só que elegância! O nosso arquivo Python agora se concentra 
100% na lógica. Mas para que ele consiga ler aquele arquivo visual que criamos, precisamos fazer alguns 
ajustes cirúrgicos.</p>""")
st.html("""<p class="fonte_texto">A primeira grande mudança está na importação. Trouxemos a biblioteca 
nativa <span class="palavras_reservadas">import </span><span class="texto_python">os</span>. Ela é 
indispensável para lidarmos com caminhos de arquivos e pastas dentro do sistema operacional, seja ele 
Windows, Mac ou Linux.</p>""")
st.html("""<p class="fonte_texto">No nosso método <span class="funcao_python">build</span>
<span class="texto_python">()</span>, nós removemos aquele 
<span class="texto_python">Builder.load_string()</span> antigo e fizemos as coisas do jeito certo. Preste 
muita atenção nesta linha: <span class="texto_python">caminho_kv = os.path.join(os.path.dirname(
__file__), </span><span class="variaveis">'interface.kv'</span>
<span class="texto_python">)</span>. O que essa sopa de letrinhas faz?</p>""")
st.html("""<p class="fonte_texto">O comando <span class="texto_python">__file__</span> pega o caminho 
exato de onde o seu script Python está salvo no computador. O 
<span class="texto_python">os.path.dirname</span> extrai apenas o nome da pasta desse caminho. Por fim, o 
<span class="texto_python">os.path.join</span> junta o endereço dessa pasta com o nome do nosso arquivo 
<span class="variaveis">'interface.kv'</span>.</p>""")
st.html("""<p class="fonte_texto">Por que fazer toda essa volta em vez de só escrever o nome do arquivo? 
Porque isso garante que o Python sempre encontrará o seu arquivo KV, não importa por onde você tente 
rodar o script no terminal! É um código à prova de falhas. Logo abaixo, executamos o 
<span class="texto_python">Builder.load_file(caminho_kv)</span>, e pronto: interface carregada e 
renderizada!</p>""")
st.html("""<p class="fonte_texto">Por fim, criamos o método 
<span class="palavras_reservadas">def </span><span class="funcao_python">acao_botao</span>
<span class="texto_python">(</span><span class="self_python">self</span>
<span class="texto_python">):</span> exatamente abaixo do <span class="funcao_python">build</span>
<span class="texto_python">()</span>. Lembra que o botão lá no KV Lang estava chamando essa função? Pois 
é! Agora, quando você rodar o aplicativo e clicar no botão "EXECUTAR AÇÃO", a tela avisará o Python, que 
rodará esse bloco de código. Por enquanto, nós apenas colocamos um 
<span class="funcoes_python">print</span><span class="texto_python">()</span> para jogar uma mensagem no 
terminal, mas é exatamente aqui que, no futuro, conectaremos bancos de dados, fazer cálculos ou 
enviar informações para servidores! A ponte de comunicação está oficialmente construída!</p>""")
st.divider()

# --- Linkar a interface gráfica com a lógica --- #
st.html('<h1 class="fonte_titulo_aula">Linkar a interface gráfica com a lógica</h1>')
st.html("""<p class="fonte_texto">Até agora, nós vínhamos construindo nossas telas de forma "mista", o que 
é ótimo para aprender, mas nada prático para projetos reais. Imagine ter que lidar com centenas de linhas 
de código onde a definição de um botão se confunde com uma regra de banco de dados! A partir de agora, 
vamos adotar a separação de preocupações. A ideia é simples: o arquivo 
<span class="texto_python">.kv</span> é o artista da equipe, cuidando apenas da aparência, enquanto o 
arquivo <span class="texto_python">.py</span> é o engenheiro, cuidando de toda a lógica e 
processamento.</p>""")
st.html("""<p class="fonte_texto">Essa divisão não é apenas uma questão de estética no seu código; ela 
transforma a sua produtividade. Com a interface isolada em um arquivo próprio, você pode alterar cores,
 mover botões ou ajustar ícones sem correr o risco de quebrar uma função lógica importante. Da mesma 
 forma, você pode atualizar o seu algoritmo de cálculo no Python sem se preocupar em ter que "redesenhar" 
 o layout. Essa é a base de qualquer sistema escalável e profissional. Vamos ver como essa mágica funciona 
 na prática, linkando o seu front-end (KV) ao seu back-end (Python)!</p>""")
st.html("""<p class="fonte_texto">Aqui estão os códigos que dão vida a essa etapa. Vamos colocar tudo no 
seu devido lugar: primeiro a nossa interface visual e, em seguida, o cérebro do nosso aplicativo:</p>""")
st.code('''MDScreen:
    md_bg_color: self.theme_cls.bg_normal

    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: 'Aula 02: Estrutura KV'
            elevation: 4
            pos_hint: {'top': 1}
            md_bg_color: app.theme_cls.primary_color
            specific_text_color: 1, 1, 1, 1

        MDBoxLayout:
            orientation: 'vertical'
            padding: '20dp'
            spacing: '15dp'

            MDLabel:
                id: label_feedback
                text: 'Aguardando interação...'
                halign: 'center'
                font_style: 'H5'
                adaptative_height: True

            MDTextField:
                id: entrada_usuario
                hint_text: 'Qual é o seu nome?'
                helper_text: 'Digite seu nome e clique no botão abaixo'
                helper_text_mode: 'on_focus'
                mode: 'fill'
                icon_left: 'account'
                mode: 'rectangle'

            MDRaisedButton:
                text: 'CONFIRMAR DADOS'
                pos_hint: {'center_x': 0.5}
                # --- PAssar o conteúdo do campo de texto diretamente como argumento --- #
                on_release: app.processar_entrada(entrada_usuario.text)

            MDFillRoundFlatButton:
                text: 'LIMPAR FORMULÁRIO'
                pos_hint: {'center_x': 0.5}
                # --- Lógica simples pode ser escrita diretamente no KV --- #
                on_release:
                    entrada_usuario.text = ''
                    label_feedback.text = 'Campos resetados'
                    label_feedback.theme_text_color: 'Secondary'

            # --- O widget genérico atua como um espaçador flexível --- #
            Widget:''', line_numbers=True, language='kv')
st.html("""<p class="fonte_texto">Vamos esmiuçar as novidades fantásticas do nosso arquivo KV! A grande 
estrela desta etapa é a propriedade <span class="texto_python">id</span>. Pense no 
<span class="texto_python">id</span> como o "nome de batismo" ou o "CPF" de um widget. Quando você tem 
vários botões e textos na tela, como o Python saberá quem é quem na hora de mudar uma cor ou pegar um 
texto? É o <span class="texto_python">id</span> que resolve isso!</p>""")
st.html("""<p class="fonte_texto">No nosso código KV, nós batizamos a nossa label principal como 
<span class="texto_python">id: label_feedback</span> e o nosso campo de texto como 
<span class="texto_python">id: entrada_usuario</span>. Lembre-se desta regra de ouro: os IDs devem ser 
únicos em toda a sua tela.</p>""")
st.html("""<p class="fonte_texto">Além dos IDs, nós incrementamos o visual do nosso 
<span class="texto_python">MDTextField</span>:</p>""")
st.html('<ul class="fonte_texto">'
        '<li><span class="texto_python">helper_text</span>: É um texto de ajuda que fica embaixo da '
        'linha de digitação.</li>'
        '<li><span class="texto_python">helper_text_mode: "on_focus"</span>: Faz com que esse texto de '
        'ajuda só apareça quando o usuário clicar no campo para digitar (quando ele ganhar o "foco").</li>'
        '<li><span class="texto_python">icon_left: "account"</span>: Coloca o ícone clássico de '
        '"bonequinho de usuário" do lado esquerdo do campo.</li>'
        '</ul>')
st.html("""<p class="fonte_texto">Agora, preste muita atenção nos nossos dois botões, porque eles fazem 
coisas bem diferentes:</p>""")
st.html('<ol type=1 class="fonte_texto">'
        '<li>No <span class="texto_python">MDRaisedButton</span> (CONFIRMAR DADOS), nós atualizamos o '
        '<span class=texrto_python">on_release</span> para: '
        '<span class="texto_python">app.processar_entrada(entrada_usuario.text)</span>. Olha a mágica '
        'acontecendo! Nós estamos pegando o <span class="texto_python">id</span> do campo de texto ('
        '<span class="texto_python">entrada_usuario</span>), extraindo o que está escrito nele ('
        '<span class="texto_python">.text</span>) e enviando essa informação empacotada direto para a '
        'função <span class="texto_python">processar_entrada</span> lá no Python!</li>'
        '<li>Já o nosso novo botão <span class="texto_python">MDFillRoundFlatButton</span> '
        '(LIMPAR FORMULÁRIO) tem um truque maravilhoso. O Kivy permite que você escreva lógicas simples '
        'de atribuição diretamente no arquivo KV, sem precisar ir até o Python. No '
        '<span class="texto_python">on_release</span> dele, nós usamos a indentação para passar três '
        'comandos diretos: apagar o texto do campo de entrada ('
        '<span class="texto_python">entrada_usuario.text = ""</span>), mudar a mensagem da label e '
        'devolver a cor dela para <i>Secondary</i>. É o front-end resolvendo os próprios problemas! '
        '<i>Atenção: como aqui é lógica de atribuição, usamos o sinal de igual ('
        '<span class="texto_python">=</span>) em vez de dois pontos ('
        '<span class="texto_python">:</span>).</i></li>'
        '</ol>')
st.html("""<p class="fonte_texto">Agora, virando a chave para o nosso arquivo Python:</p>""")
st.code('''# --- Importar os módulos --- #
import os
from kivymd.app import MDApp
from kivy.lang import Builder


class Aula02App(MDApp):
    def build(self):
        # --- O método build() deve retornar o widget raiz da aplicação --- #
        # --- Configurações globais de tema qie afeta os widgets declarados --- #
        self.theme_cls.primary_palette = 'Teal'
        self.theme_cls.theme_style = 'Light'

        # --- Builder.load_file() carrega o arquivo KV e instancia os objetos --- #
        caminho_kv = os.path.join(os.path.dirname(__file__), 'interface.kv')
        return Builder.load_file(caminho_kv)

    def processar_entrada(self, texto):
        # --- Acessar o widget via seu ID para feedback dinâmico --- #
        if texto.strip():
            self.root.ids.label_feedback.text = f'Bem-vindo, {texto}!'
            self.root.ids.label_feedback.theme_text_color = 'Primary'

        else:
            self.root.ids.label_feedback.text = 'Por favor, digite um nome!'
            self.root.ids.label_feedback.theme_text_color = 'Error'


if __name__ == '__main__':
    Aula02App().run()''', line_numbers=True)
st.html("""<p class="fonte_texto">No nosso método <span class="funcao_python">build</span>
<span class="texto_python">()</span>, antes de carregar o arquivo KV, nós definimos o tema global usando o 
<span class="self_python">self</span>
<span class="texto_python">.theme_cls</span>. Setamos a paleta primária para 
<span class="variaveis">'Teal'</span> (um tom de verde-azulado bem bonito) e forçamos o aplicativo a 
rodar no modo <span class="variaveis">'Light'</span> (claro).</p>""")
st.html("""<p class="fonte_texto">Mas o grande brilho do nosso back-end está no novo método: 
<span class="palavras_reservadas">def </span><span class="funcao_python">processar_entrada</span>
<span class="texto_python">(</span><span class="self_python">self</span>
<span class="texto_python">, texto):</span>. Lembra que o botão lá no KV Lang mandou o texto preenchido? É 
essa variável <span class="texto_python">texto</span> que recebe a informação!</p>""")
st.html("""<p class="fonte_texto">Dentro dessa função, nós criamos a nossa lógica de validação: A função 
<span class="texto_python">.strip()</span> verifica se o usuário realmente digitou algo válido, removendo 
espaços em branco acidentais antes e depois da palavra.</p>""")
st.html('<ul class="fonte_texto">'
        '<li>Se ele digitou algo (o <span class="palavras_reservadas">if</span> for verdadeiro), nós '
        'precisamos alterar o texto de boas-vindas na tela. E como acessamos a tela a partir do Python? '
        'Usando o dicionário mágico <span class="self_python">self</span>'
        '<span class="texto_python">.root.ids</span>. Vamos traduzir esse comando '
        '<span class="self_python">self</span>'
        '<span class="texto_python">.root.ids.label_feedback.text</span>. O '
        '<span class="self_python">self</span> é o nosso app. O <span class="texto_python">root</span> '
        'é o widget raiz da interface (o nosso <span class="texto_python">MDScreen</span>). O '
        '<span class="texto_python">ids</span> é a lista de todos os "CPFs" dos widgets. Aí nós chamamos o '
        '<span class="texto_python">label_feedback</span> pelo nome e alteramos a propriedade '
        '<span class="texto_python">.text</span> dele usando uma f-string do Python. Na linha de baixo, '
        'fazemos o mesmo caminho para alterar a cor do texto para '
        '<span class="variaveis">"Primary"</span>.</li>'
        '<li>Caso contrário (o <span class="palavras_reservadas">else</span> indicando que o usuário '
        'enviou o campo vazio), usamos o mesmo caminho do <span class="self_python">self</span>'
        '<span class="texto_python">.root.ids</span> para dar uma bronca no usuário e mudamos a cor do '
        'texto para <span class="variaveis">"Error"</span>, que fará a '
        'mensagem ficar em vermelho (cor padrão de erro no Material Design).</li>'
        '</ul>')
st.html("""<p class="fonte_texto">Execute o aplicativo e brinque com ele! Digite seu nome, confirme, 
apague tudo no botão de limpar, tente confirmar vazio para ver o erro em vermelho. Você acaba de criar 
a ponte definitiva de comunicação entre o Python e o KV Lang!</p>""")
st.divider()

# --- Criar um aplicativo mais completo --- #
st.html('<h1 class="fonte_titulo_aula">Criar um aplicativo mais completo</h1>')
st.html("""<p class="fonte_texto">Para fechar a nossa aula com chave de ouro, vamos transformar aquele 
nosso formulário básico em uma tela de "Registro de Desenvolvedor" completa, bonita e super funcional. 
Aqui, juntaremos tudo o que aprendemos e adicionar algumas cerejas no bolo, como ícones na barra 
superior, botões lado a lado e um painel de status (Card) digno de um aplicativo profissional!</p>""")
st.html("""<p class="fonte_texto">Aqui estão os códigos finais. Vamos primeiro à nossa interface visual e, 
em seguida, ao nosso cérebro lógico:</p>""")
st.code('''MDScreen:
    md_bg_color: self.theme_cls.bg_normal

    MDBoxLayout:
        orientation: 'vertical'

        # --- Cabeçalho profissional --- #
        MDTopAppBar:
            title: 'Aula 02: Estrutura KV'
            elevation: 4
            pos_hint: {'top': 1}
            md_bg_color: app.theme_cls.primary_color
            specific_text_color: 1, 1, 1, 1
            right_action_items: [['dots-vertical', lambda x: print('Menu aberto')]]

        # --- Container principal com padding para respeitar a hierarquia visual --- #
        MDBoxLayout:
            orientation: 'vertical'
            padding: '24dp'
            spacing: '15dp'

            MDLabel:
                text: 'Registro de Desenvolvedor'
                halign: 'left'
                font_style: 'H6'
                theme_text_color: 'Primary'
                adaptative_height: True

            MDLabel:
                text: 'Preencha os dados para validar sua integração KV-Python.'
                halign: 'left'
                font_style: 'Body2'
                theme_text_color: 'Secondary'
                adaptative_height: True

            # --- Campos de entrada de dados --- #
            MDTextField:
                id: input_nome
                hint_text: 'Nome completo'
                icon_left: 'account-edit'
                mode: 'rectangle'

            MDTextField:
                id: input_projeto
                hint_text: 'Nome do projeto'
                icon_left: 'folder-star'
                mode: 'rectangle'

            # --- Layout horizontal para botões de ação --- #
            MDBoxLayout:
                orientation: 'horizontal'
                spacing: '10dp'
                adaptative_height: True

                MDRaisedButton:
                    text: 'VALIDAR'
                    icon: 'check-circle'
                    pos_hint: {'center_x': 0.5}
                    # --- Passar o conteúdo do campo de texto diretamente como argumento --- #
                    on_release: app.validar_registro(input_nome.text, input_projeto.text)

                MDFlatButton:
                    text: 'REINICIAR'
                    on_release: app.reiniciar_campos()

            # --- Superfície de feedback usando MDCard --- #
            MDCard:
                size_hint: (1, None)
                height: '140dp'
                padding: '20dp'
                elevation: 2
                radius: [15, ]
                md_bg_color: app.theme_cls.primary_light if app.theme_cls.theme_style == 'Light' else [0.2, 0.2, 0.2, 1]

                MDBoxLayout:
                    orientation: 'vertical'
                    spacing: '5dp'

                    MDLabel:
                        text: 'STATUS DO SISTEMA'
                        font_style: 'Caption'
                        theme_text_color: 'Hint'

                    MDLabel:
                        id: feedback_final
                        text: 'Aguardadndo submissão de dados pelo usuário.'
                        halign: 'center'
                        font_style: 'Subtitle1'
                        theme_text_color: 'Secondary'

            # --- O widget genérico atua como um espaçador flexível --- #
            Widget:''', line_numbers=True, language='kv')
st.html("""<p class="fonte_texto">Olha o tamanho dessa evolução! Vamos começar destrinchando as novidades 
maravilhosas que colocamos no nosso arquivo <span class="texto_python">.kv</span>:</p>""")
st.html('<ol type=1 class="fonte_texto">'
        '<li><b>TopAppBar com Menu:</b> Na nossa barra superior, adicionamos a propriedade '
        '<span class="texto_python">right_action_items</span>. Essa lista nos permite colocar ícones '
        'clicáveis no canto direito da barra! Passamos o ícone '
        '<span class="texto_python">"dots-vertical"</span> (aqueles três pontinhos clássicos de '
        'menu) e atrelamos a ele uma pequena função anônima ('
        '<span class="texto_python">lambda x: print(...)</span>) só para registrar o clique. Nas '
        'próximas aulas, usaremos isso para abrir menus reais!</li>'
        '<li><b>Dois Campos de Entrada:</b> Evoluímos o nosso formulário adicionando dois '
        '<span class="texto_python">MDTextField</span> distintos, cada um com o seu próprio '
        '<span class="texto_python">id</span> (<span class="texto_python">input_nome</span> e '
        '<span class="texto_python">input_projeto</span>) e seus respectivos ícones ('
        '<span class="texto_python">account-edit</span> e '
        '<span class="texto_python">folder-star</span>).</li>'
        '<li><b>Botões Lado a Lado (Layout Horizontal):</b> Lembra que o '
        '<span class="texto_python">MDBoxLayout</span> empilhava tudo de cima para baixo? A grande sacada '
        'aqui foi criar um <i>novo</i> <span class="texto_python">MDBoxLayout</span> no meio da tela, '
        'mas dessa vez com <span class="texto_python">orientation: "horizontal"</span>. Tudo o que '
        'colocarmos dentro dele ficará um do lado do outro. É por isso que os botões "VALIDAR" e '
        '"REINICIAR" agora dividem o mesmo espaço de forma super elegante!</li>'
        '<li><b>O Poderoso MDCard:</b> Para dar aquele visual profissional de painel de informações ('
        'status do sistema), nós não usamos uma Label flutuando no vazio, usamos um '
        '<span class="texto_python">MDCard</span>! O Card é um widget que funciona como um "cartão" '
        'em relevo.</li>'
        '<ul class="fonte_texto">'
        '<li><span class="texto_python">size_hint: (1, None)</span>: Ele ocupa 100% da largura ('
        '<span class="texto_python">1</span>), mas a '
        'altura (<span class="texto_python">None</span>) será fixa.</li>'
        '<li><span class="texto_python">height: "140dp"</span>: Definimos a altura fixa dele em '
        '140 pixels.</li>'
        '<li><span class="texto_python">radius: [15, ]</span>: Arredondamos as bordas dele.</li>'
        '<li><span class="texto_python">md_bg_color</span>: Aqui fizemos uma brincadeira lógica genial no '
        'KV! Falamos para ele pintar o fundo com uma cor clarinha ('
        '<span class="texto_python">primary_light</span>) SE o tema for claro. Caso contrário ('
        '<span class="texto_python">else</span>), ele pinta de cinza escuro.</li>'
        '</ul>'
        '</ol>')
st.html("""<p class="fonte_texto">Agora, vamos entender as mudanças lógicas lá no nosso arquivo 
Python:</p>""")
st.code('''# --- Importar os módulos --- #
import os
from kivymd.app import MDApp
from kivy.lang import Builder


class Aula02App(MDApp):
    def build(self):
        # --- O método build() deve retornar o widget raiz da aplicação --- #
        # --- Configurações globais de tema qie afeta os widgets declarados --- #
        self.theme_cls.primary_palette = 'Indigo'
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.accent_palette = 'Amber'

        # --- Builder.load_file() carrega o arquivo KV e instancia os objetos --- #
        caminho_kv = os.path.join(os.path.dirname(__file__), 'interface.kv')
        return Builder.load_file(caminho_kv)

    def validar_registro(self, nome, projeto):
        """Lógica de negócios que interage com a interface declarativa via IDs."""
        if nome.strip() and projeto.strip():
            # --- Acesso direto aos widgets do KV através do dicionário self.root.ids --- #
            self.root.ids.feedback_final.text = f'Sucesso! Projeto {projeto} registrado para {nome}.'
            self.root.ids.feedback_final.theme_text_color = 'Primary'
            print(f'Log: Registro validado para {nome} em {projeto}')
        else:
            self.root.ids.feedback_final.text = 'Erro: Preencha todos os campos obrigatórios!'
            self.root.ids.feedback_final.theme_text_color = 'Error'

    def reiniciar_campos(self):
        """Reseta o estado da interface para os valores padrão."""
        self.root.ids.input_nome.text = ''
        self.root.ids.input_projeto.text = ''
        self.root.ids.feedback_final.text = 'Formulário reiniciado. Aguardando novos dados.'
        self.root.ids.feedback_final.theme_text_color = 'Secondary'


if __name__ == '__main__':
    Aula02App().run()''', line_numbers=True)
st.html("""<p class="fonte_texto">No nosso 
<span class="texto_python">build</span>, nós apenas setamos a nossa paleta primária para 
<span class="variaveis">'Indigo'</span> e adicionamos uma cor de destaque com o 
<span class="texto_python">accent_palette = </span><span class="variaveis">'Amber'</span>.</p>""")
st.html("""<p class="fonte_texto">O coração do aplicativo agora bate no método 
<span class="texto_python">validar_registro</span>. Veja que agora ele recebe dois argumentos: 
<span class="texto_python">nome</span> e <span class="texto_python">projeto</span>. Lá no arquivo KV, o 
botão VALIDAR chamou essa função enviando os textos dos dois campos simultaneamente. Dentro do método, nós 
atualizamos o nosso validador para <span class="palavras_reservadas">if </span>
<span class="texto_python">nome.strip() </span><span class="palavras_reservadas">and </span>
<span class="texto_python">projeto.strip():</span>. Isso garante que o usuário não seja espertinho e tente 
enviar o formulário preenchendo só um dos campos. Se tudo estiver preenchido, nós usamos o nosso 
queridinho dicionário <span class="self_python">self</span>
<span class="texto_python">.root.ids</span> para buscar o 
<span class="texto_python">id: feedback_final</span> (que está lá dentro do 
<span class="texto_python">MDCard</span>) e atualizar o texto dele com uma mensagem de sucesso, alterando 
a cor para a primária. Se faltar algum dado, ele cai no 
<span class="palavras_reservadas">else</span> e avisa sobre o erro.</p>""")
st.html("""<p class="fonte_texto">Por fim, nós extraímos a lógica de limpar o formulário que antes estava 
misturada no arquivo KV e criamos um método novinho em folha no Python: o 
<span class="funcao_python">reiniciar_campos</span><span class="texto_python">(</span>
<span class="self_python">self</span><span class="texto_python">)</span>. É uma prática muito mais 
profissional! Ao clicar em "REINICIAR", o botão chama essa função no Python, e ela faz o trabalho de 
buscar os campos pelos seus IDs, redefinir os textos para uma string vazia (
<span class="variaveis">''</span>) e voltar a mensagem do painel de status para o estado original.</p>""")
st.html("""<p class="fonte_texto">Com isso, o nosso aplicativo não é mais apenas uma tela bonitinha; é um 
sistema robusto, que valida dados, lida com erros, reseta estados e tem um design sensacional!</p>""")
st.divider()

# --- Resumo --- #
st.html('<h1 class="fonte_titulo_aula">Resumo</h1>')
st.html("""<p class="fonte_texto">Nesta segunda aula, demos um salto definitivo rumo ao desenvolvimento 
profissional com KivyMD ao aprendermos a separar a interface visual (front-end) da nossa lógica de 
programação (back-end). Conhecemos a poderosa <b>Linguagem KV (KV Lang)</b>, que nos permite desenhar 
telas de forma limpa e declarativa usando apenas indentação e propriedades. Começamos criando a interface 
dentro de uma string no Python e, logo em seguida, evoluímos para a arquitetura ideal: um arquivo 
<span class="texto_python">.kv</span> dedicado e independente, carregado no nosso script principal 
através do módulo <span class="texto_python">Builder</span> de forma segura.</p>""")
st.html("""<p class="fonte_texto">No lado visual, exploramos a fundo como organizar os elementos na tela 
usando os layouts, com destaque para o <span class="texto_python">MDBoxLayout</span>, que nos permitiu 
empilhar componentes verticalmente ou alinhá-los lado a lado de forma horizontal. Construímos uma 
interface digna de aplicativos reais, implementando uma barra de navegação superior (
<span class="texto_python">MDTopAppBar</span>), campos de texto interativos com ícones e dicas (
<span class="texto_python">MDTextField</span>), e um elegante painel flutuante de status utilizando o 
<span class="texto_python">MDCard</span>.</p>""")
st.html("""<p class="fonte_texto">Por fim, a grande mágica da aula foi estabelecer a ponte de comunicação 
entre esses dois mundos separados através da propriedade <span class="texto_python">id</span>. Ao 
batizarmos os nossos componentes no arquivo KV, conseguimos capturar cliques de botões (
<span class="texto_python">on_release</span>) e enviar informações preenchidas diretamente para as 
funções no Python. Do lado lógico, dominamos o uso do dicionário 
<span class="self_python">self</span><span class="texto_python">.root.ids</span> para processar os dados 
recebidos, criar regras de validação e devolver respostas dinâmicas em tempo real para a interface, 
alterando textos e cores de erro ou sucesso. Temos em mãos, agora, uma estrutura robusta, organizada e 
totalmente pronta para projetos do mundo real!</p>""")
st.divider()

# --- Conclusão --- #
st.html('<h1 class="fonte_titulo_aula">Conclusão</h1>')
st.html("""<p class="fonte_texto">E assim finalizamos a nossa segunda aula com um salto gigantesco na sua 
jornada como desenvolvedor mobile! Se na primeira aula nós construímos a fundação, hoje nós aprendemos a 
organizar a casa como verdadeiros profissionais. A transição de um código misturado para uma arquitetura 
limpa (separando o design no arquivo <span class="texto_python">.kv</span> e a inteligência no arquivo 
<span class="texto_python">.py</span>) é o grande divisor de águas entre um script amador e um aplicativo 
robusto e escalável. Essa separação de responsabilidades é a exata mentalidade exigida no mercado de 
tecnologia e te poupará muitas dores de cabeça no futuro.</p>""")
st.html("""<p class="fonte_texto">Olhe para trás e veja o nível do projeto que você acabou de construir: 
não é mais apenas uma tela preta com um texto solto. Nós desenhamos um formulário interativo completo, com 
barras de navegação elegantes, campos de texto organizados em layouts inteligentes e um painel de status 
em formato de card que reage em tempo real. E o mais impressionante: você dominou a arte de fazer o 
front-end e o back-end conversarem perfeitamente através dos 
<span class="texto_python">ids</span> e do <span class="self_python">self</span>
<span class="texto_python">.root.ids</span>. Agora você sabe exatamente como capturar o clique do 
usuário na tela e transformar isso em ações lógicas dentro do Python!</p>""")
st.html("""<p class="fonte_texto">O meu conselho de ouro para você agora é: não deixe esse código apenas 
salvo em uma pasta. Quebre-o, modifique-o e brinque com ele! Tente adicionar novos campos de texto, mude 
as cores do <span class="texto_python">MDCard</span> para outras situações ou crie botões adicionais com 
funções diferentes. O domínio da linguagem KV vem com a prática constante e a experimentação. Nós já 
temos a base visual e lógica perfeitamente integradas e prontas para escalar.</p>""")
st.subheader('No mais é isso, nos vemos na próxima aula! Até lá, fiquem com Deus e fui!')