# --- Importar as bibliotecas --- #
import numpy as np
import pandas as pd
from PIL import Image
import streamlit as st

# --- Configurações iniciais da página --- #
st.set_page_config(
    page_title='Pandas Masterclass - Aula 03',
    page_icon=Image.open('./assets/logo/logo.png'),
    layout='wide'
)

# --- Carregar o estilo das fontes --- #
with open('./assets/css/style.css', 'r') as css:
    st.html(f'<style>{css.read()}</style>')

# --- Colocar o título da aula --- #
st.html('<h1 class="fonte_titulo_aula">Aula 03: Explorando Dados</h1>')

# --- Vídeo --- #
with st.expander('Se quiser acompanhar com o vídeo, acesse aqui! 👇'):
    st.video('https://youtu.be/WoRAylZCwI8')

# --- Código da aula --- #
st.subheader('Se quiser acessar o código completo da aula, clique [aqui](https://github.com/GTL98/canal_mundo_python/blob/main/Pandas%20Masterclass%3A%20Do%20Zero%20ao%20Her%C3%B3i%20dos%20Dados/Aula%2003/aula_03.ipynb)')
st.divider()

# --- Introdução --- #
st.subheader('E fala, devs! Tudo bem com vocês? Espero que sim!')
st.html('<h1 class="fonte_titulo_aula">Introdução</h1>')
st.html('<p class="fonte_texto">A análise de dados contemporânea exige não apenas a capacidade de '
        'processar grandes volumes de informação, mas, fundamentalmente, a habilidade de realizar um '
        'diagnóstico preciso da "saúde" dos dados antes de qualquer tentativa de modelagem ou inferência. '
        'No contexto do ecossistema Python, essa tarefa é liderada pela biblioteca Pandas, frequentemente '
        'operando em simbiose com o NumPy. Este capítulo dedica-se a explorar as técnicas fundamentais de '
        'inspeção, estruturação e avaliação de conjuntos de dados. O objetivo central é capacitar o '
        'profissional a realizar um "raio-X" completo de um dataset, identificando desde sua volumetria '
        'básica até nuances de distribuição estatística e integridade informacional.</p>')
st.html('<p class="fonte_texto">A prática da ciência de dados começa muito antes da aplicação de '
        'algoritmos complexos; ela se inicia na compreensão da estrutura da matriz de dados e na '
        'identificação de lacunas que possam comprometer a validade dos resultados. Entender os tipos '
        'de dados e a presença de valores ausentes é o que define a qualidade de um projeto analítico. '
        'Através de uma abordagem didática e técnica, este capítulo desmembra os comandos essenciais que '
        'servem como as primeiras ferramentas de qualquer analista: o exame visual, a validação '
        'estrutural, o diagnóstico de metadados e o mapeamento estatístico descritivo.</p>')
st.divider()

# --- O Alicerce Tecnológico: Configuração e Importação --- #
st.html('<h1 class="fonte_titulo_aula">O Alicerce Tecnológico: Configuração e Importação</h1>')
st.html('<p class="fonte_texto">A base de qualquer operação analítica robusta em Python repousa sobre '
        'a importação correta das ferramentas de manipulação. O Pandas é a estrutura de dados de alto '
        'nível que permite a manipulação de tabelas (DataFrames), enquanto o NumPy fornece o suporte '
        'matemático e a representação para dados numéricos de baixa latência e valores especiais de '
        'nulidade:</p>')
st.code('''# --- Importar as bibliotecas --- #
import numpy as np
import pandas as pd''', line_numbers=True)
st.html('<p class="fonte_texto">O Pandas utiliza o NumPy internamente para gerenciar arrays, o que '
        'confere ao sistema uma eficiência computacional necessária para lidar com milhões de registros '
        'sem sobrecarregar a memória de forma desnecessária. A interação entre essas duas bibliotecas é '
        'o que permite, por exemplo, o tratamento de valores nulos através do objeto '
        '<span class="texto_python">np.nan</span>.</p>')

# --- Construção e Estruturação do Dataset de Estudo --- #
st.html('<h1 class="fonte_titulo_aula">Construção e Estruturação do Dataset de Estudo</h1>')
st.html('<p class="fonte_texto">Para que possamos compreender por completo, é necessário um conjunto '
        'de dados que simule as imperfeições e a heterogeneidade do mundo real. Criaremos um dicionário '
        'de dados que abrange diversas categorias de informação: identificadores, nomes, dados '
        'demográficos, tipos de serviço, valores financeiros, datas e indicadores booleanos:</p>')
