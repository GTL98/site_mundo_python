# --- Importar as bibliotecas --- #
from PIL import Image
import streamlit as st
from carregar_css import carregar_css

# --- Configurações iniciais da página --- #
st.set_page_config(
    page_title='Streamlit Fullstack - Aula 02',
    page_icon=Image.open('./assets/logo/logo.png'),
    layout='wide'
)

# --- Carregar o CSS --- #
carregar_css()

# --- Colocar o título da aula --- #
st.html('<h1 class="fonte_titulo_aula">Aula 02: Layouts Avançados – Colunas, Abas e Popovers!</h1>')

# --- Vídeo --- #
with st.expander('Se quiser acompanhar com o vídeo, acesse aqui! 👇'):
    st.video('https://youtu.be/1ZWgWqLl_b4')

# --- Código da aula --- #
st.subheader('Se quiser acessar o código completo da aula, clique [aqui](https://github.com/GTL98/canal_mundo_python/blob/main/Streamlit%20Full-Stack%3A%20Crie%20Aplica%C3%A7%C3%B5es%20Web%20Completas%20com%20Python/Aula%2002/aula_02.py)')
st.divider()

# --- Introdução --- #
st.subheader('E fala, devs! Tudo bem com vocês? Espero que sim!')
st.html('<h1 class="fonte_titulo_aula">Introdução</h1>')
st.html('''<p class="fonte_texto">Seja muito bem-vindo à nossa segunda aula do curso de Streamlit 
Full-Stack. Se na primeira aula nós já começamos a sujar as mãos com o básico, hoje o nosso objetivo é 
elevar o nível da sua aplicação e transformá-la em um site robusto e profissional. Você já sentiu que, 
conforme adiciona mais gráficos e botões, seu site começa a ficar com uma cara de "planilha gigante" onde 
o usuário precisa rolar a página infinitamente? É exatamente isso que resolveremos agora!</p>''')
st.html('''<p class="fonte_texto">Neste tutorial, mergulharemos fundo nos layouts avançados. Aprenderemos 
a organizar visualmente as informações do seu site de forma estratégica. Uma boa aplicação não 
apenas exibe dados, mas conta uma história visual clara. Organizar bem o espaço garante que o seu 
usuário tenha uma excelente experiência, lendo e interagindo com o seu site de forma intuitiva e 
dinâmica.</p>''')
st.subheader('Então sem mais delongas, bora para a aula!')
st.divider()

# --- Inicialização do site --- #
st.html('<h1 class="fonte_titulo_aula">Inicialização do site</h1>')
st.html('''<p class="fonte_texto">Antes de começarmos a fatiar a nossa tela com colunas e abas, 
precisamos preparar o terreno. Pense no Streamlit como uma grande tela em branco. A primeira coisa que 
um pintor faz é escolher o tamanho do seu quadro e separar as suas tintas. No nosso caso, isso 
significa configurar o comportamento inicial da página da web (dizendo ao navegador como queremos que 
o site ocupe a tela) e gerar um conjunto de dados fictícios (nossas "tintas") que servirá de base 
para todos os gráficos e métricas que vamos construir ao longo da aula. Sem essa base sólida e 
configurada para expansão, nossos layouts complexos ficariam espremidos no meio da tela:</p>''')
st.code("""# --- Importar as bibliotecas --- #
import numpy as np
import pandas as pd
import streamlit as st

# --- Configuração inicial da página para permitir a estruturação espacial completa --- #
st.set_page_config(
    page_title='Aula 02: Layouts',
    layout='wide',
    initial_sidebar_state='expanded'
)

# --- Título da página --- #
st.title('🚀 Aula 02: Estruturação Espacial')
st.markdown('''Nesta aula, construiremos um dashboard modular. O código evoluirá em cada seção,
adicionando camadas de complexidade até termos uma aplicação completa e funcional.''')

# --- Base de dados para utilizarmos nas visualizações --- #
dados = pd.DataFrame(
    np.random.randn(20, 5),
    columns=['Vendas', 'Lucro', 'Meta', 'Custo', 'Retorno']
)""", line_numbers=True)
st.html('''<p class="fonte_texto">Para que o nosso dashboard funcione perfeitamente, o primeiro passo é 
invocar as ferramentas que farão o trabalho pesado por nós. Nas primeiras linhas, fazemos a importação 
das bibliotecas. O <span class="texto_python">streamlit</span> (apelidado carinhosamente de 
<span class="texto_python">st</span>) é o coração do nosso site, responsável por toda a interface web. Já 
o <span class="texto_python">numpy</span> (<span class="texto_python">np</span>) e o 
<span class="texto_python">pandas</span> (<span class="texto_python">pd</span>) são os nossos motores de 
dados. Em um projeto real, você usaria o Pandas para ler um arquivo Excel, CSV ou conectar ao seu banco 
de dados.</p>''')
st.html('''<p class="fonte_texto">Em seguida, entramos em um dos comandos mais cruciais quando se trata 
de design no Streamlit: o <span class="texto_python">st.set_page_config()</span>. Essa função só pode 
ser chamada uma única vez e deve ser o primeiro comando Streamlit do seu script. Veja os parâmetros que 
utilizamos:</p>''')
st.html('''<ul class="fonte_texto">
        <li><span class="texto_python">page_title</span>: Define o nome que vai aparecerá em cima, 
        na aba do seu navegador, ao lado do ícone (favicon). Isso dá um toque super profissional 
        logo de cara.</li>
        <li><span class="texto_python">layout=</span><span class="variaveis">'wide'</span>: Este é o 
        verdadeiro "pulo do gato" desta aula! Por padrão, o Streamlit centraliza tudo em uma coluna 
        estreita no meio da tela. Ao mudar para <span class="variaveis">'wide'</span> (largo), nós 
        mandamos o site se esticar e aproveitar 100% da largura do monitor do usuário. Como criaremos 
        múltiplas colunas e abas mais para frente, precisamos de todo o espaço horizontal disponível 
        para que os gráficos não fiquem espremidos.</li>
        <li><span class="texto_python">initial_sidebar_state=</span>
        <span class="variaveis">'expanded'</span>: Garante que, caso a gente adicione um menu lateral 
        (sidebar) no futuro, ele já carregue aberto por padrão.</li>
        </ul>''')
