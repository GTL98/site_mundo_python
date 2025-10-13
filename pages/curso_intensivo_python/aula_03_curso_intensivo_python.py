# --- Importar as bibliotecas --- #
from PIL import Image
import streamlit as st

# --- Configurações iniciais da página --- #
st.set_page_config(
    page_title='Capítulo 03 - Introdução à listas',
    page_icon=Image.open('./assets/logo/logo.png'),
    layout='wide'
)

# --- Carregar o estilo das fontes --- #
with open('./assets/css/style.css', 'r') as css:
    st.html(f'<style>{css.read()}</style>')

# --- Colocar o banner do capítulo --- #
st.image('./assets/imagens/curso_intensivo_python/aula_03/aula_03.png')

# --- Introdução --- #
st.html('<h1 class="fonte_titulo_aula">Introdução</h1>')
st.html('<p class="fonte_texto">Neste capítulo e no próximo, você aprenderá o que são listas e como '
        'começar a trabalhar com os elementos em uma lista. As listas permitem que você armazene conjuntos '
        'de informações em um só lugar, quer você tenha apenas alguns itens ou milhões de itens. As listas '
        'são um dos recursos mais poderosos do Python prontamente acessíveis a novos programadores, e elas '
        'unem muitos conceitos importantes na programação.</p>')

# --- O que é uma lista? --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">O que é uma lista?</h1>')
st.html('<p class="fonte_texto">Uma <b>lista</b> é uma coleção de itens em uma ordem específica. Você '
        'pode fazer uma lista que inclua as letras do alfabeto, os dígitos de 0 a 9 ou os nomes de todas '
        'as pessoas da sua família. Você pode colocar o que quiser em uma lista, e os itens na sua lista '
        'não precisam estar relacionados de nenhuma maneira específica. Como uma lista geralmente contém '
        'mais de um elemento, é uma boa ideia tornar o nome da sua lista plural.</p>')
st.html('<p class="fonte_texto">Em Python, colchetes ([]) indicam uma lista, e elementos individuais na '
        'lista são separados por vírgulas. Aqui está um exemplo simples de uma lista que contém alguns '
        'tipos de bicicletas:</p>')
st.code("""bicicletas = ['elétrica', 'passeio', 'mountain bike', 'corrida']
print(bicicletas)""", line_numbers=True)
st.html('<p class="fonte_texto">Se você pedir ao Python para imprimir uma lista, o Python retornará '
        'sua representação da lista, incluindo os colchetes.</p>')
st.html('<p class="fonte_texto">Como esta não é a saída que você deseja que seus usuários vejam, '
        'vamos aprender como acessar os itens individuais em uma lista.</p>')

# --- Acessando elementos em uma lista --- #
st.html('<h2 class="fonte_subtitulo_aula">Acessando elementos em uma lista</h2>')
st.html('<p class="fonte_texto">Listas são coleções ordenadas, então você pode acessar qualquer elemento '
        'em uma lista informando ao Python a posição, ou <b>índice</b>, do item desejado. Para acessar '
        'um elemento em uma lista, escreva o nome da lista seguido pelo índice do item entre colchetes. '
        'Por exemplo, vamos retirar a primeira bicicleta da lista <i>bicicletas</i>:</p>')
st.code("""print(bicicletas[0])""", line_numbers=True)
st.html('<p class="fonte_texto">Quando solicitamos um único item de uma lista, o Python retorna apenas '
        'esse elemento sem colchetes. Este é o resultado que você quer que seus usuários vejam: uma saída '
        'limpa e bem formatada. Você também pode usar os métodos de string do Capítulo 2 em qualquer '
        'elemento desta lista. Por exemplo, você pode formatar o elemento <i>"elétrica"</i> para parecer '
        'mais apresentável usando o método <b>title()</b>:</p>')
st.code("""print(bicicletas[0].title())""", line_numbers=True)
st.html('<p class="fonte_texto">Este exemplo produz a mesma saída do exemplo anterior, exceto '
        'que <i>"Elétrica"</i> é escrito em maiúscula.</p>')

# --- As posições do índice começam em 0, não em 1 --- #
st.html('<h2 class="fonte_subtitulo_aula">As posições do índice começam em 0, não em 1</h2>')
st.html('<p class="fonte_texto">O Python considera o primeiro item em uma lista como estando na posição 0, '
        'não na posição 1. Isso é verdade para a maioria das linguagens de programação, e o motivo tem a ver '
        'com a forma como as operações de lista são implementadas em um nível mais baixo. Se você estiver '
        'recebendo resultados inesperados, pergunte a si mesmo se está cometendo um erro <i>offby-one</i> '
        'simples, mas comum.</p>')
st.html('<p class="fonte_texto">O segundo item em uma lista tem um índice de 1. Usando esse sistema de '
        'contagem, você pode obter qualquer elemento que quiser de uma lista subtraindo um de sua posição '
        'na lista. Por exemplo, para acessar o quarto item em uma lista, você solicita o item no '
        'índice 3:</p>')
st.code("""print(bicicletas[1])
print(bicicletas[3])""", line_numbers=True)
st.html('<p class="fonte_texto">Este código retorna a segunda e a quarta bicicleta da lista. Python tem '
        'uma sintaxe especial para acessar o último elemento em uma lista. Se você pedir o item no '
        'índice -1, Python sempre retorna o último item na lista:</p>')
st.html('<p class="fonte_texto">Este código retorna a segunda e a quarta bicicleta da lista. Python tem '
        'uma sintaxe especial para acessar o último elemento em uma lista. Se você pedir o item no '
        'índice -1, Python sempre retorna o último item na lista:</p>')