st.code('''# --- Gerar os dados (com NaNs) --- #
dados = {
    'ID Usuário': range(1001, 1011),
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo',
             'Fernanda', 'Gabriel', 'Helena', 'Ítalo', 'Júlia'],
    'Idade': [25, 34, np.nan, 45, 23, 31, 19, np.nan, 40, 28],
    'Plano': ['Premium', 'Básico', 'Premium', 'Padrão', 'Básico',
              'Padrão', 'Básico', 'Premium', 'Premium', 'Padrão'],
    'Mensalidade': [55.90, 29.90, 55.90, 39.90, 29.90,
                    39.90, 29.90, 55.90, 55.90, 39.90],
    'Data adesão': pd.to_datetime(['2022-01-10', '2022-03-15', '2021-11-20', '2023-01-05', 
                                   '2022-06-12', '2022-08-30', '2023-02-14', '2021-05-20', 
                                   '2022-12-01', '2023-03-10']),
    'Ativo': [True, True, False, True, True,
              False, True, True, True, True]
}

df = pd.DataFrame(dados)
df''', line_numbers=True)

dados = {
    'ID Usuário': range(1001, 1011),
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo',
             'Fernanda', 'Gabriel', 'Helena', 'Ítalo', 'Júlia'],
    'Idade': [25, 34, np.nan, 45, 23, 31, 19, np.nan, 40, 28],
    'Plano': ['Premium', 'Básico', 'Premium', 'Padrão', 'Básico',
              'Padrão', 'Básico', 'Premium', 'Premium', 'Padrão'],
    'Mensalidade': [55.90, 29.90, 55.90, 39.90, 29.90,
                    39.90, 29.90, 55.90, 55.90, 39.90],
    'Data adesão': pd.to_datetime(['2022-01-10', '2022-03-15', '2021-11-20', '2023-01-05',
                                   '2022-06-12', '2022-08-30', '2023-02-14', '2021-05-20',
                                   '2022-12-01', '2023-03-10']),
    'Ativo': [True, True, False, True, True,
              False, True, True, True, True]
}
df = pd.DataFrame(dados)
st.dataframe(df)
st.html('<p class="fonte_texto">A função <span class="texto_python">pd.DataFrame(dados)</span> '
        'atua como o catalisador que transforma uma estrutura de dados Python comum (o dicionário) '
        'em um objeto de análise sofisticado. Nesta etapa, algumas decisões técnicas '
        'merecem destaque:</p>')
st.html("<ol type=1 class='fonte_texto'>"
        "<li><b>Geração de IDs:</b> O uso de <span class='funcoes_python'>range</span>"
        "<span class='texto_python'>(</span><span class='numeros'>1001</span>"
        "<span class='texto_python'>,</span> <span class='numeros'>1011</span>"
        "<span class='texto_python'>)</span> cria uma sequência numérica automática, simulando uma "
        "chave primária de banco de dados.</li>"
        "<li><b>Valores Ausentes</b> <span class='texto_python'>(np.nan)</span><b>:</b> A inclusão "
        "deliberada de <span class='texto_python'>np.nan</span> na coluna 'Idade' é fundamental para "
        "demonstrar como o Pandas lida com a falta de informação. O "
        "<span class='texto_python'>NaN</span> (<i>Not a Number</i>) é um valor de ponto flutuante que "
        "serve como sentinela para dados faltantes, permitindo que o Pandas os identifique sem "
        "interromper cálculos matemáticos.</li>"
        "<li><b>Conversão de Séries Temporais:</b> A função "
        "<span class='texto_python'>pd.to_datetime()</span> converte strings de texto em objetos de "
        "data/hora (<i>timestamps</i>), o que é essencial para que o sistema reconheça a cronologia "
        "e permita cálculos de delta de tempo no futuro.</li>"
        "<li><b>Tipagem Booleana:</b> A coluna <span class='variaveis'>'Ativo'</span> utiliza valores "
        "<span class='palavras_reservadas'>True</span> e <span class='palavras_reservadas'>False</span>, "
        "demonstrando a capacidade da biblioteca de gerenciar lógica binária de forma nativa.</li>"
        "</ol>")
