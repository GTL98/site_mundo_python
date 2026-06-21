# --- Importar as bibliotecas --- #
from PIL import Image
import streamlit as st
from carregar_css import carregar_css

# --- Configurações iniciais da página --- #
st.set_page_config(
    page_title='PySide6 Maestria - Aula 01',
    page_icon=Image.open('./assets/logo/logo.png'),
    layout='wide'
)

# --- Carregar o CSS --- #
carregar_css()

# --- Colocar o título da aula --- #
st.html('<h1 class="fonte_titulo_aula">Aula 01: Ciclo de Vida da QApplication!</h1>')

# --- Vídeo --- #
with st.expander('Se quiser acompanhar com o vídeo, acesse aqui! 👇'):
    st.video('https://youtu.be/OYWPGnhuULc')

# --- Código da aula --- #
st.subheader('Se quiser acessar o código completo da aula, clique [aqui](https://github.com/GTL98/canal_mundo_python/blob/main/Maestria%20em%20PySide6%3A%20O%20Guia%20Definitivo/Aula%2001/aula_01.py)')
st.divider()

# --- Introdução --- #
st.subheader('E fala, devs! Tudo bem com vocês? Espero que sim!')
st.html('<h1 class="fonte_titulo_aula">Introdução</h1>')
st.html('''<p class="fonte_texto">Se você já domina o Python no terminal, mas sente que falta aquele 
"tchan" para transformar seus scripts robustos em softwares reais que qualquer pessoa possa usar, você 
está no lugar certo! Estamos dando o pontapé inicial no nosso guia de PySide6, a ferramenta definitiva 
para criar interfaces gráficas (GUIs) incríveis e profissionais. Afinal, de nada adianta ter um código 
super inteligente por trás se o usuário final não tiver uma tela bonita e intuitiva para interagir, não 
é verdade?</p>''')
st.html('''<p class="fonte_texto">E aqui vai a melhor notícia de todas: o PySide6 é totalmente gratuito 
e de uso livre! Ao contrário do PyQt6, que exige o pagamento de uma licença comercial caso você queira 
vender os seus aplicativos, o PySide6 adota uma licença amigável que permite que você monetize suas 
criações sem gastar um tostão. É a oportunidade perfeita para construir um portfólio de respeito e se 
destacar como um desenvolvedor completo. Prepare o seu editor de código, porque hoje entenderemos a 
base absoluta de onde tudo começa!</p>''')
st.subheader('Então sem mais delongas, bora para a aula!')
st.divider()

# --- Iniciando o ciclo de vida: a instância e o sys.argv --- #
st.html('<h1 class="fonte_titulo_aula">Iniciando o ciclo de vida: a instância e o '
        '<span class="texto_python">sys.argv</span></h1>')
st.html('''<p class="fonte_texto">Para que qualquer interface gráfica ganhe vida, existe um "maestro" 
invisível trabalhando intensamente nos bastidores. No universo do PySide6, esse maestro se chama 
<span class="texto_python">QApplication</span>. Ele é o coração do seu programa: é o responsável por 
gerenciar o ciclo de vida completo do aplicativo, lidar com as configurações do sistema operacional e 
preparar o terreno para que as janelas e botões apareçam. Sem ele, o Qt simplesmente não consegue 
renderizar nada na tela.</p>''')
st.html('''<p class="fonte_texto">Mas para esse maestro começar a trabalhar com o pé direito, ele precisa 
entender o ambiente onde está rodando. É aí que entra o 
<span class="texto_python">sys.argv</span>. Esse carinha captura qualquer argumento ou comando que tenha 
sido passado via prompt de comando (terminal) na hora de executar o script. Ao entregar essa lista de 
argumentos para a <span class="texto_python">QApplication</span>, seu aplicativo ganha a capacidade de se 
adaptar automaticamente a configurações nativas do sistema, de forma 100% transparente e sem que você 
precise configurar tudo manualmente.</p>''')
st.html('''<p class="fonte_texto">Veja abaixo a estrutura básica para dar a partida nesse motor:</p>''')
st.code('''# --- Importar as bibliotecas --- #
import sys
from PySide6.QtWidgets import QApplication, QLabel


def aula_01():
    # --- QApplication deve ser a primeira coisa a ser criada --- #
    app = QApplication(sys.argv)

    print('QApplication instanciada com sucesso!')


if __name__ == '__main__':
    aula_01()''', line_numbers=True)
