# --- Importar as bibliotecas --- #
from PIL import Image
import streamlit as st

# --- Configurações iniciais da página --- #
st.set_page_config(
    page_title='Capítulo 02 - Codando os nossos primeiros neurônios',
    page_icon=Image.open('./assets/logo/logo.png'),
    layout='wide'
)

# --- Carregar o estilo das fontes --- #
with open('./assets/css/style.css', 'r') as css:
    st.html(f'<style>{css.read()}</style>')

# --- Colocar o banner do capítulo --- #
st.image('./assets/imagens/redes_neurais_zero/aula_02/aula_02.png')

# --- Um único neurônio --- #
st.html('<h1 class="fonte_titulo_aula">Um único neurônio</h1>')
st.html('<p class="fonte_texto">Digamos que temos um único neurônio e que existem três entradas para esse '
        'neurônio. Como na maioria dos casos, quando você inicializa parâmetros em redes neurais, nossa '
        'rede terá pesos inicializados aleatoriamente e vieses definidos como zero para iniciar. Por que '
        'fazemos isso ficará claro mais tarde. A entrada serão dados de treinamento reais ou saídas de '
        'neurônios da camada anterior da rede neural. Vamos apenas inventar valores para começar como '
        'entrada por enquanto:</p>')
st.code('entradas = [1, 2, 3]', line_numbers=True)
st.html('<p class="fonte_texto">Cada entrada também precisa de um peso associado a ela. As entradas são os '
        'dados que passamos para o modelo para obter os resultados desejados, enquanto os pesos são os '
        'parâmetros que ajustaremos mais tarde para obter esses resultados. Os pesos são um dos tipos de '
        'valores que mudam dentro do modelo durante a fase de treinamento, junto com os vieses que também '
        'mudam durante o treinamento. Os valores dos pesos e vieses são o que são “treinados” e são o que '
        'fazem um modelo realmente funcionar (ou não funcionar). Começaremos inventando pesos por enquanto. '
        'Digamos que a primeira entrada, no índice 0, que é 1, tenha peso de 0,2, a segunda entrada tenha '
        'peso de 0,8 e a terceira entrada tenha peso de -0,5. Nossas listas de entradas e pesos agora devem '
        'ser:</p>')
st.code('''entradas = [1, 2, 3]
pesos = [0.2, 0.8, -0.5]''', line_numbers=True)
st.html('<p class="fonte_texto">Em seguida, precisamos do viés. No momento, estamos modelando um '
        'único neurônio com três entradas. Como estamos modelando um único neurônio, temos apenas um viés, '
        'pois há apenas um valor de viés por neurônio. O viés é um valor ajustável adicional, mas não '
        'está associado a nenhuma entrada, em contraste com os pesos. Selecionaremos aleatoriamente um '
        'valor de 2 como viés para este exemplo:</p>')
st.code('''entradas = [1, 2, 3]
pesos = [0.2, 0.8, -0.5]
vies = 2''', line_numbers=True)
st.html('<p class="fonte_texto">Este neurônio soma cada entrada multiplicada pelo peso dessa entrada e, em '
        'seguida, adiciona o viés. Tudo o que o neurônio faz é pegar as frações das entradas, onde essas '
        'frações (pesos) são os parâmetros ajustáveis, e adicionar outro parâmetro ajustável (o viés) e '
        'então gerar o resultado. Nossa saída seria calculada até este ponto como:</p>')
st.code('''saida = (entrada[0] * peso[0] +
         entrada[1] * peso[1] +
         entrada[2] * peso[2] + vies)
print(saida)''', line_numbers=True)
st.html('<p class="fonte_texto">A saída aqui deve ser <b>2.3</b>.</p>')
st.image('./assets/imagens/redes_neurais_zero/aula_02/figura_01.png',
         caption='Figura 2-1. Visualizando o código que compõe a matemática de um neurônio básico.')
with st.expander('Animação da Figura 2-1'):
    st.video('https://www.youtube.com/watch?v=vbeanwfm0Q4')
st.html('<p class="fonte_texto">O que precisaremos mudar se tivermos 4 entradas, em vez das 3 que acabamos '
        'de mostrar? Ao lado da entrada adicional, precisamos adicionar um peso associado, pelo qual esta '
        'nova entrada será multiplicada. Também criaremos um valor para esse novo peso. O código para esses '
        'dados poderia ser:</p>')
st.code('''entradas = [1.0, 2.0, 3.0, 2.5]
pesos = [0.2, 0.8, -0.5, 1.0]
vies = 2.0''', line_numbers=True)
st.image('./assets/imagens/redes_neurais_zero/aula_02/figura_02.png',
         caption='Figura 2-2. Visualizando como as entradas, pesos e tendências do código interagem com o '
                 'neurônio.')
with st.expander('Animação da Figura 2-2'):
    st.video('https://www.youtube.com/watch?v=MBIJc6XtLjg')
st.html('<p class="fonte_texto">Tudo junto no código, incluindo a nova entrada e peso, para produzir a '
        'saída:</p>')
st.code('''entradas = [1.0, 2.0, 3.0, 2.5]
pesos = [0.2, 0.8, -0.5, 1.0]
vies = 2.0

saida = (entradas[0] * pesos[0] +
         entradas[1] * pesos[1] +
         entradas[2] * pesos[2] +
         entradas[3] * pesos[3] + vies)

print(saida)''', line_numbers=True)
st.html('<p class="fonte_texto">Visualmente:</p>')
st.image('./assets/imagens/redes_neurais_zero/aula_02/figura_03.png',
         caption='Figura 2-3. Visualizando o código que compõe um neurônio básico, desta vez com 4 entradas.')

# --- Uma camada de neurônios --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Uma camada de neurônios</h1>')
st.html('<p class="fonte_texto">As redes neurais normalmente possuem camadas que consistem em mais de um '
        'neurônio. As camadas nada mais são do que grupos de neurônios. Cada neurônio em uma camada recebe '
        'exatamente a mesma entrada, a entrada dada à camada (que pode ser os dados de treinamento ou a '
        'saída da camada anterior), mas contém seu próprio conjunto de pesos e seu próprio viés, produzindo '
        'sua própria saída exclusiva. A saída da camada é um conjunto de cada uma dessas saídas, uma para '
        'cada neurônio. Digamos que temos um cenário com 3 neurônios em uma camada e 4 entradas:</p>')
st.image('./assets/imagens/redes_neurais_zero/aula_02/figura_04.png',
         caption='Figura 2-4. Visualizando uma camada de neurônios com entrada comum.')
with st.expander('Animação da Figura 2-4'):
    st.video('https://www.youtube.com/watch?v=Uvngs6sWyBg')
