# --- Importar as bibliotecas --- #
from PIL import Image
import streamlit as st

# --- Configurações iniciais da página --- #
st.set_page_config(
    page_title='Capítulo 04 - Trabalhando com listas',
    page_icon=Image.open('./assets/logo/logo.png'),
    layout='wide'
)

# --- Carregar o estilo das fontes --- #
with open('./assets/css/style.css', 'r') as css:
    st.html(f'<style>{css.read()}</style>')

# --- Colocar o banner do capítulo --- #
st.image('./assets/imagens/curso_intensivo_python/aula_04/aula_04.png')

# --- Introdução --- #
st.html('<h1 class="fonte_titulo_aula">Introdução</h1>')
st.html('<p class="fonte_texto">No <a href="https://mundopython.streamlit.app/aula_03_curso_intensivo_'
        'python">Capítulo 3</a>, você aprendeu a fazer uma lista simples e a trabalhar com os elementos '
        'individuais em uma lista. Neste capítulo, você aprenderá a fazer um loop por uma lista inteira '
        'usando apenas algumas linhas de código, independentemente do tamanho da lista. O loop permite '
        'que você execute a mesma ação, ou conjunto de ações, com cada item em uma lista. Como resultado, '
        'você poderá trabalhar eficientemente com listas de qualquer tamanho, incluindo aquelas com '
        'milhares ou até milhões de itens.</p>')

# --- Percorrendo uma lista inteira --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Percorrendo uma lista inteira</h1>')
st.html('<p class="fonte_texto">Muitas vezes você vai querer percorrer todas as entradas em uma lista, '
        'realizando a mesma tarefa com cada item. Por exemplo, em um jogo, você pode querer mover todos '
        'os elementos na tela na mesma quantidade. Em uma lista de números, você pode querer realizar a '
        'mesma operação estatística em todos os elementos. Ou talvez você queira exibir cada título de uma '
        'lista de artigos em um site. Quando você quiser fazer a mesma ação com cada item em uma lista, '
        'você pode usar o loop <b>for</b> do Python.</p>')
st.html('<p class="fonte_texto">Digamos que temos uma lista de nomes de mágicos e queremos imprimir cada '
        'nome na lista. Poderíamos fazer isso recuperando cada nome da lista individualmente, mas essa '
        'abordagem poderia causar vários problemas. Por um lado, seria repetitivo fazer isso com uma '
        'longa lista de nomes. Além disso, teríamos que alterar nosso código cada vez que o comprimento '
        'da lista mudasse. Usar um loop <b>for</b> evita esses dois problemas, permitindo que o Python os '
        'gerencie internamente. Vamos usar um loop <b>for</b> para imprimir cada nome em uma lista de '
        'mágicos:</p>')
st.code('''magicos = ['felipe', 'criss', 'houdini']
for magico in magicos:
    print(magico)''', line_numbers=True)
st.html('<p class="fonte_texto">Começamos definindo uma lista, assim como fizemos no <a '
        'href="https://mundopython.streamlit.app/aula_03_curso_intensivo_python">Capítulo 3</a>. '
        'Então definimos um loop <b>for</b>. Esta linha diz ao Python para extrair um nome da lista '
        '<i>magicos</i> e associá-lo à variável magico. Em seguida, dizemos ao Python para imprimir o '
        'nome que acabou de ser atribuído a magico. O Python então repete essas duas últimas linhas, '
        'uma para cada nome na lista. Pode ajudar ler este código como "Para cada mágico na lista de '
        'mágicos, imprima o nome do mágico". A saída é uma impressão simples de cada nome na lista.</p>')
st.html('<h2 class="fonte_subtitulo_aula">Um olhar mais atento ao looping</h2>')
st.html('<p class="fonte_texto">O loop é importante porque é uma das formas mais comuns de um computador '
        'automatizar tarefas repetitivas. Por exemplo, em um loop simples como o que fizemos, o Python '
        'inicialmente lê a primeira linha do loop:</p>')
st.code('for magico in magicos', line_numbers=True)
st.html('<p class="fonte_texto">Esta linha diz ao Python para recuperar o primeiro valor da lista '
        '<i>magicos</i> e '
        'associá-lo à variável <i>magico</i>. Este primeiro valor é "felipe". O Python então lê a próxima '
        'linha:</p>')