st.html('''<p class="fonte_texto">Agora que temos o código em mãos, vamos dissecar cada linha 
detalhadamente para entender exatamente o que está acontecendo por baixo dos panos.</p>''')
st.html('''<p class="fonte_texto">Primeiro, olhe para as importações. Começamos com o 
<span class="palavras_reservadas">import</span> <span class="texto_python">sys</span>. A biblioteca 
<span class="texto_python">sys</span> é nativa do Python e serve para interagir diretamente com o 
interpretador e com o sistema que está executando o script (ela é diferente da biblioteca 
<span class="texto_python">os</span>, que lida com o sistema operacional em si). Logo abaixo, temos 
<span class="palavras_reservadas">from</span> <span class="texto_python">PySide6.QtWidgets</span> 
<span class="palavras_reservadas">import</span> 
<span class="texto_python">QApplication, QLabel</span>. O módulo 
<span class="texto_python">QtWidgets</span> é como um grande baú de tesouros cheio de componentes visuais. 
Desse baú, estamos extraindo a <span class="texto_python">QApplication</span> (o nosso maestro 
gerenciador) e a <span class="texto_python">QLabel</span> (um componente usado para exibir textos ou 
imagens, que usaremos logo mais).</p>''')
st.html('''<p class="fonte_texto">Entrando na nossa função 
<span class="palavras_reservadas">def</span> <span class="funcao_python">aula_01</span>
<span class="texto_python">():</span>, encontramos a linha mais crucial deste início: 
<span class="texto_python">app = QApplication(sys.argv)</span>. Grave isso na mente: a 
<span class="texto_python">QApplication</span> deve ser, obrigatoriamente, a primeira coisa a ser criada 
no seu código de interface gráfica. Se você tentar criar um botão, uma janela ou qualquer texto antes 
dessa linha, o Python fechará o programa com um erro na sua cara, porque os componentes visuais não 
sabem onde se apoiar sem uma aplicação ativa. Aqui, criamos a variável 
<span class="texto_python">app</span> e guardamos nela a instância do nosso aplicativo, alimentando-a com 
o <span class="texto_python">sys.argv</span>.</p>''')
st.html('''<p class="fonte_texto">Para garantir que tudo correu bem, colocamos um simples 
<span class="funcoes_python">print</span><span class="texto_python">(</span>
<span class="variaveis">'QApplication instanciada com sucesso!'</span><span class="texto_python">)</span>. 
Como ainda não pedimos para nenhuma janela visual aparecer na tela, ao rodar o script você verá apenas 
essa mensagem brilhando no seu terminal. Isso prova que o motor do PySide6 foi ligado com sucesso e está 
pronto para receber as próximas engrenagens!</p>''')
st.html('''<p class="fonte_texto">Por fim, fechamos com a famosa estrutura 
<span class="palavras_reservadas">if </span><span class="texto_python">__name__ == </span>
<span class="variaveis">'__main__'</span><span class="texto_python">:</span>. Essa é uma excelente 
prática no Python. Ela funciona como um segurança de balada, garantindo que a função 
<span class="funcao_python">aula_01</span><span class="texto_python">()</span> só seja executada se você 
estiver rodando este arquivo diretamente. Se por acaso você importasse este arquivo em outro script no 
futuro, o código não sairia executando sozinho sem a sua permissão.</p>''')
st.html('''<p class="fonte_texto">Dando continuidade à nossa jornada, agora que o motor do nosso 
aplicativo já está ligado com a <span class="texto_python">QApplication</span>, chegou a hora de dar a 
ele uma identidade própria e, finalmente, um "corpo" visual! Afinal, um aplicativo invisível e sem nome 
não é exatamente o que queremos entregar para o nosso usuário final, certo?</p>''')
st.html('''<p class="fonte_texto">Nesta etapa, vamos focar em dois pilares fundamentais: a 
profissionalização do seu software através dos metadados e a criação da sua primeiríssima janela na 
tela. É aqui que começamos a transformar linhas de código em algo que você pode realmente ver e 
interagir. Vamos deixar de lado o terminal escuro e trazer nosso programa para a luz!</p>''')
st.divider()

