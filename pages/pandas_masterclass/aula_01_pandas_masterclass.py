# --- Importar as bibliotecas --- #
import pandas as pd
from PIL import Image
import streamlit as st

# --- Configurações iniciais da página --- #
st.set_page_config(
    page_title='Pandas Masterclass - Aula 01',
    page_icon=Image.open('./assets/logo/logo.png'),
    layout='wide'
)

# --- Carregar o estilo das fontes --- #
with open('./assets/css/style.css', 'r') as css:
    st.html(f'<style>{css.read()}</style>')

# --- Colocar o título da aula --- #
st.html('<h1 class="fonte_titulo_aula">Aula 01: Criando seu Primeiro DataFrame</h1>')

# --- Vídeo --- #
with st.expander('Se quiser acompanhar com o vídeo, acesse aqui! 👇'):
        st.video('https://youtu.be/luIGjQQtTPY')

# --- Código da aula --- #
st.subheader('Se quiser acessar o código completo da aula, clique [aqui](https://github.com/GTL98/canal_mundo_python/blob/main/Pandas%20Masterclass%3A%20Do%20Zero%20ao%20Her%C3%B3i%20dos%20Dados/Aula%2001/aula_01.ipynb)')
st.divider()

# --- Introdução --- #
st.subheader('E fala, devs! Tudo bem com vocês? Espero que sim!')
st.html('<h1 class="fonte_titulo_aula">Introdução</h1>')
st.html('<p class="fonte_texto">A análise de dados moderna no ecossistema Python gravita em torno de uma '
        'biblioteca central que redefiniu a forma como profissionais lidam com informações estruturadas: o '
        'Pandas. Esta biblioteca, construída sobre o poder computacional do NumPy, oferece abstrações de '
        'alto nível que permitem a manipulação de tabelas e séries temporais com uma eficiência que antes '
        'era reservada a linguagens de baixo nível ou sistemas de gerenciamento de bancos de dados '
        'relacionais. O domínio do Pandas não se inicia pela complexidade estatística, mas sim pela '
        'compreensão profunda de suas estruturas fundamentais: a Series e o DataFrame. Este capítulo '
        'dedica-se a explorar a gênese dessas estruturas, desde a sua criação manual até a dissecação de '
        'sua anatomia interna, estabelecendo uma base sólida para qualquer desenvolvedor que pretenda '
        'transitar do código procedural para a análise de dados profissional.</p>')
st.divider()

# --- O Paradigma do Pandas e a Preparação do Ambiente --- #
st.html('<h1 class="fonte_titulo_aula">O Paradigma do Pandas e a Preparação do Ambiente</h1>')
st.html('<p class="fonte_texto">A transição para o Pandas exige que abandonemos a manipulação iterativa '
        'de listas e dicionários em favor de operações vetorizadas. No Python puro, processar uma lista de '
        'dez milhões de itens requer um laço de repetição (<span class=palavras_reservadas>for</span> '
        'ou <span class="palavras_reservadas">while</span>), o que é '
        'computacionalmente caro devido ao overhead do interpretador. O Pandas resolve essa limitação '
        'ao utilizar arrays do NumPy por baixo da interface amigável, permitindo que os dados sejam '
        'processados em blocos de memória contíguos e otimizados em C.</p>')
st.html('<p class="fonte_texto">Para iniciar qualquer projeto, a primeira etapa é a importação da '
        'biblioteca. No ambiente de desenvolvimento, especialmente em plataformas baseadas em nuvem como '
        'o Google Colab, o Pandas já vem pré-instalado, bastando chamá-lo para a sessão atual:</p>')
st.code('''# --- Importar o Pandas --- #
import pandas as pd''', line_numbers=True)
st.html('<p class="fonte_texto">O uso do alias <span class="texto_python">pd</span> não é apenas uma '
        'convenção estética; é uma norma '
        'de mercado que facilita a legibilidade e a manutenção do código por equipes multidisciplinares. '
        'Ao importar o Pandas desta forma, sinalizamos que todas as operações subsequentes utilizarão o '
        'motor de processamento desta biblioteca.</p>')
