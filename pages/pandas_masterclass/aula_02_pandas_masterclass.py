# --- Importar as bibliotecas --- #
import numpy as np
import pandas as pd
from PIL import Image
import streamlit as st

# --- Configurações iniciais da página --- #
st.set_page_config(
    page_title='Pandas Masterclass - Aula 02',
    page_icon=Image.open('./assets/logo/logo.png'),
    layout='wide'
)

# --- Carregar o estilo das fontes --- #
with open('./assets/css/style.css', 'r') as css:
    st.html(f'<style>{css.read()}</style>')

# --- Colocar o título da aula --- #
st.html('<h1 class="fonte_titulo_aula">Aula 02: Domine a Importação de Dados</h1>')

# --- Vídeo --- #
with st.expander('Se quiser acompanhar com o vídeo, acesse aqui! 👇'):
        st.video('https://youtu.be/uSPPRzi5dMQ')

# --- Código da aula --- #
st.subheader('Se quiser acessar o código completo da aula, clique [aqui](https://github.com/GTL98/canal_mundo_python/blob/main/Pandas%20Masterclass%3A%20Do%20Zero%20ao%20Her%C3%B3i%20dos%20Dados/Aula%2002/aula_02.ipynb)')
st.divider()

# --- Introdução --- #
st.subheader('E fala, devs! Tudo bem com vocês? Espero que sim!')
st.html('<h1 class="fonte_titulo_aula">Introdução</h1>')
st.html('<p class="fonte_texto">A base de qualquer sistema de análise de dados ou inteligência artificial '
        'reside na qualidade e eficiência da ingestão de informações. No ecossistema Python, essa tarefa '
        'é predominantemente liderada por duas bibliotecas fundamentais: NumPy e Pandas. Enquanto o NumPy '
        'fornece a infraestrutura para computação numérica de alto desempenho e geração de dados '
        'estatísticos, o Pandas oferece a abstração de alto nível necessária para manipular tabelas '
        'complexas, conhecidas como DataFrames. O processo de carregar dados de fontes externas, sejam '
        'elas arquivos de texto, planilhas corporativas ou formatos binários otimizados, exige uma '
        'compreensão profunda dos parâmetros de configuração e das implicações arquiteturais de '
        'cada escolha.</p>')
st.subheader('Então sem mais delongas, bora para a aula!')
st.divider()

# --- O Ecossistema de Manipulação de Dados: Fundamentos de NumPy e Pandas --- #
st.html('<h1 class="fonte_titulo_aula">O Ecossistema de Manipulação de Dados: Fundamentos de NumPy e '
        'Pandas</h1>')
st.html('<p class="fonte_texto">A construção de um pipeline de dados começa com a importação de ferramentas '
        'que permitem a manipulação eficiente de memória e cálculos vetorizados. O NumPy é essencial para '
        'lidar com arrays multidimensionais, enquanto o Pandas se especializa em dados tabulares '
        'heterogêneos. A integração entre essas bibliotecas é tão íntima que o Pandas utiliza arrays do '
        'NumPy internamente para armazenar dados de colunas, garantindo que operações matemáticas em '
        'larga escala sejam executadas em velocidade de linguagem C:</p>')
st.code('''# --- Importar as bibliotecas --- #
import numpy as np
import pandas as pd''', line_numbers=True)
st.html('<p class="fonte_texto">A importação do NumPy como <span class="texto_python">np</span> '
        'e do Pandas como <span class="texto_python">pd</span> convenção universal na comunidade '
        'de ciência de dados. Essa prática facilita a legibilidade do código e a colaboração entre '
        'equipes de engenharia. O NumPy será o motor por trás da geração de valores aleatórios e '
        'distribuições estatísticas, enquanto o Pandas atuará como o arquiteto que organiza esses valores '
        'em uma estrutura lógica de linhas e colunas.</p>')
st.divider()