st.html('''<p class="fonte_texto">Depois de configurar a nossa "tela", começamos a "pintar". Usamos o 
<span class="texto_python">st.title()</span> para colocar o título principal e chamativo da nossa página, 
já incluindo um emoji de foguete para dar aquela animada! Logo abaixo, utilizamos o 
<span class="texto_python">st.markdown()</span>. Essa é uma função incrivelmente versátil que permite 
escrever blocos de texto maiores aceitando formatações Markdown (como negrito, itálico, listas, etc.). 
É uma ótima maneira de dar contexto ao usuário sobre o que ele está visualizando, funcionando como uma 
pequena introdução textual dentro da própria aplicação.</p>''')
st.html('''<p class="fonte_texto">Por fim, criamos a nossa Base de Dados. Como o foco da aula é o 
design visual e a interatividade, não queremos perder tempo conectando bancos de dados complexos agora. 
Então, usamos uma jogada rápida do Numpy (
<span class="texto_python">np.random.randn(</span><span class="numeros">20</span>
<span class="texto_python">, </span><span class="numeros">5</span><span class="texto_python">)</span>) 
para gerar uma matriz de números aleatórios com 20 linhas e 5 colunas. Imediatamente, envelopamos esses 
números em um <span class="texto_python">pd.DataFrame</span>, batizando nossas 5 colunas com nomes de 
métricas de negócios do mundo real: Vendas, Lucro, Meta, Custo e Retorno. A variável dados agora guarda 
essa tabela e será a nossa "massa de modelar" para todos os gráficos, KPIs e tabelas visuais que 
criaremos nos próximos passos!</p>''')
st.divider()

# --- Adição de colunas com st.columns() --- #
st.html('<h1 class="fonte_titulo_aula">Adição de colunas com '
        '<span class="texto_python">st.columns()</span></h1>')
st.html('''<p class="fonte_texto">Agora que o nosso terreno está preparado e a tela esticada, chegou a 
hora da mágica acontecer! Você já notou como a maioria dos scripts básicos em Python empilha as 
informações uma embaixo da outra, criando aquele efeito de "papiro infinito"? Pois é, nós daremos um 
fim nisso agora mesmo. O Streamlit nos permite quebrar essa linearidade e fatiar a nossa tela 
horizontalmente, como se estivéssemos desenhando o grid de uma revista ou o painel de um avião.</p>''')
st.html('''<p class="fonte_texto">É aqui que entra o poder do particionamento espacial. Distribuir o 
conteúdo lado a lado não é apenas uma questão de estética; é uma questão de usabilidade pura! 
Pense nisso: você pode ter os seus KPIs (Indicadores-Chave de Desempenho) mais importantes piscando de 
um lado, um gráfico dinâmico desenhando tendências no meio, e os botões de ação prontos para o clique 
do outro. Tudo isso ao alcance dos olhos do usuário, garantindo uma leitura limpa e sem que ele precise 
dar um único <i>scroll</i> na página!</p>''')
st.html('''<p class="fonte_texto">Para criar essa maravilha horizontal, utilizamos a poderosa função 
<span class="texto_python">st.columns()</span>. A grande sacada dessa ferramenta está na sua 
flexibilidade. Você não é obrigado a ter colunas engessadas do mesmo tamanho. O Streamlit trabalha com 
um sistema incrível de "pesos" ou proporções. Ao passarmos uma lista de valores, estamos dizendo ao 
sistema exatamente o peso que cada coluna deve ter na balança da nossa tela. Isso é perfeito para dar 
um destaque gigantesco ao que realmente importa (como as nossas visualizações de dados), enquanto 
mantemos indicadores e menus de configuração organizados discretamente nos cantos.</p>''')
st.html('''<p class="fonte_texto">Além de fatiar a tela, nós temos o controle fino sobre o design dessas 
fatias. Podemos espaçá-las, alinhá-las verticalmente para que os elementos não fiquem "dançando" (um 
mais alto, outro mais baixo) e até emoldurá-las com bordas, criando contêineres visuais muito bem 
definidos. E para colocar o conteúdo lá dentro? Usamos a sintaxe mágica do 
<span class="palavras_reservadas">with</span> no Python, que funciona como um "portal": tudo o que for 
codificado dentro daquele bloco parará automaticamente dentro da coluna que escolhemos:</p>''')
st.code('''...(continuação do código)
st.header('O poder das colunas a alinhamento vertical')

# --- Criar colunas com pesos/tamanhos diferentes --- #
colunas = st.columns(
    spec=[1, 3, 1],
    gap='medium',  # controla o espaçamento entre as colunas
    vertical_alignment='center',  # garante que os widgets fiquem visualmente equilibrados
    border=True  # adiciona borda às colunas
)

# --- Adicionar as informações nas colunas --- #
with colunas[0]:
    st.subheader('Indicadores')
    st.metric(
        label='Vendas totais',
        value='R$ 1.250,00',
        delta='12%'
    )
    st.metric(
        label='Lucro líquido',
        value='R$ 450,00',
        delta='-3%'
    )
with colunas[1]:
    st.subheader('Análise visual')
    st.line_chart(dados)
with colunas[2]:
    st.subheader('Ações')
    st.button('Atualizar dados', key='atualizar_dados', use_container_width=True)
    st.button('Exportar PDF', key='exportar_pdf', use_container_width=True)
    st.checkbox('Habilitar modo noturno', key='modo_noturno')
st.divider()''', line_numbers=True)
st.html('''<p class="fonte_texto">Começamos o bloco com o 
<span class="texto_python">st.header()</span>, que cria um cabeçalho de nível 2 para separar 
visualmente esta nova seção do nosso site.</p>''')
st.html('''<p class="fonte_texto">Logo em seguida, invocamos o maestro desta aula: a função 
<span class="texto_python">st.columns()</span>. Nós armazenamos o resultado dessa função na variável 
<span class="texto_python">colunas</span>. É fundamental entender que essa função não retorna apenas uma 
coluna, mas sim uma lista de colunas, que nós acessaremos através de seus índices (
<span class="numeros">0</span>, <span class="numeros">1</span> e <span class="numeros">2</span>). Olha 
só os parâmetros avançados que utilizamos para deixá-las com cara de sistema corporativo:</p>''')
st.html('''<ul class="fonte_texto">
        <li><span class="texto_python">spec=[</span><span class="numeros">1</span>
        <span class="texto_python">, </span><span class="numeros">3</span>
        <span class="texto_python">, </span><span class="numeros">1</span>
        <span class="texto_python">]</span>: Este é o coração do nosso layout. Estamos pedindo três 
        colunas. O número <span class="numeros">3</span> no meio significa que a segunda coluna será 
        três vezes mais larga que a primeira e a terceira. A coluna do meio será o palco principal do 
        nosso gráfico.</li>
        <li><span class="texto_python">gap=</span><span class="variaveis">'medium'</span>: Define que 
        queremos um espaço médio entre as colunas, para que elas não fiquem coladas umas nas outras, 
        garantindo um visual limpo e de fácil leitura.</li>
        <li><span class="texto_python">vertical_alignment=</span>
        <span class="variaveis">'center'</span>: Se uma coluna tiver muito texto e a outra tiver apenas 
        um botão pequeno, esse botão poderia ficar flutuando lá no topo. Com esse comando, garantimos 
        que todos os elementos, independente do tamanho, fiquem perfeitamente centralizados 
        verticalmente. Fica muito mais harmônico.</li>
        <li><span class="texto_python">border=</span><span class="palavras_reservadas">True</span>: 
        Desenha uma caixinha sutil ao redor de cada coluna, separando visualmente os agrupamentos de 
        informações.</li>
        </ul>''')