st.divider()

# --- A Unidade Fundamental: Pandas Series --- #
st.html('<h1 class="fonte_titulo_aula">A Unidade Fundamental: Pandas Series</h1>')
st.html('<p class="fonte_texto">A Series é o bloco de construção mais simples do Pandas. Tecnicamente, '
        'ela é descrita como um array unidimensional rotulado, capaz de armazenar qualquer tipo de dado '
        '(inteiros, strings, objetos Python, entre outros). Didaticamente, a Series pode ser visualizada '
        'como uma única coluna de uma planilha eletrônica ou uma lista de Python que recebeu superpoderes, '
        'como um índice associado a cada valor.</p>')

# --- Criação e Propriedades da Series --- #
st.html('<h2 class="fonte_subtitulo_aula">Criação e Propriedades da Series</h2>')
st.html('<p class="fonte_texto">Diferente de uma lista comum, onde o acesso é feito puramente pela posição '
        'numérica, uma Series permite que cada elemento tenha um rótulo identificador. Além disso, ela '
        'carrega metadados, como o próprio nome da estrutura:</p>')
st.code('''# --- Criar uma Series --- #
precos = pd.Series(
    data=[4500, 1200, 300, 8000],
    name='Preços'
)
precos''', line_numbers=True)
st.container()
precos = pd.Series(
    data=[4500, 1200, 300, 8000],
    name='Preços'
)
st.dataframe(precos, width=120)
st.html('<p class="fonte_texto">Neste bloco de código, a função <span class="texto_python">pd.Series</span> '
        'é utilizada para '
        'transformar uma lista de inteiros em um objeto do Pandas. O parâmetro '
        '<span class="texto_python">data</span> recebe os '
        'valores brutos, enquanto o parâmetro <span class="texto_python">name</span> define o título/nome '
        '(rótulo) da coluna. O '
        'resultado exibido no console mostra dois componentes principais: à esquerda, o índice (que por '
        'padrão inicia em 0) e, à direita, os valores propriamente ditos. A inclusão do nome "Preços" é '
        'uma etapa de organização que se torna vital quando múltiplas Series são combinadas para formar '
        'uma tabela.</p>')
st.html('<p class="fonte_texto">A Series é homogênea em termos de tipo de dado por padrão. Se uma lista '
        'contém apenas inteiros, o Pandas atribuirá o tipo <span class="texto_python">int64</span> a '
        'essa Series, otimizando o espaço '
        'em memória. Essa estrutura unidimensional é o que permite a implementação de cálculos matemáticos '
        'rápidos em toda a coluna sem a necessidade de escrever loops manuais.</p>')
st.html('''<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-69a3{font-family:Arial, Helvetica, sans-serif !important;font-size:16px;text-align:center;vertical-align:top}
.tg .tg-pvun{border-color:inherit;font-family:Arial, Helvetica, sans-serif !important;font-size:16px;font-weight:bold;
  text-align:center;vertical-align:top}
.tg .tg-jxpu{border-color:inherit;font-family:Arial, Helvetica, sans-serif !important;font-size:16px;text-align:center;
  vertical-align:top}
</style>
<table class="tg"><thead>
  <tr>
    <th class="tg-pvun">Características da Series</th>
    <th class="tg-pvun">Descrição técnica</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-jxpu">Dimensões</td>
    <td class="tg-jxpu">Sempre unidimensional (1D)</td>
  </tr>
  <tr>
    <td class="tg-69a3">Índices</td>
    <td class="tg-69a3">Possui rótulos de eixo para cada elemento</td>
  </tr>
  <tr>
    <td class="tg-69a3">Vetorização</td>
    <td class="tg-69a3">Permite operações matemáticas em todos os elementos simultaneamente</td>
  </tr>
  <tr>
    <td class="tg-69a3">Homogeneidade</td>
    <td class="tg-69a3">Geralmente armazena dados em um único tipo para performance</td>
  </tr>
</tbody>
</table>''')
st.divider()