# --- Arquitetura de Simulação: Preparando o Laboratório de Dados --- #
st.html('<h1 class="fonte_titulo_aula">Arquitetura de Simulação: Preparando o Laboratório de Dados</h1>')
st.html('<p class="fonte_texto">Antes de processar dados do mundo real, é uma prática de engenharia comum '
        'criar ambientes controlados, ou "laboratórios", para validar algoritmos e fluxos de trabalho. '
        'A geração de dados sintéticos permite testar a robustez de um sistema contra volumes variados e '
        'tipos de dados específicos. Para isso, utilizamos dicionários Python como moldes iniciais para a '
        'criação de DataFrames:</p>')
st.code('''# --- Criar um conjunto de dados --- #
dados = {
    'ID venda': range(1, 101),
    'Produto': np.random.choice(['Notebook', 'Tablet', 'Celular'], 100),
    'Preço': np.random.uniform(1000, 5000, 100).round(2),
    'Data': pd.date_range(start='2025-01-01', periods=100)
}
# --- Criar o DataFrame --- #
df = pd.DataFrame(dados)''', line_numbers=True)
dados = {
    'ID venda': range(1, 101),
    'Produto': np.random.choice(['Notebook', 'Tablet', 'Celular'], 100),
    'Preço': np.random.uniform(1000, 5000, 100).round(2),
    'Data': pd.date_range(start='2025-01-01', periods=100)
}
df = pd.DataFrame(dados)
st.dataframe(df, width=410)
st.html("<p class='fonte_texto'>A estrutura acima demonstra a versatilidade na criação de tipos de dados. "
        "A coluna <span class='variaveis'>'ID venda'</span> utiliza a função "
        "<span class='funcoes_python'>range</span> nativa do Python, gerando uma sequência numérica simples "
        "de 1 a 100. Contudo, a verdadeira potência surge com o uso do NumPy para simular comportamentos "
        "de mercado</p>")

# --- Distribuições Aleatórias e Amostragem Categórica --- #
st.html('<h2 class="fonte_subtitulo_aula">Distribuições Aleatórias e Amostragem Categórica</h2>')
st.html("<p class='fonte_texto'>A função <span class='texto_python'>np.random.choice()</span> é utilizada "
        "para gerar a coluna <span class='variaveis'>'Produto'</span>. Ela realiza uma amostragem "
        "aleatória a partir de uma lista de categorias fornecida "
        "(<span class='variaveis'>'Notebook'</span>, <span class='variaveis'>'Tablet'</span>, "
        "<span class='variaveis'>'Celular'</span>), preenchendo 100 registros. Por padrão, essa função "
        "assume uma distribuição uniforme, onde cada produto tem a mesma probabilidade de ser "
        "selecionado, a menos que probabilidades específicas sejam passadas através do parâmetro "
        "<span class='texto_python'>p</span>. Essa técnica é fundamental para simular inventários e "
        "comportamentos de escolha do consumidor em modelos de teste.</p>")
st.html("<p class='fonte_texto'>Para valores financeiros, a precisão e a distribuição são críticas. A "
        "função <span class='texto_python'>np.random.uniform(</span>"
        "<span class='numeros'>1000</span>, <span class='numeros'>5000</span>, "
        "<span class='numeros'>100</span><span class='texto_python'>)</span> gera 100 números de ponto "
        "flutuante distribuídos uniformemente entre 1000 e 5000. Matematicamente, em uma distribuição "
        "uniforme contínua, a probabilidade de qualquer valor dentro do intervalo "
        "<span class='texto_python'>[a, b)</span> é constante, dada pela função de densidade:</p>")
st.latex(r'f(x) = \begin{cases} \frac{1}{b-a} & \text{para } a \le x < b \\ 0 & \text{para } '
         r'x < a \text{ ou } x \ge b \end{cases}')