st.code("""print(bicicletas[-1])""", line_numbers=True)
st.html('<p class="fonte_texto">Este código retorna o valor <i>"corrida"</i>. Esta sintaxe é bem útil, '
        'porque você frequentemente desejará acessar os últimos itens em uma lista sem saber exatamente '
        'o quão longa a lista é. Esta convenção se estende a outros valores de índice negativo também. '
        'O índice -2 retorna o penúltimo item da lista, o índice -3 retorna o antepenúltimo item da lista, '
        'e assim por diante.</p>')

# --- Usando valores individuais de uma lista --- #
st.html('<h2 class="fonte_subtitulo_aula">Usando valores individuais de uma lista</h2>')
st.html('<p class="fonte_texto">Você pode usar valores individuais de uma lista assim como faria com '
        'qualquer outra variável. Por exemplo, você pode usar f-strings para criar uma mensagem com base '
        'em um valor de uma lista. Vamos tentar pegar a primeira bicicleta da lista e compor uma mensagem '
        'usando esse valor:</p>')
st.code("""mensagem = f'Minha primeira bicicleta foi uma {bicicletas[0].title()}'
print(mensagem)""", line_numbers=True)
st.html('<p class="fonte_texto">Construímos uma frase usando o valor em <i>bicicletas[0]</i> e atribuímos '
        'à variável mensagem. A saída é uma frase simples sobre a primeira bicicleta na lista.</p>')

# --- Tente você mesmo! --- #
st.html('<h2 class="fonte_subtitulo_aula">Tente você mesmo!</h2>')
st.html('<p class="fonte_texto"><b>Exercício 01:</b> Armazene os nomes de alguns dos seus amigos em '
        'uma lista chamada <i>nomes</i>. Imprima o nome de cada pessoa acessando cada elemento na '
        'lista, um de cada vez.</p>')
with st.expander('Resposta'):
    st.code("""# --- Lista com os nomes --- #
nomes = ['João', 'Maria', 'Lucas']

# --- Mostrar os nomes --- #
print(nomes[0])
print(nomes[1])
print(nomes[2])""", line_numbers=True)
st.html('<p class="fonte_texto"><b>Exercício 02:</b> Comece com a lista que você usou no exercício 1, '
        'mas em vez de apenas imprimir o nome de cada pessoa, imprima uma mensagem para elas. O texto '
        'de cada mensagem deve ser o mesmo, mas cada mensagem deve ser personalizada com o nome '
        'da pessoa.</p>')
with st.expander('Resposta'):
    st.code("""# --- Lista com os nomes --- #
nomes = ['João', 'Maria', 'Lucas']

# --- Escrever a mensagem de saudação com o nome da pessoa --- #
print(f'Que bom que você veio, {nomes[0]}')
print(f'Que bom que você veio, {nomes[1]}')
print(f'Que bom que você veio, {nomes[2]}')""", line_numbers=True)
st.html('<p class="fonte_texto"><b>Exercício 03:</b> Pense no seu meio de transporte favorito, como '
        'uma motocicleta ou um carro, e faça uma lista que armazene vários exemplos. Use sua lista para '
        'imprimir uma série de declarações sobre esses itens, como "Eu gostaria de ter uma moto Honda".</p>')
with st.expander('Resposta'):
    st.code("""# --- Lista com os veículos --- #
veiculos = ['volvo', 'ford', 'yamaha']

# --- Frase com os veículos --- #
print(f'Nós temos um carro da {veiculos[0].title()}')
print(f'Já tivemos um carro da {veiculos[1].title()}')
print(f'Nunca tivemos uma moto da {veiculos[2].title()}')""", line_numbers=True)

# --- Modificando, adicionando e removendo elementos --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Modificando, adicionando e removendo elementos</h1>')
st.html('<p class="fonte_texto">A maioria das listas que você criar será <b>dinâmica</b>, o que significa '
        'que você criará uma lista e então adicionará e removerá elementos dela conforme seu programa '
        'segue seu curso. Por exemplo, você pode criar um jogo no qual um jogador tem que atirar em '
        'alienígenas no céu. Você pode armazenar o conjunto inicial de alienígenas em uma lista e então '
        'remover um alienígena da lista toda vez que um for abatido. Cada vez que um novo alienígena '
        'aparecer na tela, você o adiciona à lista. Sua lista de alienígenas aumentará e diminuirá de '
        'tamanho ao longo do curso do jogo.</p>')

# --- Modificando elementos em uma lista --- #
st.html('<h2 class="fonte_subtitulo_aula">Modificando elementos em uma lista</h2>')
st.html('<p class="fonte_texto">A sintaxe para modificar um elemento é similar à sintaxe para acessar um '
        'elemento em uma lista. Para alterar um elemento, use o nome da lista seguido pelo índice do '
        'elemento que você quer alterar e então forneça o novo valor que você quer que o item tenha.</p>')
st.html('<p class="fonte_texto">Por exemplo, digamos que temos uma lista de motos e o primeiro item na '
        'lista é <i>"honda"</i>. Podemos alterar o valor deste primeiro item após a lista ter '
        'sido criada:</p>')
st.code("""motos = ['honda', 'yamaha', 'suzuki']
print(motos)

motos[0] = 'ducati'
print(motos)""", line_numbers=True)
st.html('<p class="fonte_texto">Aqui definimos a lista de motos, com <i>"honda"</i> como o primeiro '
        'elemento. Então mudamos o valor do primeiro item para <i>"ducati"</i>. A saída mostra que o '
        'primeiro item foi alterado, enquanto o resto da lista permanece o mesmo. Você pode alterar o '
        'valor de qualquer item em uma lista, não apenas o primeiro item.</p>')