# --- A Estrutura Complexa: O DataFrame --- #
st.html('<h1 class="fonte_titulo_aula">A Estrutura Complexa: O DataFrame</h1>')
st.html('<p class="fonte_texto">Se a Series representa uma coluna isolada, o DataFrame é a representação '
        'completa de uma tabela de dados. Ele é uma estrutura bidimensional, com linhas e colunas '
        'rotuladas. No contexto do Pandas, um DataFrame é definido como um "coletivo de Series", onde '
        'cada coluna é tecnicamente uma Series que compartilha o mesmo índice de linhas com as demais.</p>')

# --- Construção de um DataFrame a partir de Dicionários --- #
st.html('<h2 class="fonte_subtitulo_aula">Construção de um DataFrame a partir de Dicionários</h2>')
st.html('<p class="fonte_texto">Uma das metodologias mais eficazes para a criação manual de datasets em '
        'Python é a utilização de dicionários. Nesta estrutura, a chave do dicionário representa o nome '
        'da coluna, e o valor associado (geralmente uma lista) representa os dados contidos nela:</p>')
st.code('''# --- Criar um DataFrame --- #
dados_loja = {
    'Produto': ['MacBook Pro', 'Teclado mecânico', 'Mouse Gamer', 'Monitor 4k'],
    'Categoria': ['Computadores', 'Acessórios', 'Acessórios', 'Monitores'],
    'Preço': [15000, 450, 300, 3500],
    'Estoque': [5, 15, 20, 10],
    'Data entrada': ['2023-01-10', '2023-02-15', '2023-02-20', '2023-03-01']
}
df = pd.DataFrame(dados_loja)
df''')
dados_loja = {
    'Produto': ['MacBook Pro', 'Teclado mecânico', 'Mouse Gamer', 'Monitor 4k'],
    'Categoria': ['Computadores', 'Acessórios', 'Acessórios', 'Monitores'],
    'Preço': [15000, 450, 300, 3500],
    'Estoque': [5, 15, 20, 10],
    'Data entrada': ['2023-01-10', '2023-02-15', '2023-02-20', '2023-03-01']
}
df = pd.DataFrame(dados_loja)
st.dataframe(df)
st.html("<p class='fonte_texto'>Este código exemplifica a conversão de uma estrutura de dados nativa do "
        "Python em uma matriz tabular robusta. O Pandas percorre o dicionário e utiliza as chaves "
        "(<span class='variaveis'>'Produto'</span>, <span class='variaveis'>'Categoria'</span>, etc.) "
        "para criar os cabeçalhos das colunas. É imperativo "
        "que todas as listas no dicionário possuam exatamente o mesmo comprimento. Caso uma coluna tenha "
        "quatro itens e outra tenha cinco, o interpretador lançará um "
        "<span class='erro_python'>ValueError</span>, pois o "
        "DataFrame exige uma conformidade matricial estrita para garantir a integridade dos dados.</p>")
st.html('<p class="fonte_texto">A versatilidade do DataFrame reside na sua heterogeneidade. Enquanto uma '
        'única Series tende a ser homogênea, um DataFrame pode conter colunas de diferentes tipos: uma '
        'coluna de strings para nomes de produtos, uma coluna de inteiros para estoque e uma de '
        'flutuantes para preços. Essa capacidade de organizar dados diversos sob um único objeto rotulado '
        'é o que torna o Pandas a ferramenta preferida para análise de dados tabulares.</p>')
st.divider()

# --- Anatomia do DataFrame e Metadados --- #
st.html('<h1 class="fonte_titulo_aula">Anatomia do DataFrame e Metadados</h1>')
st.html('<p class="fonte_texto">Para um programador avançado, olhar para um DataFrame não significa '
        'apenas observar os dados, mas entender a estrutura que os sustenta. O Pandas disponibiliza uma '
        'série de atributos que permitem realizar uma inspeção técnica profunda na tabela, revelando '
        'informações sobre sua forma, tipos de dados e identificadores:</p>')