st.html('<p class="fonte_texto">Manteremos as 4 entradas iniciais e o conjunto de pesos para o primeiro '
        'neurônio iguais aos que usamos até agora. Adicionaremos 2 conjuntos adicionais de pesos e 2 vieses '
        'adicionais para formar 2 novos neurônios, totalizando 3 na camada. A saída da camada será uma '
        'lista de 3 valores, não apenas um único valor como para um único neurônio.</p>')
st.code('''entradas = [1, 2, 3, 2.5]
pesos_1 = [0.2, 0.8, -0.2, 1]
pesos_2 = [0.5, -0.91, 0.26, -0.5]
pesos_3 = [-0.26, -0.27, 0.17, 0.87]

vies_1 = 2
vies_2 = 3
vies_3 = 0.5

saidas = [
    # --- Neurônio 1 --- #
    entradas[0] * pesos_1[0] +
    entradas[1] * pesos_1[1] +
    entradas[2] * pesos_1[2] +
    entradas[3] * pesos_1[3] + vies_1,

    # --- Neurônio 2 --- #
    entradas[0] * pesos_2[0] +
    entradas[1] * pesos_2[1] +
    entradas[2] * pesos_2[2] +
    entradas[3] * pesos_2[3] + vies_2,

    # --- Neurônio 3 --- #
    entradas[0] * pesos_3[0] +
    entradas[1] * pesos_3[1] +
    entradas[2] * pesos_3[2] +
    entradas[3] * pesos_3[3] + vies_3,
]

print(saidas)''', line_numbers=True)
st.image('./assets/imagens/redes_neurais_zero/aula_02/figura_05.png',
         caption='Figura 2-5. Matemática e recursos visuais por trás de uma camada de neurônios.')
st.html('<p class="fonte_texto">Neste código, temos três conjuntos de pesos e três vieses, que definem '
        'três neurônios. Cada neurônio está “conectado” às mesmas entradas. A diferença está nos pesos e '
        'vieses separados que cada neurônio aplica à entrada. Isso é chamado de rede neural <b>totalmente '
        'conectada</b>, cada neurônio na camada atual tem conexões com todos os neurônios da camada '
        'anterior. Este é um tipo de rede neural muito comum, mas deve-se observar que não há necessidade '
        'de conectar tudo totalmente assim. Neste ponto, mostramos apenas o código para uma única camada '
        'com poucos neurônios. Imagine codificar muito mais camadas e mais neurônios. Isso seria muito '
        'desafiador para codificar usando nossos métodos atuais. Em vez disso, poderíamos usar um loop '
        'para dimensionar e lidar com entradas e camadas de tamanho dinâmico. Transformamos as variáveis '
        'de peso separadas em uma lista de pesos para que possamos iterá-las e alteramos o código para '
        'usar loops em vez de operações codificadas.</p>')
st.code('''entradas = [1, 2, 3, 2.5]
pesos = [
    [0.2, 0.8, -0.5, 1],
    [0.5, -0.91, 0.26, -0.5],
    [-0.26, -0.27, 0.17, 0.87]
]
vieses = [2, 3, 0.5]

# --- Saída da camada atual --- #
camada_saida = []

# --- Iterar sobre cada neurônio --- #
for pesos_neuronio, vies_neuronio in zip(pesos, vieses):
    # --- Saída zerada do neurônio iterado --- #
    saida_neuronio = 0

    # --- Iterar sobre cada entrada e peso do neurônio --- #
    for entrada_neuronio, peso in zip(entradas, pesos_neuronio):
        # --- Cálculo da saída do neurônio --- #
        saida_neuronio += entrada_neuronio * peso

    # --- Adicionar o viés --- #
    saida_neuronio += vies_neuronio

    # --- Colocar a saída do neurônio na lista da camada de saída --- #
    camada_saida.append(saida_neuronio)
    
print(camada_saida)''', line_numbers=True)
st.html('<p class="fonte_texto">Isso faz a mesma coisa que antes, apenas de uma forma mais dinâmica e '
        'escalonável. Se você ficar confuso em alguma das etapas, <b>print()</b> exibe os objetos para '
        'ver o que eles são e o que está acontecendo. A função <b>zip()</b> nos permite iterar vários '
        'iteráveis (listas neste caso) simultaneamente. Novamente, tudo o que estamos fazendo é, '
        'para cada neurônio (o loop externo no código acima, sobre os pesos e vieses dos neurônios), '
        'tomando cada valor de entrada multiplicado pelo peso associado para essa entrada (o loop interno '
        'no código acima, sobre entradas e pesos), somando tudo isso e, em seguida, adicionando um viés '
        'no final. Por fim, enviar a saída do neurônio para a lista da camada de saída.</p>')
st.html('<p class="fonte_texto">É isso! Como sabemos que temos três neurônios? Por que temos três? Podemos '
        'dizer que temos três neurônios porque existem 3 conjuntos de pesos e 3 vieses. Ao criar sua '
        'própria rede neural, você também decide quantos neurônios deseja para cada uma das camadas. Você '
        'pode combinar quantas entradas receber com quantos neurônios desejar. À medida que você avança '
        'neste estudo, você terá alguma intuição sobre quantos neurônios tentar usar. Começaremos usando '
        'números triviais de neurônios para ajudar a entender como as redes neurais funcionam em seu '
        'núcleo.</p>')
st.html('<p class="fonte_texto">Com nosso código acima que usa loops, poderíamos modificar nosso número de '
        'entradas ou neurônios em nossa camada para ser o que quiséssemos, e nosso loop cuidaria disso. '
        'Como dissemos anteriormente, seria um péssimo serviço não mostrar o NumPy aqui, já que o Python '
        'sozinho não faz matemática de matrizes/tensores/arrays com muita eficiência. Mas, primeiro, o '
        'motivo pelo qual a biblioteca de aprendizado profundo mais popular em Python é chamada de '
        '“TensorFlow” é que se trata de realizar operações em <b>tensores</b>.</p>')

# --- Tensores, matrizes e vetores --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Tensores, matrizes e vetores</h1>')
st.html('<p class="fonte_texto">O que são <i>“tensores?”</i></p>')
st.html('<p class="fonte_texto">Os tensores estão <i>intimamente relacionados</i> aos arrays. Se você '
        'trocar tensor/matriz/array quando se trata de aprendizado de máquina, as pessoas provavelmente '
        'entenderão. Mas existem diferenças sutis e são principalmente o contexto ou '
        'os atributos do objeto tensor. Para entender um tensor, vamos comparar e descrever alguns dos '
        'outros contêineres de dados em Python (coisas que contêm dados). Vamos começar com uma lista. Uma '
        'lista Python é definida por objetos separados por vírgula contidos entre colchetes. Até agora, '
        'temos usado listas. Este é um exemplo de uma lista simples:</p>')