st.html('<p class="fonte_texto">A tabela abaixo resume a estrutura lógica resultante dessa criação:</p>')
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
    <th class="tg-hsa2">Coluna</th>
    <th class="tg-hsa2">Representação Técnica</th>
    <th class="tg-hsa2">Propósito Analítico</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-69a3">ID Usuário</td>
    <td class="tg-69a3">Inteiro (<span class='texto_python'>int64</span>)</td>
    <td class="tg-69a3">Identificação única e ordenação</td>
  </tr>
  <tr>
    <td class="tg-69a3">Nome</td>
    <td class="tg-69a3">String (<span class='texto_python'>object</span>)</td>
    <td class="tg-69a3">Identificação nominal do indivíduo</td>
  </tr>
  <tr>
    <td class="tg-69a3">Idade</td>
    <td class="tg-69a3">Inteiro (<span class='texto_python'>int64</span>)</td>
    <td class="tg-69a3">Análise demográfica e detecção de nulos</td>
  </tr>
  <tr>
    <td class="tg-69a3">Plano</td>
    <td class="tg-69a3">String (<span class='texto_python'>object</span>)</td>
    <td class="tg-69a3">Categorização de serviços</td>
  </tr>
  <tr>
    <td class="tg-69a3">Mensalidade</td>
    <td class="tg-69a3">Flutuante (<span class='texto_python'>float64</span>)</td>
    <td class="tg-69a3">Análise financeira e de receita</td>
  </tr>
  <tr>
    <td class="tg-69a3">Data adesão</td>
    <td class="tg-69a3">Data (<span class='texto_python'>datetime</span>)</td>
    <td class="tg-69a3">Análise de coorte e retenção</td>
  </tr>
  <tr>
    <td class="tg-69a3">Ativo</td>
    <td class="tg-69a3">Booleano (<span class='texto_python'>bool</span>)</td>
    <td class="tg-69a3">Status operacional e churn</td>
  </tr>
