# --- Importar as bibliotecas --- #
from PIL import Image
import streamlit as st

# --- Configurações iniciais da página --- #
st.set_page_config(
    page_title='Capítulo 02 - Variáveis e tipos de dados simples',
    page_icon=Image.open('./assets/logo/logo.png'),
    layout='wide'
)

# --- Carregar o estilo das fontes --- #
with open('./assets/css/style.css', 'r') as css:
    st.html(f'<style>{css.read()}</style>')

# --- Colocar o banner do capítulo --- #
st.image('./assets/imagens/curso_intensivo_python/aula_02/aula_02.png')

# --- Introdução --- #
st.html('<p class="fonte_texto">Neste capítulo você aprenderá sobre os diferentes tipos de dados com os '
        'quais pode trabalhar em seus programas Python. Você também aprenderá como usar variáveis para '
        'representar dados em seus programas.</p>')

# --- O que realmente acontece quando executamos um código Python --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">O que realmente acontece quando executamos um código Python</h1>')
st.html('<p class="fonte_texto">Vamos dar uma olhada mais de perto no que o Python faz quando você o '
        'executa. Acontece que o Python faz bastante trabalho, mesmo quando executa um programa simples. '
        'Vejamos o que ele faz quando passamos um código:</p>')
st.code("print('Olá, mundo!')", line_numbers=True)
st.html('<p class="fonte_texto">Seu editor executa o código por meio do interpretador Python, que lê o '
        'programa e determina o que cada palavra do programa significa. Por exemplo, quando o interpretador '
        'vê a palavra <b>print</b> seguida de parênteses, ele imprime na tela tudo o que está dentro '
        'dos parênteses.</p>')
st.html('<p class="fonte_texto">À medida que você escreve seus programas, seu editor destaca diferentes '
        'partes do programa de diferentes maneiras. Por exemplo, ele reconhece que <b>print()</b> é o '
        'nome de uma função e exibe essa palavra em uma cor. Ele reconhece que <i>"Olá, mundo!"</i> não é código '
        'Python e exibe essa frase em uma cor diferente. Esse recurso é chamado de destaque de sintaxe '
        'e é bastante útil quando você começa a escrever seus próprios programas.</p>')

# --- Variáveis --- #
st.html('<h2 class="fonte_subtitulo_aula">Variáveis</h2>')
st.html('<p class="fonte_texto">Vamos tentar usar uma variável. Adicione uma nova linha e modifique o '
        'que está dentro do <b>print()</b>. Você deve ter o mesmo resultado de antes: </p>')
st.code('''mensagem = 'Olá, mundo!'
print(mensagem)''', line_numbers=True)
st.html('<p class="fonte_texto">Adicionamos uma <b>variável</b> chamada <i>mensagem</i>. Cada '
        'variável está conectada a um valor, que é a informação associada a essa variável. Nesse caso, '
        'o valor é o texto <i>"Olá, mundo!"</i>.</p>')
st.html('<p class="fonte_texto">Adicionar uma variável dá um pouco mais de trabalho ao interpretador '
        'Python. Ao processar a primeira linha, ele associa a variável <i>mensagem</i> ao texto <i>"Olá, '
        'mundo!"</i>. Ao chegar à segunda linha, imprime na tela o valor associado à <i>mensagem</i>.</p>')
st.html('<p class="fonte_texto">Vamos expandir este programa modificando a célula anterior para imprimir '
        'uma segunda mensagem. Adicione uma linha em branco e, em seguida, adicione duas novas linhas '
        'de código:</p>')
st.code('''mensagem = 'Olá, mundo!'
print(mensagem)
mensagem = 'Olá, mundo Python!'
print(mensagem)''', line_numbers=True)
st.html('<p class="fonte_texto">Você pode alterar o valor de uma variável em seu programa a qualquer '
        'momento, e o Python sempre acompanhará seu valor atual.</p>')

# --- Nomeando e usando variáveis --- #
st.html('<h2 class="fonte_subtitulo_aula">Nomeando e usando variáveis</h2>')
st.html('<p class="fonte_texto">Ao usar variáveis em Python, você precisa seguir algumas regras e '
        'diretrizes. Quebrar algumas dessas regras causará erros; outras diretrizes apenas ajudam você '
        'a escrever um código mais fácil de ler e entender. Lembre-se das seguintes regras ao trabalhar '
        'com variáveis:</p>')
st.html('<li class="fonte_texto">Os nomes das variáveis podem conter apenas letras, números e '
        'sublinhados. Eles podem começar com uma letra ou sublinhado, mas não com um número. Por exemplo, '
        'você pode chamar uma variável <i>mensagem_1</i>, mas não <i>1_mensagem</i>;</li>')
st.html('<li class="fonte_texto">Espaços não são permitidos em nomes de variáveis, mas sublinhados podem '
        'ser usados para separar palavras em nomes de variáveis. Por exemplo, <i>saudacao_mensagem</i> '
        'funciona, mas <i>saudacao mensagem</i> causará erros;</li>')
st.html('<li class="fonte_texto">Evite usar palavras-chave Python e nomes de funções como nomes de '
        'variáveis. Por exemplo, não use a palavra print como nome de variável; Python a reservou para um '
        'propósito programático específico;</li>')