st.code('l = [1, 5, 6, 2]', line_numbers=True)
st.html('<p class="fonte_texto">Uma lista de listas:</p>')
st.code('''ldl = [[1, 5, 6, 2],
       [3, 2, 1, 3]]''', line_numbers=True)
st.html('<p class="fonte_texto">Uma lista de listas de listas:</p>')
st.code('''ldldl = [[[1, 5, 6, 2],
          [3, 2, 1, 3]],
         [[5, 2, 1, 2],
          [6, 4, 8, 4]],
         [[2, 8, 5, 3],
          [1, 1, 9, 4]]''', line_numbers=True)
st.html('<p class="fonte_texto">Tudo mostrado até agora também pode ser um array ou uma representação de '
        'array de um tensor. Uma lista é apenas uma lista e pode fazer praticamente tudo o que quiser, '
        'incluindo:</p>')
st.code('''outra_lista_de_listas = [[4, 2, 3],
                         [5, 1]]''', line_numbers=True)
st.html('<p class="fonte_texto">A lista de listas acima não pode ser um array porque não é <b>homóloga</b>. '
        'Uma lista de listas é homóloga se cada lista ao longo de uma dimensão for identicamente longa, e '
        'isso deve ser verdadeiro para cada dimensão. No caso da lista mostrada acima, é uma lista '
        'bidimensional. O comprimento da primeira dimensão é o número de sublistas na lista total (2). '
        'A segunda dimensão é o comprimento de cada uma dessas sublistas (3, depois 2). No exemplo acima, '
        'ao ler através da dimensão “linha” (também chamada de segunda dimensão), a primeira lista tem 3 '
        'elementos e a segunda lista tem 2 elementos — isso não é homólogo e, portanto, não pode ser uma '
        'matriz. Embora não ser consistente numa dimensão seja suficiente para mostrar que este exemplo '
        'não é homólogo, poderíamos também ler a dimensão “coluna” (a primeira dimensão); as duas '
        'primeiras colunas têm 2 elementos, enquanto a terceira coluna contém apenas 1 elemento. Observe '
        'que todas as dimensões não precisam necessariamente ter o mesmo comprimento; é perfeitamente '
        'aceitável ter um array com 4 linhas e 3 colunas (ou seja, 4x3).</p>')
st.html('<p class="fonte_texto">Uma matriz é bastante simples. É uma matriz retangular. Possui colunas e '
        'linhas. É bidimensional. Portanto, uma matriz pode ser um array (um array 2D). Todas os arrays '
        'podem ser matrizes? Não. Uma matriz pode ser muito mais do que apenas colunas e linhas, pois '
        'pode ter quatro dimensões, vinte dimensões e assim por diante.</p>')
st.code('''lista_matriz_array = [[4, 2]
                      [5, 1]
                      [8, 2]]''', line_numbers=True)
st.html('<p class="fonte_texto">A lista acima também pode ser uma matriz válida (devido às suas colunas e '
        'linhas), o que significa automaticamente que também pode ser um array. A “forma” deste array '
        'seria 3x2, ou mais formalmente descrita como uma forma de <i>(3, 2)</i>, pois possui 3 linhas e '
        '2 colunas.</p>')
st.html('<p class="fonte_texto">Para denotar uma forma, precisamos verificar todas as dimensões. Como já '
        'aprendemos, uma matriz é uma matriz bidimensional. A primeira dimensão é o que está dentro dos '
        'colchetes mais externos, e se olharmos para a matriz acima, podemos ver 3 listas lá: <b>[4,2]</b>, '
        '<b>[5,1]</b> e <b>[8,2]</b>; portanto, o tamanho nesta dimensão é 3 e cada uma dessas listas '
        'deve ter o mesmo formato para formar um array (e matriz neste caso). O tamanho da próxima '
        'dimensão é o número de elementos dentro deste par de colchetes mais interno, e vemos que é 2, '
        'pois todos eles contêm 2 elementos.</p>')
st.html('<p class="fonte_texto">Com arrays tridimensionais, como no <b>ldldl</b> abaixo, teremos um terceiro '
        'nível de colchetes:</p>')
st.code('''ldldl = [[[1, 5, 6, 2],
          [3, 2, 1, 3]],
         [[5, 2, 1, 2],
          [6, 4, 8, 4]],
         [[2, 8, 5, 3],
          [1, 1, 9, 4]]''', line_numbers=True)
st.html('<p class="fonte_texto">O primeiro nível desta matriz contém 3 matrizes:</p>')
st.code('''[[1, 5, 6, 2],
[3, 2, 1, 3]]


[[5, 2, 1, 2],
[6, 4, 8, 4]]

# e

[[2, 8, 5, 3],
[1, 1, 9, 4]]''', line_numbers=True)
st.html('<p class="fonte_texto">Isso é o que está dentro dos colchetes mais externos e o tamanho desta '
        'dimensão é então 3. Se olharmos para a primeira matriz, podemos ver que ela contém 2 listas: '
        '<b>[1,5,6,2]</b> e <b>[3,2,1,3]</b> então o tamanho desta dimensão é 2, enquanto cada lista desta '
        'matriz interna inclui 4 elementos. Esses 4 elementos constituem a 3ª e última dimensão desta '
        'matriz, pois não existem mais colchetes internos. Portanto, a forma deste array é '
        '<i>(3, 2, 4)</i> e é um array tridimensional, já que o formato contém 3 dimensões.</p>')
with st.expander('Animação 2-5'):
    st.video('https://www.youtube.com/watch?v=z_fcBg6_bKU')
st.html('<p class="fonte_texto">Finalmente, o que é um tensor? Quando se trata da discussão entre tensores '
        'versus matrizes no contexto da ciência da computação, surgiram páginas e mais páginas de debate. '
        'Este intenso debate parece ser causado pelo fato de as pessoas discutirem em locais totalmente '
        'diferentes. Não há dúvida de que um tensor não é apenas uma matriz, mas a verdadeira questão é: '
        '“O que é um tensor, para um cientista da computação, no contexto do aprendizado profundo?” '
        'Acreditamos que podemos resolver o debate em uma linha:</p>')
st.html('<p class="fonte_texto"><b><i>Um objeto tensor é um objeto que pode ser representado como um '
        'array.</i></b></p>')
st.html('<p class="fonte_texto">O que isso significa é que, como programadores, podemos (e iremos) tratar '
        'tensores como arrays no contexto de aprendizado profundo, e isso é realmente tudo o que precisamos '
        'pensar nisso. Todos os tensores são apenas arrays? Não, mas eles são representados como arrays em '
        'nosso código, então, para nós, eles são apenas arrays, e é por isso que há tanta discussão e '
        'confusão.</p>')