st.code(r"""# Verificar os componentes da tabela
print(f'''Colunas: {df.columns}
Índices: {df.index}
Formato (linhas, colunas): {df.shape}
Tipo de dados em cada coluna: \n{df.dtypes}''')""", line_numbers=True)

# --- O Sistema de Eixos: Colunas e Índices --- #
st.html('<h2 class="fonte_subtitulo_aula">O Sistema de Eixos: Colunas e Índices</h2>')
st.html('<p class="fonte_texto">O atributo <span class="texto_python">.columns</span> retorna um objeto '
        '<span class="texto_python">Index</span> que '
        'contém os nomes de todos os cabeçalhos. Isso é fundamental para automações onde o código '
        'precisa iterar sobre os nomes das variáveis ou verificar se uma coluna específica existe antes '
        'de realizar um cálculo. Já o atributo <span class="texto_python">.index</span> detalha os '
        'rótulos das linhas. Por padrão, '
        'o Pandas atribui um <span class="texto_python">RangeIndex</span> (0, 1, 2, ...), mas, como '
        'veremos adiante, esses '
        'índices podem ser customizados para representar chaves primárias, como um ID único.</p>')

# --- Dimensionalidade e o Atributo shape --- #
st.html('<h2 class="fonte_subtitulo_aula">Dimensionalidade e o Atributo '
        '<span class="texto_python">shape</span></h2>')
st.html('<p class="fonte_texto">O atributo <span class="texto_python">.shape</span> é uma propriedade '
        'que retorna uma tupla indicando '
        'as dimensões do objeto. O primeiro elemento da tupla é o número de linhas e o segundo é o número '
        'de colunas. Em uma tabela com 4 linhas e 5 colunas, o '
        '<span class="texto_python">.shape</span> retornará <span class="texto_python">(4, 5)</span>. '
        'Diferente de métodos que exigem parênteses, o <span class="texto_python">.shape</span> é um '
        'atributo direto, o que '
        'significa que seu acesso é instantâneo e não exige processamento adicional.</p>')

# --- Tipagem e Gerenciamento de Memória: dtypes --- #
st.html('<h2 class="fonte_subtitulo_aula">Tipagem e Gerenciamento de Memória: '
        '<span class="texto_python">dtypes</span></h2>')
st.html('<p class="fonte_texto">A inspeção de tipos de dados através do '
        '<span class="texto_python">.dtypes</span> é uma das etapas '
        'mais críticas da análise. O Pandas mapeia tipos do Python para tipos otimizados do NumPy. '
        'Compreender esse mapeamento é essencial para evitar o consumo excessivo de memória e erros de '
        'cálculo.</p>')
st.html('''<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-hsa2{font-family:Arial, Helvetica, sans-serif !important;font-size:16px;font-weight:bold;text-align:center;
  vertical-align:top}
.tg .tg-69a3{font-family:Arial, Helvetica, sans-serif !important;font-size:16px;text-align:center;vertical-align:top}
</style>
<table class="tg"><thead>
  <tr>
    <th class="tg-hsa2">Pandas Dtype</th>
    <th class="tg-hsa2">Python/NumPy equivalente</th>
    <th class="tg-hsa2">Uso comum</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-69a3"><span class="texto_python">int64</span></td>
    <td class="tg-69a3"><span class="texto_python">int</span></td>
    <td class="tg-69a3">Números inteiros, contagens, estoque</td>
  </tr>
  <tr>
    <td class="tg-69a3"><span class="texto_python">float64</span></td>
    <td class="tg-69a3"><span class="texto_python">float</span></td>
    <td class="tg-69a3">Números decimais, preços, medidas científicas</td>
  </tr>
  <tr>
    <td class="tg-69a3"><span class="texto_python">object</span></td>
    <td class="tg-69a3"><span class="texto_python">str</span> ou misto</td>
    <td class="tg-69a3">Texto, strings ou dados de tipos variados</td>
  </tr>
  <tr>
    <td class="tg-69a3"><span class="texto_python">bool</span></td>
    <td class="tg-69a3"><span class="texto_python">bool</span></td>
    <td class="tg-69a3">Valores verdadeiro/falso (<span class="palavras_reservadas">True</span>/
    <span class="palavras_reservadas">False</span>)</td>
  </tr>
  <tr>
    <td class="tg-69a3">datetime64</td>
    <td class="tg-69a3">datetime</td>
    <td class="tg-69a3">Datas e horários específicos</td>
  </tr>
</tbody>
</table>''')
st.html('<p class="fonte_texto">Um ponto de atenção especial deve ser dado ao tipo '
        '<span class="texto_python">object</span>. No '
        'Pandas, strings são armazenadas como objetos, o que significa que a coluna contém ponteiros para '
        'os endereços de memória onde as strings estão localizadas, em vez de armazenar o dado diretamente '
        'de forma compacta. Isso confere flexibilidade, mas introduz um custo de performance em '
        'comparação com colunas puramente numéricas.</p>')