st.html('''<p class="fonte_texto">Com as colunas criadas na memória, é hora de preenchê-las. Para isso, 
abrimos o contexto de cada uma usando o <span class="palavras_reservadas">with</span>:</p>''')
st.html('''<p class="fonte_texto"><b>1. A Primeira Coluna (</b>
<span class="palavras_reservadas">with </span><span class="texto_python">colunas[</span>
<span class="numeros">0</span><span class="texto_python">]</span><b>)</b>:
Aqui é a casa dos nossos indicadores rápidos! Adicionamos um subtítulo e usamos o incrível widget 
<span class="texto_python">st.metric()</span>. Ele cria aqueles famosos "cartões de KPI" (<i>Key 
Performance Indicator</i>). Passamos o <span class="texto_python">label</span> (o título da métrica), o 
<span class="texto_python">value</span> (o número principal) e o <span class="texto_python">delta</span>
 (a variação percentual). O mais legal do delta é que o Streamlit é inteligente: se você passa um número 
 positivo (<span class="variaveis">'12%'</span>), ele pinta de verde com uma setinha para cima; se passa 
 negativo (<span class="variaveis">'-3%'</span>), ele pinta de vermelho com a setinha para baixo, tudo 
 automaticamente.</p>''')
st.html('''<p class="fonte_texto"><b>2. A Segunda Coluna (</b>
<span class="palavras_reservadas">with </span><span class="texto_python">colunas[</span>
<span class="numeros">1</span><span class="texto_python">]</span><b>)</b>:
Lembra que demos peso 3 para ela? É porque ela precisa de espaço! Aqui nós colocamos o nosso subtítulo e 
chamamos o <span class="texto_python">st.line_chart(dados)</span>. Lembra daquele DataFrame cheio de 
números aleatórios que criamos na etapa anterior? Ele entra aqui. O Streamlit pega todas aquelas colunas 
(Vendas, Lucro, Meta...) e instantaneamente plota um gráfico de linhas interativo deslumbrante, que 
ocupa toda a largura generosa desta coluna central.</p>''')
st.html('''<p class="fonte_texto"><b>3. A Terceira Coluna (</b>
<span class="palavras_reservadas">with </span><span class="texto_python">colunas[</span>
<span class="numeros">2</span><span class="texto_python">]</span><b>)</b>:
Este é o nosso painel de controle lateral. Aqui colocamos botões de ação com 
<span class="texto_python">st.button()</span>. Note dois detalhes vitais aqui:</p>''')
st.html('''<ul class="fonte_texto">
        <li>O parâmetro <span class="texto_python">key</span>: Ao criar vários botões, é importantíssimo 
        dar um "nome de identidade" único (<span class="texto_python">key</span>) para cada um, evitando 
        que o Streamlit se confunda internamente.</li>
        <li>O parâmetro <span class="texto_python">use_container_width=</span>
        <span class="palavras_reservadas">True</span>: Por padrão, o botão tem apenas o tamanho do texto 
        dele. Ao ativarmos isso, o botão se estica e preenche toda a largura da coluna, deixando o 
        layout com aquele aspecto de menu profissional e padronizado. Fechamos essa coluna adicionando 
        um <span class="texto_python">st.checkbox()</span> simples para simular uma opção de configuração, 
        como um modo noturno.</li>
        </ul>''')
st.html('''<p class="fonte_texto">Por fim, usamos o <span class="texto_python">st.divider()</span>. Ele 
desenha uma linha horizontal suave na tela, indicando visualmente para o usuário que aquela seção acabou 
e um novo assunto vai começar no site.</p>''')
st.divider()

# --- Blocos horizontais com st.container() --- #
st.html('<h1 class="fonte_titulo_aula">Blocos horizontais com '
        '<span class="texto_python">st.container()</span></h1>')