st.html('<p class="fonte_texto">Agora, o que é um array? Em nosso estudo, definimos um array como um '
        'contêiner homólogo ordenado para números e usamos esse termo principalmente ao trabalhar com o '
        'pacote NumPy, pois é assim que a estrutura de dados principal é chamada dentro dele. Um array '
        'linear, também chamado de array unidimensional, é o exemplo mais simples de um array e, em '
        'Python simples, seria uma lista. As matrizes também podem consistir em dados multidimensionais, '
        'e um dos exemplos mais conhecidos é o que chamamos de matriz em matemática, que representaremos '
        'como uma matriz bidimensional. Cada elemento do array pode ser acessado usando uma tupla de '
        'índices como chave, o que significa que podemos recuperar qualquer elemento do array.</p>')
st.html('<p class="fonte_texto">Precisamos aprender mais uma noção: um vetor. Simplificando, um vetor em '
        'matemática é o que chamamos de lista em Python ou array unidimensional em NumPy. É claro que '
        'listas e arrays NumPy não têm as mesmas propriedades de um vetor, mas, assim como podemos escrever '
        'uma matriz como uma lista de listas em Python, também podemos escrever um vetor como uma lista '
        'ou array! Além disso, veremos o vetor algebricamente (matematicamente) como um conjunto de '
        'números entre parênteses. Isto contrasta com a perspectiva da física, onde a representação do '
        'vetor é geralmente vista como uma seta, caracterizada por uma magnitude e uma direção.</p>')

# --- Produto escalar e adição de vetores --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Produto escalar e adição de vetores</h1>')
st.html('<p class="fonte_texto">Vamos agora abordar a multiplicação de vetores, pois é uma das operações '
        'mais importantes que realizaremos em vetores. Podemos obter o mesmo resultado que em nossa '
        'implementação Python pura de multiplicar cada elemento em nossos vetores de entradas e pesos '
        'elemento a elemento usando um <b>produto escalar</b>, que explicaremos em breve. Tradicionalmente, '
        'usamos produtos escalares para <b>vetores</b> (mais um nome para um contêiner), e certamente '
        'podemos nos referir ao que estamos fazendo aqui como trabalhar com vetores, assim como podemos '
        'chamá-los de “tensores”. No entanto, isso parece aumentar o misticismo das redes neurais, como se '
        'elas fossem objetos em um espaço vetorial multidimensional complexo que nunca entenderemos. '
        'Continue pensando em vetores como arrays, um array unidimensional é apenas um vetor (ou uma lista '
        'em Python).</p>')
st.html('<p class="fonte_texto">Devido ao grande número de variáveis e interconexões feitas, podemos '
        'modelar relações muito complexas e não lineares com funções de ativação não lineares e realmente '
        'nos sentirmos como magos, mas isso pode fazer mais mal do que bem. Sim, usaremos o “produto '
        'escalar”, mas estamos fazendo isso porque resulta em uma forma limpa de realizar os cálculos '
        'necessários. Não é nada mais aprofundado do que isso – como você já viu, podemos fazer essa '
        'matemática com palavras que soam muito mais rudimentares. Ao multiplicar vetores, você executa '
        'um produto escalar ou um produto vetorial. Um produto vetorial resulta em um vetor, enquanto um '
        'produto escalar resulta em um escalar (um único valor/número).</p>')
st.html('<p class="fonte_texto">Primeiro, vamos explicar o que é um produto escalar de dois vetores. Os '
        'matemáticos diriam:</p>')
st.latex(r'\vec{a}\cdot \vec{b} = \sum_{i=1}^{n}a_{i}b_{i} = a_{1}b_{1} + a_{2}b_{2} + \cdots a_{n}b_{n}')
st.html('<p class="fonte_texto">Um produto escalar de dois vetores é uma soma de produtos de elementos '
        'vetoriais consecutivos. Ambos os vetores devem ter o mesmo tamanho (ter igual número de '
        'elementos).</p>')
st.html('<p class="fonte_texto">Vamos escrever como um produto escalar é calculado em Python. Para isso, '
        'você tem dois vetores, que podemos representar como listas em Python. Em seguida, multiplicamos '
        'seus elementos a partir dos mesmos valores de índice e adicionamos todos os produtos resultantes. '
        'Digamos que temos duas listas atuando como nossos vetores:</p>')
st.code('''a = [1, 2, 3]
b = [2, 3, 4]''', line_numbers=True)
st.html('<p class="fonte_texto">Para obter o produto escalar:</p>')
st.code('''produto_escalar = a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
print(produto_escalar)''', line_numbers=True)
with st.expander('Animação 2-6'):
    st.video('https://www.youtube.com/watch?v=_hNzxGjwkYY')
st.html('<p class="fonte_texto">Agora, e se chamássemos <i>a</i> de “entradas” e <i>b</i> de “pesos?” De '
        'repente, esse produto escalar parece uma maneira sucinta de realizar as operações que precisamos '
        'e que já realizamos em Python simples. Precisamos multiplicar nossos pesos e entradas dos mesmos '
        'valores de índice e somar os valores resultantes. O produto escalar executa exatamente esse tipo '
        'de operação; portanto, faz muito sentido usar aqui. Voltando ao código da rede neural, vamos usar '
        'este produto escalar. O Python puro não contém métodos ou funções para realizar tal operação, '
        'então usaremos o pacote NumPy, que é capaz de fazer isso, e muitas outras operações que usaremos '
        'no futuro.</p>')
st.html('<p class="fonte_texto">Também precisaremos realizar uma operação de adição de vetores num futuro '
        'não muito distante. Felizmente, NumPy nos permite fazer isso de forma natural; usando o sinal de '
        'mais com as variáveis que contêm vetores dos dados. A adição dos dois vetores é uma '
        'operação realizada elemento a elemento, o que significa que ambos os vetores devem ser do mesmo '
        'tamanho, e o resultado também se tornará um vetor deste tamanho. O resultado é um vetor calculado '
        'como a soma dos elementos consecutivos do vetor:</p>')
st.latex(r'\vec{a}+\vec{b}=[a_{1}+b_{1},a_{2}+b_{2},\cdots,a_{n}+b_{n}]')

# --- Um único neurônio com NumPy --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Um único neurônio com NumPy</h1>')
st.html('<p class="fonte_texto">Vamos codificar a solução, para iniciar um único neurônio, usando o produto '
        'escalar e a adição dos vetores com NumPy. Isso torna o código muito mais simples de ler e '
        'escrever (e mais rápido de executar):</p>')