st.divider()

# --- Engenharia de Índices no Pandas --- #
st.html('<h1 class="fonte_titulo_aula">Engenharia de Índices no Pandas</h1>')
st.html('<p class="fonte_texto">O índice de um DataFrame é o seu sistema de endereçamento. Sem um '
        'índice eficiente, a recuperação de dados seria lenta e baseada apenas em varreduras sequenciais. '
        'O Pandas permite que tomemos o controle desse sistema, definindo índices personalizados que '
        'façam sentido para o domínio do problema.</p>')

# --- Índices Manuais e Identificadores Únicos --- #
st.html('<h2 class="fonte_subtitulo_aula">Índices Manuais e Identificadores Únicos</h2>')
st.html('<p class="fonte_texto">Muitas vezes, o índice numérico padrão não é informativo. Em um dataset '
        'de loja, pode ser preferível identificar as linhas por um ID de transação ou código de '
        'barras:</p>')
st.code('''# --- Passar os índices para o DataFrame --- #
dados_loja = {
    'Produto': ['MacBook Pro', 'Teclado mecânico', 'Mouse Gamer', 'Monitor 4k'],
    'Categoria': ['Computadores', 'Acessórios', 'Acessórios', 'Monitores'],
    'Preço': [15000, 450, 300, 3500],
    'Estoque': [5, 15, 20, 10],
    'Data entrada': ['2023-01-10', '2023-02-15', '2023-02-20', '2023-03-01']
}
df = pd.DataFrame(
    data=dados_loja,
    index=['ID 430', 'ID 931', 'ID 187', 'ID 277']
)
df''', line_numbers=True)
dados_loja = {
    'Produto': ['MacBook Pro', 'Teclado mecânico', 'Mouse Gamer', 'Monitor 4k'],
    'Categoria': ['Computadores', 'Acessórios', 'Acessórios', 'Monitores'],
    'Preço': [15000, 450, 300, 3500],
    'Estoque': [5, 15, 20, 10],
    'Data entrada': ['2023-01-10', '2023-02-15', '2023-02-20', '2023-03-01']
}
df = pd.DataFrame(
    data=dados_loja,
    index=['ID 430', 'ID 931', 'ID 187', 'ID 277']
)
st.dataframe(df)
st.html('<p class="fonte_texto">Ao fornecer uma lista para o parâmetro '
        '<span class="texto_python">index</span> durante a criação '
        'do DataFrame, substituímos o <span class="texto_python">RangeIndex</span> automático por '
        'rótulos explícitos. Isso '
        'facilita a seleção de dados por rótulo, tornando o código mais legível e menos propenso a '
        'erros causados por mudanças na ordem das linhas.</p>')

# --- O Método set_index(): Elevando Colunas a Identificadores --- #
st.html('<h2 class="fonte_subtitulo_aula">O Método '
        '<span class="texto_python">set_index()</span>: Elevando Colunas a Identificadores</h2>')