st.html('''<p class="fonte_texto">Já dominamos as colunas e vimos como fatiar a tela verticalmente, mas 
e quando precisamos agrupar pequenos elementos de forma rápida, como em um menu de opções, ou destacar 
um bloco inteiro de texto? É aqui que os contêineres entram em cena para elevar ainda mais o design da 
nossa aplicação.</p>''')
st.html('''<p class="fonte_texto">Pense no <span class="texto_python">st.container()</span> como uma 
daquelas caixas organizadoras que você tem no seu escritório. Você guarda ferramentas relacionadas lá 
dentro e, de repente, tudo fica mais limpo e lógico. A grande revolução nas versões mais recentes do 
Streamlit é que os contêineres ganharam superpoderes de layout. Antes, eles apenas empilhavam itens de 
cima para baixo. Agora, eles conseguem organizar tudo lado a lado automaticamente! Isso significa que 
podemos criar "barras de ferramentas" (toolbars) dinâmicas, como as que vemos em aplicativos modernos, 
sem precisar fazer malabarismos matemáticos criando dezenas de colunas fininhas.</p>''')
st.html('''<p class="fonte_texto">Além disso, temos o controle absoluto do tamanho dessa "caixa". Podemos 
dizer para ela "abraçar" os itens, ocupando apenas o espaço estritamente necessário (ideal para menus 
compactos), ou mandar ela se esticar por toda a tela (perfeito para destacar blocos de leitura ou avisos 
importantes). Vejamos como isso se traduz no nosso painel:</p>''')
st.code('''...(continuação do código)
st.header('Containers dinâmicos e layout horizontal')

# --- Criar um container que se comporta como uma barra de ferramentas --- #
st.write('Configurações da seção:')
barra_ferramenta = st.container(
    horizontal=True,  # alinha os elementos internamente em linha
    border=True,
    width='content',  # o container ocupa apenas o espaço necessário
    horizontal_alignment='left'
)

# --- Colocar o container --- #
with barra_ferramenta:
    st.toggle('Filtrar finais de semana', key='filtro_fim_semana')
    st.toggle('Mostrar médias', key='mostrar_medias')
    st.segmented_control(
        label='Escala',
        options=['Diário', 'Semanal', 'Mensal'],
        default='Diário'
    )

# --- Container para exibição de status, utilizando a largura total padrão (stretch) --- #
with st.container(border=True):
    st.info('Esse container demosntra como o conteúdo adapta-se à largura total disponível.')
    st.write('Este bloco pode conter qualquer tipo de widget, como tabelas ou textos longos.')
st.divider()''', line_numbers=True)
st.html('''<p class="fonte_texto">Começamos com o nosso clássico 
<span class="texto_python">st.header()</span> para abrir a nova seção do site. Em seguida, damos uma 
instrução visual simples usando <span class="texto_python">st.write(</span>
<span class="variaveis">'Configurações da seção:'</span><span class="texto_python">)</span> para que o 
usuário saiba do que se trata aquele bloco.</p>''')
st.html('''<p class="fonte_sub_subtitulo_aula"><b>1. A Barra de Ferramentas Compacta:</b></p>''')
st.html('''<p class="fonte_texto">Aqui nós criamos e salvamos o nosso contêiner na variável 
<span class="texto_python">barra_ferramenta</span>. Olha só a genialidade dos parâmetros que usamos dentro do 
<span class="texto_python">st.container()</span>:</p>''')
st.html('''<ul class="fonte_texto">
        <li><span class="texto_python">horizontal=</span>
        <span class="palavras_reservadas">True</span>: Esse é o passe de mágica! Em vez de empilhar os 
        botões um embaixo do outro, o Streamlit vai colocá-los lado a lado, formando uma linha 
        contínua.</li>
        <li><span class="texto_python">border=</span><span class="palavras_reservadas">True</span>: 
        Assim como nas colunas, criamos uma moldura visível em torno do nosso menu.</li>
        <li><span class="texto_python">width=</span><span class="variaveis">'content'</span>: Este 
        parâmetro é super importante. Ele diz ao contêiner: "Não ocupe a tela toda! Cresça apenas o 
        suficiente para abrigar o que está dentro de você". O contêiner fica "apertadinho" em volta 
        dos botões.</li>
        <li><span class="texto_python">horizontal_alignment=</span><span class="variaveis">'left'</span>: 
        Garante que os nossos botões comecem a ser alinhados sempre a partir da esquerda do contêiner.</li>
        </ul>''')
st.html('''<p class="fonte_texto">Em seguida, abrimos o contexto com 
<span class="palavras_reservadas">with</span> <span class="texto_python">barra_ferramenta:</span> e 
jogamos nossos widgets lá dentro. Inserimos dois <span class="texto_python">st.toggle()</span>. O 
<i>toggle</i> é aquele interruptor clássico de celular que você desliza para ativar ou desativar algo 
(passamos as chaves <span class="texto_python">key</span> únicas para eles, claro). Para fechar o menu, 
usamos o elegantíssimo <span class="texto_python">st.segmented_control()</span>. Ele é uma alternativa 
moderna aos antigos <i>radio buttons</i>. Passamos uma lista de opções (
<span class="texto_python">[</span><span class="variaveis">'Diário'</span>
<span class="texto_python">, </span><span class="variaveis">'Semanal'</span>
<span class="texto_python">, </span><span class="variaveis">'Mensal'</span>
<span class="texto_python">]</span>) e definimos que ele já deve iniciar com a opção 
<span class="variaveis">'Diário'</span> selecionada. O resultado é um menu de seleção horizontal e super 
intuitivo.</p>''')
st.html('''<p class="fonte_sub_subtitulo_aula"><b>2. O Contêiner de Largura Total (Stretch):</b></p>''')
st.html('''<p class="fonte_texto">Na segunda parte do código, mostramos o comportamento oposto. Em vez de 
salvar o contêiner em uma variável, nós o instanciamos diretamente com o comando 
<span class="texto_python">with </span><span class="texto_python">st.container(border=</span>
<span class="palavras_reservadas">True</span><span class="texto_python">):</span>.</p>''')
st.html('''<p class="fonte_texto">Como não passamos o parâmetro <span class="texto_python">width</span>, 
o Streamlit assume o comportamento padrão, que é se esticar até os limites da tela (ou da coluna onde ele 
estiver inserido). Isso é o que chamamos de <i>stretch</i>. Dentro dessa caixa espaçosa, utilizamos o widget 
<span class="texto_python">st.info()</span>, que cria uma barra colorida e destacada (geralmente azul), 
perfeita para chamar a atenção do usuário para uma mensagem de status ou um aviso 
do sistema. Embaixo do aviso, um <span class="texto_python">st.write()</span> comum para simular onde 
entraríamos com um texto mais longo.</p>''')
st.html('''<p class="fonte_texto">Viu a diferença? No primeiro bloco, criamos um menu enxuto e compacto. 
No segundo, criamos um quadro de avisos expansivo. Tudo isso apenas manipulando as propriedades dos 
contêineres.</p>''')
st.divider()

# --- Criar abas com st.tabs() --- #
st.html('<h1 class="fonte_titulo_aula">Criar abas com '
        '<span class="texto_python">st.tabs()</span></h1>')