</tbody></table>''')
st.divider()

# --- Primeiras Impressões: O Exame Visual com head() e tail() --- #
st.html("<h1 class='fonte_titulo_aula'>Primeiras Impressões: O Exame Visual com "
        "<span class='texto_python'>head()</span> e <span class='texto_python'>tail()</span></h1>")
st.html('<p class="fonte_texto">Após a carga ou criação dos dados, o primeiro passo de qualquer '
        'analista é a inspeção visual. Isso não serve apenas para "ver" os dados, mas para garantir '
        'que a estrutura de colunas e o conteúdo das linhas estejam em conformidade com o esperado. '
        'O método <span class="texto_python">head()</span> é a ferramenta padrão para exibir as '
        'primeiras entradas do DataFrame:</p>')
st.code('''# --- Ver as 5 primeiras linhas (padrão) --- #
df.head()''', line_numbers=True)
st.dataframe(df.head())
st.html('''<p class="fonte_texto">Por padrão, o <span class="texto_python">head()</span> retorna as 
cinco primeiras linhas. Este comando é vital para verificar se os cabeçalhos das colunas foram lidos 
corretamente e se o alinhamento dos dados está preservado; é o equivalente a abrir a tampa de um motor 
para verificar se todas as peças estão no lugar.</p>''')
st.html('''<p class="fonte_texto">Complementarmente, o método 
<span class="texto_python">tail()</span> permite visualizar o final do conjunto de dados. Isso é 
particularmente útil para identificar se houve algum erro na ingestão de dados que pudesse ter 
causado o truncamento do arquivo ou a inclusão de linhas de rodapé indesejadas:</p>''')
st.code('''# --- Ver o final do DataFrame --- #
df.tail(3)''', line_numbers=True)
st.dataframe(df.tail(3))
st.html('''<p class="fonte_texto">A capacidade de passar um argumento numérico, como o 
<span class="numeros">3</span> no exemplo acima, permite que ajustemos a profundidade da amostra 
visual conforme a necessidade de contexto. O instrutor enfatiza que esses métodos são "testes de 
sanidade" rápidos que evitam o processamento visual desnecessário de milhares de linhas, focando apenas 
no início e no fim da massa de dados.''')
st.divider()

# --- O DNA dos Dados: Desvendando shape e dtypes --- #
st.html('''<h1 class="fonte_titulo_aula">O DNA dos Dados: Desvendando 
<span class="texto_python">shape</span> e <span class="texto_python">dtypes</span></h1>''')
st.html('''<p class="fonte_texto">Para uma compreensão técnica profunda, devemos olhar para além do 
conteúdo visual e focar na estrutura subjacente do objeto. O atributo 
<span class="texto_python">shape</span> fornece a dimensionalidade da matriz, retornando uma tupla 
contendo o número total de linhas e colunas. Saber que o dataset possui dez registros e sete colunas 
permite planejar a escalabilidade das operações subsequentes:''')
st.code("""print(f'''Dimensões (linha, coluna): {df.shape}
Tipos de dados em cada coluna: \n{df.dtypes}''')""", line_numbers=True)
st.html('''<p class="fonte_texto">O atributo <span class="texto_python">dtypes</span> é, talvez, um 
dos metadados mais cruciais no Pandas. Ele revela como a biblioteca interpretou cada coluna na memória. 
A tipagem correta é o que permite a execução de operações matemáticas: você não pode calcular a média 
de uma coluna que o Pandas interpretou como texto (<span class="texto_python">object</span>).''')
st.html('''<p class="fonte_texto">A transição da coluna <span class="variaveis">'Idade'</span> para o 
tipo <span class="texto_python">float64</span>, apesar de conter números inteiros, ocorre devido à 
presença do <span class="texto_python">np.nan</span>. Como o NumPy tradicionalmente gerencia o 
<span class="texto_python">NaN</span> como um objeto de ponto flutuante, a coluna inteira sofre uma 
coerção de tipo para manter a homogeneidade do array subjacente. Este é um exemplo clássico de como 
a presença de um único dado nulo pode alterar a assinatura técnica de uma variável inteira.''')
st.divider()

# --- O DNA dos Dados: Desvendando shape e dtypes --- #
st.html('''<h1 class="fonte_titulo_aula">O Diagnóstico de Saúde: O Poder do Método 
<span class="texto_python">info()</span></h1>''')
st.html('''<p class="fonte_texto">Se o <span class="texto_python">shape</span> e o 
<span class="texto_python">dtypes</span< fornecem as dimensões e os tipos, o método 
<span class="texto_python">info()</span> fornece o prontuário médico completo do DataFrame. Ele 
compila em um único relatório informações sobre o índice de linha, o tipo de cada coluna, a contagem 
de valores não nulos e o consumo de memória:''')
st.code('''# --- Saber as informações do DataFrame --- #
df.info()''', line_numbers=True)
st.html('''<p class="fonte_texto">A coluna <b>Non-Null Count</b> dentro do relatório do 
<span class="texto_python">info()</span> é a bússola para identificar a ausência de dados. Ao comparar 
o número de entradas não nulas com o índice total, podemos identifica instantaneamente onde estão as 
falhas informacionais. Por exemplo, se a coluna <span class="variaveis">'Idade'</span> reporta apenas 
8 valores não nulos para 10 entradas, o analista sabe de imediato que há um gap de 20% nessa variável.''')
st.html('''<p class="fonte_texto">Além disso, o <span class="texto_python">info()</span> oferece uma 
estimativa do uso de memória. Para datasets de grande porte, usamos o parâmetro 
<span class="texto_python">memory_usage=</span><span class="variaveis">'deep'</span>, que realiza uma 
inspeção profunda na memória RAM para reportar o consumo exato de objetos como strings, permitindo 
estratégias de otimização de recursos antes que o sistema atinja seus limites físicos.''')
st.divider()

# --- O Mapa Estatístico: Análise Quantitativa com describe() --- #
st.html('''<h1 class="fonte_titulo_aula">O Mapa Estatístico: Análise Quantitativa com 
<span class="texto_python">describe()</span></h1>''')
st.html('''<p class="fonte_texto">Após validar a saúde e a estrutura, o próximo passo lógico é a 
exploração estatística. O método <span class="texto_python">describe()</span> é o mecanismo que gera 
estatísticas descritivas básicas que resumem a tendência central, a dispersão e a forma da distribuição 
do conjunto de dados, excluindo automaticamente os valores <span class="texto_python">NaN</span> para 
não distorcer os resultados:''')
st.code('''# --- Informações estatísticas --- #
df.describe().T''', line_numbers=True)
st.dataframe(df.describe().T)
st.html('''<p class="fonte_texto">As métricas fornecidas para dados numéricos incluem:''')
st.html('<ul class="fonte_texto">'
        '<li><b>Count:</b> O número de observações válidas (não nulas).</li>'
        '<li><b>Mean:</b> A média aritmética das observações.</li>'
        '<li><b>Std:</b> O desvio padrão, indicando quão dispersos os dados estão em relação à média.</li>'
        '<li><b>Min:</b> O valor mínimo encontrado na coluna.</li>'
        '<li><b>Quartis (25%, 50%, 75%):</b> Indicadores de posição que dividem os dados. O 50% é '
        'equivalente à mediana.</li>'
        '<li><b>Max:</b> O valor máximo observado.</li>'
        '</ul>')
st.html('''<p class="fonte_texto">O uso do atributo <span class="texto_python">.T</span> 
(transposta) é uma técnica de ergonomia visual. Ao transpor a tabela resultante, as métricas passam a 
ser colunas e as variáveis originais tornam-se linhas, o que facilita a leitura quando lidamos com 
muitas colunas, permitindo uma comparação vertical mais intuitiva.''')

# --- A Lógica Categórica: unique() e value_counts() --- #
st.html('''<h1 class="fonte_titulo_aula">A Lógica Categórica: 
<span class="texto_python">unique()</span> e <span class="texto_python">value_counts()</span></h1>''')
st.html('''<p class="fonte_texto">Nem todos os dados são numéricos, e entender a diversidade e a 
frequência de categorias é vital para qualquer análise de negócio. Para as colunas qualitativas, como 
<span class="variaveis">'Plano'</span> ou <span class="variaveis">'Nome'</span>, o Pandas oferece 
ferramentas de identificação e contagem que revelam a composição do dataset.''')
st.html('''<p class="fonte_texto">O método <span class="texto_python">unique()</span> extrai uma 
lista (array) de todos os valores distintos presentes em uma coluna específica, preservando a ordem 
de primeira aparição. Isso é essencial para identificar categorias válidas ou detectar erros de entrada 
de dados, como variações de grafia para um mesmo item:''')
st.code('''# --- Saber os dados não numéricos (coluna "Nome") --- #
df['Nome'].unique()''', line_numbers=True)
st.dataframe(df['Nome'].unique(), width=100)
st.code('''# --- Saber os dados não numéricos (coluna "Plano") --- #
df['Plano'].unique()''')
st.dataframe(df['Plano'].unique(), width=100)
st.html('''<p class="fonte_texto">Enquanto o <span class="texto_python">unique()</span> foca na 
identificação, o método <span class="texto_python">value_counts()</span> foca na frequência. Ele 
retorna uma Series que mapeia cada valor único à sua contagem absoluta de ocorrências, ordenando-os 
automaticamente do mais frequente para o menos frequente.''')
st.code('''# --- Saber quanto de cada dado não numérico há na coluna (valor absoluto) --- #
df['Plano'].value_counts()''')
st.dataframe(df['Plano'].value_counts(), width=130)
st.html('''<p class="fonte_texto">Uma funcionalidade poderosa é a normalização dos resultados através 
do parâmetro <span class="texto_python">normalize=</span><span class="palavras_reservadas">True</span>. 
Isso converte as contagens absolutas em frequências relativas (proporções), permitindo que entendamos 
a distribuição percentual de cada categoria no universo do dataset:''')
st.code('''# --- Saber quanto de cada dados não numérico há na coluna (porcentagem) --- #
df['Plano'].value_counts(normalize=True)''', line_numbers=True)
st.dataframe(df['Plano'].value_counts(normalize=True), width=160)
st.html('''<p class="fonte_texto">Essa visão percentual é crucial para o planejamento estratégico. 
Saber que o plano <span class="variaveis">'Premium'</span> representa 40% da base instalada oferece uma 
compreensão muito mais rica do que apenas saber o número absoluto de usuários, facilitando a 
visualização de fatias de mercado internas e tendências de consumo.''')
st.divider()

# --- Resumo --- #
st.html('''<h1 class="fonte_titulo_aula">Resumo</h1>''')
st.html('''<p class="fonte_texto">A jornada de análise apresentada nesta aula estabelece um protocolo 
rigoroso para o primeiro contato com qualquer conjunto de dados. A sequência lógica de inspeção garante 
que não apenas conheçamos os dados, mas que compreenda suas limitações técnicas e estruturais. O 
processo começa com a amostragem visual das extremidades (
<span class="texto_python">head()</span> e <span class="texto_python">tail()</span>), avança para a definição 
do volume e tipagem (<span class="texto_python">shape</span> e <span class="texto_python">dtypes</span>), 
aprofunda-se na integridade informacional (<span class="texto_python">info()</span>), sintetiza as medidas 
de tendência central e dispersão (<span class="texto_python">describe()</span>) e finaliza com a 
decodificação da composição categórica (<span class="texto_python">unique()</span> 
e <span class="texto_python">value_counts()</span>).''')
st.html('''<p class="fonte_texto">O uso estratégico do NumPy, através do 
<span class="texto_python">np.nan</span>, permite que o Pandas gerencie o desconhecido de forma 
sistêmica, enquanto funções como <span class="texto_python">pd.to_datetime()</span> elevam o nível de 
abstração dos dados brutos para tipos significativos para o negócio. A tabela a seguir consolida os 
principais comandos e seus objetivos:''')
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
    <th class="tg-hsa2">Comando</th>
    <th class="tg-hsa2">Função Técnica</th>
    <th class="tg-hsa2">Valor Didático/Insight</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-69a3"><span class="texto_python">df.head(n)</span></td>
    <td class="tg-69a3">Retorna as n primeiras linhas</td>
    <td class="tg-69a3">Verificar se o cabeçalho e os primeiros dados estão corretos</td>
  </tr>
  <tr>
    <td class="tg-69a3"><span class="texto_python">df.tail(n)</span></td>
    <td class="tg-69a3">Retorna as n últimas linhas</td>
    <td class="tg-69a3">Garantir que não houve truncamento ou erro no final da tabela</td>
  </tr>
  <tr>
    <td class="tg-69a3"><span class="texto_python">df.shape</span></td>
    <td class="tg-69a3">Atributo de dimensionalidade</td>
    <td class="tg-69a3">Definir a escala da tabela (linhas vs colunas)</td>
  </tr>
  <tr>
    <td class="tg-69a3"><span class="texto_python">df.dtypes</span></td>
    <td class="tg-69a3">Atributo de tipos de dados</td>
    <td class="tg-69a3">Previnir erros de cálculo ao garantir a tipagem correta</td>
  </tr>
  <tr>
    <td class="tg-69a3"><span class="texto_python">df.info()</span></td>
    <td class="tg-69a3">Resumo de metadados</td>
    <td class="tg-69a3">Diagnosticar a saúde (nulos) e o consumo de hardware</td>
  </tr>
  <tr>
    <td class="tg-69a3"><span class="texto_python">df.describe()</span></td>
    <td class="tg-69a3">Estatísticas resumidas</td>
    <td class="tg-69a3">Perfil quantitativo e detecção de anomalias estatísticas</td>
  </tr>
  <tr>
    <td class="tg-69a3"><span class="texto_python">unique()</span></td>
    <td class="tg-69a3">Identificação de distintos</td>
    <td class="tg-69a3">Mapear a diversidade e identificar erros de digitação</td>
  </tr>
  <tr>
    <td class="tg-69a3"><span class="texto_python">value_counts()</span></td>
    <td class="tg-69a3">Contagem de frequências</td>
    <td class="tg-69a3">Revelar distribuição de massa e dominância de categorias</td>
  </tr>
</tbody></table>''')
st.divider()