st.html("<p class='fonte_texto'>Onde <span class='texto_python'>a=1000</span> e "
        "<span class='texto_python'>b=5000</span>. O uso do método "
        "<span class='texto_python'>.</span><span class='funcoes_python'>round</span>"
        "<span class='texto_python'>(</span><span class='numeros'>2</span>"
        "<span class='texto_python'>)</span> ao final da geração garante que os preços simulem valores "
        "monetários reais com duas casas decimais, o que é essencial para evitar erros de arredondamento "
        "em cálculos de agregação posteriores.</p>")

# --- Engenharia de Séries Temporais com pd.date_range() --- #
st.html('<h2 class="fonte_subtitulo_aula">Engenharia de Séries Temporais com '
        '<span class="texto_python">pd.date_range()</span></h2>')
st.html("<p class='fonte_texto'>A gestão de tempo é um dos aspectos mais complexos da engenharia de "
        "dados. O Pandas resolve essa complexidade com a função "
        "<span class='texto_python'>pd.date_range()</span>, que cria um "
        "<span class='texto_python'>DatetimeIndex</span> altamente otimizado. No exemplo, iniciamos em "
        "<span class='variaveis'>'2025-01-01'</span> e geramos 100 períodos. Por padrão, a frequência é "
        "diária (<span class='variaveis'>'D'</span>), resultando em uma sequência contínua de datas. "
        "Esta função é vital para análises de séries temporais, pois permite operações de reamostragem "
        "(<i>resampling</i>) e deslocamento (<i>shifting</i>) de forma nativa e performática.</p>")
st.divider()

# --- Estratégias de Persistência e Exportação de Dados --- #
st.html('<h1 class="fonte_titulo_aula">Estratégias de Persistência e Exportação de Dados</h1>')
st.html("<p class='fonte_texto'>Uma vez que o DataFrame está estruturado na memória RAM, o próximo passo "
        "é a persistência em disco. A escolha do formato de saída impacta não apenas o espaço de "
        "armazenamento, mas também a integridade dos dados para processos futuros:</p>")
st.code('''# --- Salvar o DataFrame --- #
df.to_csv('vendas.csv', index=False, sep=';')
df.to_excel('vendas.xlsx', index=False, sheet_name='Vendas')
df.to_parquet('vendas.parquet', index=False)
print('Arquivos criados com sucesso!')''', line_numbers=True)
st.html("<p class='fonte_texto'>A função <span class='texto_python'>to_csv()</span> converte o DataFrame "
        "em um arquivo de texto simples. O parâmetro <span class='texto_python'>index=</span>"
        "<span class='palavras_reservadas'>False</span> é crucial; ele impede que o Pandas adicione uma "
        "coluna extra com os índices numéricos da linha, o que frequentemente causa redundância e erros "
        "de leitura em outros sistemas. O uso de <span class='texto_python'>sep=</span>"
        "<span class='variaveis'>';'</span> define o ponto e vírgula como delimitador, uma prática comum "
        "em regiões onde a vírgula é reservada para casas decimais.</p>")
st.html("<p class='fonte_texto'>Para o formato Excel, utilizamos "
        "<span class='texto_python'>to_excel()</span>. Diferente do CSV, o Excel é um formato de "
        "contêiner que permite múltiplas abas; o parâmetro <span class='texto_python'>sheet_name=</span>"
        "<span class='variaveis'>'Vendas'</span> organiza os dados em uma planilha específica dentro do "
        "arquivo. Por fim, <span class='texto_python'>to_parquet()</span> exporta os dados no formato "
        "Apache Parquet, uma escolha binária e colunar que oferece compressão superior e preservação "
        "estrita de tipos de dados.</p>")
st.divider()

# --- CSV: Superando Desafios de Estrutura e Codificação --- #
st.html('<h1 class="fonte_titulo_aula">CSV: Superando Desafios de Estrutura e Codificação</h1>')
st.html('<p class="fonte_texto">O formato CSV é amplamente utilizado por sua simplicidade, mas é '
        'inerentemente limitado por ser baseado em texto puro e carecer de uma definição de esquema '
        '(<i>schema</i>). Isso significa que todos os dados são armazenados como caracteres, exigindo que '
        'o interpretador "adivinhe" ou seja instruído sobre como converter esses caracteres de volta em '
        'números, datas ou categorias.</p>')