st.code('''import numpy as np

entradas = [1, 2, 3, 2.5]
pesos = [0.2, 0.8, -0.5, 1]
vies = 2

saida = np.dot(pesos, entradas) + vies

print(saida)''', line_numbers=True)
with st.expander('Animação 2-7'):
    st.video('https://www.youtube.com/watch?v=7ReqEO4U7Lc')

# --- Uma camada de neurônios com NumPy --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Uma camada de neurônios com NumPy</h1>')
st.html('<p class="fonte_texto">Agora voltamos ao ponto em que gostaríamos de calcular a saída de uma '
        'camada de 3 neurônios, o que significa que os pesos serão uma matriz ou lista de vetores de peso. '
        'Em Python simples, escrevemos isso como uma lista de listas. Com NumPy, este será um array '
        'bidimensional, que chamaremos de matriz. Anteriormente, com o exemplo de 3 neurônios, realizamos '
        'uma multiplicação desses pesos por uma lista contendo entradas, o que resultou em uma lista de '
        'valores de saída, um por neurônio.</p>')
st.html('<p class="fonte_texto">Também descrevemos o produto escalar de dois vetores, mas os pesos agora '
        'são uma matriz e precisamos realizar um produto escalar deles e do vetor de entrada. NumPy torna '
        'isso muito fácil para nós, tratando esta matriz como uma lista de vetores e realizando o produto '
        'escalar um por um com o vetor de entradas, retornando uma lista de produtos escalares.</p>')
st.html('<p class="fonte_texto">O resultado do produto escalar, no nosso caso, é um vetor (ou uma lista) de '
        'somas de peso e produtos de entrada para cada um dos neurônios. A partir daqui, ainda precisamos '
        'adicionar vieses correspondentes a eles. Os viéses podem ser facilmente adicionadas ao '
        'resultado da operação do produto escalar, pois são um vetor do mesmo tamanho. Também podemos usar '
        'a lista simples do Python diretamente aqui, pois o NumPy irá convertê-la em um array '
        'internamente.</p>')
st.html('<p class="fonte_texto">Anteriormente, calculamos as saídas de cada neurônio realizando um produto '
        'escalar e adicionando um viés, um por um. Agora alteramos a ordem dessas operações, estamos '
        'realizando o produto escalar primeiro como uma operação em todos os neurônios e entradas e, em '
        'seguida, estamos adicionando um viés na próxima operação. Quando adicionamos dois '
        'vetores usando NumPy, cada i-ésimo elemento é adicionado, resultando em um novo vetor do mesmo '
        'tamanho. Isso é uma simplificação e uma otimização, proporcionando um código mais simples e '
        'rápido.</p>')
st.code('''import numpy as np

entradas = [1, 2, 3, 2.5]
pesos = [[0.2, 0.8, -0.5, 1],
         [0.5, -0.91, 0.26, -0.5],
         [-0.26, -0.27, 0.17, 0.87]]
vieses = [2, 3, 0.5]

camada_saida = np.dot(pesos, entradas) + vieses

print(camada_saida)''', line_numbers=True)
with st.expander('Animação 2-8'):
    st.video('https://www.youtube.com/watch?v=Fhbcl0grca8')
st.html('<p class="fonte_texto">Esta sintaxe envolvendo o produto escalar de pesos e entradas seguido pela '
        'adição vetorial de viés é a forma mais comumente usada para representar este cálculo de '
        '<b>entradas·pesos+viés</b>. Para explicar a ordem dos parâmetros que estamos passando para '
        '<b>np.dot()</b>, devemos pensar nisso como o que vier primeiro decidirá o formato da saída. No '
        'nosso caso, estamos passando primeiro uma lista de pesos de neurônios e depois as entradas, pois '
        'nosso objetivo é obter uma lista de saídas de neurônios. Como mencionamos, um produto escalar de '
        'uma matriz e um vetor resulta em uma lista de produtos escalares. O método <b>np.dot()</b> trata '
        'a matriz como uma lista de vetores e realiza um produto escalar de cada um desses vetores com o '
        'outro vetor. Neste exemplo, usamos essa propriedade para passar uma matriz, que era uma lista de '
        'vetores de peso de neurônios e um vetor de entradas e obter uma lista de produtos escalares: '
        'saídas de neurônios.</p>')

# --- Um lote de dados --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Um lote de dados</h1>')
st.html('<p class="fonte_texto">Para treinar, as redes neurais tendem a receber dados em <b>lotes</b>. Até '
        'agora, os dados de entrada de exemplo foram apenas uma amostra (ou <b>observação</b>) de vários '
        'recursos chamados de conjunto de recursos:</p>')
st.code('entradas = [1, 2, 3, 2.5]', line_numbers=True)
st.html('<p class="fonte_texto">Aqui, os dados <b>[1, 2, 3, 2.5]</b> são de alguma forma significativos e '
        'descritivos para a saída que desejamos. Imagine cada número como um valor de um sensor diferente, '
        'do exemplo do '
        '<a href="https://mundopython.streamlit.app/aula_01_redes_neurais_zero">Capítulo 1</a>, todos '
        'simultaneamente. Cada um desses valores é um dado de observação de '
        'recurso e, juntos, eles formam uma <b>instância de conjunto de recursos</b>, também chamada de '
        '<b>observação</b> ou, mais comumente, de <b>amostra</b>.</p>')
with st.expander('Animação 2-9'):
    st.video('https://www.youtube.com/watch?v=9aeqyXT504o')
st.html('<p class="fonte_texto">Frequentemente, as redes neurais esperam coletar muitas <b>amostras</b> de '
        'cada vez por dois motivos. Um dos motivos é que é mais rápido treinar em lotes no processamento '
        'paralelo, e o outro motivo é que os lotes ajudam na generalização durante o treinamento. Se você '
        'ajustar (realizar uma etapa de um processo de treinamento) uma amostra por vez, é muito provável '
        'que continue ajustando a essa amostra individual, em vez de produzir lentamente ajustes gerais nos '
        'pesos e vieses que se ajustem a todo o conjunto de dados. Ajustar ou treinar em lotes oferece '
        'uma chance maior de fazer alterações mais significativas nos pesos e vieses. Para o conceito '
        'de montagem em lotes, em vez de uma amostra por vez, a seguinte animação pode ajudar:</p>')
st.image('./assets/imagens/redes_neurais_zero/aula_02/figura_06.png',
         caption='Figura 2-6. Exemplo de uma equação linear ajustando lotes de 32 amostras escolhidas. Veja '
                 'a animação abaixo para outros tamanhos de amostras por vez para ver quanta diferença o '
                 'tamanho do lote pode fazer.')
with st.expander('Animação 2-10'):
    st.video('https://www.youtube.com/watch?v=s164HyJuL94')