# --- Metadados e identidade da aplicação --- #
st.html('<h1 class="fonte_titulo_aula">Metadados e identidade da aplicação</span></h1>')
st.html('''<p class="fonte_texto">Os metadados são, basicamente, "dados sobre outros dados". No 
contexto do PySide6, eles servem para registrar as informações de registro civil do seu aplicativo. 
Estamos falando do nome do programa, a versão em que ele se encontra e quem foi a mente brilhante (ou a 
empresa) que o desenvolveu. Se você omitir essas informações, o seu programa funcionará 
perfeitamente? Sim, vai. Porém, ao preencher esses dados, você eleva o nível do seu código para um 
padrão profissional. Essas informações são frequentemente utilizadas pelo sistema operacional para 
gerenciar atalhos, salvar configurações de usuário no registro do Windows ou nos arquivos 
<span class="texto_python">.plist</span> do macOS, e facilitar manutenções futuras.</p>''')
st.html('''<p class="fonte_texto">Além de dar um RG para o nosso aplicativo, precisamos dar a ele um 
rosto. No universo do PySide (e do Qt em geral), tudo o que aparece na tela é chamado de 
<b>Widget</b> (janelas, botões, caixas de texto, etc.). Um conceito importantíssimo que você precisa 
dominar desde já é que todo widget nasce invisível por padrão. O framework faz isso de propósito para 
que você possa montar toda a sua tela, adicionar textos e configurar tamanhos nos bastidores da memória, 
e só exibir tudo para o usuário quando a tela estiver 100% pronta.</p>''')
st.html('''<p class="fonte_texto">Veja como isso se traduz no nosso código:</p>''')
st.code('''...(continuação do código)
def aula_01():
    # --- QApplication deve ser a primeira coisa a ser criada --- #
    app = QApplication(sys.argv)

    # --- Configurações dos metadados --- #
    app.setApplicationName('Aula 01')
    app.setApplicationVersion('0.0.1')
    app.setOrganizationName('Mundo Python')
    app.setOrganizationDomain('https://www.youtube.com/@Mundo_Python')

    # --- Criar uma label --- #
    # --- O QLabel é um widget que exibe texto ou imagens --- #
    janela = QLabel('Aplicativo iniciado!')
    janela.setWindowTitle('Status do framework')
    janela.resize(400, 200)

    # --- O método show() é necessário para mostrar os widgets que são invisívels por padrão --- #
    janela.show()

    print(f'A aplicação {app.applicationName()} foi inicializada')
(continuação do código)...''', line_numbers=True)
st.html('''<p class="fonte_texto">Vamos esmiuçar o que foi adicionado! Logo após instanciar a nossa 
<span class="texto_python">QApplication</span>, nós iniciamos a sessão de metadados utilizando os 
métodos da própria variável app.</p>''')
st.html('''<ul class="fonte_texto">
        <li><span class="texto_python">app.setApplicationName(</span>
        <span class="variaveis">'Aula 01'</span><span class="texto_python">)</span>: Define o nome 
        oficial do seu programa.</li>
        <li><span class="texto_python">app.setApplicationVersion(</span>
        <span class="variaveis">'0.0.1'</span><span class="texto_python">)</span>: Define a versão 
        atual. Isso é excelente para rastrear atualizações.</li>
        <li><span class="texto_python">app.setOrganizationName(</span>
        <span class="variaveis">'Mundo Python'</span><span class="texto_python">)</span>: Registra o 
        nome da sua empresa, equipe ou o seu próprio nome.</li>
        <li><span class="texto_python">app.setOrganizationDomain(</span>
        <span class="variaveis">'...'</span><span class="texto_python">)</span>: Geralmente usado para 
        o site de contato ou suporte da organização.</li>
        </ul>''')