st.html('''<p class="fonte_texto">Preparado para dominar mais um nível de maestria no Streamlit? Nós já 
aprendemos a fatiar a nossa tela usando colunas e a agrupar botões em contêineres horizontais. Mas e 
quando o seu projeto cresce tanto que, mesmo organizando tudo lado a lado, a tela continua lotada de 
informações? É nessa hora que a gente saca da manga um dos recursos mais elegantes para o design de 
interfaces: as abas (ou <i>tabs</i>).</p>''')
st.html('''<p class="fonte_texto">Em vez de obrigar o seu usuário a navegar por múltiplas páginas 
diferentes (o que exige tempo de carregamento e tira o foco), nós podemos empilhar várias telas virtuais 
em um único lugar. Com as abas, você cria "camadas" de informação na mesma página. O usuário pode olhar os 
gráficos em uma aba, pular para a tabela de dados brutos na aba seguinte e, logo depois, ajustar os 
parâmetros do sistema em uma aba de configurações. Tudo isso a um clique de distância, garantindo uma 
navegação fluida, intuitiva e super profissional.</p>''')
st.html('''<p class="fonte_texto">Mas a grande estrela desta seção não é apenas a estética, e sim a 
performance. Pense comigo: se você tem 10 abas lotadas de gráficos pesados e consultas a bancos de dados, 
carregar tudo isso de uma vez ao abrir o site faria o seu servidor "chorar", consumindo muita memória e 
CPU desnecessariamente. A sacada de mestre que vamos implementar aqui é a renderização condicional. Nós 
ensinaremos o Streamlit a ser preguiçoso do jeito certo: ele só processará e desenhará os gráficos da 
aba que o usuário estiver olhando naquele exato momento. O que está escondido nas outras abas, não 
consome recurso! Tri legal né, guria? Bora ver como isso funciona no código:</p>''')
st.code('''...(continuação do código)
st.header('Profundidade de iterface com abas reativas')

# --- Criar abas que rastreiam seu estado através de uma chave (key) --- #
abas = st.tabs(
    tabs=['Visualização', 'Dados brutos', 'Configurações'],
    on_change='rerun',  # habilita a propriedade .open em cada aba
    key='navegacao_principal'
)

# --- Adicionar informações às abas --- #
with abas[0]:
    # --- A propriedade .open permite executar lógica condicional de alta performance --- #
    if abas[0].open:
        st.write('Renderizando visualização complexas sob demanda...')
        colunas = st.columns(2, gap='large')
        with colunas[0]:
            st.bar_chart(dados['Vendas'])
        with colunas[1]:
            st.area_chart(dados['Lucro'])
with abas[1]:
    if abas[1].open:
        st.write('Exibindo dados brutos da operação:')
        st.dataframe(dados.style.highlight_max(axis=0), width='stretch')
with abas[2]:
    if abas[2].open:
        st.write('Paínel de controle do administrador')
        st.slider('Ajustar limite de alerta', 0, 100, 50)
st.divider()''', line_numbers=True)
st.html('''<p class="fonte_texto">Usamos a função <span class="texto_python">st.tabs()</span> e a 
armazenamos na variável <span class="texto_python">abas</span> (que, assim como nas colunas, se tornará 
uma lista com o índice de cada aba). Vamos analisar os parâmetros vitais que passamos aqui:</p>''')
st.html('''<ul class="fonte_texto">
        <li><span class="texto_python">tabs=[</span><span class="variaveis">'Visualização'</span>
        <span class="texto_python">, </span><span class="variaveis">'Dados brutos'</span>
        <span class="texto_python">, </span><span class="variaveis">'Configurações'</span>
        <span class="texto_python">]</span>: Aqui passamos uma lista com os nomes exatos que aparecerão 
        escritos em cada aba no topo da tela. Teremos três abas no total.</li>
        <li><span class="texto_python">key=</span>
        <span class="variaveis">'navegacao_principal'</span>: Damos um nome de identificação único para 
        esse conjunto de abas no sistema.</li>
        <li><span class="texto_python">on_change=</span>
        <span class="variaveis">'rerun'</span>: Este é o truque de ouro da aula! Ao adicionar esse 
        parâmetro, estamos dizendo ao Streamlit: "Toda vez que o usuário trocar de aba, recarregue a 
        página rapidamente". Mas por que queremos isso? Porque é exatamente esse comando que "acorda" a 
        propriedade especial <span class="texto_python">.open</span> que usaremos logo abaixo para salvar 
        memória.</li>
        </ul>''')