st.html('<p class="fonte_texto">Um exemplo de lote de dados poderia ser assim:</p>')
with st.expander('Animação 2-11'):
    st.video('https://www.youtube.com/watch?v=9aeqyXT504o')
st.html('<p class="fonte_texto">Lembre-se de que em Python, e em nosso caso, as listas são recipientes '
        'úteis para armazenar uma amostra, bem como múltiplas amostras que constituem um lote de '
        'observações. Um exemplo de lote de observações, cada uma com sua própria amostra, é '
        'semelhante a:</p>')
st.code('''entradas = [
        [1, 2, 3, 2.5],
        [2, 5, -1, 2],
        [-1.5, 2.7, 3.3, -0.8]
]''', line_numbers=True)
st.html('<p class="fonte_texto">Esta lista de listas pode ser transformada em um array, pois é homóloga. '
        'Observe que cada “lista” nesta lista maior é uma amostra que representa um conjunto de recursos. '
        '<b>[1, 2, 3, 2.5]</b>, <b>[2, 5, -1, 2]</b> e <b>[-1.5, 2.7, 3.3, -0.8]</b> são todos '
        '<b>amostras</b> e também são chamados de <b>instâncias de conjunto de recursos</b> ou '
        '<b>observações</b>.</p>')
st.html('<p class="fonte_texto">Temos uma matriz de entradas e uma matriz de pesos agora, e precisamos '
        'realizar o produto escalar sobre eles de alguma forma, mas como e qual será o resultado? Da mesma '
        'forma, ao realizarmos um produto escalar em uma matriz e um vetor, tratamos a matriz como uma '
        'lista de vetores, resultando em uma lista de produtos escalares. Neste exemplo, precisamos '
        'gerenciar ambas as matrizes como listas de vetores e realizar produtos escalares em todas elas em '
        'todas as combinações, resultando em uma lista de listas de saídas, ou uma matriz; esta operação '
        'é chamada de <b>produto de matriz</b>.</p>')

# --- Produto de matriz --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Produto de matriz</h1>')
st.html('<p class="fonte_texto">O <b>produto de matrizes</b> é uma operação na qual temos 2 matrizes, e '
        'estamos realizando produtos escalares de todas as combinações de linhas da primeira matriz e das '
        'colunas da 2ª matriz, resultando em uma matriz desses <b>produtos escalares</b> atômicos:</p>')
st.image('./assets/imagens/redes_neurais_zero/aula_02/figura_07.png',
         caption='Figura 2-7. Visualizando como um único elemento na matriz resultante do produto matricial é '
                 'calculado. Veja a animação para o cálculo completo de cada elemento.')
with st.expander('Animação 2-12'):
    st.video('https://www.youtube.com/watch?v=KBPvlUp-m5Y')
st.html('<p class="fonte_texto">Para realizar um produto matricial, o tamanho da segunda dimensão da matriz '
        'esquerda deve corresponder ao tamanho da primeira dimensão da matriz direita. Por exemplo, se a '
        'matriz esquerda tiver uma forma de <i>(5, 4)</i> então a matriz direita deverá corresponder a este '
        '4 dentro do primeiro valor de forma <i>(4, 7)</i>. A forma do array resultante é sempre a '
        'primeira dimensão do array esquerdo e a segunda dimensão do array direito, <i>(5, 7)</i>. No '
        'exemplo acima, a matriz esquerda tem o formato <i>(5, 4)</i> e a matriz superior direita tem o '
        'formato <i>(4, 5)</i>. A segunda dimensão da matriz esquerda e a primeira dimensão da segunda '
        'matriz são ambas 4, elas correspondem e a matriz resultante tem o formato <i>(5, 5)</i>.</p>')
st.html('<p class="fonte_texto">Para elaborar, também podemos mostrar que podemos realizar o produto de '
        'matrizes em vetores. Em matemática, podemos ter algo chamado vetor coluna e vetor linha, que '
        'explicaremos melhor em breve. Eles são vetores, mas representados como matrizes com uma das '
        'dimensões tendo tamanho 1:</p>')
st.latex(r'''a=[1\hspace{3mm}2\hspace{3mm}3] \\
b=\begin{bmatrix}
2 \\
3 \\
4
\end{bmatrix}''')
st.html('<p class="fonte_texto"><i>a</i> é um vetor linha. É muito semelhante a um vetor <i>a</i> (com uma '
        'seta acima) descrito anteriormente junto com o produto vetorial. A diferença na notação entre um '
        'vetor linha e um vetor são vírgulas entre os valores e a seta acima do símbolo <i>a</i> está '
        'faltando em um vetor linha. É chamado de vetor linha porque é o vetor de uma linha de uma '
        'matriz. <i>b</i>, por outro lado, é chamado de vetor coluna porque é uma coluna de uma matriz. '
        'Como os vetores linha e coluna são tecnicamente matrizes, não os denotamos mais com setas '
        'vetoriais.</p>')
st.html('<p class="fonte_texto">Quando realizamos o produto matricial sobre eles, o resultado também se '
        'torna uma matriz, como no exemplo anterior, mas contendo apenas um único valor, o mesmo valor do '
        'exemplo do produto escalar que discutimos anteriormente:</p>')
st.latex(r'''ab=[1\hspace{3mm}2\hspace{3mm}3]
\begin{bmatrix}
2 \\
3 \\
4
\end{bmatrix}=[20]''')
with st.expander('Animação 2-13'):
    st.video('https://www.youtube.com/watch?v=UGPmXFdRJp4')
st.html('<p class="fonte_texto">Em outras palavras, vetores linha e coluna são matrizes com uma de suas '
        'dimensões tendo tamanho 1; e executamos o <b>produto de matriz</b> neles em vez do <b>produto '
        'escalar</b>, o que resulta em uma matriz contendo um único valor. Neste caso, realizamos uma '
        'multiplicação de matrizes com formas <i>(1, 3)</i> e <i>(3, 1)</i>, então o array resultante tem '
        'a forma <i>(1, 1)</i> ou um tamanho de <i>1x1</i>.</p>')

# --- Transposição para o produto matriz --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Transposição para o produto matriz</h1>')
st.html('<p class="fonte_texto">Como passamos repentinamente de 2 vetores para vetores de linha e coluna? '
        'Usamos a relação do produto escalar e do produto matricial dizendo que um produto escalar de dois '
        'vetores é igual a um produto matricial de um vetor linha e coluna (as setas acima das letras '
        'significam que são vetores):</p>')
st.latex(r'\vec{a}\cdot\vec{b}=ab^{T}')
st.html('<p class="fonte_texto">Também usamos temporariamente alguma simplificação, não mostrando que o '
        'vetor coluna <i>b</i> é na verdade um vetor <b>transposto</b> <i>b</i>. A equação adequada, '
        'combinando o produto escalar dos vetores <i>a</i> e <i>b</i> escrito como produto matricial, deve '
        'ser semelhante a:</p>')