# --- Conclusão --- #
st.html('''<h1 class="fonte_titulo_aula">Conclusão</h1>''')
st.html('''<p class="fonte_texto">A análise de dados eficiente é construída sobre o alicerce de um 
diagnóstico bem executado. Dominar o "raio-X" dos dados, como visto neste capítulo, transforma o 
programador em um analista capaz de garantir a integridade de todo o ciclo de vida da informação. A 
capacidade de identificar dados nulos, compreender a tipagem subjacente e mapear distribuições 
estatísticas é o que separa a análise superficial da exploração de dados profissional e fidedigna.''')
st.html('''<p class="fonte_texto">Ao utilizar comandos como <span class="texto_python">info()</span> 
para auditar a integridade e <span class="texto_python">describe()</span> para entender a variabilidade, 
o profissional estabelece uma fundação sólida para qualquer etapa posterior, seja ela uma visualização 
gráfica, uma limpeza de dados ou o treinamento de um modelo preditivo. O Pandas e o NumPy, quando 
operados com essa mentalidade diagnóstica, deixam de ser meras bibliotecas de manipulação e tornam-se 
ferramentas de precisão para a decifração da realidade contida nos números. O sucesso na ciência de 
dados não reside na complexidade do modelo final, mas na profundidade e no rigor do primeiro olhar 
sobre o conjunto de dados.''')
st.subheader('No mais é isso, nos vemos na próxima aula! Até lá, fiquem com Deus e fui!')