# --- Adicionando elementos a uma lista --- #
st.html('<h2 class="fonte_subtitulo_aula">Adicionando elementos a uma lista</h2>')
st.html('<p class="fonte_texto">Você pode querer adicionar um novo elemento a uma lista por vários '
        'motivos. Por exemplo, você pode querer fazer novos alienígenas aparecerem em um jogo, adicionar '
        'novos dados a uma visualização ou adicionar novos usuários registrados a um site que você '
        'construiu. O Python fornece várias maneiras de adicionar novos dados a listas existentes.</p>')

# --- Acrescentando elementos ao final de uma lista --- #
st.html('<h3 class="fonte_sub_subtitulo_aula">Acrescentando elementos ao final de uma lista</h3>')
st.html('<p class="fonte_texto">A maneira mais simples de adicionar um novo elemento a uma lista é '
        'anexar o item à lista. Quando você anexa um item a uma lista, o novo elemento é adicionado ao '
        'final da lista. Usando a mesma lista que tínhamos no exemplo anterior, adicionaremos o novo '
        'elemento <i>"ducati"</i> ao final da lista:</p>')
st.code("""motos = ['honda', 'yamaha', 'suzuki']
print(motos)

motos.append('ducati')
print(motos)""", line_numbers=True)
st.html('<p class="fonte_texto">Aqui, o método <b>append()</b> adiciona <i>"ducati"</i> ao final da '
        'lista, sem afetar nenhum dos outros elementos da lista. O método <b>append()</b> facilita a '
        'construção dinâmica de listas. Por exemplo, você pode começar com uma lista vazia e então '
        'adicionar itens à lista usando uma série de chamadas <b>append()</b>. Usando uma lista vazia, '
        'vamos adicionar os elementos <i>"honda"</i>, <i>"yamaha"</i> e <i>"suzuki"</i> à lista:</p>')
st.code("""motos = []

motos.append('honda')
motos.append('yamaha')
motos.append('suzuki')

print(motos)""", line_numbers=True)
st.html('<p class="fonte_texto">A lista resultante é exatamente igual às listas dos exemplos '
        'anteriores. Construir listas dessa forma é muito comum, porque você frequentemente não saberá '
        'os dados que seus usuários querem armazenar em um programa até que o programa esteja em '
        'execução. Para colocar seus usuários no controle, comece definindo uma lista vazia que conterá '
        'os valores dos usuários. Então anexe cada novo valor fornecido à lista que você '
        'acabou de criar.</p>')

# --- Inserindo elementos em uma lista --- #
st.html('<h3 class="fonte_sub_subtitulo_aula">Inserindo elementos em uma lista</h3>')
st.html('<p class="fonte_texto">Você pode adicionar um novo elemento em qualquer posição da sua lista '
        'usando o método <b>insert()</b>. Você faz isso especificando o índice do novo elemento e o '
        'valor do novo item:</p>')
st.code("""motos = ['honda', 'yamaha', 'suziki']
motos.insert(0, 'ducati')
print(motos)""", line_numbers=True)
st.html('<p class="fonte_texto">Neste exemplo, inserimos o valor <i>"ducati"</i> no início da lista. '
        'O método <b>insert()</b> abre um espaço na posição 0 e armazena o valor <i>"ducati"</i> naquele '
        'local. Esta operação desloca todos os outros valores na lista uma posição para a direita.</p>')

# --- Removendo elementos de uma lista --- #
st.html('<h2 class="fonte_subtitulo_aula">Removendo elementos de uma lista</h2>')
st.html('<p class="fonte_texto">Frequentemente, você desejará remover um item ou um conjunto de itens '
        'de uma lista. Por exemplo, quando um jogador derruba um alienígena do céu, você provavelmente '
        'desejará removê-lo da lista de alienígenas ativos. Ou quando um usuário decide cancelar sua '
        'conta em um aplicativo da web que você criou, você desejará remover esse usuário da lista de '
        'usuários ativos. Você pode remover um item de acordo com sua posição na lista ou de acordo com '
        'seu valor.</p>')

# --- Removendo um item usando a instrução del --- #
st.html('<h3 class="fonte_sub_subtitulo_aula">Removendo um item usando a instrução del</h3>')
st.html('<p class="fonte_texto">Se você souber a posição do item que deseja remover de uma lista, '
        'poderá usar a instrução <b>del</b>:</p>')
st.code("""motos = ['honda', 'yamaha', 'suziki']
print(motos)

del motos[0]
print(motos)""", line_numbers=True)
st.html('<p class="fonte_texto">Aqui usamos a instrução del para remover o primeiro item, <i>"honda"</i>, '
        'da lista de motos. Você pode remover um item de qualquer posição em uma lista usando a instrução '
        '<b>del</b> se você souber seu índice. Por exemplo, aqui está como remover o segundo item, '
        '<i>"yamaha"</i>, da lista:</p>')
st.code("""motos = ['honda', 'yamaha', 'suziki']
print(motos)

del motos[1]
print(motos)""", line_numbers=True)
st.html('<p class="fonte_texto">A segunda motocicleta é excluída da lista. Em ambos os exemplos, você '
        'não pode mais acessar o valor que foi removido da lista depois que a instrução <b>del</b> '
        'foi usada.</p>')

# --- Removendo um item usando o método pop() --- #
st.html('<h3 class="fonte_sub_subtitulo_aula">Removendo um item usando o método pop()</h3>')
st.html('<p class="fonte_texto">Às vezes, você vai querer usar o valor de um item depois de removê-lo de '
        'uma lista. Por exemplo, você pode querer obter a posição <i>x</i> e <i>y</i> de um alienígena '
        'que acabou de ser abatido, para poder desenhar uma explosão nessa posição. Em um aplicativo da '
        'web, você pode querer remover um usuário de uma lista de membros ativos e, em seguida, adicionar '
        'esse usuário a uma lista de membros inativos.</p>')