st.divider()

# --- Ingestão Seletiva e Gerenciamento de Memória --- #
st.html('<h1 class="fonte_titulo_aula">Ingestão Seletiva e Gerenciamento de Memória</h1>')
st.html("<p class='fonte_texto'>Ao lidar com arquivos CSV de grande escala, carregar todo o arquivo na "
        "memória pode ser ineficiente ou impossível. O Pandas oferece parâmetros avançados para controlar "
        "o processo de carga:</p>")
st.code('''# --- Carregar o arquivo CSV --- #
df_csv = pd.read_csv(
    'vendas.csv',
    sep=';',  # define o separador correto
    encoding='utf-8',  # tipo mais comum de codificação
    usecols=['Produto', 'Preço'],  # seleciona somente as colunas que importam para a análise
    nrows=10  # carrega apenas as 10 primeiras linhas do conjunto
)
df_csv''', line_numbers=True)
df_csv = pd.read_csv(
    './assets/imagens/pandas_masterclass/aula_02/arquivos/vendas.csv',
    sep=';',
    encoding='utf-8',
    usecols=['Produto', 'Preço'],
    nrows=10
)
st.dataframe(df_csv, width=220)
st.html("<p class='fonte_texto'>A parametrização correta do <span class='texto_python'>read_csv()</span>"
        " transforma um carregamento genérico em uma operação de engenharia precisa:</p>")
st.html('''<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-pvun{border-color:inherit;font-family:Arial, Helvetica, sans-serif !important;font-size:16px;font-weight:bold;
  text-align:center;vertical-align:top}
.tg .tg-jxpu{border-color:inherit;font-family:Arial, Helvetica, sans-serif !important;font-size:16px;text-align:center;
  vertical-align:top}
</style>
<table class="tg"><thead>
  <tr>
    <th class="tg-pvun">Parâmetro</th>
    <th class="tg-pvun">Função Técnica</th>
    <th class="tg-pvun">Motivo do Uso</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-jxpu"><span class='texto_python'>sep</span></td>
    <td class="tg-jxpu">Define o caractere delimitador entre campos.</td>
    <td class="tg-jxpu">Garante que o motor de parsing não aglutine colunas indevidamente.</span></td>
  </tr>
  <tr>
    <td class="tg-jxpu"><span class='texto_python'>encoding</span></td>
    <td class="tg-jxpu">Especifica o mapa de caracteres para decodificação de bytes.</td>
    <td class="tg-jxpu">Evita erros de leitura em caracteres especiais e acentuações (ex: 
    <span class='variaveis'>'utf-8'</span>, <span class='variaveis'>'latin-1'</span>).</td>
  </tr>
  <tr>
    <td class="tg-jxpu"><span class='texto_python'>usecols</span></td>
    <td class="tg-jxpu">Filtra as colunas carregadas diretamente na fonte.</td>
    <td class="tg-jxpu">Reduz significativamente o consumo de memória RAM ao ignorar dados irrelevantes.</td>
  </tr>
  <tr>
    <td class="tg-jxpu"><span class='texto_python'>nrows</span></td>
    <td class="tg-jxpu">Limita o número de registros processados.</td>
    <td class="tg-jxpu">Útil para inspeções rápidas ou processamento de amostras em datasets massivos.</td>
  </tr>
</tbody></table>''')
st.html("<p class='fonte_texto'>O uso de <span class='texto_python'>usecols</span> é uma das técnicas "
        "mais eficazes para otimização. Em vez de carregar um arquivo de 1GB para depois filtrar as "
        "colunas, o Pandas lê apenas os bytes necessários das colunas solicitadas, o que acelera o tempo "
        "de I/O e mantém o footprint de memória baixo.</p>")