st.code('print(magico)', line_numbers=True)
st.html('<p class="fonte_texto">Python imprime o valor atual de <i>magico</i>, que ainda é "felipe". '
        'Como a lista '
        'contém mais valores, Python retorna para a primeira linha do loop:</p>')
st.code('for magico in magicos', line_numbers=True)
st.html('<p class="fonte_texto">Python recupera o próximo nome na lista, "criss", e associa esse valor à '
        'variável <i>magico</i>. Python então executa a linha:</p>')
st.code('print(magico)', line_numbers=True)
st.html('<p class="fonte_texto">Python imprime o valor atual de <i>magico</i> novamente, que agora é '
        '"criss". Python repete o loop inteiro mais uma vez com o último valor na lista, "houdini". '
        'Como não há mais valores na lista, Python passa para a próxima linha no programa. Neste caso, '
        'nada vem depois do loop for, então o programa termina.</p>')
st.html('<p class="fonte_texto">Quando estiver usando loops pela primeira vez, tenha em mente que o conjunto '
        'de etapas é repetido uma vez para cada item na lista, não importa quantos itens estejam na lista. '
        'Se você tiver um milhão de itens na sua lista, o Python repete essas etapas um milhão de vezes, '
        'e geralmente muito rapidamente.</p>')
st.html('<p class="fonte_texto">Também tenha em mente, ao escrever seus próprios loops <b>for</b>, que '
        'você pode escolher qualquer nome que quiser para a variável temporária que será associada a '
        'cada valor na lista. No entanto, é útil escolher um nome significativo que represente um único '
        'item da lista. Por exemplo, aqui está uma boa maneira de iniciar um loop for para uma lista de '
        'gatos, uma lista de cães e uma lista geral de itens:</p>')
st.code('''for gato in gatos:
for cachorro in cachorros:
for item in lista_de_itens:''', line_numbers=True)
st.html('<h2 class="fonte_subtitulo_aula">Fazendo mais trabalho dentro de um loop <b>for</b></h2>')
st.html('<p class="fonte_texto">Essas convenções de nomenclatura podem ajudar você a seguir a ação sendo '
        'feita em cada item dentro de um loop <b>for</b>. Usar nomes singulares e plurais pode ajudar '
        'você a identificar se uma seção de código está trabalhando com um único elemento da lista ou com '
        'a lista inteira.</p>')
st.html('<p class="fonte_texto">Você pode fazer praticamente qualquer coisa com cada item em um '
        'loop <b>for</b>. Vamos construir sobre o exemplo anterior imprimindo uma mensagem para cada '
        'mágico, dizendo a eles que eles realizaram um grande truque:</p>')
st.code('''magicos = ['felipe', 'criss', 'houdini']
for magico in magicos:
    print(f'{magico.title()}, isso foi um grande truque!')''', line_numbers=True)
st.html('<p class="fonte_texto">A única diferença neste código é onde compomos uma mensagem para '
        'cada mágico, começando com o nome daquele mágico. Na primeira vez no loop, o valor de <i>magico</i>'
        ' é "felipe", então o Python inicia a primeira mensagem com o nome "Felipe". Na segunda vez, a '
        'mensagem começará com "Criss", e na terceira vez, a mensagem começará com "Houdini". A saída '
        'mostra uma mensagem personalizada para cada mágico na lista.</p>')
st.html('<p class="fonte_texto">Você também pode escrever quantas linhas de código quiser no '
        'loop <b>for</b>. Cada linha recuada após a linha <i>for magico in magicos</i> é considerada '
        '<b><i>dentro do loop</i></b>, e cada linha recuada é executada uma vez para cada valor na lista. '
        'Portanto, você pode fazer tanto trabalho quanto quiser com cada valor na lista. Vamos adicionar '
        'uma segunda linha à nossa mensagem, dizendo a cada mágico que estamos ansiosos pelo seu próximo '
        'truque:</p>')
st.code(r'''magicos = ['felipe', 'criss', 'houdini']
for magico in magicos:
    print(f'{magico.title()}, isso foi um grande truque!')
    print(f'Mal posso esperara para o seu truque seguinte, {magico.title()}.\n')''', line_numbers=True)