st.html('''<p class="fonte_texto">Com as abas criadas na memória, usamos a estrutura 
<span class="palavras_reservadas">with </span><span class="texto_python">abas[indice]:</span> para 
entrar no universo de cada uma delas.</p>''')
st.html('''<p class="fonte_sub_subtitulo_aula"><b>1. A Primeira Aba (
<span class="palavras_reservadas">with </span><span class="texto_python">abas[</span>
<span class="numeros">0</span><span class="texto_python">]:</span>) - Visualização</b></p>''')
st.html('''<p class="fonte_texto">Logo de cara, colocamos a nossa trava de segurança de performance: o 
<span class="palavras_reservadas">if </span><span class="texto_python">abas[</span>
<span class="numeros">0</span><span class="texto_python">].open:</span>. Esse 
<span class="palavras_reservadas">if</span> verifica se esta aba está sendo vista pelo usuário no momento. 
Se não estiver, o Python ignora completamente todo o código que está dentro dela! Se ela estiver aberta, 
imprimimos um texto com <span class="texto_python">st.write()</span> e, em seguida, criamos duas colunas 
com <span class="texto_python">st.columns(</span><span class="numeros">2</span>
<span class="texto_python">, gap=</span><span class="variaveis">'large'</span>
<span class="texto_python">)</span> para fatiar o espaço dessa aba. Na primeira coluna, jogamos um 
gráfico de barras focando apenas nas vendas (<span class="texto_python">st.bar_chart(dados[</span>
<span class="variaveis">'Vendas'</span><span class="texto_python">])</span>). Na segunda, um gráfico de 
área focado no lucro (<span class="texto_python">st.area_chart(dados[</span>
<span class="variaveis">'Lucro'</span><span class="texto_python">])</span>).</p>''')
st.html('''<p class="fonte_sub_subtitulo_aula"><b>2. A Segunda Aba (
<span class="palavras_reservadas">with </span><span class="texto_python">abas[</span>
<span class="numeros">1</span><span class="texto_python">]:</span>) - Dados Brutos</b></p>''')
st.html('''<p class="fonte_texto">Novamente, protegemos o bloco com 
<span class="palavras_reservadas">if </span><span class="texto_python">abas[</span>
<span class="numeros">1</span><span class="texto_python">].open:</span>. O objetivo desta aba é mostrar a 
nossa tabela original, sem gráficos. Usamos o <span class="texto_python">st.dataframe()</span> 
para exibir os dados, mas com um toque especial do Pandas: 
<span class="texto_python">dados.style.highlight_max(axis=</span><span class="numeros">0</span>
<span class="texto_python">)</span>. Esse comandinho mágico vai percorrer cada coluna (
<span class="texto_python">axis=</span><span class="numeros">0</span>) da nossa tabela e pintar de 
amarelo (ou destacar) a célula que contiver o maior valor! É um detalhe visual incrível que poupa o 
usuário de ficar caçando o maior número na tabela. E para garantir que a tabela fique bonita e espaçosa, 
usamos o parâmetro <span class="texto_python">width=</span><span class="variaveis">'stretch'</span> 
para que ela ocupe toda a largura disponível da aba.</p>''')
st.html('''<p class="fonte_sub_subtitulo_aula"><b>3. A Terceira Aba (
<span class="palavras_reservadas">with </span><span class="texto_python">abas[</span>
<span class="numeros">2</span><span class="texto_python">]:</span>) - Configurações</b></p>''')
st.html('''<p class="fonte_texto">Mais uma vez, a verificação mágica 
<span class="palavras_reservadas">if </span><span class="texto_python">abas[</span>
<span class="numeros">2</span><span class="texto_python">].open:</span> está lá. Aqui, simulamos um 
painel de administrador bem simples inserindo um <span class="texto_python">st.slider()</span>. O 
slider é aquele botão deslizante clássico de ajustar volume. Passamos os parâmetros: o texto explicativo (
<span class="variaveis">'Ajustar limite de alerta'</span>), o valor mínimo (
<span class="numeros">0</span>), o valor máximo (<span class="numeros">100</span>) e o valor onde a 
"bolinha" deve começar por padrão (<span class="numeros">50</span>).</p>''')
st.html('''<p class="fonte_texto">Resumindo: Você acabou de criar uma estrutura de navegação robusta, 
limpa, cheia de recursos visuais e, o mais importante, otimizada para não travar o computador de 
ninguém!</p>''')
st.divider()

# --- Informações úteis com st.popover() e st.expander() --- #
st.html('<h1 class="fonte_titulo_aula">Informações úteis com '
        '<span class="texto_python">st.popover()</span> e '
        '<span class="texto_python">st.expander()</span></h1>')
st.html('''<p class="fonte_texto">E chegamos à cereja do bolo! Nosso painel já conta com colunas 
elegantes, contêineres horizontais organizados e abas de alta performance. Mas me diz uma coisa: e quando 
você precisa adicionar aquele monte de opções de filtros avançados, notas técnicas de auditoria ou um 
glossário inteiro no seu app? Se você jogar todas essas informações de uma vez na tela principal, todo 
aquele layout limpo que construímos vai por água abaixo e o usuário ficará sobrecarregado. A solução de 
ouro no design de interfaces para esse problema se chama revelação progressiva: nós escondemos os 
detalhes secundários e só os mostramos quando o usuário realmente precisar ver!</p>''')
st.html('''<p class="fonte_texto">Para fazer essa mágica de "esconde-esconde" funcionar, o Streamlit 
nos entrega dois widgets fantásticos: o <span class="texto_python">st.popover</span> e o 
<span class="texto_python">st.expander</span>. A diferença visual e de comportamento entre eles é 
simples, mas crucial. O Popover é um botão que abre um painel flutuante por cima do seu site; ele não 
empurra os outros elementos, não quebra o layout e é perfeito para guardar menus de configuração e 
filtros de dados. Já o <b>Expander</b> (expansor) funciona como uma gaveta sanfonada; ao clicar nele, ele 
expande, empurrando o resto do conteúdo para baixo para revelar o que está guardado lá dentro (ideal 
para textos longos e explicações embutidas). E, para deixar a nossa aula com chave de ouro, vamos 
aprender a disparar uma notificação pop-up na tela inteira com o <span class="texto_python">st.toast</span>, 
uma referência claríssima àquela clássica aparição do "Toasty!".</p>''')
st.code('''...(continuação do código)
st.header('Revelação progressiva e popovers')

# --- Criar um popover para filtros avançados que não precisam ocupar espaço fixo --- #
# --- O popover flutua sobre o conteúdo, ideal para menus de configuração --- #
with st.popover('🔍 Filtros avançados e explicações', icon='🛠️'):
    st.write('Use os campos abaixo para refinar sua análise:')
    st.date_input('Filtrar por período', value=None)
    st.multiselect('Selecionar regiões', options=['Norte', 'Sul', 'Leste', 'Oeste'])

    # --- Podemos aninhar em estruturas simples para organização interna --- #
    with st.expander('Ver glossário de termos'):
        st.caption('Vendas: Velor bruto faturado no período.')
        st.caption('Lucro: Valor líquido após deduções operacionais.')

# --- Exemplo de st.expander() que reage à abertura --- #
def abrir_detalhes():
    st.toast('Você está visualizando os detalhes técnicos', icon='👀')

with st.expander('📄 Detalhes da auditoria (clique para ver)', on_change=abrir_detalhes):
    st.write(f'Timestamp da última atualização: {pd.Timestamp.now()}')''', line_numbers=True)
st.html('''<p class="fonte_sub_subtitulo_aula"><b>1. O Painel Flutuante (Popover)</b></p>''')
st.html('''<p class="fonte_texto">Aqui nós chamamos o contexto com 
<span class="palavras_reservadas">with </span><span class="texto_python">st.popover()</span>. Passamos 
o texto que ficará escrito no botão e aproveitamos o parâmetro icon para colocar um emoji de ferramentas 
bem bacana. Tudo o que estiver dentro deste bloco <span class="palavras_variaveis">with</span> ficará 
invisível até o usuário clicar no botão. Lá dentro, usamos um 
<span class="texto_python">st.write()</span> para dar uma instrução e adicionamos dois widgets 
clássicos de formulário:</p>''')
st.html('''<ul class="fonte_texto">
        <li>O <span class="texto_python">st.date_input()</span>: Abre um calendário interativo para o usuário 
        escolher datas. Passamos <span class="texto_python">value=</span>
        <span class="palavras_reservadas">None</span> para que ele venha em branco por padrão.</li>
        <li>O <span class="texto_python">st.multiselect()</span>: Uma caixa de seleção super flexível que 
        permite ao usuário escolher várias regiões ao mesmo tempo (como Norte e Sul) dentre as opções que 
        passamos na lista <span class="texto_python">options</span>.</li>
        </ul>''')