# --- O Dilema do Encoding e Decodificação --- #
st.html('<h2 class="fonte_subtitulo_aula">O Dilema do Encoding e Decodificação</h2>')
st.html("<p class='fonte_texto'>A codificação de caracteres (<span class='texto_python'>encoding</span>) "
        "é frequentemente a fonte de falhas em pipelines de dados. O padrão "
        "<span class='texto_python'>utf-8</span> é capaz de representar quase todos os caracteres de todas "
        "as línguas, mas sistemas mais antigos podem exportar dados em "
        "<span class='texto_python'>latin-1</span> (ISO-8859-1) ou cp1252. Se o encoding estiver "
        "incorreto, caracteres como <span class='variaveis'>'é'</span> ou "
        "<span class='variaveis'>'ç'</span> aparecerão corrompidos como símbolos estranhos (ex: Ã©) ou "
        "dispararão um <span class='erro_python'>UnicodeDecodeError</span>. A especificação explícita "
        "do encoding garante que a tradução de bytes para strings seja fiel à origem do dado.</p>")
st.divider()

# --- Excel: O Formato de Intercâmbio Corporativo --- #
st.html('<h1 class="fonte_titulo_aula">Excel: O Formato de Intercâmbio Corporativo</h1>')
st.html("<p class='fonte_texto'>Embora o Excel não seja otimizado para grandes volumes de dados devido ao "
        "overhead do formato XML e à lentidão dos motores de leitura, ele continua sendo a ferramenta "
        "principal para a comunicação entre analistas e áreas de negócio. O Pandas facilita essa "
        "integração através do método <span class='texto_python'>read_excel()</span>:</p>")
st.code('''# --- Carregar o arquivo Excel --- #
df_excel = pd.read_excel(
    'vendas.xlsx',
    sheet_name='Vendas'
)
df_excel''', line_numbers=True)
df_excel = pd.read_excel(
    './assets/imagens/pandas_masterclass/aula_02/arquivos/vendas.xlsx',
    sheet_name='Vendas'
)
st.dataframe(df_excel, width=450)
st.html("<p class='fonte_texto'>Diferente do CSV, o Excel armazena metadados básicos sobre os tipos de "
        "células, mas o parâmetro mais crítico aqui é o <span class='texto_python'>sheet_name</span>. "
        "Um arquivo Excel pode conter dezenas de abas, e o Pandas permite acessar uma específica pelo "
        "nome (string) ou pela posição (inteiro, começando em 0). Caso o objetivo seja carregar todos os "
        "dados de uma vez, passar <span class='texto_python'>sheet_name=</span>"
        "<span class='palavras_reservadas'>None</span> retornará um dicionário de DataFrames, onde cada "
        "chave corresponde ao nome de uma aba, permitindo iterações programáticas sobre todo o livro de "
        "planilhas.</p>")
st.html("<p class='fonte_texto'>A eficiência do carregamento de Excel também depende do motor "
        "(<i>engine</i>) instalado. O openpyxl é o padrão para arquivos "
        "<span class='texto_python'>.xlsx</span>, enquanto o xlrd lida com o antigo formato "
        "<span class='texto_python'>.xls</span>. Para programadores avançados, o parâmetro "
        "<span class='texto_python'>usecols</span> também está disponível para Excel, aceitando inclusive "
        "intervalos de colunas no formato de letras (ex: 'A:C') ou nomes de colunas, ajudando a mitigar "
        "a lentidão inerente ao formato.")
st.divider()

# --- Parquet: Performance Colunar e Tipagem Robusta --- #
st.html('<h1 class="fonte_titulo_aula">Parquet: Performance Colunar e Tipagem Robusta</h1>')
st.html("<p class='fonte_texto'>Para profissionais que lidam com Big Data, o formato Apache Parquet é "
        "a escolha superior em comparação ao CSV ou Excel. O Parquet é um formato colunar, o que "
        "significa que os valores de uma mesma coluna são armazenados juntos em disco, permitindo "
        "compressões extremamente eficientes e saltos de leitura (seek) que ignoram colunas não "
        "utilizadas:</p>")