st.html('<li class="fonte_texto">Os nomes das variáveis devem ser curtos, mas descritivos. Por exemplo, '
        '<i>nome</i> é melhor que <i>n</i>, <i>nome_aluno</i> é melhor que <i>n_a</i> e <i>tamanho_nome</i> '
        'é melhor que <i>tamanho_do_nome_da_pessoa</i> e;</li>')
st.html('<li class="fonte_texto">Tenha cuidado ao usar a letra <i>l</i> minúscula e a letra <i>O</i> '
        'maiúscula, pois podem ser confundidas com os números 1 e 0.</li>')
st.html('<p class="fonte_texto">Pode ser necessária alguma prática para aprender como criar bons nomes de '
        'variáveis, especialmente à medida que seus programas se tornam mais interessantes e complicados. '
        'À medida que você escreve mais programas e começa a ler o código de outras pessoas, você ficará '
        'melhor em encontrar nomes significativos.</p>')

# --- Evitando erros em nomes ao usar variáveis --- #
st.html('<h2 class="fonte_subtitulo_aula">Evitando erros em nomes ao usar variáveis</h2>')
st.html('<p class="fonte_texto">Todo programador comete erros, e a maioria comete erros todos os dias. '
        'Embora bons programadores possam criar erros, eles também sabem como responder a esses erros de '
        'forma eficiente. Vejamos um erro que você provavelmente cometerá logo no início e aprenderemos '
        'como corrigi-lo.</p>')
st.html('<p class="fonte_texto">Escreveremos algum código que gere um erro propositalmente. '
        'Digite o seguinte código, incluindo a palavra <i>mensagem</i> com erro ortográfico:</p>')
st.code('''mensagem = 'Olá, mundo!'
print(menssagem)''', line_numbers=True)
st.html('<p class="fonte_texto">Quando ocorre um erro em seu programa, o interpretador Python faz o '
        'possível para ajudá-lo a descobrir onde está o problema. O interpretador fornece um rastreamento '
        'quando um programa não pode ser executado com êxito. Um <b>traceback</b> é um registro de onde o '
        'interpretador teve problemas ao tentar executar seu código.</p>')
st.html('<p class="fonte_texto">Neste exemplo adicionamos a letra <i>s</i> no nome da variável '
        '<i>mensagem</i> na segunda linha. O interpretador Python não verifica a ortografia do seu código, '
        'mas garante que os nomes das variáveis sejam escritos de forma consistente. Por exemplo, observe '
        'o que acontece quando escrevemos <i>mensagem</i> incorretamente na linha que define a variável:</p>')
st.code('''menssagem = 'Olá, mundo!'
print(menssagem)''', line_numbers=True)
st.html('<p class="fonte_texto">Nesse caso, o programa executa sem erros!</p>')
st.html('<p class="fonte_texto">Os nomes das variáveis correspondem, então o Python não vê nenhum '
        'problema. As linguagens de programação são rígidas, mas desconsideram a boa e a má ortografia. '
        'Como resultado, você não precisa considerar as regras ortográficas e gramaticais do português '
        'ao tentar criar nomes de variáveis e escrever código.</p>')
st.html('<p class="fonte_texto">Muitos erros de programação são erros simples de digitação de um único '
        'caractere em uma linha de um programa. Se você passa muito tempo procurando um desses erros, '
        'saiba que está em boa companhia. Muitos programadores experientes e talentosos passam horas '
        'caçando esses pequenos erros. Tente rir disso e seguir em frente, sabendo que isso acontecerá '
        'com frequência ao longo de sua vida como programador.</p>')

# --- Variáveis são rótulos --- #
st.html('<h2 class="fonte_subtitulo_aula">Variáveis são rótulos</h2>')
st.html('<p class="fonte_texto">As variáveis são frequentemente descritas como caixas nas quais você '
        'pode armazenar valores. Essa ideia pode ser útil nas primeiras vezes que você usa uma variável, '
        'mas não é uma maneira precisa de descrever como as variáveis são representadas internamente em '
        'Python. É muito melhor pensar nas variáveis como rótulos que você pode atribuir aos valores. '
        'Você também pode dizer que uma variável faz referência a um determinado valor.</p>')
st.html('<p class="fonte_texto">Essa distinção provavelmente não importará muito em seus programas '
        'iniciais, mas vale a pena aprender mais cedo ou mais tarde. Em algum momento, você verá um '
        'comportamento inesperado de uma variável, e uma compreensão precisa de como as variáveis '
        'funcionam o ajudará a identificar o que está acontecendo em seu código.</p>')

# --- Faça você mesmo --- #
st.html('<h2 class="fonte_subtitulo_aula">Faça você mesmo!</h2>')
st.html('<p class="fonte_texto"><b>Exercício 01:</b> Atribua uma mensagem a uma variável e depois '
        'imprima essa mensagem.</p>')
st.html('<p class="fonte_texto"><b>Exercício 02:</b> Atribua uma mensagem a uma variável e imprima '
        'essa mensagem. Em seguida, altere o valor da variável para uma nova mensagem e imprima a '
        'nova mensagem.</p>')

# --- Strings --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Strings</h1>')
st.html('<p class="fonte_texto">Como a maioria dos programas define e reúne algum tipo de dados e '
        'depois faz algo útil com eles, é útil classificar diferentes tipos de dados. O primeiro tipo '
        'de dados que veremos é a string. As strings são muito simples à primeira vista, mas você pode '
        'usá-las de muitas maneiras diferentes.</p>')