st.html('<p class="fonte_texto">Em fluxos de trabalho típicos, os dados chegam com todas as informações '
        'dispostas em colunas. O método <span class="texto_python">.set_index()</span> permite que uma '
        'dessas colunas seja promovida a índice da tabela:</p>')
st.code('''# --- Transformar uma coluna no índice --- #
dados_loja = {
    'Produto': ['MacBook Pro', 'Teclado mecânico', 'Mouse Gamer', 'Monitor 4k'],
    'Categoria': ['Computadores', 'Acessórios', 'Acessórios', 'Monitores'],
    'Preço': [15000, 450, 300, 3500],
    'Estoque': [5, 15, 20, 10],
    'Data entrada': ['2023-01-10', '2023-02-15', '2023-02-20', '2023-03-01']
}
df = pd.DataFrame(dados_loja)
df = df.set_index('Data entrada')
df''', line_numbers=True)
dados_loja = {
    'Produto': ['MacBook Pro', 'Teclado mecânico', 'Mouse Gamer', 'Monitor 4k'],
    'Categoria': ['Computadores', 'Acessórios', 'Acessórios', 'Monitores'],
    'Preço': [15000, 450, 300, 3500],
    'Estoque': [5, 15, 20, 10],
    'Data entrada': ['2023-01-10', '2023-02-15', '2023-02-20', '2023-03-01']
}
df = pd.DataFrame(dados_loja)
df = df.set_index('Data entrada')
st.dataframe(df)
st.html("<p class='fonte_texto'>Neste exemplo, a coluna "
        "<span class='variaveis'>'Data entrada'</span> torna-se o índice. Por "
        "padrão, o Pandas remove a coluna original do corpo do DataFrame ao transformá-la em índice para "
        "evitar duplicidade de dados, a menos que o parâmetro "
        "<span class='texto_python'>drop=</span><span class='palavras_reservadas'>False</span> seja "
        "utilizado. Definir "
        "datas como índices é uma técnica vital em análise de Séries Temporais, pois permite que o "
        "Pandas otimize buscas por períodos e realize o alinhamento de datas de forma inteligente durante "
        "operações de junção.")
st.divider()

# --- O DataFrame como Coleção Alinhada de Series --- #
st.html('<h1 class="fonte_titulo_aula">O DataFrame como Coleção Alinhada de Series</h1>')
st.html('<p class="fonte_texto">Uma das provas conceituais mais importantes do Pandas é que um DataFrame '
        'pode ser construído peça por peça a partir de Series individuais. Isso demonstra como o DataFrame '
        'gerencia o alinhamento de dados através de índices compartilhados:</p>')