st.code('''# --- Carregar o arquivo Parquet --- #
df_parquet = pd.read_parquet('vendas.parquet')
df_parquet''', line_numbers=True)
df_parquet = pd.read_parquet('./assets/imagens/pandas_masterclass/aula_02/arquivos/vendas.parquet')
st.dataframe(df_parquet, width=450)

# --- Preservação de dtypes: O Experimento de Comparação --- #
st.html('<h2 class="fonte_subtitulo_aula">Preservação de '
        '<span class="texto_python">dtypes</span>: O Experimento de Comparação</h2>')
st.html("<p class='fonte_texto'>Uma das maiores vantagens do Parquet é a preservação do esquema e dos "
        "tipos de dados (<span class='texto_python'>dtypes</span>). Enquanto o CSV perde informações "
        "sobre o que é uma data ou um número, convertendo tudo para texto, o Parquet armazena o tipo "
        "exato de cada dado. O código abaixo demonstra essa divergência na prática:</p>")
st.code("""# --- Comparação entre o CSV e Parquet --- #
df_csv = pd.read_csv('vendas.csv', sep=';')
print(f'''dtype de "Data" no CSV: {df_csv["Data"].dtype}
dtype do "Data" no Parquet: {df_parquet["Data"].dtype}''')""", line_numbers=True)
st.html("<p class='fonte_texto'>Ao executar esta comparação, observa-se que o CSV frequentemente "
        "carrega a coluna de datas como o tipo <span class='texto_python'>object</span> (basicamente "
        "strings), a menos que o parâmetro <span class='texto_python'>parse_dates</span> seja "
        "utilizado. Por outro lado, o Parquet mantém a coluna como "
        "<span class='texto_python'>datetime64[ns]</span> de forma nativa.</p>")
st.html("<p class='fonte_texto'>Essa diferença tem implicações profundas na performance e na precisão:</p>")
st.html('<ol type=1 class="fonte_texto">'
        '<li><b>Consumo de Memória:</b> Tipos nativos (como datetime ou int64) ocupam menos espaço que '
        'suas representações em string.</li>'
        '<li><b>Velocidade de Processamento:</b> Operações de filtro em datas nativas são ordens de grandeza '
        'mais rápidas do que em strings, pois não exigem conversão em tempo de execução.</li>'
        '<li><b>Integridade:</b> Elimina a ambiguidade de formatos de data (ex: DD/MM vs MM/DD), já que o '
        'Parquet armazena o valor temporal absoluto.</li>'
        '</ol>')

# --- Estrutura Interna e Eficiência de I/O --- #
st.html('<h2 class="fonte_subtitulo_aula">Estrutura Interna e Eficiência de I/O</h2>')
st.html("<p class='fonte_texto'>O Parquet organiza os dados em <i>Row Groups</i> (grupos de linhas) e "
        "<i>Column Chunks</i> (pedaços de colunas). Isso permite uma técnica chamada "
        "<i>Predicate Pushdown</i>, onde o motor de leitura decide ignorar fatias inteiras do arquivo "
        "sem sequer lê-las, caso os metadados indiquem que os valores buscados não estão lá.</p>")
st.divider()

# --- Ingestão via URL: Flexibilidade na Nuvem --- #
st.html('<h1 class="fonte_titulo_aula">Ingestão via URL: Flexibilidade na Nuvem</h1>')
st.html("<p class='fonte_texto'>A arquitetura moderna de dados frequentemente exige o carregamento de "
        "arquivos hospedados em servidores remotos, buckets de armazenamento em nuvem ou repositórios "
        "públicos como o GitHub. O Pandas facilita essa tarefa ao permitir que as funções de leitura "
        "aceitem URLs diretamente no lugar de caminhos de arquivos locais:</p>")