st.html('''<p class="fonte_sub_subtitulo_aula">2. Aninhamento: Um Expander dentro do Popover</p>''')
st.html('''<p class="fonte_texto">O Streamlit é tão poderoso que permite colocar um bloco dentro do outro! 
Ainda dentro do nosso Popover, abrimos um 
<span class="palavras_reservadas">with </span><span class="texto_python">st.expander(</span>
<span class="variaveis">'Ver glossário de termos'</span>
<span class="texto_python">):</span>. Isso cria uma "gavetinha" dentro do menu flutuante. Dentro desse 
expander, usamos a função <span class="texto_python">st.caption()</span>. Essa função é maravilhosa 
porque ela escreve o texto em uma fonte menor e mais discreta, perfeita para notas de rodapé ou, neste 
caso, explicações curtas sobre o que significa "Vendas" e "Lucro".</p>''')
st.html('''<p class="fonte_sub_subtitulo_aula"><b>3. O Expander Interativo e o Efeito "Toast"</b></p>''')
st.html('''<p class="fonte_texto">Agora, saindo do nosso Popover (de volta à tela principal), nós vamos 
criar um Expander que é "reativo". Primeiro, definimos uma função chamada 
<span class="funcao_python">abrir_detalhes</span><span class="texto_python">()</span>. O único trabalho 
dessa função é chamar o <span class="texto_python">st.toast()</span>, passando uma mensagem e um ícone 
de "olhinhos". O <span class="texto_python">toast</span> é aquela notificação estilosa e temporária que 
surge flutuando no canto da tela.</p>''')
st.html('''<p class="fonte_texto">A grande jogada está na hora de criar o Expander final: 
<span class="palavras_reservadas">with </span><span class="texto_python">st.expander(..., on_change=
abrir_detalhes):</span>. Preste muita atenção no parâmetro <span class="texto_python">on_change</span>. 
Nós passamos o nome da função <span class="texto_python">abrir_detalhes</span> <b>SEM os parênteses no 
final</b>. Se você colocar os parênteses (ex: 
<span class="funcao_python">abrir_detalhes</span><span class="texto_python">()</span>), o código vai 
disparar a notificação na mesma hora em que o site carregar. Passando sem os parênteses, estamos dizendo 
ao Streamlit: "Guarde essa função na memória e só a execute no exato momento em que o usuário 
interagir/clicar neste Expander".</p>''')
st.html('''<p class="fonte_texto">Por fim, dentro do Expander, usamos um pequeno truque com 
<i>f-strings</i> do Python misturado com a biblioteca Pandas: 
<span class="texto_python">pd.Timestamp.now()</span>. Isso garante que, toda vez que o painel for 
atualizado, ele exiba a data e a hora exatas em que a execução ocorreu.</p>''')
st.divider()

# --- Código final --- #
st.html('<h1 class="fonte_titulo_aula">Código final</h1>')
st.html('''<p class="fonte_texto">Se você acompanhou a aula até aqui, parabéns! Você não apenas escreveu 
código, mas entendeu a arquitetura visual por trás de um dashboard profissional. Nós pegamos uma tela em 
branco e a transformamos em uma aplicação dinâmica, onde cada informação tem o seu lugar certo:</p>''')
st.code("""# --- Importar as bibliotecas --- #
import numpy as np
import pandas as pd
import streamlit as st

# --- Configuração inicial da página para permitir a estruturação espacial completa --- #
st.set_page_config(
    page_title='Aula 02: Layouts',
    layout='wide'
)

# --- Título da página --- #
st.title('🚀 Aula 02: Estruturação Espacial')
st.markdown('''Nesta aula, contruiremos um dashboard moduloar. O código evuluirá em cada seção,
adicionando camadas de complexidade até termos uma aplicação **completa** e *funcional*.''')

# --- Base de dados para utilizarmos nas visualizações --- #
dados = pd.DataFrame(
    np.random.randn(20, 5),
    columns=['Vendas', 'Lucro', 'Meta', 'Custo', 'Retorno']
)

st.header('O poder das colunas e alinhamento vertical')

# --- Criar colunas com pesos/tamanhos diferentes --- #
colunas = st.columns(
    spec=[1, 3, 1],
    gap='medium',  # controla o espaçemento entre as colunas
    vertical_alignment='center',  # garante que os widgets fiquem visualmente equilibrados
    border=True  # adicionar borda às colunas
)

# --- Adicionar as informações nas colunas --- #
with colunas[0]:
    st.subheader('Indicadores')
    st.metric(
        label='Vendas totais',
        value='R$ 1.250,00',
        delta='12%'
    )
    st.metric(
        label='Lucro líquido',
        value='R$ 450,00',
        delta='-3%'
    )
with colunas[1]:
    st.subheader('Análise visual')
    st.line_chart(dados)
with colunas[2]:
    st.subheader('Ações')
    st.button('Atualizar dados', key='atualizar_dados', use_container_width=True)
    st.button('Exportar PDF', key='exportar_pdf', use_container_width=True)
    st.checkbox('Habilitar modo noturno', key='modo_norturno')
st.divider()

st.header('Containers dinâmicos e layout horizontal')

# --- Criar um container que se comporta como uma barra de ferramentas --- #
st.write('Configurações da seção:')
barra_ferramentas = st.container(
    horizontal=True,  # alinha os elementos internamente em linha
    border=True,
    width='content',  # o container ocupa apenas o espaço necessário
    horizontal_alignment='left'
)

# --- Colocar o container --- #
with barra_ferramentas:
    st.toggle('Filtrar finais de semana', key='filtro_fim_semana')
    st.toggle('Mostrar médias', key='mostrar_medias')
    st.segmented_control(
        label='Escala',
        options=['Diário', 'Semanal', 'Mensal'],
        default='Diário'
    )

# --- Container para exibição de status, utilizando a largura total padrão (stretch) --- #
with st.container(border=True):
    st.info('Esse container demonstra como o conteúdo adapta-se à largura total disponível.')
    st.write('Este bloco pode conter qualquer tipo de widget, como tabelas ou textos longos.')
st.divider()

st.header('Profundidade de interface com abas reativas')

# --- Criar abas que rastreiam seu estado através de uma chave (key) --- #
abas = st.tabs(
    tabs=['Visualização', 'Dados brutos', 'Configurações'],
    on_change='rerun',  # habilita a propriedade .open em cada aba
    key='navegacao_principal'
)

# --- Adicionar informações às abas --- #
with abas[0]:
    # --- A propriedade .open permite executar a lógica condicional de alta performance --- #
    if abas[0].open:
        st.write('Renderizando visualização complexa sob demanda...')
        colunas = st.columns(2, gap='large')
        with colunas[0]:
            st.bar_chart(dados['Vendas'])
        with colunas[1]:
            st.area_chart(dados['Lucro'])
with abas[1]:
    if abas[1].open:
        st.write('Exibindo dados brutos da operação:')
        st.dataframe(dados.style.highlight_max(axis=0), width='stretch')
with abas[2]:
    if abas[2].open:
        st.write('Painel de controle do administrador')
        st.slider('Ajustar limite de alerta', 0, 100, 50)
st.divider()

st.header('Revelação progressiva e popovers')

# --- Criar um popover para filtros avançados que não precisam ocupar espaço fixo --- #
# --- O popover fluta sobre o conteúdo, ideal para menus de configuração --- #
with st.popover('🔍 Filtros avançados e explicações', icon='🛠️'):
    st.write('Use os campos abaixo para refinar sua análise:')
    st.date_input('Filtrar por período', value=None)
    st.multiselect('Selecionar regiões', options=['Norte', 'Sul', 'Leste', 'Oeste'])

    # --- Podemos aninhar em estruturas simples para organização interna --- #
    with st.expander('Ver glossário de termos:'):
        st.caption('Vendas: Valor bruto faturado no período.')
        st.caption('Lucro: Valor líquido após deduções operacionais.')

# --- Exemplo de st.expander() que reage à abertura --- #
def abrir_detalhes():
    st.toast('Você está visualizando os detalhes técnicos', icon='👀')

with st.expander('📄 Detalhes da auditoria (clique para ver)', on_change=abrir_detalhes):
    st.write(f'Timestamp da última atualização: {pd.Timestamp.now()}')""", line_numbers=True)