st.html('<p class="fonte_texto">Uma <b>string</b> é uma série de caracteres. Qualquer coisa entre '
        'aspas é considerada uma string em Python, e você pode usar aspas simples ou duplas em torno '
        'de suas strings assim:</p>')
st.code('''
'Isso é uma string'
"Isso também é uma string"
''', line_numbers=True)

# --- Alterando maiúsculas e minúsculas em uma string com métodos --- #
st.html('<h2 class="fonte_subtitulo_aula">Alterando maiúsculas e minúsculas em uma string com métodos</h2>')
st.html('<p class="fonte_texto">Uma das tarefas mais simples que você pode realizar com strings é '
        'alterar as letras entre maiúsculas e minúsculas das palavras em uma string. Observe o código '
        'a seguir e tente determinar o que está acontecendo:</p>')
st.code('''nome = 'ada lovelace'
print(nome.title())''', line_numbers=True)
st.html('<p class="fonte_texto">Neste exemplo, variável nome refere-se à string minúscula '
        '<i>"ada lovelace"</i>. O método <b>title()</b> aparece após a variável na chamada de '
        '<b>print()</b>. Um método é uma ação que o Python pode executar em um dado. O ponto (.) após '
        'o nome em <b>nome.title()</b> diz ao Python para fazer o método <b>title()</b> atuar no nome '
        'da variável. Cada método é seguido por um conjunto de parênteses, porque os métodos geralmente '
        'precisam de informações adicionais para realizar seu trabalho. Essas informações são fornecidas '
        'entre parênteses. A função <b>title()</b> não precisa de nenhuma informação adicional, '
        'portanto seus parênteses estão vazios.</p>')
st.html('<p class="fonte_texto">O método <b>title()</b> altera cada palavra para maiúsculas e minúsculas, '
        'onde cada palavra começa com uma letra maiúscula. Isso é útil porque muitas vezes você desejará '
        'pensar em um nome como uma informação. Por exemplo, você pode querer que seu programa reconheça '
        'os valores de entrada <i>Ada</i>, <i>ADA</i> e <i>ada</i> como o mesmo nome e exiba todos '
        'eles como <i>Ada</i>.</p>')
st.html('<p class="fonte_texto">Vários outros métodos úteis também estão disponíveis para lidar com casos. '
        'Por exemplo, você pode alterar uma string para todas as letras maiúsculas ou minúsculas assim:</p>')
st.code('''nome = 'Ada Lovelace'
print(nome.upper())
print(nome.lower()))''', line_numbers=True)
st.html('<p class="fonte_texto">O método <b>lower()</b> é particularmente útil para armazenar dados. '
        'Normalmente, você não vai querer confiar na capitalização fornecida por seus usuários, então '
        'converterá as strings em minúsculas antes de armazená-las. Então, quando quiser exibir as '
        'informações, você usará o formato que faz mais sentido para cada string.</p>')

# --- Usando variáveis em strings --- #
st.html('<h2 class="fonte_subtitulo_aula">Usando variáveis em strings</h2>')
st.html('<p class="fonte_texto">Em algumas situações, você desejará usar o valor de uma variável '
        'dentro de uma string. Por exemplo, você pode querer usar duas variáveis para representar um '
        'nome e um sobrenome, respectivamente, e depois combinar esses valores para exibir o nome '
        'completo de alguém:</p>')
st.code('''nome = 'ada'
sobrenome = 'lovelace'
nome_completo = f'{nome} {sobrenome}'
print(nome_completo)''', line_numbers=True)
st.html('<p class="fonte_texto">O nome completo é usado em uma frase que cumprimenta o usuário, '
        'e o método <b>title()</b> altera o nome para maiúsculas e minúsculas. Este código retorna '
        'uma saudação simples, mas bem formatada.</p>')
st.html('<p class="fonte_texto">Você também pode usar <b><i>f-strings</b></i> para compor uma mensagem '
        'e, em seguida, atribuir a mensagem inteira a uma variável:</p>')
st.code('''nome = 'ada'
sobrenome = 'lovelace'
nome_completo = f'{nome} {sobrenome}'
mensagem = f'Olá, {nome_completo.title()}!'
print(mensagem)''', line_numbers=True)
st.html('<p class="fonte_texto">Este código exibe a mensagem <i>Olá, Ada Lovelace!</i> também, mas ao '
        'atribuir a mensagem a uma variável tornamos a chamada final de <b>print()</b> '
        'muito mais simples.</p>')

# --- Adicionando espaços em branco a strings com tabulações ou novas linhas --- #
st.html('<h2 class="fonte_subtitulo_aula">Adicionando espaços em branco a strings com '
        'tabulações ou novas linhas</h2>')
st.html('<p class="fonte_texto">Na programação, <b>espaço em branco</b> refere-se a quaisquer caracteres '
        'não imprimíveis, como espaços, tabulações e símbolos de fim de linha. Você pode usar espaços em '
        'branco para organizar sua saída para que seja mais fácil de ler para os usuários.</p>')
st.html('<p class="fonte_texto">Para adicionar uma tabulação ao seu texto, use a combinação de '
        r'caracteres <b>\t</b>:</p>')