st.html(r'<p class="fonte_texto">Como recuamos ambas as chamadas para <b>print()</b>, cada '
        r'linha será executada uma vez para cada mágico na lista. A nova linha ("\n") na segunda chamada '
        r'<b>print()</b> insere uma linha em branco após cada passagem pelo loop. Isso cria um conjunto '
        r'de mensagens que são agrupadas ordenadamente para cada pessoa na lista.</p>')
st.html('<p class="fonte_texto">Você pode usar quantas linhas quiser em seus loops <b>for</b>. '
        'Na prática, você frequentemente achará útil fazer uma série de operações diferentes com cada '
        'item em uma lista quando usar um loop <b>for</b>.</p>')
st.html('<h2 class="fonte_subtitulo_aula">Fazendo algo após um loop <b>for</b></h2>')
st.html('<p class="fonte_texto">O que acontece quando um loop <b>for</b> termina de ser executado? '
        'Normalmente, você vai querer resumir um bloco de saída ou passar para outro trabalho que seu '
        'programa deve realizar.</p>')
st.html('<p class="fonte_texto">Quaisquer linhas de código após o loop <b>for</b> que não sejam recuadas '
        'são executadas uma vez sem repetição. Vamos escrever um agradecimento ao grupo de mágicos como '
        'um todo, agradecendo-os por fazerem um show excelente. Para exibir esta mensagem de grupo após '
        'todas as mensagens individuais terem sido impressas, colocamos a mensagem de agradecimento após '
        'o loop <b>for</b>, sem recuo:</p>')
st.code(r'''magicos = ['felipe', 'criss', 'houdini']
for magico in magicos:
    print(f'{magico.title()}, isso foi um grande truque!')
    print(f'Mal posso esperara para o seu truque seguinte, {magico.title()}.\n')

print('Muito obrigado a todos pelo show! Foi fantástico!')''', line_numbers=True)
st.html('<p class="fonte_texto">As duas primeiras chamadas para <b>print()</b> são repetidas uma vez '
        'para cada mágico na lista, como você viu antes. No entanto, como a última linha não é recuada, '
        'ela é impressa apenas uma vez.</p>')
st.html('<p class="fonte_texto">Ao processar dados usando um loop <b>for</b>, você verá que esta é uma boa '
        'maneira de resumir uma operação que foi realizada em um conjunto de dados inteiro. Por exemplo, '
        'você pode usar um loop <b>for</b> para inicializar um jogo executando uma lista de personagens e '
        'exibindo cada personagem na tela. Você pode então escrever algum código adicional após este loop '
        'que exibe um botão <i>Jogar Agora</i> depois que todos os personagens foram desenhados na tela.</p>')

# --- Evitando erros de indentação --- #
st.html('<h1 class="fonte_titulo_aula">Evitando erros de indentação</h1>')
st.html('<p class="fonte_texto">Python usa indentação para determinar como uma linha, ou grupo de linhas, '
        'está relacionada ao resto do programa. Nos exemplos anteriores, as linhas que imprimiam mensagens '
        'para mágicos individuais faziam parte do loop <b>for</b> porque eram recuadas. O uso de recuo '
        'pelo Python torna o código muito fácil de ler. Basicamente, ele usa espaços em branco para forçar '
        'você a escrever um código bem formatado com uma estrutura visual clara. Em programas Python mais '
        'longos, você notará blocos de código recuados em alguns níveis diferentes. Esses níveis de recuo '
        'ajudam você a ter uma noção geral da organização geral do programa.</p>')
st.html('<p class="fonte_texto">Conforme você começa a escrever código que depende de recuo adequado, você '
        'precisará observar alguns <i>erros de indentação</i> comuns. Por exemplo, as pessoas às vezes '
        'recuam linhas de código que não precisam ser recuadas ou esquecem de recuar linhas que precisam '
        'ser recuadas. Ver exemplos desses erros agora ajudará você a evitá-los no futuro e corrigi-los '
        'quando eles aparecerem em seus próprios programas. Vamos examinar alguns dos erros de indentação '
        'mais comuns.</p>')
st.html('<h2 class="fonte_subtitulo_aula">Esquecendo de indentar</h2>')
st.html('<p class="fonte_texto">Sempre recue a linha após a instrução <b>for</b> em um loop. Se você '
        'esquecer, o Python irá lembrá-lo:</p>')