st.html('''<p class="fonte_texto">Em seguida, mergulhamos na criação da interface. Para não complicar 
as coisas logo de cara com janelas complexas, utilizamos um 
<span class="texto_python">QLabel</span>. O <span class="texto_python">QLabel</span> é um widget super 
versátil, feito para exibir textos (rótulos) ou até mesmo imagens de forma estática. Quando passamos o 
texto <span class="variaveis">'Aplicativo iniciado!'</span> dentro dos parênteses da classe 
<span class="texto_python">QLabel</span>, já estamos dizendo qual será o conteúdo interno desse widget. 
E para que possamos manipular esse widget mais tarde, nós o salvamos na variável chamada 
<span class="texto_python">janela</span>.</p>''')
st.html('''<p class="fonte_texto">Com a variável <span class="texto_python">janela</span> em mãos, 
podemos usar os métodos herdados dos widgets do PySide6 para moldá-la:</p>''')
st.html('''<ul class="fonte_texto">
        <li><span class="texto_python">janela.setWindowTitle(</span>
        <span class="variaveis">'Status do framework'</span><span class="texto_python">)</span>: Este 
        comando altera aquele texto que fica lá no topo da janela (na barra de título), dando um 
        contexto para o usuário sobre o que é aquela tela.</li>
        <li><span class="texto_python">janela.resize(</span>
        <span class="numeros">400</span><span class="texto_python">, </span>
        <span class="numeros">200</span><span class="texto_python">)</span>: Define o tamanho inicial 
        da sua janela quando ela for aberta, sendo o primeiro valor a largura (400 pixels) e o segundo a 
        altura (200 pixels).</li>
        </ul>''')
st.html('''<p class="fonte_texto">Agora, o pulo do gato: a linha 
<span class="texto_python">janela.show()</span>. Lembra que eu disse que todo widget nasce invisível? Se 
você não colocar o método <span class="texto_python">.show()</span>, o código rodará até o final e 
você não verá absolutamente nada na tela, mesmo tendo configurado tudo perfeitamente. O 
<span class="texto_python">.show()</span> é o comando que pega tudo o que estava na memória e desenha 
no seu monitor!</p>''')
st.html('''<p class="fonte_texto">Para fechar com chave de ouro, modificamos o nosso 
<span class="funcoes_python">print</span><span class="texto_python">()</span> final. Em vez 
de escrever o nome do aplicativo manualmente, usamos o método 
<span class="texto_python">app.applicationName()</span>. Ele resgatará dinamicamente a string 
<span class="variaveis">'Aula 01'</span> que definimos lá nos metadados. Isso é código inteligente: se 
você mudar o nome do aplicativo no topo, o 
<span class="funcoes_python">print</span><span class="texto_python">()</span> se atualiza sozinho!</p>''')
st.html('''<p class="fonte_texto">Um aviso rápido se você rodar o código agora: Você notará que a janela 
apenas "pisca" rapidamente na tela e some. Não se desespere! O código não está com erro. Isso acontece 
porque o interpretador Python leu todas as linhas, abriu a janela no 
<span class="texto_python">.show()</span>, chegou no final do script e encerrou o programa em 
milissegundos. Para manter a janela aberta e interativa, precisamos do poderoso "Loop de Eventos", que 
será exatamente o nosso próximo passo!</p>''')
st.divider()

# --- O loop de eventos: a magia do exec() --- #
st.html('<h1 class="fonte_titulo_aula">O loop de eventos: a magia do '
        '<span class="texto_python">exec()</span></span></h1>')