st.html('<p class="fonte_texto">O método <b>pop()</b> remove o último item de uma lista, mas permite que '
        'você trabalhe com esse item após removê-lo. O termo pop vem de pensar em uma lista como uma '
        'pilha de itens e retirar um item do topo da pilha. Nessa analogia, o topo de uma pilha corresponde '
        'ao fim de uma lista. Vamos tirar uma moto da lista de motos:</p>')
st.code("""motos = ['honda', 'yamaha', 'suziki']  # 1
print(motos)

moto_tirada = motos.pop()  # 2
print(motos)  # 3
print(moto_tirada)  # 4""", line_numbers=True)
st.html('<p class="fonte_texto">Começamos definindo e imprimindo a lista <i>motos</i> (1). Então, '
        'retiramos um valor da lista e atribuímos esse valor à variável <i>moto_tirada</i> (2). '
        'Imprimimos a lista (3) para mostrar que um valor foi removido da lista. Então, imprimimos o '
        'valor retirado (4) para provar que ainda temos acesso ao valor que foi removido. '
        'A saída mostra que o valor <i>"suzuki"</i> foi removido do final da lista e agora está '
        'atribuído à variável <i>moto_tirada</i>.</p>')
st.html('<p class="fonte_texto">Como esse método <b>pop()</b> pode ser útil? Imagine que as motos na '
        'lista são armazenadas em ordem cronológica, de acordo com quando as possuímos. Se esse for o '
        'caso, podemos usar o método <b>pop()</b> para imprimir uma declaração sobre a última moto '
        'que compramos:</p>')
st.code("""motos = ['honda', 'yamaha', 'suzuki']
ultima_compra = motos.pop()
print(f'A última moto que comprei foi a {ultima_compra.title()}')""", line_numbers=True)
st.html('<p class="fonte_texto">O resultado é uma frase simples sobre a moto mais recente que compramos.</p>')

# --- Retirando itens de qualquer posição em uma lista --- #
st.html('<h3 class="fonte_sub_subtitulo_aula">Retirando itens de qualquer posição em uma lista</h3>')
st.html('<p class="fonte_texto">Você pode usar <b>pop()</b> para remover um item de qualquer posição '
        'em uma lista incluindo o índice do item que deseja remover entre parênteses:</p>')
st.code("""motos = ['honda', 'yamaha', 'suzuki']
primeira_compra = motos.pop(0)
print(f'A primeira moto que comprei foi a {primeira_compra.title()}')""", line_numbers=True)
st.html('<p class="fonte_texto">Começamos colocando a primeira moto na lista e então imprimimos uma '
        'mensagem sobre essa moto. A saída é uma frase simples descrevendo a primeira moto que tive. '
        'Lembre-se de que cada vez que você usa <b>pop()</b>, o item com o qual você trabalha não é '
        'mais armazenado na lista.</p>')
st.html('<p class="fonte_texto">Se você não tiver certeza se deve usar a instrução <b>del</b> ou o método '
        '<b>pop()</b>, aqui está uma maneira simples de decidir: quando quiser excluir um item de uma '
        'lista e não usá-lo de forma alguma, use a instrução <b>del</b>; se quiser usar um item ao '
        'removê-lo, use o método <b>pop()</b>.</p>')

# --- Removendo um item por valora --- #
st.html('<h3 class="fonte_sub_subtitulo_aula">Removendo um item por valor</h3>')
st.html('<p class="fonte_texto">Às vezes, você não saberá a posição do valor que deseja remover de uma '
        'lista. Se você só souber o valor do item que deseja remover, poderá usar o método <b>remove()</b>. '
        'Por exemplo, digamos que queremos remover o valor <i>"ducati"</i> da lista de motos:</p>')
st.code("""motos = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motos)

motos.remove('ducati')
print(motos)""", line_numbers=True)
st.html('<p class="fonte_texto">Aqui, o método <b>remove()</b> diz ao Python para descobrir onde '
        '"<i>ducati"</i> aparece na lista e remover esse elemento. Você também pode usar o método '
        '<b>remove()</b> para trabalhar com um valor que está sendo removido de uma lista. Vamos remover '
        'o valor <i>"ducati"</i> e imprimir um motivo para removê-lo da lista:</p>')
st.code("""motos = ['honda', 'yamaha', 'suzuki', 'ducati']  # 1
print(motos)

muito_cara = 'ducati'  # 2
motos.remove(muito_cara)  # 3
print(motos)
print(f'\nA moto {muito_cara.title()} é muito cara para mim')  # 4""", line_numbers=True)
st.html('<p class="fonte_texto">Após definir a lista (1), atribuímos o valor <i>"ducati"</i> a uma variável '
        'chamada <i>muito_cara</i> (2). Em seguida, usamos essa variável para informar ao Python qual '
        'valor remover da lista (3). O valor <i>"ducati"</i> foi removido da lista (4), mas ainda é '
        'acessível por meio da variável <i>muito_cara</i>, permitindo-nos imprimir uma declaração sobre '
        'o motivo pelo qual removemos <i>"ducati"</i> da lista de motos.</p>')
st.html('<p class="fonte_texto">O método <b>remove()</b> exclui apenas a primeira ocorrência do valor '
        'que você especificar. Se houver a possibilidade de o valor aparecer mais de uma vez na lista, '
        'você precisará usar um loop para garantir que todas as ocorrências do valor sejam removidas.</p>')

# --- Tente você mesmo! --- #
st.html('<h2 class="fonte_subtitulo_aula">Tente você mesmo!</h2>')
st.html('<p class="fonte_texto"><b>Exercício 04:</b> Se você pudesse convidar alguém, vivo ou falecido, '
        'para jantar, quem você convidaria? Faça uma lista que inclua pelo menos três pessoas que você '
        'gostaria de convidar para jantar. Então use sua lista para imprimir uma mensagem para cada '
        'pessoa, convidando-as para jantar.</p>')