st.divider()

# --- Resumo --- #
st.html('<h1 class="fonte_titulo_aula">Resumo</h1>')
st.html('''<p class="fonte_texto">Resumindo a nossa jornada nesta segunda aula de Streamlit Full-Stack, 
o grande foco foi transformar uma aplicação linear e espremida em um dashboard robusto e organizado 
espacialmente. Começamos expandindo a nossa "tela de pintura" com a configuração inicial de layout amplo 
(<span class="texto_python">layout=</span><span class="variaveis">'wide'</span>) e aprendemos a fatiar o 
espaço utilizando o <span class="texto_python">st.columns</span>, o que nos permite alinhar gráficos, 
métricas e botões lado a lado com proporções personalizadas. Em seguida, dominamos os contêineres 
dinâmicos com o <span class="texto_python">st.container</span> configurado horizontalmente, criando 
barras de ferramentas enxutas e painéis de status que otimizam o espaço sem poluir a visão do 
usuário.</p>''')
st.html('''<p class="fonte_texto">Para levar o projeto ao nível profissional, aplicamos conceitos 
avançados de UI/UX focados em performance e limpeza visual. Com o 
<span class="texto_python">st.tabs</span>, criamos camadas de navegação na mesma página e utilizamos a 
genial propriedade <span class="texto_python">.open</span> para garantir que o sistema processe apenas 
os dados e gráficos da aba ativa no momento, poupando muita memória e processamento da máquina.</p>''')
st.html('''<p class="fonte_texto">Por fim, implementamos a técnica de "revelação progressiva" escondendo 
filtros avançados e glossários dentro de menus flutuantes (<span class="texto_python">st.popover</span>) 
e gavetas expansíveis (<span class="texto_python">st.expander</span>). Isso garante um layout principal 
super limpo e direto ao ponto, mas mantendo todas as ferramentas de controle a um clique de distância, 
com direito até a uma notificação pop-up na tela usando o divertido <span class="texto_python">st.toast</span>. 
Com essa estruturação feita puramente em Python, seu site ganha uma cara totalmente nova e pronta para o 
mercado!</p>''')
st.divider()

# --- Conclusão --- #
st.html('<h1 class="fonte_titulo_aula">Conclusão</h1>')
st.html('''<p class="fonte_texto">Para encerrar essa nossa segunda aula, é fundamental reconhecer o 
gigantesco salto de qualidade que a sua aplicação deu hoje. Deixamos para trás a ideia de que um script 
em Python precisa ser apenas uma sequência vertical e infinita de informações. Ao dominar colunas, 
contêineres, abas reativas e elementos de revelação progressiva como popovers e expanders, você agora 
tem nas mãos o poder de criar verdadeiros dashboards corporativos. E o mais impressionante: você está 
aplicando conceitos reais de design e experiência do usuário (UI/UX) focados em performance, tudo isso 
sem precisar escrever uma única linha de HTML ou CSS.</p>''')
st.html('''<p class="fonte_texto">O próximo passo agora é colocar a mão na massa! Pegue todo esse código 
final que construímos juntos e faça dele o seu laboratório. Tente substituir a nossa base de dados 
fictícia gerada pelo Numpy por uma planilha real de algum projeto ou análise que você já tenha. Brinque 
com os pesos das colunas, crie novas abas temáticas e experimente organizar os seus próprios filtros 
dentro dos menus flutuantes. Lembre-se de que a melhor forma de fixar a programação é quebrando o código, 
entendendo o erro e consertando de novo. É essa organização espacial estratégica que vai destacar o seu 
portfólio no mercado.</p>''')
st.subheader('No mais é isso, nos vemos na próxima aula! Até lá, fiquem com Deus e fui!')