st.code('''magicos = ['felipe', 'criss', 'houdini']
for magico in magicos:
print(magico)  # 1''', line_numbers=True)
st.html('<p class="fonte_texto">A chamada para <b>print()</b> (1) deveria ser recuada, mas não é. Quando '
        'o Python espera um bloco recuado e não encontra nenhum, ele permite que você saiba com qual '
        'linha ele teve um problema.</p>')
st.html('<h2 class="fonte_subtitulo_aula">Esquecendo de indentar linhas adicionais</h2>')
st.html('<p class="fonte_texto">Às vezes, seu loop rodará sem erros, mas não produzirá o resultado '
        'esperado. Isso pode acontecer quando você está tentando fazer várias tarefas em um loop e '
        'esquece de recuar algumas de suas linhas.</p>')
st.html('<p class="fonte_texto">Por exemplo, é isso que acontece quando esquecemos de recuar a segunda '
        'linha do loop que diz a cada mágico que estamos ansiosos pelo seu próximo truque:</p>')
st.code(r'''magicos = ['felipe', 'criss', 'houdini']
for magico in magicos:
    print(f'{magico.title()}, isso foi um grande truque!')
print(f'Mal posso esperara para o seu truque seguinte, {magico.title()}.\n')  # 1''', line_numbers=True)
st.html('<p class="fonte_texto">A segunda chamada para <b>print()</b> (1) deve ser recuada, mas como o '
        'Python encontra pelo menos uma linha recuada após a instrução <b>for</b>, ele não relata um erro. '
        'Como resultado, a primeira chamada <b>print()</b> é executada uma vez para cada nome na lista porque '
        'é recuada. A segunda chamada <b>print()</b> não é indentada, então ela é executada apenas uma vez após '
        'o loop terminar de ser executado. Como o valor final associado a <i>magico</i> é "houdini", ela é '
        'a única que recebe a mensagem “Mal posso esperara para o seu truque seguinte”.</p>')
st.html('<p class="fonte_texto">Este é um <i>erro lógico</i>. A sintaxe é um código Python válido, mas '
        'o código não produz o resultado desejado porque ocorre um problema em sua lógica. Se você '
        'espera ver uma determinada ação repetida uma vez para cada item em uma lista e ela é executada '
        'apenas uma vez, determine se você precisa simplesmente recuar uma linha ou um grupo de linhas.</p>')
st.html('<h2 class="fonte_subtitulo_aula">Indentação desnecessária</h2>')
st.html('<p class="fonte_texto">Se você acidentalmente recuar uma linha que não precisa ser recuada, o '
        'Python informa sobre o recuo inesperado:</p>')
st.code('''mensagem = 'Olá, Mundo Python!'
    print(mensagem)''', line_numbers=True)
st.html('<p class="fonte_texto">Não precisamos recuar a chamada <b>print()</b>, porque ela não faz parte '
        'de um loop; portanto, o Python relata este erro.</p>')
st.html('<p class="fonte_texto">Você pode evitar erros de indentação inesperados indentando somente '
        'quando tiver um motivo específico para isso. Nos programas que você está escrevendo neste ponto, '
        'as únicas linhas que você deve recuar são as ações que você quer repetir para cada item em um '
        'loop <b>for</b>.</p>')
st.html('<h2 class="fonte_subtitulo_aula">Indentação desnecessária após o loop</h2>')
st.html('<p class="fonte_texto">Se você acidentalmente recuar o código que deveria ser executado após um '
        'loop ter terminado, esse código será repetido uma vez para cada item na lista. Às vezes, isso '
        'faz com que o Python relate um erro, mas frequentemente isso resultará em um erro lógico.</p>')
st.html('<p class="fonte_texto">Por exemplo, vamos ver o que acontece quando acidentalmente recuamos a '
        'linha que agradeceu aos mágicos como um grupo por fazerem um bom show:</p>')
st.code(r'''magicos = ['felipe', 'criss', 'houdini']
for magico in magicos:
    print(f'{magico.title()}, isso foi um grande truque!')
    print(f'Mal posso esperara para o seu truque seguinte, {magico.title()}.\n')
        
        print('Muito obrigado a todos pelo show! Foi fantástico!')  # 1''', line_numbers=True)
st.html('<p class="fonte_texto">Como a última linha (1) é recuada, ela é impressa uma vez para cada '
        'pessoa na lista.</p>')