with st.expander('Resposta'):
    st.code("""# --- Lista com os convidados --- #
convidados = ['Vivaldi', 'Bach', 'Mozart']

# --- Escrver a mensagem do convite --- #
print(f'Compareça ao meu jantar, {convidados[0]} e toque Primavera!')
print(f'Compareça ao meu jantar, {convidados[1]} e anime o pessoal com o Bourée em E menor')
print(f'Compareça ao meu jantar, {convidados[2]} e divirta o pessoal com Sonata No. 16 em C maior')""", line_numbers=True)
st.html('<p class="fonte_texto"><b>Exercício 05:</b> Você acabou de ouvir que um dos seus convidados '
        'não pode ir ao jantar, então você precisa enviar um novo conjunto de convites. Você terá que '
        'pensar em outra pessoa para convidar:</p>')
st.html('<ul class="fonte_texto">'
        '<li>Comece com seu programa do exercício 4. Adicione uma chamada <b>print()</b> no final do seu '
        'programa, informando o nome do convidado que não pode comparecer.</li>'
        '<li>Modifique sua lista, substituindo o nome do convidado que não pode comparecer pelo nome '
        'da nova pessoa que você está convidando.</li>'
        '<li>Imprima um segundo conjunto de mensagens de convite, uma para cada pessoa que ainda '
        'está na sua lista.</li>'
        '</ul>')
with st.expander('Resposta'):
        st.code('''# --- Lista com os convidados --- #
convidados = ['Vivaldi', 'Bach', 'Mozart']

# --- Avisar qual convidado não pode comparecer --- #
print(f'O convidado {convidados[1]} não pode comparecer')

# --- Trocar o convidado que não pode comparecer --- #
convidados[1] = 'Handel'

# --- Escrever a mensagem do convite --- #
print(f'Compareça ao meu jantar, {convidados[0]} e toque Primavera!')
print(f'Compareça ao meu jantar, {convidados[1]} e toque Hallelujah')
print(f'Compareça ao meu jantar, {convidados[2]} e divirta o pessoal com Sonata No. 16 em C maior')''', line_numbers=True)
st.html('<p class="fonte_texto"><b>Exercício 06:</b> Você acabou de encontrar uma mesa de jantar maior, '
        'então agora há mais espaço disponível. Pense em mais três convidados para convidar para '
        'o jantar:</p>')
st.html('<ul class="fonte_texto">'
        '<li>Comece com seu programa do exercício 4 ou 5. Adicione uma chamada <b>print()</b> ao final do '
        'seu programa, informando às pessoas que você encontrou uma mesa maior.</li>'
        '<li>Use <b>insert()</b> para adicionar um novo convidado ao início da sua lista.</li>'
        '<li>Use <b>insert()</b> para adicionar um novo convidado no meio da sua lista.</li>'
        '<li>Use <b>append()</b> para adicionar um novo convidado ao final da sua lista.</li>'
        '<li>Imprima um novo conjunto de mensagens de convite, uma para cada pessoa na sua lista.</li>'
        '</ul>')
with st.expander('Resposta'):
        st.code('''# --- Lista com os convidados --- #
convidados = ['Vivaldi', 'Bach', 'Mozart']

# --- Inserir mais convidados --- #
convidados.insert(0, 'Salieri')
convidados.insert(2, 'Handel')

# --- Adicionar ao final da lista o último convidado --- #
convidados.append('Beethoven')

# --- Escrever a mensagem do convite --- #
print(f'{convidados[0]}, venha para a minha festa! Há uma mesa maior dessa vez!')
print(f'{convidados[1]}, venha para a minha festa! Há uma mesa maior dessa vez!')
print(f'{convidados[2]}, venha para a minha festa! Há uma mesa maior dessa vez!')
print(f'{convidados[3]}, venha para a minha festa! Há uma mesa maior dessa vez!')
print(f'{convidados[4]}, venha para a minha festa! Há uma mesa maior dessa vez!')
print(f'{convidados[5]}, venha para a minha festa! Há uma mesa maior dessa vez!')''', line_numbers=True)
st.html('<p class="fonte_texto"><b>Exercício 07:</b> Você acabou de descobrir que sua nova mesa de jantar '
        'não chegará a tempo para o jantar e agora você tem espaço para apenas dois convidados:</p>')
st.html('<ul class="fonte_texto">'
        '<li>Comece com seu programa do exercício 6. Adicione uma nova linha que imprima uma mensagem dizendo '
        'que você pode convidar apenas duas pessoas para o jantar.</li>'
        '<li>Use <b>pop()</b> para remover convidados da sua lista, um de cada vez, até que restem apenas dois '
        'nomes na sua lista. Cada vez que você remover um nome da sua lista, imprima uma mensagem para essa '
        'pessoa informando que você lamenta não poder convidá-la para jantar.</li>'
        '<li>Imprima uma mensagem para cada uma das duas pessoas que ainda estão na sua lista, informando '
        'que ainda estão convidadas.</li>'
        '<li>Use <b>del</b> para remover os dois últimos nomes da sua lista, para que você tenha uma lista '
        'vazia. Imprima sua lista para ter certeza de que você realmente tem uma lista vazia no final do seu '
        'programa.</li>'
        '</ul>')