st.latex(r'''ab^{T}=[1\hspace{3mm}2\hspace{3mm}3]
\begin{bmatrix}
2 \\
3 \\
4
\end{bmatrix}=[20]''')
st.html('<p class="fonte_texto">Aqui introduzimos mais uma nova operação, <b>transposição</b>. A '
        'transposição simplesmente modifica uma matriz de forma que suas linhas se tornem colunas e as '
        'colunas se tornem linhas:</p>')
st.image('./assets/imagens/redes_neurais_zero/aula_02/figura_08.png',
         caption='Figura 2-8. Exemplo de uma transposição de matriz.')
with st.expander('Animação 2-14'):
    st.video('https://www.youtube.com/watch?v=D-zJAbTxwtg')
st.image('./assets/imagens/redes_neurais_zero/aula_02/figura_09.png',
     caption='Figura 2-9. Outro exemplo de uma transposição de matriz.')
with st.expander('Animação 2-15'):
    st.video('https://www.youtube.com/watch?v=ZN60jdWk8aM')
st.html('<p class="fonte_texto">Agora precisamos voltar às definições de vetores de linha e coluna e '
        'atualizá-las com o que acabamos de aprender.</p>')
st.html('<p class="fonte_texto">Um vetor linha é uma matriz cujo tamanho da primeira dimensão (o número de '
        'linhas) é igual a 1 e o tamanho da segunda dimensão (o número de colunas) é igual a <i>n</i>; o '
        'tamanho do vetor. Em outras palavras, é uma matriz 1×n ou matriz de formato (1, n):</p>')
st.latex(r'a=[a_{1} a_{2} a_{3} \cdots a_{n}]')
st.html('<p class="fonte_texto">Com NumPy e com 3 valores, nós o definiríamos como:</p>')
st.code('np.array([[1, 2, 3]])', line_numbers=True)
st.html('<p class="fonte_texto">Observe o uso de colchetes duplos aqui. Para transformar uma lista em uma '
        'matriz contendo uma única linha (realizar uma operação equivalente de transformar um vetor em '
        'vetor linha), podemos colocá-la em uma lista e criar um array numpy:</p>')
st.code('''a = [1, 2, 3]
np.array([a])''', line_numbers=True)
st.html('<p class="fonte_texto">Novamente, observe que colocamos a entre colchetes antes de converter para '
        'um array neste caso. Ou podemos transformá-lo em um array 1D e expandir as dimensões usando uma '
        'das habilidades do NumPy:</p>')
st.code('''a = [1, 2, 3]
np.expand_dims(np.array[a], axis=0)''', line_numbers=True)
st.html('<p class="fonte_texto">Onde <b>np.expand_dims()</b> adiciona uma nova dimensão no índice do '
        '<i>axis</i>. Um vetor coluna é uma matriz onde o tamanho da segunda dimensão é igual a 1, ou seja, '
        'é uma matriz de forma (n, 1):</p>')
st.latex(r''' b=\begin{bmatrix}
b_{1} \\
b_{2} \\
b_{3} \\
\cdots  \\
b_{n} \\
\end{bmatrix}''')
st.html('<p class="fonte_texto">Com NumPy ele pode ser criado da mesma forma que um vetor linha, mas '
        'precisa ser transposto adicionalmente, a transposição transforma linhas em colunas e colunas em '
        'linhas:</p>')
st.latex(r'''[b_{1}\hspace{3mm}b_{2}\hspace{3mm}b_{3}\cdots b_{n}]^{T}=\begin{bmatrix}
b_{1} \\
b_{2} \\
b_{3} \\
\cdots \\
b_{n} \\
\end{bmatrix} \\
\begin{bmatrix}
b_{1} \\
b_{2} \\
b_{3} \\
\cdots \\
b_{n} \\
\end{bmatrix}^{T}=[b_{1}\hspace{3mm}b_{2}\hspace{3mm}b_{3}\cdots b_{n}]''')
st.html('<p class="fonte_texto">Para transformar o vetor <i>b</i> em vetor linha <i>b</i>, usaremos o mesmo '
        'método que usamos para transformar o vetor <i>a</i> em vetor linha <i>a</i>, então podemos '
        'realizar uma transposição nele para torná-lo um vetor coluna <i>b</i>:</p>')
st.latex(r'''b=[2\hspace{3mm}3\hspace{3mm}4] \\
b^{T}=[2\hspace{3mm}3\hspace{3mm}4]^{T}=\begin{bmatrix}
2 \\
3 \\
4 \\
\end{bmatrix}''')
st.html('<p class="fonte_texto">Com NumPy:</p>')
st.code('''import numpy as np

a = [1, 2, 3]
b = [2, 3, 4]

a = np.array([a])
b = np.array([b]).T

print(np.dot(a, b))''', line_numbers=True)
st.html('<p class="fonte_texto">Alcançamos o mesmo resultado do produto escalar de dois vetores, mas '
        'realizado em matrizes e retornando uma matriz, exatamente o que esperávamos e queríamos. Vale '
        'ressaltar que NumPy não possui um método dedicado para realizar o produto matricial, o produto '
        'escalar e o produto matricial são ambos implementados em um único método: <b>np.dot()</b>.</p>')
st.html('<p class="fonte_texto">Como podemos ver, para realizar um produto matricial em dois vetores, '
        'pegamos um como está, transformando-o em um vetor linha, e o segundo usando a transposição nele '
        'para transformá-lo em um vetor coluna. Isso nos permitiu realizar um produto matricial que '
        'retornava uma matriz contendo um único valor. Também realizamos o produto matricial em dois '
        'arrays de exemplo para aprender como funciona um produto matricial, ele cria uma matriz de '
        'produtos escalares de todas as combinações de vetores de linha e coluna.</p>')

# --- Uma camada de neurônios e lote de dados com NumPy --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Uma camada de neurônios e lote de dados com NumPy</h1>')
st.html('<p class="fonte_texto">Vamos voltar às nossas entradas e pesos, ao abordá-los, mencionamos que '
        'precisamos realizar produtos escalares em todos os vetores que consistem em matrizes de entradas '
        'e de pesos. Como acabamos de aprender, esta é a operação que o produto da matriz realiza. '
        'Precisamos apenas realizar a transposição em seu segundo argumento, que é a matriz de pesos no '
        'nosso caso, para transformar os vetores linha que a compõem atualmente em vetores coluna.</p>')