st.code(r'''print('Python')
print('\tPython')''', line_numbers=True)
st.html('<p class="fonte_texto">Para adicionar uma nova linha em uma string, use a combinação '
        r'de caracteres <b>\n</b>:</p>')
st.code(r'''print('Linguagens:\nPython\nC\nJava')''', line_numbers=True)
st.html('<p class="fonte_texto">Você também pode combinar tabulações e novas linhas em uma única string. '
        r'A string <b>"\n\t"</b> diz ao Python para passar para uma nova linha e iniciar a próxima '
        r'linha com uma tabulação. O exemplo a seguir mostra como você pode usar uma string de uma '
        r'linha para gerar quatro linhas de saída:</p>')
st.code(r'''print('Linguagens:\n\tPython\n\tC\n\tJava')''', line_numbers=True)

# --- Removendo espaços em branco --- #
st.html('<h2 class="fonte_subtitulo_aula">Removendo espaços em branco</h2>')
st.html('<p class="fonte_texto">Espaços em branco extras podem ser confusos em seus programas. Para os '
        'programadores, <i>"Python"</i> e <i>"Python "</i> parecem praticamente iguais. Mas para um '
        'programa, são duas strings diferentes. O Python detecta o espaço extra em <i>"Python "</i> e o '
        'considera significativo, a menos que você diga o contrário.</p>')
st.html('<p class="fonte_texto">É importante pensar nos espaços em branco, porque muitas vezes você '
        'desejará comparar duas strings para determinar se elas são iguais. Por exemplo, um caso '
        'importante pode envolver a verificação dos nomes de usuário das pessoas quando elas fazem '
        'login em um site. Espaços em branco extras também podem ser confusos em situações muito mais '
        'simples. Felizmente, o Python facilita a eliminação de espaços em branco extras dos dados '
        'inseridos pelas pessoas.</p>')
st.html('<p class="fonte_texto">Python pode procurar espaços em branco extras nos lados direito e '
        'esquerdo de uma string. Para garantir que não exista nenhum espaço em branco no lado direito '
        'de uma string, use o método <b>rstrip()</b>:</p>')
st.code('''linguagem_favorita = 'Python '
print(linguagem_favorita)
print(linguagem_favorita.rstrip())
print(linguagem_favorita)''', line_numbers=True)
st.html('<p class="fonte_texto">O valor associado a <i>linguagem_favorita</i> contém espaços em branco '
        'extras no final da string. Ao solicitar esse valor ao Python em uma sessão de terminal, '
        'você pode ver o espaço no final do valor. Quando o método <b>rstrip()</b> atua na variável '
        '<i>linguagem_favorita</i> , esse espaço extra é removido. No entanto, ele é removido apenas '
        'temporariamente. Se você solicitar o valor de <i>linguagem_favorita</i> novamente, a string '
        'terá a mesma aparência de quando foi inserida, incluindo o espaço em branco extra.</p>')
st.html('<p class="fonte_texto">Para remover permanentemente o espaço em branco da string, você '
        'deve associar o valor removido ao nome da variável:</p>')
st.code('''linguagem_favorita = 'Python '
linguagem_favorita = linguagem_favorita.rstrip()
print(linguagem_favorita)''', line_numbers=True)
st.html('<p class="fonte_texto">Para remover o espaço em branco da string, retire o espaço em branco '
        'do lado direito da string e associe esse novo valor à variável original. A alteração do valor '
        'de uma variável é feita frequentemente na programação. É assim que o valor de uma variável pode '
        'ser atualizado à medida que um programa é executado ou em resposta à entrada do usuário.</p>')
st.html('<p class="fonte_texto">Você também pode remover espaços em branco do lado esquerdo de uma '
        'string usando o método <b>lstrip()</b>, ou de ambos os lados ao mesmo tempo '
        'usando <b>strip()</b>:</p>')
st.code('''linguagem_favorita = ' Python '
print(linguagem_favorita.rstrip())
print(linguagem_favorita.lstrip())
print(linguagem_favorita.strip())''', line_numbers=True)
st.html('<p class="fonte_texto">Neste exemplo, começamos com um valor que possui espaços em '
        'branco no início e no final. Em seguida, removemos o espaço extra do lado direito, do '
        'lado esquerdo e de ambos os lados. Experimentar essas funções de remoção pode ajudá-lo a se '
        'familiarizar com a manipulação de strings. No mundo real, essas funções de remoção são usadas '
        'com mais frequência para limpar a entrada do usuário antes de armazená-la em um programa.</p>')

# --- Removendo prefixos --- #
st.html('<h2 class="fonte_subtitulo_aula">Removendo prefixos</h2>')
st.html('<p class="fonte_texto">Ao trabalhar com strings, outra tarefa comum é remover um prefixo. '
        'Considere uma URL com o prefixo comum <i>https://</i>. Queremos remover esse prefixo para que '
        'possamos nos concentrar apenas na parte da URL que os usuários precisam inserir na barra de '
        'endereço. Veja como fazer isso:</p>')