with st.expander('Resposta'):
        st.code('''# --- Lista com os convidados --- #
convidados = ['Vivaldi', 'Bach', 'Mozart']

# --- Inserir mais convidados --- #
convidados.insert(0, 'Salieri')
convidados.insert(2, 'Handel')

# --- Adicionar ao final da lista o último convidado --- #
convidados.append('Beethoven')

# --- Mensagem que só posso conidar duas pessoas --- #
print('Perdão pelo transtono, mas só posso convidar duas pessoas')

# --- Retirar os convidados da lista --- #
convidado_1 = convidados.pop()
convidado_2 = convidados.pop()
convidado_3 = convidados.pop()
convidado_4 = convidados.pop()

# --- Mensagem para cada convidado retirado da lista --- #
print(f'Desculpe o transtorno, {convidado_1}, mas você não está mais convidado')
print(f'Desculpe o transtorno, {convidado_2}, mas você não está mais convidado')
print(f'Desculpe o transtorno, {convidado_3}, mas você não está mais convidado')
print(f'Desculpe o transtorno, {convidado_4}, mas você não está mais convidado')

# --- Mensagem para os convidados que ainda estão na lista --- #
print(f'{convidados[0]}, você ainda está convidado para a festa')
print(f'{convidados[1]}, você ainda está convidado para a festa')

# --- Deletar os convidados da lista --- #
del convidados[0]
del convidados[0]

# --- Mostrar que a lista de convidados está vazia --- #
print(f'Lista de convidados: {convidados}')''', line_numbers=True)


# --- Organizando uma lista --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">O que é uma lista?</h1>')
st.html('<p class="fonte_texto">Frequentemente, suas listas serão criadas em uma ordem imprevisível, '
        'porque você nem sempre pode controlar a ordem em que seus usuários fornecem seus dados. Embora '
        'isso seja inevitável na maioria das circunstâncias, você frequentemente desejará apresentar suas '
        'informações em uma ordem específica. Às vezes, você desejará preservar a ordem original de sua '
        'lista e, outras vezes, desejará alterar a ordem original. O Python fornece várias maneiras '
        'diferentes de organizar suas listas, dependendo da situação.</p>')
st.html('<h2 class="fonte_subtitulo_aula">Classificando uma lista permanentemente com o método '
        '<b>sort()</b></h2>')
st.html('<p class="fonte_texto">O método <b>sort()</b> do Python torna relativamente fácil classificar '
        'uma lista. Imagine que temos uma lista de carros e queremos alterar a ordem da lista para '
        'armazená-los em ordem alfabética. Para manter a tarefa simples, vamos supor que todos os valores '
        'na lista sejam minúsculos:</p>')
st.code('''carros = ['bmw', 'audi', 'toyota', 'subaru']
carros.sort()
print(carros)''', line_numbers=True)
st.html('<p class="fonte_texto">O método <b>sort()</b> altera a ordem da lista permanentemente. Os carros '
        'agora estão em ordem alfabética, e nunca podemos reverter para a ordem original. Você também pode '
        'classificar esta lista em ordem alfabética reversa passando o argumento <b>reverse=True</b> para '
        'o método <b>sort()</b>. O exemplo a seguir classifica a lista de carros em ordem alfabética '
        'reversa:</p>')
st.code('''carros = ['bmw', 'audi', 'toyota', 'subaru']
carros.sort(reverse=True)
print(carros)''')
st.html('<p class="fonte_texto">Novamente, a ordem da lista é alterada permanentemente.</p>')
st.html('<h2 class="fonte_subtitulo_aula">Classificando uma lista temporariamente com a função '
        '<b>sorted()</b></h2>')
st.html('<p class="fonte_texto">Para manter a ordem original de uma lista, mas apresentá-la em uma ordem '
        'classificada, você pode usar a função <b>sorted()</b>. A função <b>sorted()</b> permite que você '
        'exiba sua lista em uma ordem específica, mas não afeta a ordem real da lista. Vamos tentar esta '
        'função na lista de carros:</p>')
st.code(r'''carros = ['bmw', 'audi', 'toyota', 'subaru']

print('Lista original:')  # 1
print(carros)

print('\nLista ordenada:')  # 2
print(sorted(carros))

print('\nLista original de volta:')  # 3
print(carros)''', line_numbers=True)
st.html('<p class="fonte_texto">Primeiro imprimimos a lista em sua ordem original (1) e depois em ordem '
        'alfabética (2). Depois que a lista é exibida na nova ordem, mostramos que a lista ainda está '
        'armazenada em sua ordem original (3).</p>')
st.html('<p class="fonte_texto">Observe que a lista ainda existe em sua ordem original após a função '
        '<b>sorted()</b> ter sido usada. A função <b>sorted()</b> também pode aceitar um argumento '
        '<b>reverse=True</b> se você quiser exibir uma lista em ordem alfabética reversa.</p>')
st.html('<p class="fonte_texto">Classificar uma lista alfabeticamente é um pouco mais complicado quando '
        'todos os valores não estão em minúsculas. Há várias maneiras de interpretar letras maiúsculas '
        'ao determinar uma ordem de classificação, e especificar a ordem exata pode ser mais complexo do '
        'que queremos lidar neste momento. No entanto, a maioria das abordagens para classificação se '
        'baseará diretamente no que você aprendeu nesta seção.</p>')
st.html('<h2 class="fonte_subtitulo_aula">Imprimindo uma lista em ordem reversa</h2>')
st.html('<p class="fonte_texto">Para reverter a ordem original de uma lista, você pode usar o método '
        '<b>reverse()</b>. Se originalmente armazenássemos a lista de carros em ordem cronológica de '
        'acordo com quando os possuímos, poderíamos facilmente reorganizar a lista em ordem cronológica '
        'reversa:</p>')
st.code('''carros = ['bmw', 'audi', 'toyota', 'subaru']
print(carros)

carros.reverse()
print(carros)''', line_numbers=True)
st.html('<p class="fonte_texto">Observe que <b>reverse()</b> não classifica alfabeticamente para trás; '
        'ele simplesmente inverte a ordem da lista. Esse método altera a ordem de uma lista '
        'permanentemente, mas você pode reverter para a ordem original a qualquer momento aplicando '
        '<b>reverse()</b> à mesma lista uma segunda vez.</p>')