st.code('''# --- Acessar os dados através de uma URL --- #
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df_titanic = pd.read_csv(url)
df_titanic''', line_numbers=True)
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df_titanic = pd.read_csv(url)
st.dataframe(df_titanic)
st.html("<p class='fonte_texto'>Neste exemplo, o Pandas utiliza bibliotecas internas para gerenciar a "
        "requisição HTTP, baixar o conteúdo do arquivo <span class='texto_python'>titanic.csv</span> e "
        "processá-lo na memória RAM. Esta funcionalidade é idêntica para formatos Excel ou Parquet, "
        "desde que o link aponte diretamente para o recurso binário.</p>")
st.html("<p class='fonte_texto'>A ingestão via URL oferece várias vantagens estratégicas:</p>")
st.html('<ul class="fonte_texto">'
        '<li><b>Prototipagem Rápida:</b> Permite acessar datasets de referência sem necessidade de download '
        'manual e gestão de arquivos locais.</li>'
        '<li><b>Integração com APIs:</b> Facilita a leitura de endpoints que exportam dados em formato CSV ou '
        'JSON de forma dinâmica.</li>'
        '<li><b>Versionamento:</b> Ao apontar para URLs de repositórios específicos, garante-se que a análise '
        'esteja rodando sobre uma versão específica do dado hospedado.</li>'
        '</ul>')
st.html("<p class='fonte_texto'>No entanto, é fundamental estar ciente da latência de rede e da segurança. "
        "Para arquivos massivos, o download via URL pode se tornar um gargalo, e em ambientes de "
        "produção, tokens de autenticação podem ser necessários, os quais podem ser passados através do "
        "parâmetro <span class='texto_python'>storage_options</span> em versões recentes do Pandas.</p>")
st.divider()

# --- Comparativo Analítico de Formatos de Dados --- #
st.html('<h1 class="fonte_titulo_aula">Comparativo Analítico de Formatos de Dados</h1>')
st.html("<p class='fonte_texto'>Para a seleção adequada do formato de persistência e ingestão, é "
        "necessário avaliar o equilíbrio entre legibilidade humana, performance de máquina e custo de "
        "armazenamento.</p>")
st.html('''<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ahef{border-color:#000000;font-family:Arial, Helvetica, sans-serif !important;font-size:16px;font-weight:bold;
  text-align:center;vertical-align:top}
.tg .tg-zc62{border-color:#000000;font-family:Arial, Helvetica, sans-serif !important;font-size:16px;text-align:center;
  vertical-align:top}
</style>
<table class="tg"><thead>
  <tr>
    <th class="tg-ahef">Critério</th>
    <th class="tg-ahef">CSV</th>
    <th class="tg-ahef">Excel (XLSX)</th>
    <th class="tg-ahef">Parquet</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-zc62">Formato de Arquivo</td>
    <td class="tg-zc62">Texto Plano</td>
    <td class="tg-zc62">Binário/XML</td>
    <td class="tg-zc62">Binário Colunar</td>
  </tr>
  <tr>
    <td class="tg-zc62">Compressão Nativa</td>
    <td class="tg-zc62">Não (requer externa)</td>
    <td class="tg-zc62">Sim (ZIP interna)</td>
    <td class="tg-zc62">Sim (Snappy/Gzip)</td>
  </tr>
  <tr>
    <td class="tg-zc62">Velocidade de Leitura</td>
    <td class="tg-zc62">Moderada</td>
    <td class="tg-zc62">Baixa</td>
    <td class="tg-zc62">Alta</td>
  </tr>
  <tr>
    <td class="tg-zc62">Preservação de Tipos</td>
    <td class="tg-zc62">Não (requer parsing)</td>
    <td class="tg-zc62">Básica</td>
    <td class="tg-zc62">Completa</td>
  </tr>
  <tr>
    <td class="tg-zc62">Uso em Big Data</td>
    <td class="tg-zc62">Ineficiente</td>
    <td class="tg-zc62">Não recomendado</td>
    <td class="tg-zc62">Padrão da Indústria</td>
  </tr>
  <tr>
    <td class="tg-zc62">Legibilidade Humana</td>
    <td class="tg-zc62">Alta</td>
    <td class="tg-zc62">Alta</td>
    <td class="tg-zc62">Nula</td>
  </tr>
</tbody></table>''')
st.html("<p class='fonte_texto'>O Parquet destaca-se como o formato mais eficiente para pipelines de "
        "processamento, enquanto o CSV permanece como o padrão de ouro para portabilidade simples entre "
        "diferentes softwares e sistemas operacionais. O Excel, embora lento para processamento de máquina, "
        "é insubstituível para a entrega final de relatórios para usuários de negócios.</p>")