st.html('''<p class="fonte_texto">Chegamos a um momento crucial da nossa jornada. Lembra que no final da 
última etapa a nossa janela deu apenas uma "piscada" na tela e o programa fechou imediatamente? Isso 
acontece porque o Python, por natureza, lê o script de cima para baixo de forma sequencial. Quando ele 
termina de ler a última linha, o trabalho dele acaba e o programa é encerrado. Mas um aplicativo de 
verdade não funciona assim, não é? Ele precisa ficar aberto, aguardando pacientemente até que você 
clique em um botão, digite um texto ou arraste a janela. É exatamente aqui que entra a verdadeira magia 
das interfaces gráficas: o <b>Loop de Eventos</b>!</p>''')
st.html('''<p class="fonte_texto">O loop de eventos (ou <i>Event Loop</i>) é como um motor contínuo 
rodando nos bastidores. Ele literalmente "estaciona" a execução do seu código em um ponto específico e 
cria um ciclo infinito. Enquanto esse ciclo roda, a sua aplicação fica escutando ativamente tudo o que 
acontece ao redor dela: movimentos do mouse, cliques, redimensionamento de janela e comandos do sistema 
operacional. O programa só voltará a ler o resto do seu código no momento em que você fechar a janela, 
encerrando esse loop. Vamos ver como adicionar esse motorzinho no nosso código:</p>''')
st.code('''...(continuação do código)
def aula_01():
    ...
    # --- O método show() é necessário para mostrar os widgets que são invisívels por padrão --- #
    janela.show()

    # --- O método exec() inica o loop de eventos --- #
    # --- O programa "estaciona" aqui e processa as interações do usuário --- #
    print('Entrando em um loop de enventos...')
    execucao = app.exec()

    # --- Ele retorna um código de saída quando a aplicação é encerrada --- #
    print(f'Aplicação encerrada com código: {execucao}')
(continuação do código)...''', line_numbers=True)
st.html('''<p class="fonte_texto">Vamos entender detalhadamente o que mudou no finalzinho do nosso 
script. Adicionamos o comando <span class="funcoes_python">print</span>
<span class="texto_python">(</span><span class="variaveis">'Entrando em um loop de eventos...'</span>
<span class="texto_python">)</span> apenas para você ver no terminal o exato momento em que o Python 
está prestes a parar a leitura linear.</p>''')
st.html('''<p class="fonte_texto">Logo em seguida, temos a linha de ouro: 
<span class="texto_python">execucao = app.exec()</span>. O método 
<span class="texto_python">.exec()</span> é o comando definitivo que diz para a 
<span class="texto_python">QApplication</span>: "Ok, a janela já está montada e desenhada na tela, agora 
assuma o controle e não deixe o programa fechar!". A partir do momento que o interpretador lê 
<span class="texto_python">.exec()</span>, o seu aplicativo entra no tal estado de "espera ativa". É por 
isso que você agora consegue clicar na janela, arrastá-la pela tela do seu computador, maximizar e 
minimizar, tudo isso rodando perfeitamente!</p>''')
st.html('''<p class="fonte_texto">Um detalhe histórico e muito importante: Você pode encontrar por aí 
códigos mais antigos que usam <span class="texto_python">app.exec_()</span> (com um underline no final). 
Antigamente, na época do Python 2, a palavra <span class="texto_python">exec</span> era uma palavra 
reservada da própria linguagem Python, então os desenvolvedores do Qt tiveram que adicionar esse 
underline para não causar conflitos. Hoje em dia, isso não é mais necessário! O PySide6 ainda aceita o 
<span class="texto_python">exec_()</span> por compatibilidade, mas a recomendação oficial é usar apenas 
<span class="texto_python">exec()</span>, que mantém o padrão limpo e em conformidade com o C++ (a 
linguagem robusta que roda por baixo dos panos desenhando a interface).</p>''')
st.html('''<p class="fonte_texto">Mas preste muita atenção na última linha: 
<span class="funcoes_python">print</span><span class="texto_python">(</span>
<span class="variaveis">f'Aplicação encerrada com código: </span>
<span class="palavras_reservadas">{</span><span class="texto_python">execucao</span>
<span class="palavras_reservadas">}</span><span class="variaveis">'</span>
<span class="texto_python">)</span>. Essa linha não será lida enquanto a sua janela estiver aberta. O 
programa está "estacionado" na linha de cima. Assim que você for lá no 'X' vermelho da janela e fechar o 
aplicativo, o loop de eventos é quebrado. Nesse exato momento, o método 
<span class="texto_python">.exec()</span> retorna um número (o código de saída), que nós guardamos na 
variável <span class="texto_python">execucao</span>, e então o Python continua lendo as linhas 
seguintes.</p>''')
st.html('''<p class="fonte_texto">Se tudo ocorreu perfeitamente e o usuário fechou o programa normalmente, 
o código retornado será 0 (zero). Por isso, ao fechar a janela, você verá no terminal a mensagem 
"Aplicação encerrada com código: 0". Se aparecesse qualquer outro número, seria um indicativo do sistema 
de que o programa "crachou" ou foi forçado a fechar por algum erro bizarro. Mas como estamos fazendo 
tudo nos trinques, o zero é a confirmação do nosso sucesso total!</p>''')
st.divider()