st.code('''dados_loja = {
    'Produto': pd.Series(['MacBook Pro', 'Teclado mecânico', 'Mouse Gamer', 'Monitor 4k'],
                         index=['ID 430', 'ID 931', 'ID 187', 'ID 277']),
    'Categoria': pd.Series(['Computadores', 'Acessórios', 'Acessórios', 'Monitores'],
                           index=['ID 430', 'ID 931', 'ID 187', 'ID 277']),
    'Preço': pd.Series([15000, 450, 300, 3500],
                       index=['ID 430', 'ID 931', 'ID 187', 'ID 277']),
    'Estoque': pd.Series([5, 15, 20, 10],
                         index=['ID 430', 'ID 931', 'ID 187', 'ID 277']),
    'Data entrada': pd.Series(['2023-01-10', '2023-02-15', '2023-02-20', '2023-03-01'],
                              index=['ID 430', 'ID 931', 'ID 187', 'ID 277'])
}
df = pd.DataFrame(dados_loja)
df''', line_numbers=True)
dados_loja = {
    'Produto': pd.Series(['MacBook Pro', 'Teclado mecânico', 'Mouse Gamer', 'Monitor 4k'],
                         index=['ID 430', 'ID 931', 'ID 187', 'ID 277']),
    'Categoria': pd.Series(['Computadores', 'Acessórios', 'Acessórios', 'Monitores'],
                           index=['ID 430', 'ID 931', 'ID 187', 'ID 277']),
    'Preço': pd.Series([15000, 450, 300, 3500],
                       index=['ID 430', 'ID 931', 'ID 187', 'ID 277']),
    'Estoque': pd.Series([5, 15, 20, 10],
                         index=['ID 430', 'ID 931', 'ID 187', 'ID 277']),
    'Data entrada': pd.Series(['2023-01-10', '2023-02-15', '2023-02-20', '2023-03-01'],
                              index=['ID 430', 'ID 931', 'ID 187', 'ID 277'])
}
df = pd.DataFrame(dados_loja)
st.dataframe(df)
st.html('<p class="fonte_texto">Este código ilustra a arquitetura interna do Pandas: o DataFrame atua '
        'como um invólucro para várias Series. O ponto crucial aqui é o índice. Se as Series tivessem '
        'índices diferentes, o DataFrame resultante realizaria uma união desses índices, preenchendo as '
        'lacunas com <span class="texto_python">NaN</span> (<i>Not a Number</i>) para garantir que a estrutura permaneça tabular. '
        'O alinhamento automático baseado em rótulos é uma das maiores vantagens do Pandas sobre o NumPy '
        'ou listas puras, pois previne o erro comum de associar dados de linhas diferentes por falha na '
        'ordenação.</p>')
st.divider()

# --- Mecanismos de Acesso e Seleção de Dados --- #
st.html('<h1 class="fonte_titulo_aula">Mecanismos de Acesso e Seleção de Dados</h1>')
st.html('<p class="fonte_texto">A extração de informações de um DataFrame é uma tarefa diária para '
        'qualquer cientista de dados. O Pandas oferece múltiplos caminhos para isso, e a escolha entre '
        'eles depende do tipo de objeto que se deseja obter no retorno da operação.</p>')

# --- Seleção de Coluna Única: O Retorno da Series --- #
st.html('<h2 class="fonte_subtitulo_aula">Seleção de Coluna Única: O Retorno da Series</h2>')
st.html('<p class="fonte_texto">Para acessar uma única coluna, utilizamos a sintaxe de colchetes simples '
        'com o nome da coluna, igual a um dicionário:</p>')
st.code('''# --- Acessar uma coluna --- #
df['Estoque']''')
st.dataframe(df['Estoque'], width=150)
st.html('<p class="fonte_texto">Nesta operação, o Pandas retorna um objeto do tipo <b><i>Series</b></i>. '
        'Isso ocorre porque, ao isolar uma única dimensão de uma tabela bidimensional, o Pandas '
        'simplifica a estrutura para a sua forma unidimensional mais básica. Esta abordagem é ideal '
        'para realizar operações estatísticas rápidas, como '
        '<span class="texto_python">.mean()</span> ou <span class="texto_python">.sum()</span>, diretamente '
        'na variável selecionada.</p>')

# --- Seleção de Múltiplas Colunas: A Subtabela --- #
st.html('<h2 class="fonte_subtitulo_aula">Seleção de Múltiplas Colunas: A Subtabela</h2>')
st.html('<p class="fonte_texto">Quando o objetivo é extrair um conjunto de colunas mantendo a estrutura '
        'de tabela, utilizamos colchetes duplos. O par externo de colchetes indica ao Pandas que estamos '
        'realizando uma operação de seleção, enquanto o par interno define uma lista de nomes '
        'de colunas:</p>')