st.html('<p class="fonte_texto">Inicialmente, conseguimos realizar o produto escalar nas entradas e nos '
        'pesos sem transposição porque os pesos eram uma matriz, mas as entradas eram apenas um vetor. '
        'Nesse caso, o produto escalar resulta em um vetor de produtos escalares atômicos realizados em '
        'cada linha da matriz e deste único vetor. Quando os insumos se tornam um lote de insumos (uma '
        'matriz), precisamos realizar o produto da matriz. Ele pega todas as combinações de linhas da '
        'matriz esquerda e colunas da matriz direita, realizando o produto escalar sobre elas e colocando '
        'os resultados em uma matriz de saída. Ambas as matrizes têm a mesma forma, mas, para realizar o '
        'produto da matriz, o valor da forma do índice 1 da primeira matriz e o índice 0 da segunda matriz '
        'devem corresponder, o que não acontece agora.</p>')
st.code('''entradas = [
        [1, 2, 3, 2.5],
        [2, 5, -1, 2],
        [-1.5, 2.7, 3.3, -0.8]
]
pesos = [
        [0.2, 0.8, -0.5, 1],
        [0.5, -0.91, 0.26, -0.5],
        [-0.26, -0.27, 0.17, 0.87]
]''', line_numbers=True)
st.image('./assets/imagens/redes_neurais_zero/aula_02/figura_10.png',
         caption='Figura 2-10. Representação de por que precisamos transpor para realizar o produto'
                 'matricial.')
st.html('<p class="fonte_texto">Se transpormos o segundo array, os valores de sua forma trocam de '
        'posição.</p>')
st.image('./assets/imagens/redes_neurais_zero/aula_02/figura_11.png',
         caption='Figura 2-11. Após a transposição, podemos realizar o produto matricial.')
with st.expander('Animação 2-16'):
    st.video('https://www.youtube.com/watch?v=2c9CJ_7YT8w')
st.html('<p class="fonte_texto">Se olharmos isso da perspectiva da entrada e dos pesos, precisamos '
        'realizar o produto escalar de cada entrada e cada peso definido em todas as suas combinações. O '
        'produto escalar pega a linha da primeira matriz e a coluna da segunda, mas atualmente os dados '
        'em ambas as matrizes estão alinhados por linha. A transposição da segunda matriz molda os dados '
        'para serem alinhados às colunas. O produto matricial de entradas e pesos transpostos resultará em '
        'uma matriz contendo todos os produtos escalares atômicos que precisamos calcular. A matriz '
        'resultante consiste nas saídas de todos os neurônios após as operações realizadas em cada amostra '
        'de entrada:</p>')
st.code('''import numpy as np

entradas = [
        [1, 2, 3, 2.5],
        [2, 5, -1, 2],
        [-1.5, 2.7, 3.3, -0.8]
]
pesos = [
        [0.2, 0.8, -0.5, 1],
        [0.5, -0.91, 0.26, -0.5],
        [-0.26, -0.27, 0.17, 0.87]
]

saidas = np.dot(entradas, np.array(pesos).T)

print(saidas)''', line_numbers=True)
st.image('./assets/imagens/redes_neurais_zero/aula_02/figura_12.png',
         caption='Figura 2-12. Representação do produto escalar de entradas e pesos transpostos.')
with st.expander('Animação 2-17'):
    st.video('https://www.youtube.com/watch?v=ocrXqFCW3WE')
st.html('<p class="fonte_texto">Mencionamos que o segundo argumento para <b>np.dot()</b> serão nossos pesos '
        'transpostos, então primeiro serão as entradas, mas anteriormente os pesos eram o primeiro '
        'parâmetro. Nós mudamos isso aqui. Antes, estávamos modelando a saída do neurônio usando uma única '
        'amostra de dados, um vetor, mas agora estamos um passo à frente quando modelamos o comportamento '
        'da camada em um lote de dados. Poderíamos manter a ordem atual dos parâmetros, mas, como '
        'aprenderemos em breve, é mais útil ter um resultado que consiste em uma lista de saídas de camada '
        'para cada amostra do que uma lista de neurônios e suas saídas por amostra. Queremos que a matriz '
        'resultante seja relacionada à amostra e não aos neurônios, pois passaremos essas amostras pela '
        'rede e a próxima camada esperará um lote de entradas.</p>')
st.html('<p class="fonte_texto">Podemos codificar esta solução usando NumPy agora. Podemos executar '
        '<b>np.dot()</b> em uma lista de listas simples do Python, pois o NumPy irá convertê-las em '
        'matrizes internamente. No entanto, estamos convertendo os pesos para realizar primeiro a operação '
        'de transposição, <b>T</b> no código, já que a lista de listas simples do Python não suporta isso. '
        'Falando em vieses, não precisamos torná-lo um array NumPy pelo mesmo motivo, o NumPy fará '
        'isso internamente.</p>')
st.html('<p class="fonte_texto">Porém, os vieses são uma lista, portanto, são um array 1D como um '
        'array NumPy. A adição deste vetor de viés a uma matriz (dos produtos escalares, neste caso) '
        'funciona de forma semelhante ao produto escalar de uma matriz e um vetor que descrevemos '
        'anteriormente; o vetor de viés será adicionado a cada vetor linha da matriz. Como cada '
        'coluna do resultado do produto da matriz é uma saída de um neurônio, e o vetor será adicionado a '
        'cada vetor linha, o primeiro viés será adicionada a cada primeiro elemento desses vetores, '
        'segundo a segundo, etc. É disso que precisamos, o viés de cada neurônio precisa ser '
        'adicionada a todos os resultados deste neurônio realizados em todos os vetores de entrada '
        '(amostras).</p>')
st.code('''import numpy as np

entradas = [
        [1, 2, 3, 2.5],
        [2, 5, -1, 2],
        [-1.5, 2.7, 3.3, -0.8]
]
pesos = [
        [0.2, 0.8, -0.5, 1],
        [0.5, -0.91, 0.26, -0.5],
        [-0.26, -0.27, 0.17, 0.87]
]
vieses = [2, 3, 0.5]
saidas = np.dot(entradas, np.array(pesos).T) + vieses

print(saidas)''', line_numbers=True)
st.image('./assets/imagens/redes_neurais_zero/aula_02/figura_13.png',
         caption='Figura 2-13. Representação do produto escalar de entradas e pesos transpostos.')
with st.expander('Animação 2-18'):
    st.video('https://www.youtube.com/watch?v=iBCM3zkHXeo')
st.html('<p class="fonte_texto">Como você pode ver, nossa rede neural coleta um grupo de amostras '
        '(entradas) e gera um grupo de previsões. Se você usou alguma das bibliotecas de aprendizado '
        'profundo, é por isso que você passa uma lista de entradas (mesmo que seja apenas um conjunto de '
        'recursos) e recebe uma lista de previsões, mesmo que haja apenas uma previsão.</p>')