st.html('<p class="fonte_texto">Este é outro erro lógico, similar ao de <b>Esquecendo de indentar linhas '
        'adicionais</b>. Como o Python não sabe o que você está tentando fazer com seu código, ele '
        'executará todo o código escrito em sintaxe válida. Se uma ação for repetida muitas vezes quando '
        'deveria ser executada apenas uma vez, você provavelmente precisará desindentar o código para '
        'essa ação.</p>')
st.html('<h2 class="fonte_subtitulo_aula">Esquecendo os dois pontos</h2>')
st.html('<p class="fonte_texto">Os dois pontos no final de uma instrução <b>for</b> informam ao Python '
        'para interpretar a próxima linha como o início de um loop:</p>')
st.code('''magicos = ['felipe', 'criss', 'houdini']
for magico in magicos  # 1
    print(magico)''', line_numbers=True)
st.html('<p class="fonte_texto">Se você acidentalmente esquecer os dois pontos (1), você receberá um erro '
        'de sintaxe porque o Python não sabe exatamente o que você está tentando fazer.</p>')
st.html('<p class="fonte_texto">O Python não sabe se você simplesmente esqueceu os dois pontos ou se você '
        'quis escrever código adicional para configurar um loop mais complexo. Se o interpretador puder '
        'identificar uma possível correção, ele sugerirá uma, como adicionar dois pontos no final de uma '
        'linha, como faz aqui com a resposta <i>expected</i> ":". Alguns erros têm correções fáceis e '
        'óbvias, graças às sugestões nos tracebacks do Python. Alguns erros são muito mais difíceis de '
        'resolver, mesmo quando a correção eventual envolve apenas um único caractere. Não se sinta mal '
        'quando uma pequena correção demorar muito para ser encontrada; você não está sozinho nessa '
        'experiência.</p>')
st.html('<h2 class="fonte_subtitulo_aula">Tente você mesmo!</h2>')
st.html('<p class="fonte_texto"><b>Exercício 01</b>: Pense em pelo menos três tipos de sua pizza favorita. '
        'Armazene esses nomes de pizza em uma lista e, em seguida, use um loop for para imprimir o nome '
        'de cada pizza:</p>')
st.html('<ul class="fonte_texto">'
        '<li>Modifique seu loop <b>for</b> para imprimir uma frase usando o nome da pizza, em vez de imprimir '
        'apenas o nome da pizza. Para cada pizza, você deve ter uma linha de saída contendo uma declaração '
        'simples como <i>Eu gosto de pizza de bacon</i>.</li>'
        '<li>Adicione uma linha no final do seu programa, fora do loop <b>for</b>, que declare o quanto você '
        'gosta de pizza. A saída deve consistir em três ou mais linhas sobre os tipos de pizza que você gosta '
        'e então uma frase adicional, como <i>Eu realmente amo pizza!</i></li>'
        '</ul>')
with st.expander('Resposta'):
    st.code('''# --- Lista com os sabores de pizza --- #
pizzas = ['bacon', 'marguerita', 'frango']

# --- Iterar sob cada item da lista --- #
for pizza in pizzas:
    print(f'Eu gosto de pizza de {pizza}.')

# --- Mensagem final --- #
print('Eu realmente amo pizza!')''', line_numbers=True)
st.html('<p class="fonte_texto"><b>Exercício 02</b>: Pense em pelo menos três animais diferentes que '
        'tenham uma característica comum. Armazene os nomes desses animais em uma lista e, em seguida, '
        'use um loop <b>for</b> para imprimir o nome de cada animal:</p>')
st.html('<ul class="fonte_texto">'
        '<li>Modifique seu programa para imprimir uma declaração sobre cada animal, como '
        '<i>Um cachorro seria um ótimo animal de estimação</i>.</li>'
        '<li>Adicione uma linha no final do seu programa, declarando o que esses animais têm em comum. Você '
        'pode imprimir uma frase, como <i>Qualquer um desses animais é um ótimo animal de estimação!</i></li>'
        '</ul>')
with st.expander('Resposta'):
    st.code('''# --- Lista com o animais --- #
animais = ['gato', 'cachorro', 'peixe']

# --- Iterar sobre cada item da lista --- #
for animal in animais:
    print(f'Um {animal} seria um ótimo animal de estimação!')
print('Qualquer um desses animais é um ótimo animal de estimação!')''', line_numbers=True)

# --- Fazendo listas numéricas --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Fazendo listas numéricas</h1>')