st.html('<h2 class="fonte_subtitulo_aula">Encontrando o comprimento de uma lista</h2>')
st.html('<p class="fonte_texto">Você pode encontrar rapidamente o comprimento de uma lista usando a função '
        '<b>len()</b>. A lista neste exemplo tem quatro itens, então seu comprimento é 4:</p>')
st.code('''carros = ['bmw', 'audi', 'toyota', 'subaru']
len(carros)''', line_numbers=True)
st.html('<p class="fonte_texto">Você achará <b>len()</b> útil quando precisar identificar o número de '
        'alienígenas que ainda precisam ser abatidos em um jogo, determinar a quantidade de dados que '
        'você precisa gerenciar em uma visualização ou descobrir o número de usuários registrados em '
        'um site, entre outras tarefas.</p>')
st.html('<p class="fonte_texto">O Python conta os itens em uma lista começando com 1, então você não deve '
        'encontrar erros de defasagem de um ao determinar o comprimento de uma lista.</p>')
st.html('<h2 class="fonte_subtitulo_aula">Tente você mesmo!</h2>')
st.html('<p class="fonte_texto"><b>Exercício 08:</b> Pense em pelo menos cinco lugares no mundo que '
        'você gostaria de visitar:</p>')
st.html('<ul class="fonte_texto">'
        '<li>Armazene os locais em uma lista. Certifique-se de que a lista não esteja em ordem '
        'alfabética.</li>'
        '<li>Imprima sua lista na ordem original. Não se preocupe em imprimir a lista ordenadamente; '
        'apenas imprima-a como uma lista Python bruta.</li>'
        '<li>Use <b>sorted()</b> para imprimir sua lista em ordem alfabética sem modificar a lista '
        'real.</li>'
        '<li>Mostre que sua lista ainda está na ordem original imprimindo-a.</li>'
        '<li>Use <b>sorted()</b> para imprimir sua lista em ordem alfabética reversa sem alterar a '
        'ordem da lista original.</li>'
        '<li>Mostre que sua lista ainda está na ordem original imprimindo-a novamente.</li>'
        '<li>Use <b>reverse()</b> para alterar a ordem da sua lista. Imprima a lista para mostrar que '
        'sua ordem mudou.</li>'
        '<li>Use <b>reverse()</b> para alterar a ordem da sua lista novamente. Imprima a lista para '
        'mostrar que ela voltou à ordem original.</li>'
        '<li>Use <b>sort()</b> para alterar sua lista para que ela seja armazenada em ordem alfabética. '
        'Imprima a lista para mostrar que sua ordem foi alterada.</li>'
        '<li>Use <b>sort()</b> para alterar sua lista para que ela seja armazenada em ordem alfabética '
        'reversa. Imprima a lista para mostrar que sua ordem mudou.</li>'
        '</ul>')
with st.expander('Resposta'):
        st.code('''# --- Lista com os lugares --- #
lugares = ['Treviso', 'Houston', 'Las Vegas', 'Paris']

# --- Lista original --- #
print(f'Lista original: {lugares}')

# --- Lista ordenada temporariamente --- #
print(f'Lista ordenada temporariamente: {sorted(lugares)}')

# --- Lista original --- #
print(f'Lista original: {lugares}')

# --- Lista ordenada de modo reverso temporariamente --- #
print(f'Lista ordenada de modo reverso temporariamente: {sorted(lugares, reverse=True)}')

# --- Lista original --- #
print(f'Lista original: {lugares}')

# --- Lista no modo reverso permanentemente --- #
lugares.reverse()
print(f'Lista no modo reverso permanentemente: {lugares}')

# --- Lista na ordem original --- #
lugares.reverse()
print(f'Lista na ordem original: {lugares}')

# --- Lista ordenada permanentemente --- #
lugares.sort()
print(f'Lista ordenada permanetemente: {lugares}')

# --- Lista ordenada de modo reverso permanentemente --- #
lugares.sort(reverse=True)
print(f'Lista ordenada de modo reverso permanentemente: {lugares})''', line_numbers=True)
st.html('<p class="fonte_texto"><b>Exercício 09:</b> Trabalhando com um dos programas dos exercícios 4 a 7, '
        'use <b>len()</b> para imprimir uma mensagem indicando o número de pessoas que você está convidando para '
        'jantar.</p>')
with st.expander('Resposta'):
        st.code('''# --- Lista com os convidados --- #
convidados = ['Vivaldi', 'Bach', 'Mozart']
print(f'Quantidade de convidados: {len(convidados)}')

# --- Inserir mais convidados --- #
convidados.insert(0, 'Salieri')
print(f'Quantidade de convidados: {len(convidados)}')
convidados.insert(2, 'Handel')
print(f'Quantidade de convidados: {len(convidados)}')

# --- Adicionar ao final da lista o último convidado --- #
convidados.append('Beethoven')
print(f'Quantidade de convidados: {len(convidados)}')

# --- Retirar os convidados da lista --- #
convidado_1 = convidados.pop()
print(f'Quantidade de convidados: {len(convidados)}')

convidado_2 = convidados.pop()
print(f'Quantidade de convidados: {len(convidados)}')

convidado_3 = convidados.pop()
print(f'Quantidade de convidados: {len(convidados)}')

convidado_4 = convidados.pop()
print(f'Quantidade de convidados: {len(convidados)}')

del convidados[0]
print(f'Quantidade de convidados: {len(convidados)}')

del convidados[0]
print(f'Quantidade de convidados: {len(convidados)}')''', line_numbers=True)
st.html('<p class="fonte_texto"><b>Exercício 09:</b> Pense em coisas que você poderia armazenar em uma '
        'lista. Por exemplo, você poderia fazer uma lista de montanhas, rios, países, cidades, idiomas ou '
        'qualquer outra coisa que você queira. Escreva um programa que crie uma lista contendo esses itens '
        'e então use cada função introduzida neste capítulo pelo menos uma vez.</p>')