st.code('''youtube_url = 'https://www.youtube.com/@Mundo_Python'
print(youtube_url)
print(youtube_url.removeprefix('https://'))''', line_numbers=True)
st.html('<p class="fonte_texto">Insira o nome da variável seguido de um ponto e, em seguida, o '
        'método <b>removeprefix()</b>. Dentro dos parênteses, insira o prefixo que deseja remover '
        'da string original.</p>')
st.html('<p class="fonte_texto">Assim como os métodos para remover espaços em branco, '
        '<b>removeprefix()</b> deixa a string original inalterada. Se você quiser manter o novo valor '
        'com o prefixo removido, reatribua-o à variável original ou atribua-o a uma nova variável:</p>')
st.code('''youtube_url = 'https://www.youtube.com/@Mundo_Python'
print(youtube_url)
url_simples = youtube_url.removeprefix('https://')
print(url_simples)''', line_numbers=True)
st.html('<p class="fonte_texto">Quando você vê um URL em uma barra de endereço e a parte <i>https://</i> '
        'não é mostrada, o navegador provavelmente está usando um método como <b>removeprefix()</b> nos '
        'bastidores.</p>')
st.html('<p class="fonte_texto">A mesma ideia vale para o método <b>removesufix()</b>, onde você passará '
        'dentro dos parênteses qual é a parte que você quer retirar do final da string.</p>')

# --- Substituir strings --- #
st.html('<h2 class="fonte_subtitulo_aula">Substituir strings</h2>')
st.html('<p class="fonte_texto">Outro método muito utilizado é o <b>replace()</b>. Esse método permite '
        'que você substitua uma substring por outra dentro de uma string. Vejamos um exemplo:</p>')
st.code('''url = 'https://www.youtube.com'
print(youtube_url.replace('youtube', 'google'))''', line_numbers=True)
st.html('<p class="fonte_texto">Podemos também trocar uma substring por uma string vazia:</p>')
st.code('''url = 'https://www.youtube.com'
print(youtube_url.replace('www', ''))''', line_numbers=True)
st.html('<p class="fonte_texto">Podemos também armazenar as substrings de troca em variáveis:</p>')
st.code('''url = 'https://www.youtube.com'
antiga = 'youtube'
nova = 'google'
print(youtube_url.replace(antiga, nova))''', line_numbers=True)
st.html('<p class="fonte_texto">A diferença entre o método <b>replace()</b> e os métodos '
        '<b>removeprefix()</b> e <b>removesufix()</b> é que com ele você pode trocar ou retirar um '
        'pedaço da string, sem necessariamente estar no começo ou no final dela.</p>')

# --- Faça você mesmo --- #
st.html('<h2 class="fonte_subtitulo_aula">Faça você mesmo!</h2>')
st.html('<p class="fonte_texto"><b>Exercício 03:</b> Use uma variável para representar o nome de uma pessoa '
        'e imprima uma mensagem para essa pessoa. Sua mensagem deve ser simples, como '
        '<i>"Olá Guilherme, você gostaria de aprender Python hoje?"</i>.</p>')
st.html('<p class="fonte_texto"><b>Exercício 04:</b> Use uma variável para representar o nome de uma '
        'pessoa e, em seguida, imprima o nome dessa pessoa em letras maiúsculas, maiúsculas '
        'e maiúsculas.</p>')
st.html('<p class="fonte_texto"><b>Exercício 05:</b> Encontre uma citação de uma pessoa famosa que você '
        'admira. Imprima a citação e o nome do seu autor. Sua saída deve ser semelhante à seguinte, '
        'incluindo as aspas:'
        '<li class="fonte_texto">Albert Einstein disse uma vez: “Uma pessoa que nunca cometeu um erro nunca '
        'tentou nada novo”.</li></p>')
st.html('<p class="fonte_texto"><b>Exercício 06:</b> Repita o exercício 5, mas desta vez, represente o '
        'nome da pessoa famosa usando uma variável chamada <i>pessoa_famosa</i>. Em seguida, componha '
        'sua mensagem e represente-a com uma nova variável chamada <i>mensagem</i>. '
        'Imprima sua mensagem.</p>')
st.html('<p class="fonte_texto"><b>Exercício 07:</b> use uma variável para representar o nome de uma '
        'pessoa e inclua alguns caracteres de espaço em branco no início e no final do nome. '
        r'Certifique-se de usar cada combinação de caracteres, <b>\t</b> e <b>\n</b>, pelo menos uma vez. '
        'Imprima o nome uma vez, para que o espaço em branco ao redor do nome seja exibido. Em seguida, '
        'imprima o nome usando cada uma das três funções de remoção, '
        '<b>lstrip()</b>, <b>rstrip()</b> e <b>strip()</b>.</p>')
st.html('<p class="fonte_texto"><b>Exercício 08:</b> Python tem um método <b>removesuffix()</b> que '
        'funciona exatamente como <b>removeprefix()</b>. Atribua o valor <i>"notas_python.txt"</i> a uma '
        'variável chamada <i>arquivo</i>. Em seguida, use o método <b>removesuffix()</b> para exibir o '
        'nome do arquivo sem a extensão do arquivo, como fazem alguns navegadores de arquivos.</p>')