# --- Código completo --- #
st.html('<h1 class="fonte_titulo_aula">Código completo</h1>')
st.html('''<p class="fonte_texto">Chegamos à reta final da nossa primeiríssima aula. Agora que já 
entendemos quem é o "maestro" do nosso programa (a 
<span class="texto_python">QApplication</span>), configuramos a identidade profissional dele com os 
metadados, e descobrimos como a magia do Loop de Eventos (
<span class="texto_python">exec()</span>) mantém tudo rodando, é hora de juntar todas as peças do 
quebra-cabeça. E para fechar com chave de ouro, vamos aplicar um toque extra de controle sobre a nossa 
interface!</p>''')
st.html('''<p class="fonte_texto">Muitas vezes, quando estamos construindo um aplicativo, precisamos 
exibir textos longos ou instruções detalhadas, e uma única linha não dá conta do recado. Além disso, se 
deixarmos a janela totalmente livre, o usuário pode acabar diminuindo tanto o tamanho dela que o 
conteúdo simplesmente some ou fica todo espremido, arruinando a experiência. Para evitar essa bagunça 
visual, o PySide6 nos oferece comandos super simples para quebrar linhas de texto e impor limites 
físicos à nossa janela. Vejamos como o nosso código final fica com esses ajustes refinados:</p>''')
st.code("""# --- Importar as bibliotecas --- #
import sys
from PySide6.QtWidgets import QApplication, QLabel


def aula_01():
    # --- QApplication deve ser a primeira coisa a ser criada --- #
    app = QApplication(sys.argv)

    # --- Configurações dos metadados --- #
    app.setApplicationName('Aula 01')
    app.setApplicationVersion('0.0.1')
    app.setOrganizationName('Mundo Python')
    app.setOrganizationDomain('https://www.youtube.com/@Mundo_Python')

    # --- Criar uma label --- #
    # --- O QLabel é um widget que exibe texto ou imagens --- #
    janela = QLabel('''Aula 01: O ciclo de vida da QApplication.
O framework está ativo e aguardando eventos.''')
    janela.setWindowTitle('Status do framework')
    janela.resize(480, 320)
    janela.setMinimumSize(400, 200)

    # --- O método show() é necessário para mostrar os widgets que são invisívels por padrão --- #
    janela.show()

    # --- O método exec() inica o loop de eventos --- #
    # --- O programa "estaciona" aqui e processa as interações do usuário --- #
    print('Entrando em um loop de enventos...')
    execucao = app.exec()

    # --- Ele retorna um código de saída quando a aplicação é encerrada --- #
    print(f'Aplicação encerrada com código: {execucao}')


if __name__ == '__main__':
    aula_01()""", line_numbers=True)
st.html('''<p class="fonte_texto">Como já viramos especialistas na maior parte dessa estrutura ao longo 
da aula, vamos colocar a lupa apenas nas novidades sensacionais que adicionamos no trecho do 
<span class="texto_python">QLabel</span> e da configuração da 
<span class="texto_python">janela</span>!</p>''')
st.html("""<p class="fonte_texto">Primeiro, olhe bem para o texto dentro do 
<span class="texto_python">QLabel</span>. Em vez de usar aspas simples normais, nós utilizamos três 
aspas simples (<span class="variaveis">'''</span>). No Python, isso nos permite escrever strings 
multilinhas. Graças a isso, conseguimos dar um "Enter" literal no meio do texto no código, e a nossa 
janela reproduzirá exatamente essa quebra de linha visualmente, mostrando as duas frases empilhadas 
de forma muito mais elegante.</p>""")
st.html('''<p class="fonte_texto">Em seguida, fizemos um pequeno ajuste no método 
<span class="texto_python">.resize(</span><span class="numeros">480</span>
<span class="texto_python">, </span><span class="numeros">320</span>
<span class="texto_python">)</span>. Agora, quando o usuário abrir o aplicativo, ele nascerá um 
pouquinho maior e mais espaçoso. Mas a grande estrela desse final é o método 
<span class="texto_python">.setMinimumSize(</span><span class="numeros">400</span>
<span class="texto_python">, </span><span class="numeros">200</span>
<span class="texto_python">)</span>. Com esse comando, nós colocamos uma "trava de segurança" na 
interface. O usuário está livre para puxar as bordas e maximizar o aplicativo para ocupar o monitor 
inteiro, se quiser. Porém, se ele tentar encolher a tela, ela travará exatamente na marca de 400 
pixels de largura por 200 de altura. Ela não diminui mais que isso!</p>''')
st.html('''<p class="fonte_texto"><i>Dica de Ouro</i>: Se você quisesse fazer o oposto e impedir que a 
pessoa aumentasse a janela além de um certo ponto, bastaria usar o método 
<span class="texto_python">.setMaximumSize()</span>.</p>''')
st.divider()