st.divider()

# --- Resumo --- #
st.html('<h1 class="fonte_titulo_aula">Resumo</h1>')
st.html("<p class='fonte_texto'>Neste capítulo, exploramos a jornada completa do dado, desde sua criação "
        "sintética até a ingestão avançada de múltiplas fontes. Iniciamos com o uso do NumPy para gerar "
        "distribuições aleatórias e amostragem de categorias, simulando cenários reais de mercado através "
        "de funções como <span class='texto_python'>np.random.choice()</span> e "
        "<span class='texto_python'>np.random.uniform()</span>. Vimos como o Pandas atua como o motor "
        "central de estruturação com o <span class='texto_python'>pd.DataFrame()</span> e a gestão de "
        "séries temporais com <span class='texto_python'>pd.date_range()</span>.</p>")
st.html("<p class='fonte_texto'>Aprofundamos na mecânica de leitura de arquivos, destacando:</p>")
st.html('<ul class="fonte_texto">'
        '<li><b>CSV:</b> A importância de gerenciar delimitadores, codificações de caracteres ('
        '<span class="texto_python">encoding</span>) e a otimização de memória usando '
        '<span class="texto_python">usecols</span> e <span class="texto_python">nrows</span>.</li>'
        '<li><b>Excel:</b> A organização por abas com '
        '<span class="texto_python">sheet_name</span> e a integração com o ambiente corporativo.</li>'
        '<li><b>Parquet:</b> A revolução do armazenamento colunar, que garante performance de I/O superior e '
        'a integridade total dos tipos de dados entre sessões de processamento.</li>'
        '<li><b>URL:</b> A flexibilidade de tratar a web como um sistema de arquivos local, facilitando o '
        'acesso a dados na nuvem.</li>'
        '</ul>')
st.divider()

# --- Conclusão --- #
st.html('<h1 class="fonte_titulo_aula">Conclusão</h1>')
st.html("<p class='fonte_texto'>A ingestão de dados é frequentemente subestimada, mas é o alicerce sobre "
        "o qual toda a análise de dados é construída. A escolha correta entre formatos de arquivo e a "
        "parametrização precisa das funções de leitura do Pandas e NumPy definem se um pipeline de dados "
        "será ágil e robusto ou lento e propenso a falhas.</p>")
st.html("<p class='fonte_texto'>Para o programador Python avançado, o domínio desses conceitos permite a "
        "construção de sistemas que não apenas processam informações, mas que o fazem com eficiência de "
        "memória e precisão técnica. A transição de arquivos de texto simples (CSV) para formatos "
        "binários otimizados (Parquet) marca a evolução de um analista de dados para um engenheiro de "
        "dados capaz de lidar com volumes massivos e complexidades modernas. Ao compreender os mecanismos "
        "internos de como o Pandas interage com o disco e com a memória RAM, o desenvolvedor ganha a "
        "liberdade de desenhar soluções que escalam conforme a necessidade do negócio, garantindo a "
        "fidelidade dos dados desde a origem até o insight final.</p>")
st.subheader('No mais é isso, nos vemos na próxima aula! Até lá, fiquem com Deus e fui!')