# --- Números --- #
st.write('---')
st.html('<h1 class="fonte_subtitulo_aula">Números</h1>')
st.html('<p class="fonte_texto">Os números são usados com bastante frequência na programação para '
        'registrar pontuações em jogos, representar dados em visualizações, armazenar informações em '
        'aplicativos da web e assim por diante. Python trata os números de várias maneiras diferentes, '
        'dependendo de como eles estão sendo usados. Vejamos primeiro como o Python gerencia números '
        'inteiros, porque eles são os mais simples de trabalhar.</p>')

# --- Inteiros --- #
st.html('<h2 class="fonte_subtitulo_aula">Inteiros</h2>')
st.html('<p class="fonte_texto">Você pode somar (+), subtrair (-), multiplicar (*) e dividir (/) '
        'inteiros em Python:</p>')
st.code('''print(2 + 3)
print(3 - 2)
print(2 * 3)
print(3 / 2)''', line_numbers=True)
st.html('<p class="fonte_texto">Python usa dois símbolos de multiplicação para representar expoentes:</p>')
st.code('''print(3 ** 2)
print(3 ** 3)
print(10 ** 6)''', line_numbers=True)
st.html('<p class="fonte_texto">Python também suporta a ordem das operações, então você pode usar '
        'várias operações em uma expressão. Você também pode usar parênteses para modificar a ordem '
        'das operações para que o Python possa avaliar sua expressão na ordem especificada. Por exemplo:</p>')
st.code('''print(2 + 3 * 4)
print((2 + 3) * 4)''', line_numbers=True)
st.html('<p class="fonte_texto">O espaçamento nestes exemplos não afeta como o Python avalia as '
        'expressões; simplesmente ajuda você a identificar mais rapidamente as operações que têm '
        'prioridade ao ler o código.</p>')

# --- Flutuantes --- #
st.html('<h2 class="fonte_subtitulo_aula">Flutuantes</h2>')
st.html('<p class="fonte_texto">Python chama qualquer número com ponto decimal de <b>float</b>. Este termo '
        'é usado na maioria das linguagens de programação e se refere ao fato de que um ponto decimal '
        'pode aparecer em qualquer posição de um número. Cada linguagem de programação deve ser '
        'cuidadosamente projetada para gerenciar adequadamente os números decimais, para que os números '
        'se comportem adequadamente, não importa onde o ponto decimal apareça.</p>')
st.html('<p class="fonte_texto">Na maioria das vezes, você pode usar valores floats sem se preocupar '
        'com seu comportamento. Basta inserir os números que deseja usar e o Python provavelmente fará o '
        'que você espera:</p>')
st.code('''print(0.1 + 0.1)
print(0.2 + 0.2)
print(2 * 0.1)
print(2 * 0.2)''', line_numbers=True)
st.html('<p class="fonte_texto">No entanto, esteja ciente de que às vezes você pode obter um número '
        'arbitrário de casas decimais em sua resposta:</p>')
st.code('''print(0.2 + 0.1)
print(3 * 0.1)''', line_numbers=True)
st.html('<p class="fonte_texto">Isso acontece em todos os idiomas e é pouco preocupante. O Python '
        'tenta encontrar uma maneira de representar o resultado com a maior precisão possível, o que '
        'às vezes é difícil, dada a forma como os computadores precisam representar números '
        'internamente.</p>')

# --- Inteiros e flutuantes --- #
st.html('<h2 class="fonte_subtitulo_aula">Inteiros e flutuantes</h2>')
st.html('<p class="fonte_texto">Quando você divide quaisquer dois números, mesmo que sejam inteiros '
        'que resultem em um número inteiro, você sempre obterá um número flutuante:</p>')
st.code('''print(4/2)''', line_numbers=True)
st.html('<p class="fonte_texto">Se você misturar um inteiro e um float em qualquer outra operação, '
        'você também obterá um float:</p>')
st.code('''print(1 + 2.0)
print(2 * 3.0)
print(3.0 ** 2)''', line_numbers=True)
st.html('<p class="fonte_texto">O padrão do Python é float em qualquer operação que use um float, '
        'mesmo que a saída seja um número inteiro.</p>')

# --- Underscores em números --- #
st.html('<h2 class="fonte_subtitulo_aula"><i>Underscores</i> em números</h2>')
st.html('<p class="fonte_texto">Ao escrever números longos, você pode agrupar dígitos usando sublinhados '
        'para tornar os números grandes mais legíveis. Quando você imprime um número definido com '
        'sublinhados, o Python mostra apenas os dígitos:</p>')
st.code('''idade_universo = 14_000_000_000
print(idade_universo)''', line_numbers=True)
st.html('<p class="fonte_texto">Python ignora os sublinhados ao armazenar esses tipos de valores. '
        'Mesmo que você não agrupe os dígitos em três, o valor ainda não será afetado. Para Python, '
        '<i>1000</i> é o mesmo que <i>1_000</i>, que é o mesmo que <i>10_00</i>. Este recurso funciona '
        'tanto para números inteiros quanto para números flutuantes.</p>')

# --- Atribuição múltipla --- #
st.html('<h2 class="fonte_subtitulo_aula">Atribuição múltipla</h2>')
st.html('<p class="fonte_texto">Você pode atribuir valores a mais de uma variável usando apenas uma '
        'linha de código. Isso pode ajudar a encurtar seus programas e torná-los mais fáceis de ler; '
        'você usará essa técnica com mais frequência ao inicializar um conjunto de números.</p>')