with st.expander('Resposta'):
        st.code('''# --- Lista de compras --- #
compras = ['macarrão', 'arroz', 'manteiga', 'feijão']
print(f'Lista original: {compras}')

# --- Adicionar um item ao final da lista --- #
compras.append('banana')
print(f'Lista adicionado (append): {compras}')

# --- Adicionar um item em qualquer posição da lista --- #
compras.insert(2, 'uva')
print(f'Lista adicionado (insert): {compras}')

# --- Remover um item pelo índice --- #
del compras[0]
print(f'Lista com um item removido pelo índice: {compras}')

# --- Retirar e obter o último item da lista --- #
ultimo_item = compras.pop()
print(f'Último item: {ultimo_item}')
print(f'Lista sem o último item: {compras}')

# --- Remover um item pelo valor --- #
valor_removido = 'feijão'
print(f'Valor removido: {valor_removido}')
compras.remove(valor_removido)

print(f'Lista com um item removido pelo valor: {compras}')

# --- Ordenar de modo alfabético temporariamente --- #
print(f'Lista de compras ordenada alfabeticamente temporariamente: {sorted(compras)}')

# --- Inverter a ordem de entrada da lista --- #
compras.reverse()
print(f'Lista com a ordem de entrada invertida: {compras}')

# --- Ordenar alfabeticamente de modo permanente --- #
compras.sort()
print(f'Lista ordenada alfabeticamente de modo permanente: {compras}')''', line_numbers=True)

# --- Evitando erros de índice ao trabalhar com listas --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Evitando erros de índice ao trabalhar com listas</h1>')
st.html('<p class="fonte_texto">Há um tipo de erro que é comum ver quando você está trabalhando com listas '
        'pela primeira vez. Digamos que você tem uma lista com três itens e pede o quarto item:</p>')
st.code('''motos = ['honda', 'yamaha', 'suzuki']
print(motos[3])''', line_numbers=True)
st.html('<p class="fonte_texto">Este exemplo resulta em um <i>erro de índice</i>.</p>')
st.html('<p class="fonte_texto">O Python tenta fornecer o item no índice 3. Mas quando ele pesquisa a '
        'lista, nenhum item em motos tem um índice de 3. Devido à natureza de defasagem de um da indexação '
        'em listas, esse erro é típico. As pessoas acham que o terceiro item é o item número 3, porque '
        'começam a contar em 1. Mas no Python o terceiro item é o número 2, porque começa a indexação '
        'em 0.</p>')
st.html('<p class="fonte_texto">Um erro de índice significa que o Python não consegue encontrar um item '
        'no índice que você solicitou. Se um erro de índice ocorrer no seu programa, tente ajustar o '
        'índice que você está solicitando em 1. Em seguida, execute o programa novamente para ver se os '
        'resultados estão corretos.</p>')
st.html('<p class="fonte_texto">Tenha em mente que sempre que você quiser acessar o último item de uma '
        'lista, você deve usar o índice <b>-1</b>. Isso sempre funcionará, mesmo que sua lista tenha '
        'mudado de tamanho desde a última vez que você a acessou:</p>')
st.code('print(motos[-1]', line_numbers=True)
st.html('<p class="fonte_texto">O índice <b>-1</b> sempre retorna o último item de uma lista, neste caso '
        'o valor <b>"suzuki"</b>. A única vez que essa abordagem causará um erro é quando você solicita '
        'o último item de uma lista vazia:</p>')
st.code('''motos = []
print(motos[-1])''', line_numbers=True)
st.html('<p class="fonte_texto">Não há itens em <b>motos</b>, então Python retorna outro erro de índice. '
        'Se ocorrer um erro de índice e você não conseguir descobrir como resolvê-lo, tente imprimir sua '
        'lista ou apenas imprimir o comprimento da lista. Sua lista pode parecer muito diferente do que '
        'você pensou que era, especialmente se ela foi gerenciada dinamicamente pelo seu programa. Ver a '
        'lista real, ou o número exato de itens na sua lista, pode ajudar a resolver esses erros '
        'lógicos.</p>')
st.html('<h2 class="fonte_subtitulo_aula">Tente você mesmo!</h2>')
st.html('<p class="fonte_texto"><b>Exercício 11:</b> Se você ainda não recebeu um erro de índice em um '
        'dos seus programas, tente fazer um acontecer. Altere um índice em um dos seus programas para '
        'produzir um erro de índice. Certifique-se de corrigir o erro antes de fechar o programa.</p>')
with st.expander('Resposta'):
        st.code('''# --- Criar a lista --- #
compras = ['arroz', 'feijão', 'banana']

# --- Gerar o erro --- #
print(compras[3])''', line_numbers=True)

# --- Resumo --- #
st.html('<h1 class="fonte_titulo_aula">Resumo</h1>')
st.html('<p class="fonte_texto">Neste capítulo, você aprendeu o que são listas e como trabalhar com os '
        'itens individuais em uma lista. Você aprendeu como definir uma lista e como adicionar e remover '
        'elementos. Você aprendeu como classificar listas permanentemente e temporariamente para fins de '
        'exibição. Você também aprendeu como encontrar o comprimento de uma lista e como evitar erros de '
        'índice ao trabalhar com listas.</p>')
st.html('<p class="fonte_texto">No Capítulo 4, você aprenderá como trabalhar com itens em uma lista de '
        'forma mais eficiente. Ao fazer um loop em cada item em uma lista usando apenas algumas linhas de '
        'código, você poderá trabalhar de forma eficiente, mesmo quando sua lista contiver milhares ou '
        'milhões de itens.</p>')