st.code('''# --- Acessar duas ou mais tabelas --- #
df[['Data entrada', 'Produto', 'Preço']]''')
st.dataframe(df[['Data entrada', 'Produto', 'Preço']], width=450)
st.html("<p class='fonte_texto'>Esta operação retorna um novo "
        "<span class='texto_python'>DataFrame</span>, mesmo que a lista "
        "contenha apenas um nome (ex: <span class='texto_python'>df[[</span>"
        "<span class='variaveis'>'Produto'</span><span class='texto_python'>]]</span>). Essa distinção "
        "sintática é fundamental: "
        "enquanto colchetes simples retornam uma Series, colchetes duplos garantem que o retorno seja um "
        "DataFrame, uma subtabela. Isso é importante porque certas funções do Pandas são exclusivas de "
        "DataFrames e outras de Series; saber controlar o tipo de retorno evita erros de atributo em "
        "cadeias de processamento complexas.</p>")
st.html('<p class="fonte_texto">A seleção por múltiplos colchetes é frequentemente utilizada para criar '
        '"visões" ou cópias parciais de datasets gigantescos, permitindo que o analista foque apenas nas '
        'variáveis de interesse sem descartar a estrutura tabular que facilita a visualização e futuras '
        'junções.</p>')
st.divider()

# --- Resumo --- #
st.html('<h1 class="fonte_titulo_aula">Resumo</h1>')
st.html('<p class="fonte_texto">Neste capítulo, percorremos os pilares fundamentais da biblioteca Pandas, '
        'partindo da premissa de que a compreensão das estruturas de dados é o requisito primordial para '
        'a análise profissional. Iniciamos com a importação da biblioteca e a criação da <b>Series</b>, '
        'compreendendo-a como um array unidimensional rotulado que atua como a unidade básica de '
        'informação.</p>')
st.html('<p class="fonte_texto">Avançamos para a construção de <b>DataFrames</b>, explorando como '
        'dicionários de Python podem ser transformados em tabelas robustas, desde que respeitem a regra da '
        'uniformidade no comprimento das listas. A dissecação da <b>anatomia do DataFrame</b> nos permitiu '
        'entender metadados críticos: o formato da matriz através do '
        '<span class="texto_python">.shape</span>, a identificação de '
        'variáveis com <span class="texto_python">.columns</span>, a localização de registros com '
        '<span class="texto_python">.index</span> e a importância da '
        'gestão de memória e tipos de dados com o <span class="texto_python">.dtypes</span>.</p>')
st.html('<p class="fonte_texto">Vimos também a <b>engenharia de índices</b>, aprendendo a definir '
        'identificadores personalizados e a elevar colunas existentes ao status de índice através do '
        'método <span class="texto_python">.set_index()</span>, o que otimiza drasticamente a recuperação '
        'de dados. Finalmente, '
        'exploramos os <b>mecanismos de seleção</b>, diferenciando o acesso que retorna Series daquele que '
        'retorna DataFrames, garantindo o controle total sobre os tipos de objetos manipulados '
        'no código.</p>')
st.divider()

# --- Conclusão --- #
st.html('<h1 class="fonte_titulo_aula">Conclusão</h1>')
st.html('<p class="fonte_texto">O domínio inicial do Pandas reside na percepção de que dados não são '
        'apenas coleções de valores, mas estruturas organizadas e rotuladas que carregam contexto. A '
        'Series e o DataFrame não são meros contêineres; eles são motores de processamento que gerenciam '
        'alinhamento, tipos de dados e eficiência computacional de forma transparente para o '
        'desenvolvedor.</p>')
st.html('<p class="fonte_texto">Ao compreender que um DataFrame é um coletivo de Series alinhadas por um '
        'índice comum, ganhamos a habilidade de decompor problemas complexos em manipulações simples de '
        'colunas. A escolha cuidadosa do índice e a verificação constante dos tipos de dados ('
        '<span class="texto_python">dtypes</span>) '
        'são as práticas que separam um código funcional de um sistema de análise de dados resiliente e '
        'performático. Com esses fundamentos consolidados, o caminho está aberto para a exploração de '
        'técnicas avançadas de limpeza, transformação e visualização, pilares que sustentam toda a '
        'ciência de dados moderna em Python.</p>')
st.subheader('No mais é isso, nos vemos na próxima aula! Até lá, fiquem com Deus e fui!')