st.html('<p class="fonte_texto">Por exemplo, veja como você pode inicializar as variáveis '
        '<i>x</i>, <i>y</i> e <i>z</i> como <i>1</i>, <i>2</i> e <i>3</i>:</p>')
st.code('''x, y, z = 1, 2, 3
print(x)
print(y)
print(z)''', line_numbers=True)
st.html('<p class="fonte_texto">Você precisa separar os nomes das variáveis com vírgulas e fazer o mesmo '
        'com os valores que o Python atribuirá cada valor à sua respectiva variável. Contanto que o '
        'número de valores corresponda ao número de variáveis, o Python irá combiná-los corretamente.</p>')

# --- Constantes --- #
st.html('<h2 class="fonte_subtitulo_aula">Constantes</h2>')
st.html('<p class="fonte_texto">Uma <b>constante</b> é uma variável cujo valor permanece o mesmo durante '
        'toda a vida de um programa. Python não possui tipos constantes integrados, mas os programadores '
        'Python usam letras maiúsculas para indicar que uma variável deve ser tratada como uma constante '
        'e nunca ser alterada:</p>')
st.code('''MAX_CONEXOES = 5000''', line_numbers=True)
st.html('<p class="fonte_texto">Quando você quiser tratar uma variável como uma constante em seu código, '
        'escreva o nome da variável em letras maiúsculas.</p>')

# --- Faça você mesmo --- #
st.html('<h2 class="fonte_subtitulo_aula">Faça você mesmo!</h2>')
st.html('<p class="fonte_texto"><b>Exercício 9:</b> Escreva operações de adição, subtração, '
        'multiplicação e divisão que resultem no número 8. Certifique-se de incluir suas operações em '
        'chamadas <b>print()</b< para ver os resultados. Sua saída deve ter quatro linhas, com o '
        'número 8 aparecendo uma vez em cada linha.</p>')
st.html('<p class="fonte_texto"><b>Exercício 10:</b> Use uma variável para representar seu número favorito. '
        'Então, usando essa variável, crie uma mensagem que revele seu número favorito. Mostre essa '
        'mensagem.</p>')

# --- Comentários --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Comentários</h1>')
st.html('<p class="fonte_texto">Os comentários são um recurso extremamente útil na maioria das '
        'linguagens de programação. Tudo o que você escreveu em seus programas até agora é código Python. '
        'À medida que seus programas se tornam mais longos e complicados, você deve adicionar notas dentro '
        'deles que descrevam sua abordagem geral para o problema que você está resolvendo. '
        'Um <b>comentário</b> permite que você escreva notas em seu idioma falado, dentro '
        'de seus programas.</p>')

# --- Como escrever comentários? --- #
st.html('<h2 class="fonte_titulo_aula">Como escrever comentários?</h2>')
st.html('<p class="fonte_texto">Em Python, a hastag ou jogo da velha (#) indica um comentário. Qualquer '
        'coisa após uma marca de hash em seu código é ignorada pelo interpretador Python. Por exemplo:</p>')
st.code('''# Diga olá para todos!
print('Olá, pessoal!')''', line_numbers=True)
st.html('<p class="fonte_texto">Python ignora a primeira linha e executa a segunda.</p>')

# --- Que tipo de comentários você deve escrever? --- #
st.html('<h2 class="fonte_titulo_aula">Que tipo de comentários você deve escrever?</h2>')
st.html('<p class="fonte_texto">A principal razão para escrever comentários é explicar o que seu código '
        'deve fazer e como você o está fazendo funcionar. Quando você está trabalhando em um projeto, '
        'você entende como todas as peças se encaixam. Mas quando você retornar a um projeto depois de '
        'algum tempo afastado, provavelmente terá esquecido alguns detalhes. Você sempre pode estudar '
        'seu código por um tempo e descobrir como os segmentos deveriam funcionar, mas escrever bons '
        'comentários pode economizar tempo, resumindo claramente sua abordagem geral.</p>')
st.html('<p class="fonte_texto">Se quiser se tornar um programador profissional ou colaborar com outros '
        'programadores, você deve escrever comentários significativos. Hoje, a maior parte do software '
        'é escrita de forma colaborativa, seja por um grupo de funcionários de uma empresa ou por um '
        'grupo de pessoas trabalhando juntas em um projeto de código aberto. Programadores qualificados '
        'esperam ver comentários no código, por isso é melhor começar a adicionar comentários descritivos '
        'aos seus programas agora. Escrever comentários claros e concisos em seu código é um dos hábitos '
        'mais benéficos que você pode desenvolver como um novo programador.</p>')
st.html('<p class="fonte_texto">Ao decidir se deve escrever um comentário, pergunte-se se precisou '
        'considerar várias abordagens antes de encontrar uma maneira razoável de fazer algo funcionar; '
        'em caso afirmativo, escreva um comentário sobre sua solução. É muito mais fácil excluir '
        'comentários extras depois do que voltar e escrever comentários para um programa '
        'pouco comentado.</p>')

# --- Faça você mesmo --- #
st.html('<h2 class="fonte_subtitulo_aula">Faça você mesmo!</h2>')
st.html('<p class="fonte_texto"><b>Exercício 11:</b> Escolha dois dos programas que você escreveu e '
        'adicione pelo menos um comentário a cada um. Se você não tem nada específico para escrever '
        'porque seus programas são muito simples neste momento, basta adicionar seu nome e a data atual '
        'no topo de cada arquivo de programa. Em seguida, escreva uma frase descrevendo o que o '
        'programa faz.</p>')