# --- Resumo --- #
st.html('<h1 class="fonte_titulo_aula">Resumo</h1>')
st.html('''<p class="fonte_texto">Nesta nossa primeira aula, mergulhamos nos fundamentos do PySide6, 
uma ferramenta poderosa e de uso livre para a criação de interfaces gráficas em Python. Descobrimos que 
o coração de qualquer software visual é a <span class="texto_python">QApplication</span>. Ela precisa 
ser, obrigatoriamente, a primeira estrutura a ser instanciada no código, recebendo o 
<span class="texto_python">sys.argv</span> para se integrar perfeitamente às configurações do sistema 
operacional. É esse verdadeiro "maestro" que gerencia todo o ciclo de vida e prepara o terreno para o 
seu programa funcionar.</p>''')
st.html('''<p class="fonte_texto">Além de dar vida ao aplicativo, aprendemos a importância de 
profissionalizar o projeto logo de cara, configurando seus metadados (como nome, versão e organização). 
Na parte visual, entendemos que os elementos da tela são chamados de widgets e que eles nascem 
totalmente invisíveis. Utilizando um <span class="texto_python">QLabel</span> como nossa janela 
principal, conseguimos escrever textos multilinhas, manipular o título do cabeçalho, ajustar o tamanho 
inicial, impor limites físicos de redução com o <span class="texto_python">setMinimumSize()</span> e, o 
mais importante, exibir tudo na tela utilizando o método 
<span class="texto_python">show()</span>.</p>''')
st.html('''<p class="fonte_texto">Por fim, desvendamos o segredo que impede a janela de apenas "piscar" 
e fechar imediatamente: o Loop de Eventos! Ao acionar o método 
<span class="texto_python">exec()</span>, o interpretador Python "estaciona" a leitura do código e a 
aplicação entra em um estado de espera ativa, processando em tempo real todas as interações do usuário, 
como redimensionamentos e movimentos pela tela. O script só volta a rodar e finaliza de forma segura 
(retornando o código zero) quando o usuário decide fechar o aplicativo no 'X'. Com essa base sólida, 
você já tem tudo o que precisa para começar a construir projetos muito mais robustos!</p>''')
st.divider()

# --- Conclusão --- #
st.html('<h1 class="fonte_titulo_aula">Conclusão</h1>')
st.html('''<p class="fonte_texto">Chegar ao fim desta primeira aula marca um passo gigante na sua 
jornada como desenvolvedor Python! Você deixou para trás as limitações do terminal e abriu as portas 
para o mundo real dos softwares de desktop. Entender que todo aplicativo visual precisa de um "coração" 
( a <span class="texto_python">QApplication</span>) e de um Loop de Eventos contínuo para se manter vivo 
é a chave mestre para tudo o que vamos construir daqui para frente. Em vez de apenas copiar código, você 
agora compreende a fundação sólida, profissional e à prova de falhas que sustenta qualquer interface 
gráfica criada com o PySide6.</p>''')
st.html('''<p class="fonte_texto">Agora que esse mistério inicial foi quebrado e você domina o ciclo de 
vida da sua janela (desde a instância até o encerramento seguro com o 
<span class="texto_python">exec()</span>), o céu é o limite! Nas próximas aulas, deixaremos o nosso 
humilde <span class="texto_python">QLabel</span> de lado para mergulhar em estruturas mais parrudas, como 
a <span class="texto_python">QMainWindow</span>, adicionando botões interativos, caixas de entrada de 
dados e layouts dinâmicos. A brincadeira está apenas começando, e logo você terá todas as ferramentas 
para tirar suas ideias do papel e construir um portfólio de aplicativos incríveis.</p>''')
st.html('''<p class="fonte_texto">Não se esqueça da regra de ouro: coloque a mão na massa! Pegue o 
código que desenvolvemos hoje, mude as dimensões da janela, brinque com as quebras de linha do texto e 
veja na prática como o framework reage aos seus comandos. A prática constante é o que realmente leva à 
maestria!</p>''')
st.subheader('No mais é isso, nos vemos na próxima aula! Até lá, fiquem com Deus e fui!')