# --- O Zen do Python --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">O Zen do Python</h1>')
st.html('<p class="fonte_texto">Programadores Python experientes irão encorajá-lo a evitar a complexidade '
        'e buscar a simplicidade sempre que possível. A filosofia da comunidade Python está contida em '
        '"O Zen do Python", de Tim Peters. Não reproduzirei todo o "Zen do Python" aqui, mas '
        'compartilharei algumas linhas para ajudá-lo a entender por que elas devem ser importantes '
        'para você como um programador iniciante em Python.</p>')
st.image('./assets/imagens/curso_intensivo_python/aula_02/figura_01.png', width=800)
st.html('<p class="fonte_texto"><b><i>Belo é melhor do que feio.</b></i></p>')
st.html('<p class="fonte_texto">Os programadores Python adotam a noção de que o código pode ser bonito '
        'e elegante. Na programação, as pessoas resolvem problemas. Os programadores sempre respeitaram '
        'soluções bem projetadas, eficientes e até bonitas para os problemas. À medida que você aprende '
        'mais sobre Python e o usa para escrever mais código, alguém pode olhar por cima do seu ombro um '
        'dia e dizer: “Uau, que código lindo!”</p>')
st.html('<p class="fonte_texto"><b><i>Simples é melhor do que complexo.</b></i></p>')
st.html('<p class="fonte_texto">Se você tiver que escolher entre uma solução simples e uma complexa, e '
        'ambas funcionarem, use a solução simples. Seu código será mais fácil de manter e será mais fácil '
        'para você e outras pessoas desenvolverem esse código posteriormente.</p>')
st.html('<p class="fonte_texto"><b><i>Complexo é melhor do que complicado.</b></i></p>')
st.html('<p class="fonte_texto">A vida real é complicada e às vezes uma solução simples para um problema '
        'é inatingível. Nesse caso, use a solução mais simples que funcione.</p>')
st.html('<p class="fonte_texto"><b><i>Complexo é melhor do que complicado.</b></i></p>')
st.html('<p class="fonte_texto">A vida real é complicada e às vezes uma solução simples para um problema '
        'é inatingível. Nesse caso, use a solução mais simples que funcione.</p>')
st.html('<p class="fonte_texto"><b><i>Legibilidade conta.</b></i></p>')
st.html('<p class="fonte_texto">Mesmo quando seu código for complexo, tente torná-lo legível. Ao trabalhar '
        'em um projeto que envolve codificação complexa, concentre-se em escrever comentários informativos '
        'para esse código.</p>')
st.html('<p class="fonte_texto"><b><i>Casos especiais não são especiais ao ponto de quebrarem '
        'as regras.</b></i></p>')
st.html('<p class="fonte_texto">Nenhum caso é forte o suficiente para passar por cima de uma regra. '
        'Leia o código, veja os erros e os arrume conforme as regras da linguagem. Caso ainda não dê '
        'certo, comece novamente, não há mal nenhum nisso.</p>')
st.html('<p class="fonte_texto"><b><i>Há apenas uma (e preferencialmente uma) maneira óbvia '
        'de fazer algo.</b></i></p>')
st.html('<p class="fonte_texto">Se dois programadores Python forem solicitados a resolver o mesmo '
        'problema, eles deverão encontrar soluções bastante compatíveis. Isso não quer dizer que não '
        'haja espaço para criatividade na programação. Pelo contrário, há muito espaço para a '
        'criatividade! Entretanto, grande parte da programação consiste no uso de abordagens pequenas '
        'e comuns para situações simples dentro de um projeto maior e mais criativo. Os detalhes básicos '
        'de seus programas devem fazer sentido para outros programadores Python.</p>')
st.html('<p class="fonte_texto"><b><i>Agora é melhor do que nunca.</b></i></p>')
st.html('<p class="fonte_texto">Você poderia passar o resto da vida aprendendo todos os meandros do '
        'Python e da programação em geral, mas nunca concluiria nenhum projeto. Não tente escrever um '
        'código perfeito; escreva um código que funcione e, em seguida, decida se deseja melhorar seu '
        'código para esse projeto ou passar para algo novo.</p>')

# --- Resumo --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Resumo</h1>')
st.html('<p class="fonte_texto">Neste capítulo você aprendeu como trabalhar com variáveis. Você aprendeu '
        'a usar nomes descritivos de variáveis e a resolver erros de nome e de sintaxe quando eles '
        'surgirem. Você aprendeu o que são strings e como exibi-las usando letras minúsculas, maiúsculas '
        'e letras maiúsculas. Você começou a usar espaços em branco para organizar a saída de maneira '
        'organizada e aprendeu como remover elementos desnecessários de uma string. Você começou a '
        'trabalhar com números inteiros e flutuantes e aprendeu algumas maneiras de trabalhar com dados '
        'numéricos. Você também aprendeu a escrever comentários explicativos para facilitar a leitura do '
        'código para você e outras pessoas. Por fim, você leu sobre a filosofia de manter seu código o '
        'mais simples possível, sempre que possível.</p>')