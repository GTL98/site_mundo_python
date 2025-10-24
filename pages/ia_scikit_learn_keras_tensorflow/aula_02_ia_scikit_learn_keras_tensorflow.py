# --- Importar as bibliotecas --- #
import pandas as pd
from PIL import Image
import streamlit as st

# --- Configurações iniciais da página --- #
st.set_page_config(
    page_title='Capítulo 02 - Projeto de aprendizado de máquina de ponta a ponta',
    page_icon=Image.open('./assets/logo/logo.png'),
    layout='wide'
)

# --- Carregar o estilo das fontes --- #
with open('./assets/css/style.css', 'r') as css:
    st.html(f'<style>{css.read()}</style>')

# --- Colocar o banner do capítulo --- #
st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_02/aula_02.png')

# --- Introdução --- #
st.html('<h1 class="fonte_titulo_aula">Introdução</h1>')
st.html('<p class="fonte_texto">Neste capítulo, você trabalhará em um projeto de exemplo de ponta a ponta, '
        'fingindo ser um cientista de dados recém-contratado em uma empresa imobiliária. Aqui estão as '
        'principais etapas pelas quais você passará:</p>')
st.html('<ol type=1 class="fonte_texto">'
        '<li>Olhar para o quadro geral.</li>'
        '<li>Obter os dados.</li>'
        '<li>Descubrir e visualizar os dados para obter insights.</li>'
        '<li>Preparar os dados para algoritmos de aprendizado de máquina.</li>'
        '<li>Selecionar um modelo e treiná-lo.</li>'
        '<li>Ajustar seu modelo.</li>'
        '<li>Apresentar sua solução.</li>'
        '<li>Lançar, monitorar e mantenher seu sistema.</li>'
        '</ol>')

# --- Trabalhando com dados reais --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Trabalhando com dados reais</h1>')
st.html('<p class="fonte_texto">Quando você está aprendendo sobre aprendizado de máquina, é melhor '
        'experimentar dados do mundo real, não conjuntos de dados artificiais. Felizmente, existem '
        'milhares de conjuntos de dados abertos para escolher, abrangendo todos os tipos de domínios. '
        'Aqui estão alguns lugares onde você pode procurar para obter dados:</p>')
st.html('<ul class="fonte_texto">'
        '<li>Repositórios populares de dados abertos:</li>'
            '<ul class="fonte_texto">'
                '<li><a href="https://archive.ics.uci.edu/">UC Irvine Machine Learning Repository</a></li>'
                '<li><a href="https://www.kaggle.com/datasets">Conjunto de dados no Kaggle</a></li>'
                '<li><a href="https://registry.opendata.aws/">Conjunto de Dados no AWS da Amazon</a></li>'
            '</ul>'
        '<li>Portal Meta (eles listam repositórios de dados abertos):</li>'
            '<ul class="fonte_texto">'
                '<li><a href="https://dataportals.org/">Data Portals</a></li>'
                '<li><a href="https://project.opendatamonitor.eu/">OpenDataMonitor</a></li>'
                '<li><a href="https://data.nasdaq.com/institutional-investors">Quandl</a></li>'
            '</ul>'
        '<li>Outras páginas listando muitos repositórios populares de dados abertos:</li>'
            '<ul class="fonte_texto">'
                '<li><a href="https://en.wikipedia.org/wiki/List_of_datasets_for_machine-learning_research">Lista de conjuntos de dados de Aprendizado de Máquina do Wikipedia</a></li>'
                '<li><a href="https://www.quora.com/Where-can-I-find-large-datasets-open-to-the-public">Quora.com</a></li>'
                '<li><a href="https://www.reddit.com/r/datasets/">Conjuntos de dados no Reddit</a></li>'
            '</ul>')
st.html('<p class="fonte_texto">Neste capítulo usaremos o conjunto de dados <i>California Housing Prices</i> '
        'do repositório StatLib (veja a Figura 2-1). Este conjunto de dados é baseado em dados do censo '
        'da Califórnia de 1990. Não é exatamente recente (uma bela casa na Baía de São Francisco ainda era '
        'acessível na '
        'época), mas tem muitas qualidades para o aprendizado, então vamos fingir que são dados recentes. '
        'Para fins de ensino, adicionei um atributo categórico e removi alguns recursos.</p>')
st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_02/figura_01.png',
         caption='Figura 2-1. Preços de casas na Califórnia.')

# --- Olhe para o quadro geral --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Olhe para o quadro geral</h1>')
st.html('<p class="fonte_texto">Bem-vindo à Machine Learning Housing Corporation! A sua primeira tarefa '
        'é utilizar os dados do censo da Califórnia para construir um modelo dos preços da habitação no '
        'estado. Esses dados incluem métricas como população, renda média e preço médio da habitação para '
        'cada grupo de quarteirões na Califórnia. Os grupos de quarteirões são a menor unidade geográfica '
        'para a qual o <i>US Census Bureau</i> publica dados de amostra (um grupo de quarteirões '
        'normalmente tem '
        'uma população de 600 a 3.000 pessoas). Vamos chamá-los abreviadamente de “distritos”. Seu modelo '
        'deve aprender com esses dados e ser capaz de prever o preço médio da habitação em qualquer '
        'distrito, dadas todas as outras métricas.</p>')
with st.expander('Dica 1', icon='💡'):
    st.html('<p class="fonte_texto">Como você é um cientista de dados bem organizado, a primeira coisa que '
            'deve fazer é obter a lista de verificação do projeto de aprendizado de máquina. Neste capítulo '
            'examinaremos muitos itens da lista de verificação, mas também pularemos alguns, seja porque '
            'são autoexplicativos ou porque serão discutidos em capítulos posteriores.</p>')
st.html('<h2 class="fonte_subtitulo_aula">Enquadre o problema</h2>')
st.html('<p class="fonte_texto">A primeira pergunta a fazer ao seu chefe é qual é exatamente o objetivo do '
        'negócio. Construir um modelo provavelmente não é o objetivo final. Como a empresa espera usar e se '
        'beneficiar desse modelo? Conhecer o objetivo é importante porque determinará como você enquadra o '
        'problema, quais algoritmos você selecionará, qual medida de desempenho você usará para avaliar seu '
        'modelo e quanto esforço você gastará para ajustá-lo.</p>')
st.html('<p class="fonte_texto">O seu chefe responde que o resultado do seu modelo (uma previsão do preço '
        'médio da habitação num distrito) será transmitido a outro sistema de aprendizagem automática '
        '(ver Figura 2-2), juntamente com muitos outros sinais. Este sistema a jusante determinará se vale '
        'a pena investir numa determinada área ou não. Fazer isso da maneira certa é fundamental, pois '
        'afeta diretamente as receitas.</p>')
st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_02/figura_02.png',
         caption='Figura 2-2. Um pipeline de Aprendizado de Máquina para investimentos imobiliários.')
with st.expander('Pipeline'):
    st.html('<p class="fonte_texto">Uma sequência de componentes de processamento de dados é chamada de '
            '<i>pipeline</i> de dados. Pipelines são muito comuns em sistemas de Aprendizado de Máquina, '
            'pois há '
            'muitos dados para manipular e muitas transformações de dados para aplicar.</p>')
    st.html('<p class="fonte_texto">Os componentes normalmente são executados de forma assíncrona. Cada '
            'componente extrai uma grande quantidade de dados, processa-os e exibe o resultado em outro '
            'armazenamento de dados. Então, algum tempo depois, o próximo componente no pipeline extrai '
            'esses dados e gera sua própria saída. Cada componente é bastante independente: a interface '
            'entre os componentes é simplesmente o armazenamento de dados. Isso torna o sistema simples de '
            'entender (com a ajuda de um gráfico de fluxo de dados), e diferentes equipes podem se '
            'concentrar em diferentes componentes. Além disso, se um componente quebrar, os componentes '
            'posteriores podem muitas vezes continuar a funcionar normalmente (pelo menos por um tempo) '
            'usando apenas a última saída do componente quebrado. Isso torna a arquitetura bastante '
            'robusta.</p>')
    st.html('<p class="fonte_texto">Por outro lado, um componente quebrado pode passar despercebido por '
            'algum tempo se o monitoramento adequado não for implementado. Os dados ficam obsoletos e o '
            'desempenho geral do sistema cai.</p>')
st.html('<p class="fonte_texto">A próxima pergunta a ser feita ao seu chefe é como é a solução atual (se '
        'houver). A situação atual muitas vezes lhe dará uma referência de desempenho, bem como insights '
        'sobre como resolver o problema. O seu chefe responde que os preços da habitação distrital são '
        'atualmente estimados manualmente por especialistas: uma equipa reúne informações atualizadas '
        'sobre um distrito e, quando não conseguem obter o preço médio da habitação, estimam-no '
        'utilizando regras complexas.</p>')
st.html('<p class="fonte_texto">Isto é caro e demorado, e as estimativas não são boas; nos casos em que '
        'conseguem descobrir o preço médio real da habitação, muitas vezes percebem que as suas '
        'estimativas estavam erradas em mais de 20%. É por isso que a empresa pensa que seria útil '
        'treinar um modelo para prever o preço médio da habitação num distrito, devido a outros dados sobre '
        'esse distrito. Os dados do censo parecem ser um excelente conjunto de dados a explorar para este '
        'fim, uma vez que incluem os preços médios da habitação de milhares de distritos, bem como outros '
        'dados.</p>')
st.html('<p class="fonte_texto">Com todas essas informações, agora você está pronto para começar a '
        'projetar seu sistema. Primeiro, você precisa enquadrar o problema: é supervisionado, não '
        'supervisionado ou aprendizado por reforço? É uma tarefa de classificação, uma tarefa de regressão '
        'ou outra coisa? Você deve usar aprendizagem em lote ou técnicas de aprendizagem online? Antes '
        'de continuar lendo, faça uma pausa e tente responder a essas perguntas você mesmo.</p>')
st.html('<p class="fonte_texto">Você encontrou as respostas? Vejamos: é claramente uma tarefa típica de '
        'aprendizagem supervisionada, uma vez que lhe são dados exemplos de formação <i>etiquetados</i> '
        '(cada instância vem com o resultado esperado, ou seja, o preço médio da habitação no distrito). '
        'É também uma tarefa típica de regressão, pois é solicitado que você preveja um valor. Mais '
        'especificamente, este é um problema de <i>regressão múltipla</i>, uma vez que o sistema '
        'utilizará múltiplas características para fazer uma previsão (utilizará a população do distrito, '
        'o rendimento mediano, etc.). É também um problema de <i>regressão univariada</i>, uma vez que '
        'estamos apenas a tentar prever um único valor para cada distrito. Se estivéssemos tentando '
        'prever vários valores por distrito, seria um problema de <i>regressão multivariada</i>. '
        'Finalmente, não há fluxo contínuo de dados entrando no sistema, não há necessidade específica '
        'de se ajustar rapidamente às mudanças de dados e os dados são pequenos o suficiente para caber '
        'na memória, portanto, o aprendizado simples em lote deve funcionar perfeitamente.</p>')
with st.expander('Dica 2', icon='💡'):
    st.html('<p class="fonte_texto">Se os dados fossem enormes, você poderia dividir seu trabalho de '
            'aprendizagem em lote em vários servidores (usando a técnica MapReduce) ou usar uma técnica de '
            'aprendizagem online.</p>')
st.html('<h2 class="fonte_subtitulo_aula">Selecione uma medida de desempenho</h2>')
st.html('<p class="fonte_texto">A próxima etapa é selecionar uma medida de desempenho. Uma medida de '
        'desempenho típica para problemas de regressão é o Raiz do Erro Quadrático Médio (REQM). Dá uma ideia '
        'de quanto erro o sistema normalmente comete em suas previsões, com peso maior para erros grandes. '
        'A abaixo mostra a fórmula matemática para calcular o REQM.</p>')
st.latex(r'REQM(\mathbf{X}, h) = \sqrt{\frac{1}{m}\sum_{i=1}^{m}(h(\mathbf{x}^{(i)})) - y^{(i)}}')
with st.expander('Notações'):
    st.html('<p class="fonte_texto">Esta equação apresenta várias notações muito comuns de aprendizado de '
            'máquina que usaremos ao longo do nosso estudo:</p>')
    st.html('<ul class="fonte_texto">'
                '<li><b>m</b> é o número de instâncias no conjunto de dados em que você está medindo o '
                'REQM.</li>'
                '<ul class="fonte_texto">'
                    '<li>Por exemplo, se você estiver avaliando o REQM em um conjunto de validação de 2.000 '
                    'distritos, então m = 2.000.</li>'
                '</ul>'
                '<li><b>x&#8317;&#8305;&#8318;</b> é um vetor de todos os valores de recurso (excluindo o rótulo) do '
                '<i-ésimo</i> termo no conjunto de dados, e <b>y&#8317;&#8305;&#8318;</b> é seu rótulo (o valor de saída desejado '
                'para essa instância).</li>'
                '<ul class="fonte_texto">'
                    '<li>Por exemplo, se o primeiro distrito no conjunto de dados estiver localizado na '
                    'longitude –118,29°, latitude 33,91°, e tiver 1.416 habitantes com uma renda média de US$ '
                    '38.372, e o valor médio da casa for US$ 156.400 (ignorando os outros recursos por '
            'enquanto), então:</li>'
            '</ul>')
    st.latex(r'''\mathbf{x}^{(1)} = \begin{pmatrix}
-118,29 \\
33,91 \\
1416 \\
38.372 \\
\end{pmatrix}''')
    st.html('<p class="fonte_texto">e</p>')
    st.latex('y^{(1)} = 156.400')
    st.html('<ul class="fonte_texto">'
                '<li><b>X</b> é uma matriz que contém todos os valores de recursos (excluindo rótulos) de '
                'todas as instâncias no conjunto de dados. Há uma linha por instância, e a i-ésima linha '
                'é igual à transposta de <b>x<sup>(i)</sup></b> , notada (<b>x<sup>(i)</sup></b>)<sup>⊺'
                '</sup>.</li>'
                '<ul class="fonte_texto">'
                    '<li>Por exemplo, se o primeiro distrito for como descrito, então a matriz <b>X</b> terá '
                    'esta aparência:</li>'
                '</ul>'
            '</ul>')
    st.latex(r'''\mathbf{X} = \begin{pmatrix}
\mathbf{(x^{(1)})}^{T} \\
\mathbf{(x^{(2)})}^{T} \\
\vdots  \\
\mathbf{(x^{(1999)})}^{T} \\
\mathbf{(x^{(2000)})}^{T} \\
\end{pmatrix} = \begin{pmatrix}
-188,29 & 33,91 & 1416 & 38.372 \\
\vdots & \vdots & \vdots & \vdots \\
\end{pmatrix}''')
    st.html('<ul class="fonte_texto">'
                '<li><b>h</b> é a função de previsão do seu sistema, também chamada de <i>hipótese</i>. '
                'Quando seu sistema recebe um vetor de recursos de uma instância x<sup>(i)</sup>, '
                'ele gera um valor '
                'previsto ŷ<sup>(i)</sup> = h(x<sup>(i)</sup>) para essa instância (ŷ é pronunciado '
                '“y-hat”).</li>'
                '<ul class="fonte_texto">'
                    '<li>Por exemplo, se o seu sistema prevê que o preço médio da habitação no primeiro '
                    'distrito é de US$ 158.400, então ŷ<sup>(1)</sup> = h(x<sup>(1)</sup>) = 158.400. O '
                    'erro de previsão para este distrito é ŷ<sup>(1)</sup> – y<sup>(1)</sup> = 2.000.</li>'
                '</ul>'
                '<li>REQM(<b>X</b>,h) é a função de custo medida no conjunto de exemplos usando sua '
                'hipótese <i>h</i>.</li>'
            '</ul>')
    st.html('<p class="fonte_texto">Usamos fonte minúscula em itálico para valores escalares (como <i>m</i> '
            'ou <i>y<sup>(i)</sup></i> ) e nomes de funções (como <i>h</i>), fonte minúscula em negrito para '
            'vetores (como <b>x<sup>(i)</sup></b> ) e fonte maiúscula em negrito para matrizes (como '
            '<b>X</b>).</p>')
st.html('<p class="fonte_texto">Embora o REQM seja geralmente a medida de desempenho preferida para tarefas '
        'de regressão, em alguns contextos você pode preferir usar outra função. Por exemplo, suponha '
        'que existam muitos distritos atípicos. Nesse caso, você pode considerar usar o <i>erro médio '
        'absoluto</i> (EMA, também chamado de desvio absoluto médio):</p>')
st.latex(r'EMA(\mathbf{X}, h) = \frac{1}{m}\sum_{i=1}^{m}|h(\mathbf{x}^{(i)})-y^{(i)}|')
st.html('<p class="fonte_texto">Tanto o REQM quanto o EMA são formas de medir a distância entre dois '
        'vetores: o vetor de previsões e o vetor de valores alvo. Várias medidas de distância, ou '
        '<i>normas</i>, são possíveis:</p>')
st.html('<ul class="fonte_texto">'
            '<li>Calcular a raiz de uma soma de quadrados (REQM) corresponde à <i>norma euclidiana</i>: '
            'esta é a noção de distância com a qual você está familiarizado. Também é chamada de '
            '<i>ℓ<sub>2</sub> norma</i>, notada ∥ · ∥<sub>2</sub> (ou apenas ∥ · ∥).</li>'
            '<li>O cálculo da soma dos absolutos (EMA) corresponde à norma <i>ℓ<sub>1</sub></i>, notada '
            '∥ · ∥<sub>1</sub>. Isso às vezes é chamado de <i>norma de Manhattan</i> porque mede a '
            'distância entre dois pontos em uma cidade se você só puder viajar ao longo de quarteirões '
            'ortogonais da cidade.</li>'
            '<li>Mais genericamente, a norma <i>ℓ<sub>k</sub></i> de um vetor <b>v</b> contendo <i>n</i> '
            'elementos é definida como ∥<b>v</b>∥<sub>k</sub> = (|v<sub>0</sub>|<sup>k</sup> + '
            '|v<sub>1</sub>|<sup>k</sup> + ... + |v<sub>n</sub>|<sup>k</sup>)<sup>1/k</sup>. '
            '<i>ℓ<sub>0</sub></i> fornece o número de elementos diferentes de zero no vetor e '
            '<i>ℓ<sub>∞</sub></i> fornece o valor absoluto máximo no vetor.</li>'
            '<li>Quanto maior o índice de norma, mais ele se concentra nos valores grandes e negligencia '
            'os pequenos. É por isso que o REQM é mais sensível a valores discrepantes do que o EMA. Mas '
            'quando os valores discrepantes são exponencialmente raros (como em uma curva em forma de sino), '
            'o REQM tem um desempenho muito bom e geralmente é o preferido.</li>'
        '</ul>')
st.html('<h2 class="fonte_subtitulo_aula">Verifique as hipóteses</h2>')
st.html('<p class="fonte_texto">Por último, é uma boa prática listar e verificar as suposições feitas até '
        'agora (por você ou por outras pessoas); isso pode ajudá-lo a detectar problemas sérios desde o '
        'início. Por exemplo, os preços distritais gerados pelo seu sistema serão inseridos em um sistema '
        'de aprendizado de máquina downstream, e você assume que esses preços serão usados como tal. Mas '
        'e se o sistema a jusante converter os preços em categorias (por exemplo, “barato”, “médio” ou '
        '“caro”) e depois utilizar essas categorias em vez dos próprios preços? Neste caso, acertar o '
        'preço perfeitamente não é importante; seu sistema só precisa acertar a categoria. Se for assim, '
        'então o problema deveria ter sido enquadrado como uma tarefa de classificação, não como uma '
        'tarefa de regressão. Você não vai querer descobrir isso depois de trabalhar em um sistema de '
        'regressão por meses.</p>')
st.html('<p class="fonte_texto">Felizmente, depois de conversar com a equipe responsável pelo sistema '
        'downstream, você tem certeza de que eles realmente precisam dos preços reais, não apenas das '
        'categorias. Ótimo! Está tudo pronto, as luzes estão verdes e você pode começar a codificar '
        'agora!</p>')

# --- Obtenha os dados --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Obtenha os dados</h1>')
st.html('<p class="fonte_texto">É hora de colocar a mão na massa! Não hesite em pegar seu computador e '
        'escrever junto os códigos a seguir. Para essa aula e as futuras, recomendo que utilize o '
        '<a href="https://colab.google/">Google Colaboratory</a> ou o <a href="https://jupyter.org/">'
        'Jupyter Notebook</a>.</p>')
st.html('<h2 class="fonte_subtitulo_aula">Baixe os dados</h2>')
st.html('<p class="fonte_texto">Em ambientes típicos, seus dados estariam disponíveis em um banco de dados '
        'relacional (ou algum outro armazenamento de dados comum) e espalhados por várias '
        'tabelas/documentos/arquivos. Para acessá-lo, primeiro você precisa obter suas credenciais e '
        'autorizações de acesso e se familiarizar com o esquema de dados. Neste projeto, porém, as coisas '
        'são muito mais simples: basta baixar um único arquivo compactado, <i>housing.tgz</i>, que contém um '
        'arquivo de valores separados por vírgula (CSV) chamado <i>housing.csv</i> com todos os dados.</p>')
st.html('<p class="fonte_texto">Você pode usar seu navegador para baixar o arquivo e descompactá-lo '
        'para extrair o arquivo CSV, mas é preferível criar uma pequena '
        'função para fazer isso. Ter uma função que baixe os dados é útil principalmente se os dados mudam '
        'regularmente: você pode escrever um pequeno script que use a função para buscar os dados mais '
        'recentes (ou pode configurar um trabalho agendado para fazer isso automaticamente em intervalos '
        'regulares). Automatizar o processo de busca de dados também é útil se você precisar instalar o '
        'conjunto de dados em várias máquinas. Aqui está a função para baixar os dados:</p>')
st.code('''import os
import urllib
import tarfile

RAIZ_DOWNLOAD = 'https://raw.githubusercontent.com/ageron/handson-ml2/master/'
HOUSING_CAMINHO = os.path.join('datasets', 'housing')
HOUSING_URL = RAIZ_DOWNLOAD + 'datasets/housing/housing.tgz'

def baixar_dados_housing(housing_url=HOUSING_URL, housing_caminho=HOUSING_CAMINHO):
    os.makedirs(housing_caminho, exist_ok=True)
    caminho_tgz = os.path.join(housing_caminho, 'housing.tgz')
    urllib.request.urlretrieve(housing_url, caminho_tgz)
    housing_tgz = tarfile.open(caminho_tgz)
    housing_tgz.extractall(path=housing_caminho)
    housing_tgz.close()''', line_numbers=True)
st.html('<p class="fonte_texto">Agora, quando você chama <b>baixar_dados_housing()</b>, ele cria um '
        'diretório datasets/housing em seu espaço de trabalho, baixa o arquivo <i>housing.tgz</i> e '
        'extrai o arquivo <i>housing.csv</i> dele neste diretório:</p>')
st.code('baixar_dados_housing()', line_numbers=True)
st.html('<p class="fonte_texto">Agora vamos carregar os dados usando pandas. Mais uma vez, você deve '
        'escrever uma pequena função para carregar os dados:</p>')
st.code('''import pandas as pd

def carregar_dados_housing(housing_caminho=HOUSING_CAMINHO):
    csv_caminho = os.path.join(housing_caminho, 'housing.csv')
    return pd.read_csv(csv_caminho)''', line_numbers=True)
st.html('<p class="fonte_texto">Esta função retorna um objeto DataFrame do pandas contendo todos '
        'os dados.</p>')
st.html('<h2 class="fonte_subtitulo_aula">Dê uma olhada rápida na estrutura de dados</h2>')
st.html('<p class="fonte_texto">Vamos dar uma olhada nas cinco primeiras linhas usando o método '
        '<b>head()</b> do DataFrame:</p>')
st.code('''housing = carregar_dados_housing()
housing.head()''', line_numbers=True)
tabela_2_1 = pd.read_csv('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_02/tabela_2_1.csv')
st.dataframe(tabela_2_1, hide_index=True)
st.html('<p class="fonte_texto">Cada linha representa um distrito. Existem 10 atributos: <b>longitude</b>, '
        '<b>latitude</b>, <b>housing_median_age</b>, <b>total_rooms</b>, <b>total_bedrooms</b>, '
        '<b>population</b>, <b>households</b>, <b>median_income</b>, '
        '<b>median_house_value</b> e <b>ocean_proximity</b>.</p>')
st.html('<p class="fonte_texto">O método <b>info()</b> é útil para obter uma descrição rápida dos dados, '
        'em particular o número total de linhas, o tipo de cada atributo e o número de valores não '
        'nulos:</p>')
st.code('housing.info()', line_numbers=True)
tabela_2_2 = pd.read_csv('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_02/tabela_2_2.csv')
st.dataframe(tabela_2_2, hide_index=True)
st.html('<p class="fonte_texto">Existem 20.640 instâncias no conjunto de dados, o que significa que ele é '
        'bastante pequeno para os padrões de aprendizado de máquina, mas é perfeito para começar. Observe '
        'que o atributo <b>total_bedrooms</b> possui apenas 20.433 valores não nulos, o que significa que '
        '207 distritos não possuem esse recurso. Precisaremos cuidar disso mais tarde.</p>')
st.html('<p class="fonte_texto">Todos os atributos são numéricos, exceto o campo <b>ocean_proximity</b>. '
        'Seu tipo é <b>object</b>, então ele pode conter qualquer tipo de objeto Python. Mas como você '
        'carregou esses dados de um arquivo CSV, você sabe que deve ser um atributo de texto. Ao observar '
        'as cinco primeiras linhas, você provavelmente notou que os valores na coluna '
        '<b>ocean_proximity</b> eram repetitivos, o que significa que provavelmente é um atributo '
        'categórico. Você pode descobrir quais categorias existem e quantos distritos pertencem a cada '
        'categoria usando o método <b>value_counts()</b>:</p>')
st.code("housing['ocean_proximity'].value_counts()", line_numbers=True)
tabela_2_3 = pd.read_csv('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_02/tabela_2_3.csv')
st.dataframe(tabela_2_3, hide_index=True)
st.html('<p class="fonte_texto">Vejamos os outros campos. O método <b>describe()</b> mostra um resumo '
        'dos atributos numéricos:</p>')
st.code('housing.describe().T', line_numbers=True)
tabela_2_4 = pd.read_csv('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_02/tabela_2_4.csv')
st.dataframe(tabela_2_4, hide_index=True)
st.html('<p class="fonte_texto">As colunas <b>count</b>, <b>mean</b>, <b>min</b> e <b>max</b> são '
        'autoexplicativas. Observe que os valores nulos são ignorados (por exemplo, a <b>contagem</b> de '
        '<b>total_bedrooms</b> é 20.433, não 20.640). A coluna <b>std</b> mostra o <i>desvio padrão<i>, '
        'que mede o quão dispersos estão os valores. As colunas 25%, 50% e 75% mostram os <i>percentis</i> '
        'correspondentes: um percentil indica o valor abaixo do qual cai uma determinada porcentagem de '
        'observações em um grupo de observações. Por exemplo, 25% dos distritos têm uma '
        '<b>housing_median_age</b> inferior a 18 anos, enquanto 50% são inferiores a 29 e 75% são '
        'inferiores a 37. Estes são frequentemente chamados de primeiro <i>quartil</i>, '
        'mediana (segundo quartil) e ou terceiro quartil.</p>')
st.html('<p class="fonte_texto">Outra maneira rápida de ter uma ideia do tipo de dados com os quais você '
        'está lidando é traçar um histograma para cada atributo numérico. Um histograma mostra o número '
        'de instâncias (no eixo vertical) que possuem um determinado intervalo de valores (no eixo '
        'horizontal). Você pode plotar esse atributo por vez ou chamar o método <b>hist()</b> em todo o '
        'conjunto de dados (como mostrado no exemplo de código a seguir), e ele plotará um histograma '
        'para cada atributo numérico:</p>')
st.code('''import matplotlib.pyplot as plt

housing.hist(bins=50, figsize=(20, 15))
plt.show()''', line_numbers=True)
st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_02/figura_03.png',
         caption='Figura 2-3. Um histograma para cada atributo numérico.')
st.html('<p class="fonte_texto">Existem algumas coisas que você pode notar nesses histogramas:</p>')
st.html('<ol type="1" class="fonte_texto">'
            '<li>Primeiro, o atributo de renda mediana (<b>median_income</b>)não parece ser expresso em '
            'dólares americanos (USD). '
            'Depois de verificar com a equipe que coletou os dados, você será informado de que os dados '
            'foram dimensionados e limitados a 15 (na verdade, 15,0001) para rendas medianas mais altas e a '
            '0,5 (na verdade, 0,4999) para rendas medianas mais baixas. Os números representam '
            'aproximadamente dezenas de milhares de dólares (por exemplo, 3 na verdade significa cerca de '
            'US$ 30.000). Trabalhar com atributos pré-processados é comum em Aprendizado de Máquina e não é '
            'necessariamente um problema, mas você deve tentar entender como os dados foram computados.</li>'
            '<li>A idade média da habitação e o valor médio da casa também foram limitados. Este último '
            'pode ser um problema sério, pois é o seu atributo alvo (seus rótulos). Seus algoritmos de '
            'aprendizado de máquina podem aprender que os preços nunca ultrapassam esse limite. Você '
            'precisa verificar com a equipe do seu cliente (a equipe que usará a saída do seu sistema) se '
            'isso é um problema ou não. Se eles lhe disserem que precisam de previsões precisas, mesmo '
            'além de US$ 500.000, você terá duas opções:</li>'
                '<ol type="a" class="fonte_texto">'
                    '<li>Colete rótulos adequados para os distritos cujos rótulos foram limitados.</li>'
                    '<li>Remova esses distritos do conjunto de treinamento (e também do conjunto de testes, '
                    'pois seu sistema não deve ser mal avaliado se prever valores acima de US$ 500.000).</li>'
                '</ol>'
            '<li>Esses atributos têm escalas muito diferentes. Discutiremos isso mais tarde neste capítulo, '
            'quando explorarmos o escalonamento de recursos.</li>'
            '<li>Finalmente, muitos histogramas têm uma <i>cauda pesada</i>: eles se estendem muito mais '
            'para a direita da mediana do que para a esquerda. Isso pode tornar um pouco mais difícil para '
            'alguns algoritmos de aprendizado de máquina detectar padrões. Tentaremos transformar esses '
            'atributos mais tarde para obter distribuições mais em forma de sino.</li>'
        '</ol>')
st.html('<p class="fonte_texto">Esperamos que agora você compreenda melhor o tipo de dados com os quais '
        'está lidando.</p>')
with st.expander('Alerta 1', icon='⚡'):
    st.html('<p class="fonte_texto">Espere! Antes de examinar mais os dados, você precisa criar um conjunto '
            'de testes, colocá-lo de lado e nunca mais examiná-lo.</p>')
st.html('<h2 class="fonte_subtitulo_aula">Crie um conjunto de testes</h2>')
st.html('<p class="fonte_texto">Pode parecer estranho reservar voluntariamente parte dos dados nesta fase. '
        'Afinal, você apenas deu uma rápida olhada nos dados e certamente deveria aprender muito mais sobre '
        'eles antes de decidir quais algoritmos usar, certo? Isso é verdade, mas seu cérebro é um incrível '
        'sistema de detecção de padrões, o que significa que é altamente propenso a overfitting: se você '
        'olhar para o conjunto de testes, poderá tropeçar em algum padrão aparentemente interessante nos '
        'dados de teste que o levará a selecionar um tipo específico de modelo de aprendizado de máquina. '
        'Ao estimar o erro de generalização usando o conjunto de testes, sua estimativa será muito '
        'otimista e você iniciará um sistema que não funcionará tão bem quanto o esperado. Isso é chamado '
        'de viés de <i>rastreamento de dados</i>.</p>')
st.html('<p class="fonte_texto">Criar um conjunto de testes é teoricamente simples: escolha algumas '
        'instâncias aleatoriamente, normalmente 20% do conjunto de dados (ou menos se o seu conjunto de '
        'dados for muito grande), e reserve-as:</p>')
st.code('''import numpy as np

def separacao_treino_teste(dados, quantidade_teste):
    indices_embaralhados = np.random.permutation(len(dados))
    tamanho_conjunto_teste = int(len(dados) * quantidade_teste)
    indices_teste = indices_embaralhados[:tamanho_conjunto_teste]
    indices_treino = indices_embaralhados[tamanho_conjunto_teste:]
    return dados.iloc[indices_treino], dados.iloc[indices_teste]''', line_numbers=True)
st.html('<p class="fonte_texto">Você pode então usar esta função assim:</p>')
st.code('''conjunto_treino, conjunto_teste = separacao_treino_teste(housing, 0.2)
print(len(conjunto_treino))
print(len(conjunto_teste))''', line_numbers=True)
st.html('<p class="fonte_texto">Bem, isso funciona, mas não é perfeito: se você executar o programa '
        'novamente, ele irá gerar um conjunto de testes diferente! Com o tempo, você (ou seus algoritmos '
        'de aprendizado de máquina) conseguirá ver todo o conjunto de dados, que é o que você deseja '
        'evitar.</p>')
st.html('<p class="fonte_texto">Uma solução é salvar o conjunto de testes na primeira execução e carregá-lo '
        'nas execuções subsequentes. Outra opção é definir a semente do gerador de números aleatórios '
        '(por exemplo, com <b>np.random.seed(42)</b>) antes de chamar <b>np.random.permutation()</b> para '
        'que ele sempre gere os mesmos índices embaralhados.</p>')
st.html('<p class="fonte_texto">Mas ambas as soluções serão interrompidas na próxima vez que você buscar '
        'um conjunto de dados atualizado. Para ter uma divisão de treinamento/teste estável mesmo após a '
        'atualização do conjunto de dados, uma solução comum é usar o identificador de cada instância '
        'para decidir se deve ou não entrar no conjunto de testes (assumindo que as instâncias tenham um '
        'identificador único e imutável). Por exemplo, você poderia calcular um hash do identificador '
        'de cada instância e colocar essa instância no conjunto de teste se o hash for menor ou igual a '
        '20% do valor máximo do hash. Isto garante que o conjunto de testes permanecerá consistente em '
        'várias execuções, mesmo se você atualizar o conjunto de dados. O novo conjunto de testes '
        'conterá 20% das novas instâncias, mas não conterá nenhuma instância que estivesse anteriormente '
        'no conjunto de treinamento. Aqui está uma possível implementação:</p>')
st.code('''from zlib import crc32

def verificar_conjunto_teste(identificador, quantidade_teste):
    return crc32(np.int64(identificador)) & 0xffffffff < quantidade_teste * 2**32

def separacao_treino_teste_id(dados, quantidade_teste, id_coluna):
    ids = dados[id_coluna]
    no_conjunto_teste = ids.apply(lambda id_: verificar_conjunto_teste(id_, quantidade_teste))
    return dados.loc[~no_conjunto_teste], dados.loc[no_conjunto_teste]''', line_numbers=True)
st.html('<p class="fonte_texto">Infelizmente, o conjunto de dados habitacionais não possui uma coluna de '
        'identificador. A solução mais simples é usar o índice de linha como ID:</p>')
st.code('''housing_com_id = housing.reset_index()  # adicionar a coluna 'index'
conjunto_treino, conjunto_teste = separacao_treino_teste_id(housing_com_id, 0.2, 'index')''', line_numbers=True)
st.html('<p class="fonte_texto">Se você usar o índice de linha como um identificador exclusivo, precisará '
        'garantir que os novos dados sejam anexados ao final do conjunto de dados e que nenhuma linha seja '
        'excluída. Se isso não for possível, você pode tentar usar os recursos mais estáveis para '
        'construir um identificador exclusivo. Por exemplo, a latitude e a longitude de um distrito são '
        'garantidamente estáveis por alguns milhões de anos, então você pode combiná-las em um ID '
        'como este:</p>')
st.code('''housing_com_id['id'] = housing['longitude'] * 1000 + housing['latitude']
conjunto_treino, conjunto_teste = separacao_treino_teste_id(housing_com_id, 0.2, 'id')''', line_numbers=True)
st.html('<p class="fonte_texto">Scikit-Learn fornece algumas funções para dividir conjuntos de dados em '
        'vários subconjuntos de várias maneiras. A função mais simples é <b>train_test_split()</b>, que '
        'faz praticamente a mesma coisa que a função <b>separacao_treino_teste()</b>, com alguns recursos '
        'adicionais. Primeiro, existe um parâmetro <b>random_state</b> que permite definir a semente do '
        'gerador aleatório. Segundo, você pode passar vários conjuntos de dados com um número idêntico de '
        'linhas e dividi-los nos mesmos índices (isso é muito útil, por exemplo, se você tiver um '
        'DataFrame separado para rótulos):</p>')
st.code('''from sklearn.model_selection import train_test_split

conjunto_treino, conjunto_teste = train_test_split(housing, test_size=0.2, random_state=42)''', line_numbers=True)
st.html('<p class="fonte_texto">Até agora consideramos métodos de amostragem puramente aleatórios. '
        'Geralmente, isso é bom se o seu conjunto de dados for grande o suficiente (especialmente em '
        'relação ao número de atributos), mas se não for, você corre o risco de introduzir um viés de '
        'amostragem significativo. Quando uma empresa de pesquisas decide ligar para 1.000 pessoas para '
        'fazer algumas perguntas, ela não escolhe apenas 1.000 pessoas aleatoriamente em uma lista '
        'telefônica. Eles tentam garantir que estas 1.000 pessoas sejam representativas de toda a '
        'população. Por exemplo, a população dos EUA é composta por 51,3% de mulheres e 48,7% de homens, '
        'pelo que um inquérito bem conduzido nos EUA tentaria manter esta proporção na amostra: 513 '
        'mulheres e 487 homens. Isso é chamado de <i>amostragem estratificada</i>: a população é dividida '
        'em subgrupos homogêneos chamados <i>estratos</i>, e o número certo de instâncias é amostrado de '
        'cada estrato para garantir que o conjunto de teste seja representativo da população geral. Se as '
        'pessoas que realizam a pesquisa usassem uma amostragem puramente aleatória, haveria cerca de 12% '
        'de chance de amostrar um conjunto de testes distorcido que fosse menos de 49% de mulheres ou mais '
        'de 54% de mulheres. De qualquer forma, os resultados da pesquisa seriam significativamente '
        'tendenciosos.</p>')
st.html('<p class="fonte_texto">Suponha que você conversou com especialistas que lhe disseram que a renda '
        'média é um atributo muito importante para prever os preços médios da habitação. Talvez você queira '
        'garantir que o conjunto de testes seja representativo das diversas categorias de renda em todo o '
        'conjunto de dados. Como a renda média é um atributo numérico contínuo, primeiro é necessário '
        'criar um atributo de categoria de renda. Vejamos o histograma da renda média mais de perto (na '
        'Figura 2-3): a maioria dos valores da renda média estão agrupados em torno de 1,5 a 6 (ou seja, '
        'US$ 15.000 a US$ 60.000), mas algumas rendas médias vão muito além de 6. É importante ter um '
        'número suficiente de instâncias em seu conjunto de dados para cada estrato, caso contrário, a '
        'estimativa da importância de um estrato pode ser distorcida. Isso significa que você não deve ter '
        'muitos estratos e cada estrato deve ser grande o suficiente. O código a seguir usa a função '
        '<b>pd.cut()</b> para criar um atributo de categoria de renda com cinco categorias (rotuladas de '
        '1 a 5): a categoria 1 varia de 0 a 1,5 (ou seja, menos de US$ 15.000), a categoria 2 de 1,5 a 3 e '
        'assim por diante:</p>')
st.code('''housing['cat_renda'] = pd.cut(housing['median_income'],
                              bins=[0.0, 1.5, 3.0, 4.5, 6.0, np.inf],
                              labels=[1, 2, 3, 4, 5])''', line_numbers=True)
st.html('<p class="fonte_texto">Estas categorias de rendimento estão representadas na Figura 2-4:</p>')
st.code("housing['cat_renda'].hist()", line_numbers=True)
st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_02/figura_04.png',
         caption='Figura 2-4. Histograma das categorias de renda.')
st.html('<p class="fonte_texto">Agora você está pronto para fazer uma amostragem estratificada com base '
        'na categoria de renda. Para isso você pode usar a classe <b>StratifiedShuffleSplit</b> do '
        'Scikit-Learn:</p>')
st.code('''from sklearn.model_selection import StratifiedShuffleSplit

slipt = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for treino_indice, teste_indice in slipt.split(housing, housing['cat_renda']):
    conjunto_treino_estratificado = housing.loc[treino_indice]
    conjunto_teste_estratificado = housing.loc[teste_indice]''', line_numbers=True)
st.html('<p class="fonte_texto">Vamos ver se funcionou conforme o esperado. Você pode começar observando '
        'as proporções das categorias de renda no conjunto de teste:</p>')
st.code("conjunto_teste_estratificado['cat_renda'].value_counts() / len(conjunto_teste_estratificado)", line_numbers=True)
tabela_2_5 = pd.read_csv('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_02/tabela_2_5.csv')
st.dataframe(tabela_2_5, hide_index=True)
st.html('<p class="fonte_texto">Com um código semelhante, você pode medir as proporções das categorias de '
        'renda no conjunto de dados completo. A tabela abaixo compara as proporções das categorias de '
        'rendimento no conjunto de dados global, no conjunto de testes gerado com amostragem estratificada '
        'e num conjunto de testes gerado utilizando amostragem puramente aleatória. Como você pode ver, o '
        'conjunto de testes gerado usando amostragem estratificada tem proporções de categorias de renda '
        'quase idênticas às do conjunto de dados completo, enquanto o conjunto de testes gerado usando '
        'amostragem puramente aleatória é distorcido.</p>')
tabela_2_6 = pd.read_csv('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_02/tabela_2_6.csv')
st.dataframe(tabela_2_6, hide_index=True)
st.html('<p class="fonte_texto">Agora você deve remover o atributo <b>cat_renda</b> para que os dados '
        'voltem ao seu estado original:</p>')
st.code('''for conjunto in (conjunto_treino_estratificado, conjunto_teste_estratificado):
    conjunto.drop('cat_renda', axis=1, inplace=True)''', line_numbers=True)
st.html('<p class="fonte_texto">Passamos bastante tempo na geração de conjuntos de testes por um bom '
        'motivo: esta é uma parte frequentemente negligenciada, mas crítica de um projeto de Aprendizado '
        'de Máquina. Além disso, muitas destas ideias serão úteis mais tarde, quando discutirmos a '
        'validação cruzada. Agora é hora de passar para a próxima etapa: explorar os dados.</p>')

# --- Descubra e visualize os dados para obter insights --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Descubra e visualize os dados para obter insights</h1>')
st.html('<p class="fonte_texto">Até agora, você apenas deu uma rápida olhada nos dados para obter uma '
        'compreensão geral do tipo de dados que está manipulando. Agora o objetivo é aprofundar um pouco '
        'mais.</p>')
st.html('<p class="fonte_texto">Primeiro, certifique-se de ter deixado o conjunto de teste de lado e de '
        'estar apenas explorando o conjunto de treinamento. Além disso, se o conjunto de treinamento for '
        'muito grande, você pode querer experimentar um conjunto de exploração, para tornar as '
        'manipulações fáceis e rápidas. No nosso caso, o conjunto é bem pequeno, então você pode '
        'trabalhar diretamente no conjunto completo. Vamos criar uma cópia para que você possa brincar '
        'com ela sem prejudicar o conjunto de treinamento:</p>')
st.code('housing = conjunto_treino_estratificado.copy()', line_numbers=True)
st.html('<h2 class="fonte_subtitulo_aula">Visualizando Dados Geográficos</h2>')
st.html('<p class="fonte_texto">Como existe informação geográfica (latitude e longitude), é uma boa ideia '
        'criar um gráfico de dispersão de todos os distritos para visualizar os dados (Figura 2-5):</p>')
st.code("housing.plot(kind='scatter', x='longitude', y='latitude')", line_numbers=True)
st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_02/figura_05.png',
         caption='Figura 2-5. Um gráfico de dispersão geográfica dos dados.')
st.html('<p class="fonte_texto">Parece a Califórnia, mas fora isso é difícil ver qualquer padrão '
        'específico. Definir a opção <b>alpha</b> como <b>0.1</b> torna muito mais fácil visualizar os '
        'locais onde há uma alta densidade de pontos de dados (Figura 2-6):</p>')
st.code("housing.plot(kind='scatter', x='longitude', y='latitude', alpha='0.1')", line_numbers=True)
st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_02/figura_06.png',
         caption='Figura 2-6. Uma melhor visualização que destaca áreas de alta densidade.')
st.html('<p class="fonte_texto">Agora isso é muito melhor: você pode ver claramente as áreas de alta '
        'densidade, nomeadamente a Baía de São Francisco e ao redor de Los Angeles e San Diego, além de '
        'uma longa '
        'linha de densidade bastante alta no Vale Central, em particular em torno de Sacramento e '
        'Fresno.</p>')
st.html('<p class="fonte_texto">Nossos cérebros são muito bons em detectar padrões em imagens, mas talvez '
        'seja necessário brincar com os parâmetros de visualização para destacar os padrões.</p>')
st.html('<p class="fonte_texto">Agora vejamos os preços da habitação (Figura 2-7). O raio de cada círculo '
        'representa a população do distrito (parâmetro <b>s</b>) e a cor representa o preço '
        '(parâmetro <b>c</b>). '
        'Usaremos um mapa de cores pré-definido (parâmetro <b>cmap</b>) chamado <b>jet</b>, que varia do '
        'azul '
        '(valores baixos) ao vermelho (preços altos):</p>')
st.code("""housing.plot(kind='scatter', x='longitude', y='latitude', alpha=0.4,
             s=housing['population']/100, label='População', figsize=(10, 7),
             c='median_house_value', cmap=plt.get_cmap('jet'), colorbar=True)
plt.legend()""", line_numbers=True)
st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_02/figura_07.png',
         caption='Figura 2-7. Preços da habitação na Califórnia: vermelho é caro, azul é barato, círculos '
                 'maiores indicam áreas com maior população.')
st.html('<p class="fonte_texto">Esta imagem diz-lhe que os preços da habitação estão muito relacionados '
        'com a localização (por exemplo, perto do oceano) e com a densidade populacional, como '
        'provavelmente já sabia. Um algoritmo de agrupamento deve ser útil para detectar o cluster '
        'principal e adicionar novos recursos que medem a proximidade dos centros do cluster. O atributo '
        'de proximidade do oceano também pode ser útil, embora no Norte da Califórnia os preços da '
        'habitação nos distritos costeiros não sejam demasiado elevados, então essa não é uma regra '
        'simples.</p>')
st.html('<h2 class="fonte_subtitulo_aula">Procurando Correlações</h2>')
st.html('<p class="fonte_texto">Como o conjunto de dados não é muito grande, você pode calcular facilmente '
        'o <i>coeficiente de correlação padrão</i> (também chamado de <i>r de Pearson</i>) entre cada par '
        'de atributos usando o método <b>corr()</b>:</p>')
st.code('matriz_corr = housing.corr(numeric_only=True)', line_numbers=True)
st.html('<p class="fonte_texto">Agora vamos ver o quanto cada atributo se correlaciona com o valor '
        'médio da casa:</p>')
tabela_2_7 = pd.read_csv('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_02/tabela_2_7.csv')
st.dataframe(tabela_2_7, hide_index=True)
st.html('<p class="fonte_texto">O coeficiente de correlação varia de –1 a 1. Quando está próximo de 1, '
        'significa que existe uma forte correlação positiva; por exemplo, o valor médio da casa tende a '
        'subir quando o rendimento médio aumenta. Quando o coeficiente está próximo de –1, significa que '
        'existe uma forte correlação negativa; você pode ver uma pequena correlação negativa entre a '
        'latitude e o valor médio da casa (ou seja, os preços têm uma ligeira tendência de cair quando '
        'você vai para o norte). Finalmente, coeficientes próximos de 0 significam que não há correlação '
        'linear. A Figura 2-8 mostra vários gráficos juntamente com o coeficiente de correlação entre '
        'seus eixos horizontal e vertical.</p>')
st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_02/figura_08.png',
         caption='Figura 2-8. Coeficiente de correlação padrão de vários conjuntos de dados.')
with st.expander('Alerta 2', icon='⚡'):
    st.html('<p class="fonte_texto">O coeficiente de correlação mede apenas correlações lineares (“se '
            '<i>x</i> sobe, então <i>y</i> geralmente sobe/desce”). Pode perder completamente as relações '
            'não lineares (por exemplo, “se <i>x</i> estiver próximo de 0, então <i>y</i> geralmente '
            'sobe”). Observe como todos os gráficos da linha inferior têm um coeficiente de correlação '
            'igual a 0, apesar do fato de seus eixos claramente não serem independentes: estes são '
            'exemplos de relações não lineares. Além disso, a segunda linha mostra exemplos onde o '
            'coeficiente de correlação é igual a 1 ou –1; observe que isso não tem nada a ver com a '
            'inclinação. Por exemplo, sua altura em polegadas tem um coeficiente de correlação de 1 com '
            'sua altura em pés ou em nanômetros.</p>')
st.html('<p class="fonte_texto">Outra maneira de verificar a correlação entre atributos é usar a função '
        '<b>scatter_matrix()</b> do pandas, que plota cada atributo numérico em relação a todos os outros '
        'atributos numéricos. Como agora existem 11 atributos numéricos, você obteria 11<sup>2</sup> = 121 '
        'lotes, que não caberiam em uma página – então vamos nos concentrar apenas em alguns atributos '
        'promissores que parecem mais correlacionados com o valor médio da habitação (Figura 2-9):</p>')
st.code('''from pandas.plotting import scatter_matrix

atributos = [
    'median_house_value',
    'median_income',
    'total_rooms',
    'housing_median_age'
]
scatter_matrix(housing[atributos], figsize=(12, 8))''', line_numbers=True)
st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_02/figura_09.png',
         caption='Figura 2-9. Esta matriz de dispersão representa cada atributo numérico em relação a '
                 'todos os '
                 'outros atributos numéricos, além de um histograma de cada atributo numérico.')
st.html('<p class="fonte_texto">A diagonal principal (do canto superior esquerdo ao canto inferior direito) '
        'estaria cheia de linhas retas se os pandas traçassem cada variável contra si mesmo, o que não '
        'seria muito útil. Então, em vez disso, o pandas exibe um histograma de cada atributo (outras '
        'opções estão disponíveis; consulte a documentação do pandas para obter mais detalhes).</p>')
st.html('<p class="fonte_texto">O atributo mais promissor para prever o valor médio da casa é a renda '
        'média, então vamos ampliar o gráfico de dispersão de correlação (Figura 2-10):</p>')
st.code('''housing.plot(
    kind='scatter',
    x='median_income',
    y='median_house_value',
    alpha=0.1
)''', line_numbers=True)
st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_02/figura_10.png',
         caption='Figura 2-10. Renda média vs valor médio da casa.')
st.html('<p class="fonte_texto">Este gráfico revela algumas coisas. Primeiro, a correlação é de fato muito '
        'forte; você pode ver claramente a tendência ascendente e os pontos não estão muito dispersos. Em '
        'segundo lugar, o limite de preço que observamos anteriormente é claramente visível como uma linha '
        'horizontal em US$ 500.000. Mas este gráfico revela outras linhas retas menos óbvias: uma linha '
        'horizontal em torno de US$ 450.000, outra em torno de US$ 350.000, talvez uma em torno de US$ '
        '280.000 e mais algumas abaixo disso. Você pode tentar remover os distritos correspondentes para '
        'evitar que seus algoritmos aprendam a reproduzir essas peculiaridades dos dados.</p>')
st.html('<h2 class="fonte_subtitulo_aula">Experimentando combinações de atributos</h2>')
st.html('<p class="fonte_texto">Esperamos que as seções anteriores tenham dado uma ideia de algumas '
        'maneiras de explorar os dados e obter insights. Você identificou algumas peculiaridades dos dados '
        'que pode querer limpar antes de alimentá-los em um algoritmo de aprendizado de máquina e '
        'encontrou correlações interessantes entre atributos, em particular com o atributo de destino. '
        'Você também notou que alguns atributos têm uma distribuição com cauda pesada, então você pode '
        'querer transformá-los (por exemplo, calculando seu logaritmo). É claro que sua abordagem irá '
        'variar consideravelmente com cada projeto, mas as ideias gerais são semelhantes.</p>')
st.html('<p class="fonte_texto">Uma última coisa que você pode querer fazer antes de preparar os dados '
        'para algoritmos de aprendizado de máquina é experimentar várias combinações de atributos. Por '
        'exemplo, o número total de aposentos num distrito não é muito útil se não soubermos quantos '
        'pessoas na casa existem. O que você realmente quer é o número de aposentos por família. Da '
        'mesma forma, o número total de quartos por si só não é muito útil: você provavelmente desejará '
        'compará-lo com o número de aposentos. E a população pela quantidade de casas também parece ser uma '
        'combinação interessante de atributos a considerar. Vamos criar esses novos atributos:</p>')
st.code("""housing['aposentos_por_pessoa'] = housing['total_rooms'] / housing['households']
housing['quartos_por_aposento'] = housing['total_bedrooms'] / housing['total_rooms']
housing['pessoas_por_casa'] = housing['population'] / housing['households']""", line_numbers=True)
st.html('<p class="fonte_texto">E agora vamos dar uma olhada na matriz de correlação novamente:</p>')
tabela_2_8 = pd.read_csv('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_02/tabela_2_8.csv')
st.dataframe(tabela_2_8, hide_index=True)
st.html('<p class="fonte_texto">Ei, nada mal! O novo atributo <b>quartos_por_aposento</b> está muito mais '
        'correlacionado com o valor médio da casa do que com o número total de quartos ou aposentos. '
        'Aparentemente, casas com menor proporção quarto/aposento tendem a ser mais caras. O número de '
        'aposentos por casa também é mais informativo do que o número total de divisões num '
        'distrito – obviamente quanto maiores as casas, mais caras são.</p>')
st.html('<p class="fonte_texto">Esta rodada de exploração não precisa ser absolutamente completa; o '
        'objetivo é começar com o pé direito e obter rapidamente insights que o ajudarão a obter um '
        'primeiro protótipo razoavelmente bom. Mas este é um processo iterativo: depois de colocar um '
        'protótipo em funcionamento, você pode analisar seu resultado para obter mais insights e voltar a '
        'esta etapa de exploração. Não se esqueça de utilizar a função <b>drop()</b> nessas colunas '
        'criadas para evitar erros. Vamos criá-las de outra forma.</p>')

# --- Prepare os dados para algoritmos de aprendizado de máquina --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Prepare os dados para algoritmos de aprendizado de máquina</h1>')
st.html('<p class="fonte_texto">É hora de preparar os dados para seus algoritmos de Aprendizado de Máquina. '
        'Em vez de fazer isso manualmente, você deve escrever funções para essa finalidade, por vários bons '
        'motivos:</p>')
st.html('<ul class="fonte_texto">'
            '<li>Isso permitirá que você reproduza essas transformações facilmente em qualquer conjunto de '
            'dados (por exemplo, na próxima vez que você obtiver um novo conjunto de dados).</li>'
            '<li>Você construirá gradualmente uma biblioteca de funções de transformação que poderá '
            'reutilizar em projetos futuros.</li>'
            '<li>Você pode usar essas funções em seu sistema ativo para transformar os novos dados antes de '
            'alimentá-los em seus algoritmos.</li>'
            '<li>Isso permitirá que você experimente facilmente várias transformações e veja qual '
            'combinação de transformações funciona melhor.</li>'
        '</ul>')
st.html('<p class="fonte_texto">Mas primeiro vamos voltar para um conjunto de treinamento limpo (copiando '
        '<b>conjunto_treino_estratificado</b> mais uma vez). Vamos também separar os preditores e os '
        'rótulos, já que não queremos necessariamente aplicar as mesmas transformações aos preditores e '
        'aos valores alvo (observe que >b>drop()</b> cria uma cópia dos dados e não afeta o '
        '<b>conjunto_treino_estratificado</b>):</p>')
st.code("""housing = conjunto_treino_estratificado.drop('median_house_value', axis=1)
housing_rotulos = conjunto_treino_estratificado['median_house_value'].copy()""", line_numbers=True)
st.html('<h2 class="fonte_subtitulo_aula">Limpeza de dados</h2>')
st.html('<p class="fonte_texto">A maioria dos algoritmos de Aprendizado de Máquina não funcionam com '
        'recursos ausentes, então vamos criar algumas funções para cuidar deles. Vimos anteriormente que o '
        'atributo <b>total_bedrooms</b> possui alguns valores ausentes, então vamos corrigir isso. Você '
        'tem três opções:</p>')
st.html('<ol type="1" class="fonte_texto">'
            '<li>Livre-se dos distritos correspondentes.</li>'
            '<li>Livre-se de todo o atributo.</li>'
            '<li>Defina os valores para algum valor (zero, média, mediana, etc.).</li>'
        '</ol>')
st.html('<p class="fonte_texto">Você pode fazer isso facilmente usando os métodos <b>dropna()</b>, '
        '<b>drop()</b> e <b>fillna()</b> do DataFrame:</p>')
st.code("""housing.dropna(subset=['total_bedrooms'])  # opção 1
housing.drop('total_bedrooms', axis=1)  # opção 2
mediana = housing['total_bedrooms'].median()  # opção 3
housing['total_bedrooms'].fillna(mediana, inplace=True)""", line_numbers=True)
st.html('<p class="fonte_texto">Se você escolher a opção 3, deverá calcular o valor mediano no conjunto de '
        'treinamento e usá-lo para preencher os valores ausentes no conjunto de treinamento. Não se '
        'esqueça de salvar o valor mediano que você calculou. Você precisará dele mais tarde para '
        'substituir valores ausentes no conjunto de testes quando quiser avaliar seu sistema e também '
        'quando o sistema entrar em operação para substituir valores ausentes em novos dados.</p>')
st.html('<p class="fonte_texto">Scikit-Learn fornece uma classe útil para cuidar de valores ausentes: '
        '<b>SimpleImputer</b>. Aqui está como usá-lo. Primeiro, você precisa criar uma instância de '
        '<b>SimpleImputer</b>, especificando que deseja substituir os valores ausentes de cada atributo '
        'pela mediana desse atributo:</p>')
st.code("""from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy='median')""", line_numbers=True)
st.html('<p class="fonte_texto">Como a mediana só pode ser calculada em atributos numéricos, você precisa '
        'criar uma cópia dos dados sem o atributo de texto <b>ocean_proximity</b>:</p>')
st.code("housing_num = housing.drop('ocean_proximity', axis=1)", line_numbers=True)
st.html('<p class="fonte_texto">Agora você pode chamar a instância <b>imputer</b> aos dados de treinamento '
        'usando o método <b>fit()</b>:</p>')
st.code('imputer.fit(housing_num)', line_numbers=True)
st.html('<p class="fonte_texto">O <b>imputer</b> simplesmente calculou a mediana de cada atributo e '
        'armazenou o resultado em sua variável de instância <b>statistics_</b>. Apenas o atributo '
        '<b>total_bedrooms</b> tinha valores faltantes, mas não podemos ter certeza de que não haverá '
        'valores faltantes em novos dados após o sistema entrar em operação, por isso é mais seguro '
        'aplicar o <b>imputer</b> a todos os atributos numéricos:</p>')
st.code('''print(imputer.statistics_)
print(housing_num.median().values)''', line_numbers=True)
st.html('<p class="fonte_texto">Agora você pode usar este <b>imputer</b> “treinado” para transformar o '
        'conjunto de treinamento substituindo os valores ausentes pelas medianas aprendidas:</p>')
st.code('X = imputer.transform(housing_num)', line_numbers=True)
st.html('<p class="fonte_texto">O resultado é um array NumPy simples contendo os recursos transformados. '
        'Se você quiser colocá-lo de volta em um DataFrame do pandas, é simples:</p>')
st.code("""housing_tr = pd.DataFrame(
    X,
    columns=housing_num.columns,
    index=housing_num.index
)""", line_numbers=True)
with st.expander('Desing do Scikit-Learn'):
    st.html('<p class="fonte_texto">A API do Scikit-Learn é extremamente bem projetada. Estes são os '
            '<a href="https://arxiv.org/abs/1309.0238">principais princípios de design</a>:</p>')
    st.html('<p class="fonte_texto"><i>Consistência</i>: Todos os objetos compartilham uma interface simples e '
            'consistente.</p>')
    st.html('<p class="fonte_texto"><i>Estimadores</i>: qualquer objeto que possa estimar alguns parâmetros '
            'com base em um conjunto de dados é chamado de <i>estimador</i> (por exemplo, um '
            '<b>imputer</b> é um estimador). A estimativa em si é realizada pelo método <b>fit()</b> e leva '
            'apenas um conjunto de dados como parâmetro (ou dois para algoritmos de aprendizagem '
            'supervisionada; o segundo conjunto de dados contém os rótulos). Qualquer outro parâmetro '
            'necessário para orientar o processo de estimativa é considerado um hiperparâmetro (como uma '
            '<b>estratégia do imputer</b>) e deve ser definido como uma variável de instância (geralmente '
            'por meio de um parâmetro construtor).</p>')
    st.html('<p class="fonte_texto"><i>Transformadores</i>: Alguns estimadores (como um <b>imputer</b>) também '
            'podem transformar um conjunto de dados; estes são chamados de <i>transformadores</i>. Mais uma '
            'vez, a API é simples: a transformação é realizada pelo método <b>transform()</b> com o '
            'conjunto de dados a ser transformado como parâmetro. Ele retorna o conjunto de dados '
            'transformado. Esta transformação geralmente depende dos parâmetros aprendidos, como é o caso '
            'de um <b>imputer</b>. Todos os transformadores também possuem um método de conveniência chamado '
            '<b>fit_transform()</b> que é equivalente a chamar <b>fit()</b> e depois <b>transform()</b> '
            '(mas às vezes <b>fit_transform()</b> é otimizado e roda muito mais rápido).</p>')
    st.html('<p class="fonte_texto"><i>Preditores</i>: Finalmente, alguns estimadores, dado um conjunto de '
            'dados, são capazes de fazer previsões; eles são chamados de <i>preditores</i>. Por exemplo, o '
            'modelo <b>LinearRegression</b> do <a href="https://mundopython.streamlit.app/aula_01_ia_scikit_learn_keras_tensorflow">capítulo anterior</a> era um preditor: dado o PIB per capita de '
            'um país, previa a satisfação com a vida. Um preditor possui um método <b>predict()</b> que '
            'pega um conjunto de dados de novas instâncias e retorna um conjunto de dados de previsões '
            'correspondentes. Também possui um método <b>score()</b> que mede a qualidade das previsões, '
            'dado um conjunto de testes (e os rótulos correspondentes, no caso de algoritmos de '
            'aprendizagem supervisionada).</p>')
    st.html('<p class="fonte_texto"><i>Inspeção</i>: todos os hiperparâmetros do estimador são acessíveis '
            'diretamente por meio de variáveis de instância públicas (por exemplo, <b>imputer.strategy</b>) '
            'e todos os parâmetros aprendidos pelo estimador são acessíveis por meio de variáveis de '
            'instância públicas com um sufixo de sublinhado (por exemplo, <b>imputer.statistics_</b>).</p>')
    st.html('<p class="fonte_texto"><i>Não proliferação de classes</i>: os conjuntos de dados são '
            'representados como matrizes NumPy ou matrizes esparsas SciPy, em vez de classes Python. '
            'Hiperparâmetros são apenas strings ou números regulares do Python.</p>')
    st.html('<p class="fonte_texto"><i>Composição</i>: os blocos de construção existentes são reutilizados '
            'tanto quanto possível. Por exemplo, é fácil criar um estimador <b>Pipeline</b> a partir de '
            'uma sequência arbitrária de transformadores seguida por um estimador final, como veremos.</p>')
    st.html('<p class="fonte_texto"><i>Padrões sensatos</i>: o Scikit-Learn fornece valores padrão razoáveis '
            'para a maioria dos parâmetros, facilitando a criação rápida de um sistema funcional de linha '
            'de base.</p>')
st.html('<h2 class="fonte_subtitulo_aula">Tratamento de texto e atributos categóricos</h2>')
st.html('<p class="fonte_texto">Até agora lidamos apenas com atributos numéricos, mas agora vamos dar uma '
        'olhada nos atributos de texto. Neste conjunto de dados, existe apenas um: o atributo '
        '<b>ocean_proximity</b>. Vejamos seu valor para as primeiras 10 instâncias:</p>')
st.code("""housing_cat = housing[['ocean_proximity']]
housing_cat.head(10)""", line_numbers=True)
tabela_2_9 = pd.read_csv('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_02/tabela_2_9.csv')
st.dataframe(tabela_2_9, hide_index=True)
st.html('<p class="fonte_texto">Não é um texto arbitrário: há um número limitado de valores possíveis, '
        'cada um dos quais representa uma categoria. Portanto, este atributo é um atributo categórico. A '
        'maioria dos algoritmos de aprendizado de máquina prefere trabalhar com números, então vamos '
        'converter essas categorias de texto em números. Para isso, podemos usar a classe '
        '<b>OrdinalEncoder</b> do Scikit-Learn:</p>')
st.code('''from sklearn.preprocessing import OrdinalEncoder

codificador = OrdinalEncoder()
housing_cat_codificado = codificador.fit_transform(housing_cat)
housing_cat_codificado[:10]''', line_numbers=True)
st.html('<p class="fonte_texto">Você pode obter a lista de categorias usando a variável de instância '
        '<b>categories_</b>. É uma lista contendo um array 1D de categorias para cada atributo categórico '
        '(neste caso, uma lista contendo um único array, pois existe apenas um atributo categórico):</p>')
st.code('codificador.categories_', line_numbers=True)
st.html('<p class="fonte_texto">Um problema com esta representação é que os algoritmos de AM assumirão que '
        'dois valores próximos são mais semelhantes do que dois valores distantes. Isso pode ser bom em '
        'alguns casos (por exemplo, para categorias ordenadas como “ruim”, “médio”, “bom” e “excelente”), '
        'mas obviamente não é o caso da coluna <b>ocean_proximity</b> (por exemplo, as categorias 0 e 4 são '
        'claramente mais semelhantes que as categorias 0 e 1). Para corrigir esse problema, uma solução '
        'comum é criar um atributo binário por categoria: um atributo igual a 1 quando a categoria for '
        '“<1H OCEAN” (e 0 caso contrário), outro atributo igual a 1 quando a categoria for “INLAND” (e '
        '0 caso contrário), e assim por diante. Isso é chamado de <i>codificação one-hot</i>, porque '
        'apenas um atributo será igual a 1 (quente), enquanto os outros serão 0 (frio). Os novos atributos '
        'às vezes são chamados de atributos <i>fictícios</i>. Scikit-Learn fornece uma classe '
        '<b>OneHotEncoder</b> para converter valores categóricos em vetores one-hot:</p>')
st.code('''from sklearn.preprocessing import OneHotEncoder

codificador = OneHotEncoder()
housing_cat_1_hot = codificador.fit_transform(housing_cat)
housing_cat_1_hot''', line_numbers=True)
st.html('<p class="fonte_texto">Observe que a saída é uma <i>matriz esparsa</i> do SciPy, em vez de um '
        'array NumPy. Isto é muito útil quando você possui atributos categóricos com milhares de '
        'categorias. Após a codificação onehot, obtemos uma matriz com milhares de colunas, e a matriz '
        'está cheia de 0s, exceto um único 1 por linha. Usar toneladas de memória principalmente para '
        'armazenar zeros seria um grande desperdício; portanto, uma matriz esparsa armazena apenas a '
        'localização dos elementos diferentes de zero. Você pode usá-lo principalmente como um array 2D '
        'normal, mas se você realmente quiser convertê-lo em um array NumPy (denso), basta chamar o '
        'método <b>toarray()</b>:</p>')
st.code('housing_cat_1_hot.toarray()', line_numbers=True)
st.html('<p class="fonte_texto">Mais uma vez, você pode obter a lista de categorias usando a variável de '
        'instância <b>categories_<b/> do codificador:</p>')
st.code('codificador.categories_', line_numbers=True)
with st.expander('Dica 3', icon='💡'):
    st.html('<p class="fonte_texto">Se um atributo categórico tiver um grande número de categorias possíveis '
            '(por exemplo, código do país, profissão, espécie), então a codificação one-hot resultará em um '
            'grande número de recursos de entrada. Isso pode retardar o treinamento e degradar o desempenho. '
            'Se isso acontecer, você pode querer substituir a entrada categórica por recursos numéricos '
            'úteis relacionados às categorias: por exemplo, você pode substituir o recurso '
            '<b>ocean_proximity</b> pela distância até o oceano (da mesma forma, um código de país pode ser '
            'substituído pela população do país e pelo PIB per capita). Alternativamente, você pode '
            'substituir cada categoria por um vetor de baixa dimensão que pode ser aprendido chamado '
            '<i>incorporação</i>. A representação de cada categoria seria aprendida durante o treinamento. '
            'Este é um exemplo de aprendizagem de <i>representação</i> (veja os Capítulos 13 e 17 para mais '
            'detalhes).</p>')
st.html('<h2 class="fonte_subtitulo_aula">Transformadores personalizados</h2>')
st.html('<p class="fonte_texto">Embora o Scikit-Learn forneça muitos transformadores úteis, você precisará '
        'escrever os seus próprios para tarefas como operações de limpeza personalizadas ou combinação de '
        'atributos específicos. Você desejará que seu transformador funcione perfeitamente com as '
        'funcionalidades do Scikit-Learn (como pipelines) e, como o Scikit-Learn depende da digitação duck '
        '(não da herança), tudo o que você precisa fazer é criar uma classe e implementar três métodos: '
        '<b>fit()</b> (retornando <b>self</b>), <b>transform()</b> e <b>fit_transform()</b>.</p>')
st.html('<p class="fonte_texto">Você pode obter o último simplesmente adicionando '
        '<b>TransformerMixin</b> como classe base. Se você adicionar <b>BaseEstimator</b> como uma classe '
        'base (e evitar <b>*args</b> e <b>**kwargs</b> em seu construtor), você também obterá dois métodos '
        'extras (<b>get_params()</b> e <b>set_params()</b>) que serão úteis para ajuste automático de '
        'hiperparâmetros. Por exemplo, aqui está uma pequena classe de transformador que adiciona os '
        'atributos combinados que discutimos anteriormente:</p>')
st.code('''
from sklearn.base import BaseEstimator, TransformerMixin

aposentos_ix, quartos_ix, populacao_ix, casas_ix = 3, 4, 5, 6

class AdicionadorAtributosCombinados(BaseEstimator, TransformerMixin):
  def __init__(self, add_quartos_por_aposento=True):
    self.add_quartos_por_aposento = add_quartos_por_aposento
  
  def fit(self, X, y=None):
    return self

  def transform(self, X):
    aposentos_por_casa = X[:, aposentos_ix] / X[:, casas_ix]
    populacao_por_casa = X[:, populacao_ix] / X[:, casas_ix]
    if self.add_quartos_por_aposento:
      quartos_por_aposento = X[:, quartos_ix] / X[:, aposentos_ix]
      return np.c_[X, aposentos_por_casa, populacao_por_casa, quartos_por_aposento]
    else:
      return np.c_[X, aposentos_por_casa, populacao_por_casa]

adicionador_atributo = AdicionadorAtributosCombinados(add_quartos_por_aposento=False)
housing_atributos_extra = adicionador_atributo.transform(housing.values)''', line_numbers=True)
st.html('<p class="fonte_texto">Neste exemplo, o transformador tem um hiperparâmetro, '
        '<b>add_quartos_por_aposento</b>, definido como <b>True</b> por padrão (muitas vezes é útil '
        'fornecer padrões sensatos). Este hiperparâmetro permitirá que você descubra facilmente se '
        'adicionar este atributo ajuda os algoritmos de aprendizado de máquina ou não. De maneira mais '
        'geral, você pode adicionar um hiperparâmetro para controlar qualquer etapa de preparação de dados '
        'sobre a qual não tenha 100% de certeza. Quanto mais você automatizar essas etapas de preparação '
        'de dados, mais combinações poderá experimentar automaticamente, aumentando a probabilidade de '
        'encontrar uma ótima combinação (e economizando muito tempo).</p>')
st.html('<h2 class="fonte_subtitulo_aula">Dimensionamento de recursos</h2>')
st.html('<p class="fonte_texto">Uma das transformações mais importantes que você precisa aplicar aos seus '
        'dados é o <b>escalonamento de recursos</b>. Com poucas exceções, os algoritmos de Aprendizado '
        'de Máquina não funcionam bem quando os atributos numéricos de entrada têm escalas muito '
        'diferentes. Este é o caso dos dados de habitação: o número total de quartos varia entre cerca de '
        '6 e 39.320, enquanto os rendimentos medianos variam apenas entre 0 e 15. Note-se que geralmente '
        'não é necessário dimensionar os valores-alvo.</p>')
st.html('<p class="fonte_texto">Existem duas maneiras comuns de fazer com que todos os atributos tenham a '
        'mesma escala: <i>escala min-max</i> e <i>padronização</i>.</p>')
st.html('<p class="fonte_texto">A escala mínimo-máximo (muitas pessoas chamam isso de <i>normalização</i>) '
        'é a mais simples: os valores são deslocados e redimensionados para que acabem variando de 0 a 1. '
        'Fazemos isso subtraindo o valor mínimo e dividindo pelo máximo menos o mínimo. Scikit-Learn '
        'fornece um transformador chamado <b>MinMaxScaler</b> para isso. Ele possui um hiperparâmetro '
        '<b>feature_range</b> que permite alterar o intervalo se, por algum motivo, você não quiser '
        '0–1.</p>')
st.html('<p class="fonte_texto">A padronização é diferente: primeiro ela subtrai o valor médio (para que '
        'os valores padronizados sempre tenham média zero) e depois divide pelo desvio padrão para que a '
        'distribuição resultante tenha variância unitária. Ao contrário da escala min-max, a padronização '
        'não vincula os valores a um intervalo específico, o que pode ser um problema para alguns '
        'algoritmos (por exemplo, redes neurais geralmente esperam um valor de entrada variando de 0 a '
        '1). No entanto, a padronização é muito menos afetada por valores discrepantes. Por exemplo, '
        'suponhamos que um distrito tivesse um rendimento médio igual a 100 (por engano). A escala '
        'mínimo-máximo esmagaria todos os outros valores de 0–15 até 0–0.15, enquanto a padronização não '
        'seria muito afetada. Scikit-Learn fornece um transformador chamado <b>StandardScaler</b> para '
        'padronização.</p>')
with st.expander('Alerta 3', icon='⚡'):
    st.html('<p class="fonte_texto">Tal como acontece com todas as transformações, é importante ajustar os '
            'escalonadores apenas aos dados de treinamento, não ao conjunto de dados completo (incluindo o '
            'conjunto de teste). Só então você poderá usá-los para transformar o conjunto de treinamento e '
            'o conjunto de testes (e novos dados).</p>')
st.html('<h2 class="fonte_subtitulo_aula">Pipelines de transformação</h2>')
st.html('<p class="fonte_texto">Como você pode ver, há muitas etapas de transformação de dados que '
        'precisam ser executadas na ordem correta. Felizmente, o Scikit-Learn fornece a classe '
        '<b>Pipeline</b> para ajudar com essas sequências de transformações. Aqui está um pequeno pipeline '
        'para os atributos numéricos:</p>')
st.code("""
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('adicionador_atributos', AdicionadorAtributosCombinados()),
    ('padronizacao', StandardScaler())
])

housing_num_tr = num_pipeline.fit_transform(housing_num)""", line_numbers=True)
st.html('<p class="fonte_texto">O construtor <b>Pipeline</b> pega uma lista de pares nome/estimador que '
        'definem uma sequência de etapas. Todos, exceto o último estimador, devem ser transformadores (ou '
        'seja, eles devem ter um método <b>fit_transform()</b>). Os nomes podem ser qualquer coisa que '
        'você quiser (desde que sejam únicos e não contenham sublinhados duplos, <b>__</b>); eles serão '
        'úteis posteriormente para ajuste de hiperparâmetros.</p>')
st.html('<p class="fonte_texto">Quando você chama o método <b>fit()</b> do pipeline, ele chama '
        '<b>fit_transform()</b> sequencialmente em todos os transformadores, passando a saída de cada '
        'chamada como parâmetro para a próxima chamada até atingir o estimador final, para o qual chama o '
        'método <b>fit()</b>.</p>')
st.html('<p class="fonte_texto">O pipeline expõe os mesmos métodos do estimador final. Neste exemplo, o '
        'último estimador é um <b>StandardScaler</b>, que é um transformador, então o pipeline tem um '
        'método <b>transform()</b> que aplica todas as transformações aos dados em sequência (e, claro, '
        'também um método <b>fit_transform()</b>, que é o que usamos).</p>')
st.html('<p class="fonte_texto">Até agora, tratamos as colunas categóricas e as colunas numéricas '
        'separadamente. Seria mais conveniente ter um único transformador capaz de lidar com todas as '
        'colunas, aplicando as transformações apropriadas a cada coluna. Na versão 0.20, o Scikit-Learn '
        'introduziu o <b>ColumnTransformer</b> para esse propósito, e a boa notícia é que ele funciona '
        'muito bem com DataFrames do pandas. Vamos usá-lo para aplicar todas as transformações aos dados '
        'habitacionais:</p>')
st.code("""from sklearn.compose import ColumnTransformer

num_atributos = list(housing_num)
cat_atributos = ['ocean_proximity']

pipeline_completo = ColumnTransformer([
    ('num', num_pipeline, num_atributos),
    ('cat', OneHotEncoder(), cat_atributos)
])

housing_preparado = pipeline_completo.fit_transform(housing)""", line_numbers=True)
st.html('<p class="fonte_texto">Primeiro importamos a classe <b>ColumnTransformer</b>, em seguida obtemos '
        'a lista de nomes de colunas numéricas e a lista de nomes de colunas categóricas, e então '
        'construímos um <b>ColumnTransformer</b>. O construtor requer uma lista de tuplas, onde cada tupla '
        'contém um nome, um transformador e uma lista de nomes (ou índices) de colunas às quais o '
        'transformador deve ser aplicado. Neste exemplo, especificamos que as colunas numéricas devem ser '
        'transformadas usando o <b>num_pipeline</b> que definimos anteriormente, e as colunas categóricas '
        'devem ser transformadas usando um <b>OneHotEncoder</b>. Finalmente, aplicamos este '
        '<b>ColumnTransformer</b> aos dados: ele aplica cada transformador às colunas '
        'apropriadas e concatena as saídas ao longo do segundo eixo (os transformadores devem retornar o '
        'mesmo número de linhas).</p>')
st.html('<p class="fonte_texto">Observe que o <b>OneHotEncoder</b> retorna uma matriz esparsa, enquanto '
        'o <b>num_pipeline</b> retorna uma matriz densa. Quando existe uma mistura de matrizes esparsas e '
        'densas, o <b>ColumnTransformer</b> estima a densidade da matriz final (ou seja, a proporção de '
        'células diferentes de zero) e retorna uma matriz esparsa se a densidade for inferior a um '
        'determinado limite (por padrão, <b>sparse_threshold=0.3</b>). Neste exemplo, ele retorna uma '
        'matriz densa. E é isso! Temos um pipeline de pré-processamento que pega todos os dados da '
        'habitação e aplica as transformações apropriadas a cada coluna.</p>')
with st.expander('Dica 4', icon='💡'):
    st.html('<p class="fonte_texto">Em vez de usar um transformador, você pode especificar a string '
            '"<b>drop</b>" se quiser que as colunas sejam descartadas ou pode especificar '
            '"<b>passthrough</b>" se quiser que as colunas permaneçam intactas. Por padrão, as colunas '
            'restantes (ou seja, aquelas que não foram listadas) serão eliminadas, mas você pode definir o '
            'hiperparâmetro restante para qualquer transformador (ou para "<b>passthrough</b>") se desejar '
            'que essas colunas sejam tratadas de maneira diferente.</p>')
st.html('<p class="fonte_texto">Se você estiver usando o Scikit-Learn 0.19 ou anterior, poderá usar uma '
        'biblioteca de terceiros, como <b>sklearn-pandas</b>, ou poderá implementar seu próprio '
        'transformador personalizado para obter a mesma funcionalidade do <b>ColumnTransformer</b>. '
        'Alternativamente, você pode usar a classe <b>FeatureUnion</b>, que pode aplicar diferentes '
        'transformadores e concatenar suas saídas. Mas não é possível especificar colunas diferentes para '
        'cada transformador; todos eles se aplicam a todos os dados. É possível contornar esta limitação '
        'usando um transformador personalizado para seleção de coluna.</p>')

# --- Selecione e treine um modelo --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Selecione e treine um modelo</h1>')
st.html('<p class="fonte_texto">Estamos quase no final! Você estruturou o problema, obteve os dados e os '
        'explorou, '
        'amostrou um conjunto de treinamento e um conjunto de testes e escreveu pipelines de transformação '
        'para limpar e preparar seus dados para algoritmos de aprendizado de máquina automaticamente. '
        'Agora você está pronto para selecionar e treinar um modelo de Aprendizado de Máquina.</p>')
st.html('<h2 class="fonte_subtitulo_aula">Treinamento e avaliação no conjunto de treinamento</h2>')
st.html('<p class="fonte_texto">A boa notícia é que graças a todas essas etapas anteriores, as coisas '
        'agora serão muito mais simples do que você imagina. Vamos primeiro treinar um modelo de '
        'Regressão Linear, como fizemos no <a href="https://mundopython.streamlit.app/aula_01_ia_scikit_learn_keras_tensorflow">capítulo anterior</a>:</p>')
st.code('''from sklearn.linear_model import LinearRegression

reg_lin = LinearRegression()
reg_lin.fit(housing_preparado, housing_rotulos)''', line_numbers=True)
st.html('<p class="fonte_texto">Feito! Agora você tem um modelo de regressão linear funcional. Vamos '
        'experimentar algumas instâncias do conjunto de treinamento:</p>')
st.code('''
alguns_dados = housing.iloc[:5]
alguns_rotulos = housing_rotulos.iloc[:5]
alguns_dados_preparados = pipeline_completo.transform(alguns_dados)
print(f'Predições: {reg_lin.predict(alguns_dados_preparados)}')
print(f'Rótulos: {list(alguns_rotulos)}')''', line_numbers=True)
st.html('<p class="fonte_texto">Funciona, embora as previsões não sejam exatamente precisas. Vamos medir '
        'o REQM deste modelo de regressão em todo o conjunto de treinamento usando a função '
        '<b>mean_squared_error()</b> do Scikit-Learn:</p>')
st.code('''from sklearn.metrics import mean_squared_error

housing_predicoes = reg_lin.predict(housing_preparado)
reg_eqm = mean_squared_error(housing_rotulos, housing_predicoes)
reg_reqm = np.sqrt(reg_eqm)
print(reg_reqm)''', line_numbers=True)
st.html('<p class="fonte_texto">Isto é melhor do que nada, mas claramente não é uma grande pontuação: os '
        '<b>median_housing_values</b> da maioria dos distritos variam entre US$ 120.000 e US$ '
        '265.000, portanto, um erro de previsão típico de US$ 68.627 não é muito satisfatório (para você '
        'pode dar um valor próximo). Este é um exemplo de modelo que não se adapta aos dados de '
        'treinamento. Quando isso acontece, pode significar que os recursos não fornecem informações '
        'suficientes para fazer boas previsões ou que o modelo não é poderoso o suficiente. Como vimos '
        'no <a href="https://mundopython.streamlit.app/aula_01_ia_scikit_learn_keras_tensorflow">capítulo '
        'anterior</a>, as principais formas de corrigir o underfitting são '
        'selecionar um modelo '
        'mais poderoso, alimentar o algoritmo de treinamento com melhores recursos ou reduzir as '
        'restrições do modelo. Este modelo não está regularizado, o que exclui a última opção. Você '
        'poderia tentar adicionar mais recursos (por exemplo, o logaritmo da população), mas primeiro '
        'vamos tentar um modelo mais complexo para ver como funciona.</p>')
st.html('<p class="fonte_texto">Vamos treinar um <b>DecisionTreeRegressor</b>. Este é um modelo poderoso, '
        'capaz de encontrar relações não lineares complexas nos dados (Árvores de Decisão são apresentadas '
        'com mais detalhes no Capítulo 6). O código já deve parecer familiar:</p>')
st.code('''from sklearn.tree import DecisionTreeRegressor

arv_dec = DecisionTreeRegressor()
arv_dec.fit(housing_preparado, housing_rotulos)''', line_numbers=True)
st.html('<p class="fonte_texto">Agora que o modelo está treinado, vamos avaliá-lo no conjunto de '
        'treinamento:</p>')
st.code('''housing_predicoes = arv_dec.predict(housing_preparado)
arv_dec_eqm = mean_squared_error(housing_rotulos, housing_predicoes)
arv_dec_reqm = np.sqrt(arv_dec_eqm)
print(arv_dec_reqm)''', line_numbers=True)
st.html('<p class="fonte_texto">Espere, o que!? Nenhum erro? Este modelo poderia realmente ser '
        'absolutamente perfeito? É claro que é muito mais provável que o modelo tenha superajustado os '
        'dados. Como você pode ter certeza? Como vimos anteriormente, você não quer mexer no conjunto de '
        'teste até estar pronto para lançar um modelo no qual tenha confiança, então você precisa usar '
        'parte do conjunto de treinamento para treinamento e parte dele para validação do modelo.</p>')
st.html('<h2 class="fonte_subtitulo_aula">Melhor avaliação usando validação cruzada</h2>')
st.html('<p class="fonte_texto">Uma maneira de avaliar o modelo de árvore de decisão seria usar a função '
        '<b>train_test_split()</b> para dividir o conjunto de treinamento em um conjunto de treinamento '
        'menor e um conjunto de validação, depois treinar seus modelos em relação ao conjunto de '
        'treinamento menor e avaliá-los em relação ao conjunto de validação. Dá um pouco de trabalho, mas '
        'nada muito difícil, e funcionaria bastante bem.</p>')
st.html('<p class="fonte_texto">Uma ótima alternativa é usar o recurso <i>K-fold cross-validation</i> do '
        'Scikit-Learn. O código a seguir divide aleatoriamente o conjunto de treinamento em 10 '
        'subconjuntos distintos chamados <i>folds</i> (dobras), depois treina e avalia o modelo de árvore de '
        'decisão 10 vezes, escolhendo uma dobra diferente para avaliação a cada vez e treinando nas '
        'outras 9 dobras. O resultado é uma matriz contendo as 10 pontuações da avaliação:</p>')
st.code("""from sklearn.model_selection import cross_val_score

pontuacoes = cross_val_score(
    arv_dec,
    housing_preparado,
    housing_rotulos,
    scoring='neg_mean_squared_error',
    cv=10
)
pontuacoes_arv_dec_reqm = np.sqrt(-pontuacoes)""", line_numbers=True)
with st.expander('Alerta 4', icon='⚡'):
    st.html('<p class="fonte_texto">Os recursos de validação cruzada do Scikit-Learn esperam uma função de '
            'utilidade (quanto maior, melhor) em vez de uma função de custo (quanto menor, melhor), '
            'portanto, a função de pontuação é na verdade o oposto do EQM (ou seja, um valor negativo), e '
            'é por isso que o código anterior calcula <b>-pontuacoes</b> antes de calcular a raiz '
            'quadrada.</p>')
st.html('<p class="fonte_texto">Vejamos os resultados:</p>')
st.code("""def mostrar_pontuacoes(pontuacoes):
  print(f'''Pontuações: {pontuacoes}
Média: {pontuacoes.mean()}
Desvion padrão: {pontuacoes.std()}''')

mostrar_pontuacoes(pontuacoes_arv_dec_reqm)""", line_numbers=True)
st.html('<p class="fonte_texto">Agora a Árvore de Decisão não parece tão boa quanto antes. Na verdade, '
        'parece ter um desempenho pior do que o modelo de regressão linear! Observe que a validação '
        'cruzada permite obter não apenas uma estimativa do desempenho do seu modelo, mas também uma '
        'medida de quão precisa é essa estimativa (ou seja, seu desvio padrão). A Árvore de Decisão tem '
        'uma pontuação de aproximadamente 71.469, geralmente ±2.141. Você não teria essas informações se '
        'usasse apenas um conjunto de validação. Mas a validação cruzada tem o custo de treinar o modelo '
        'várias vezes, por isso nem sempre é possível.</p>')
st.html('<p class="fonte_texto">Vamos calcular as mesmas pontuações para o modelo de regressão linear, só '
        'para ter certeza:</p>')
st.code("""pontuacoes_reg_lin = cross_val_score(
    reg_lin,
    housing_preparado,
    housing_rotulos,
    scoring='neg_mean_squared_error',
    cv=10
)
pontuacoes_reg_lin_reqm = np.sqrt(-pontuacoes_reg_lin)
mostrar_pontuacoes(pontuacoes_reg_lin_reqm)""", line_numbers=True)
st.html('<p class="fonte_texto">É isso mesmo: o modelo de Árvore de Decisão está tão superajustado que '
        'tem um desempenho pior do que o modelo de Regressão Linear.</p>')
st.html('<p class="fonte_texto">Vamos tentar um último modelo agora: o <b>RandomForestRegressor</b>. Como '
        'veremos no Capítulo 7, as Florestas Aleatórias funcionam treinando muitas Árvores de Decisão em '
        'subconjuntos aleatórios de recursos e, em seguida, calculando a média de suas previsões. '
        'Construir um modelo sobre muitos outros modelos é chamado de <i>Ensemble Learning</i> e '
        'geralmente é uma ótima maneira de levar os algoritmos de AM ainda mais longe:</p>')
st.code("""from sklearn.ensemble import RandomForestRegressor

flo_ale = RandomForestRegressor()
flo_ale.fit(housing_preparado, housing_rotulos)
flo_ale_eqm = mean_squared_error(housing_rotulos, housing_predicoes)
flo_ale_reqm = np.sqrt(flo_ale_eqm)
print(flo_ale_reqm)

pontuacoes_flo_ale = cross_val_score(
    flo_ale,
    housing_preparado,
    housing_rotulos,
    scoring='neg_mean_squared_error',
    cv=10
)
pontuacoes_flo_ale_reqm = np.sqrt(-pontuacoes_flo_ale)
mostrar_pontuacoes(pontuacoes_flo_ale_reqm)""", line_numbers=True)
st.html('<p class="fonte_texto">Uau, isso é muito melhor: as Florestas Aleatórias parecem muito '
        'promissoras. No entanto, observe que a pontuação no conjunto de treinamento ainda é muito menor '
        'do que nos conjuntos de validação, o que significa que o modelo ainda está superajustando o '
        'conjunto de treinamento. As soluções possíveis para o overfitting são simplificar o modelo, '
        'restringi-lo (ou seja, regularizá-lo) ou obter muito mais dados de treinamento. Antes de '
        'mergulhar mais fundo nas Florestas Aleatórias, no entanto, você deve experimentar muitos outros '
        'modelos de diversas categorias de algoritmos de Aprendizado de Máquina (por exemplo, várias '
        'Máquinas de Vetores de Suporte com kernels diferentes e possivelmente uma rede neural), sem '
        'gastar muito tempo ajustando os hiperparâmetros. O objetivo é selecionar alguns (dois a cinco) '
        'modelos promissores.</p>')
with st.expander('Dica 5', icon='💡'):
    st.html('<p class="fonte_texto">Você deve salvar todos os modelos que experimentar para poder voltar '
            'facilmente a qualquer modelo que desejar. Certifique-se de salvar os hiperparâmetros e os '
            'parâmetros treinados, bem como as pontuações de validação cruzada e talvez também as previsões '
            'reais. Isso permitirá que você compare facilmente as pontuações entre os tipos de modelo e '
            'compare os tipos de erros que eles cometem. Você pode salvar facilmente modelos Scikit-Learn '
            'usando o módulo <b>pickle</b> do Python ou usando a biblioteca <b>joblib</b>, que é mais '
            'eficiente na serialização de grandes arrays NumPy (você pode instalar esta biblioteca '
            'usando pip):</p>')
    st.code("""import joblib
    
joblib.dump(meu_modelo, 'meu_modelo.pkl')
# e depois...
meu_modelo_carregado = joblib.load('meu_modelo.pkl')""", line_numbers=True)

# --- Ajuste seu modelo --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Ajuste seu modelo</h1>')
st.html('<p class="fonte_texto">Vamos supor que agora você tenha uma lista de modelos promissores. Agora '
        'você precisa ajustá-los. Vejamos algumas maneiras de fazer isso.</p>')
st.html('<h2 class="fonte_subtitulo_aula">Grid search</h2>')
st.html('<p class="fonte_texto">Uma opção seria mexer nos hiperparâmetros manualmente, até encontrar uma '
        'ótima combinação de valores de hiperparâmetros. Este seria um trabalho muito tedioso e talvez '
        'você não tenha tempo para explorar muitas combinações.</p>')
st.html('<p class="fonte_texto">Em vez disso, você deve obter o <b>GridSearchCV</b> do Scikit-Learn para '
        'procurar por você. Tudo o que você precisa fazer é informar quais hiperparâmetros deseja '
        'experimentar e quais valores testar, e ele usará a validação cruzada para avaliar todas as '
        'combinações possíveis de valores de hiperparâmetros. Por exemplo, o código a seguir procura a '
        'melhor combinação de valores de hiperparâmetros para o <b>RandomForestRegressor</b>:</p>')
st.code("""from sklearn.model_selection import GridSearchCV

parametros_grid = [
    {'n_estimators': [3, 10, 30], 'max_features': [2, 4, 6, 8]},
    {'n_estimators': [False], 'n_estimators': [3, 10], 'max_features': [2, 3, 4]}
]

flo_ale = RandomForestRegressor()

grid_search = GridSearchCV(
    flo_ale,
    parametros_grid,
    cv=5,
    scoring='neg_mean_squared_error',
    return_train_score=True
)

grid_search.fit(housing_preparado, housing_rotulos)""", line_numbers=True)
with st.expander('Dica 6', icon='💡'):
    st.html('<p class="fonte_texto">Quando você não tem ideia de qual valor um hiperparâmetro deve ter, uma '
            'abordagem simples é tentar potências consecutivas de 10 (ou um número menor se você quiser uma '
            'pesquisa mais refinada, como mostrado neste exemplo com o hiperparâmetro '
            '<b>n_estimators</b>).</p>')
st.html('<p class="fonte_texto">Este <b>parametros_grid</b> diz ao Scikit-Learn para primeiro avaliar '
        'todas as combinações 3 × 4 = 12 de <b>n_estimators</b> e <b>max_features</b> valores de '
        'hiperparâmetros especificados no primeiro <b>dict</b> (não se preocupe com o que esses '
        'hiperparâmetros significam por enquanto; eles serão explicados no Capítulo 7) e, em seguida, '
        'tente todos os 2 × 3 = 6 combinações de valores de hiperparâmetro no segundo <b>dict</b>, mas '
        'desta vez com o hiperparâmetro <b>bootstrap</b> definido como False em vez de True (que é o '
        'valor padrão para este hiperparâmetro).</p>')
st.html('<p class="fonte_texto">A pesquisa em grade (grid search) explorará 12 + 6 = 18 combinações de '
        'valores de '
        'hiperparâmetros de <b>RandomForestRegressor</b> e treinará cada modelo 5 vezes (já que estamos '
        'usando validação cruzada quíntupla). Ou seja, ao todo, serão 18 × 5 = 90 rodadas de treinamento! '
        'Pode levar bastante tempo, mas quando terminar você poderá obter a melhor combinação de '
        'parâmetros como este:</p>')
st.code('print(grid_search.best_params_)', line_numbers=True)
with st.expander('Dica 7', icon='💡'):
    st.html('<p class="fonte_texto">Como 8 e 30 são os valores máximos avaliados, você provavelmente '
            'deveria tentar pesquisar novamente com valores mais altos; a pontuação pode continuar a '
            'melhorar.</p>')
st.html('<p class="fonte_texto">Você também pode obter o melhor estimador diretamente:</p>')
st.code('print(grid_search.best_estimator_)', line_numbers=True)
with st.expander('Nota 1', icon='📝'):
    st.html('<p class="fonte_texto">Se <b>GridSearchCV</b> for inicializado com <b>refit=True</b> (que é '
            'o padrão), depois de encontrar o melhor estimador usando validação cruzada, ele o treinará '
            'novamente em todo o conjunto de treinamento. Geralmente, isso é uma boa ideia, pois fornecer '
            'mais dados provavelmente melhorará seu desempenho.</p>')
st.html('<p class="fonte_texto">E é claro que as pontuações da avaliação também estão disponíveis:</p>')
st.code("""resultados = grid_search.cv_results_
for media, parametros in zip(resultados['mean_test_score'], resultados['params']):
  print(np.sqrt(-media), parametros)""", line_numbers=True)
st.html('<p class="fonte_texto">Neste exemplo, obtemos a melhor solução definindo o hiperparâmetro '
        '<b>max_features</b> como 8 e o hiperparâmetro <b>n_estimators</b> como 30. A pontuação REQM para '
        'esta combinação é 49.819 (para você será diferente o valor), o que é um pouco melhor do que a '
        'pontuação obtida anteriormente usando os valores padrão do hiperparâmetro. Parabéns, você '
        'ajustou com sucesso seu melhor modelo!</p>')
with st.expander('Dica 8', icon='💡'):
    st.html('<p class="fonte_texto">Não se esqueça de que você pode tratar algumas etapas de preparação de '
            'dados como hiperparâmetros. Por exemplo, a pesquisa em grade descobrirá automaticamente se '
            'deve ou não adicionar um recurso sobre o qual você não tinha certeza (por exemplo, usando o '
            'hiperparâmetro <b>add_quartos_por_aposento</b> do seu transformador '
            '<b>AdicionadorAtributosCombinados</b>). Da mesma forma, ele pode ser usado para encontrar '
            'automaticamente a melhor maneira de lidar com valores discrepantes, recursos ausentes, seleção '
            'de recursos e muito mais.</p>')
st.html('<h2 class="fonte_subtitulo_aula">Pesquisa aleatória</h2>')
st.html('<p class="fonte_texto">A abordagem de pesquisa em grade é adequada quando você explora '
        'relativamente poucas combinações, como no exemplo anterior, mas quando o espaço de pesquisa do '
        'hiperparâmetro é grande, geralmente é preferível usar <b>RandomizedSearchCV</b>. Esta classe '
        'pode ser usada da mesma maneira que a classe <b>GridSearchCV</b>, mas em vez de testar todas as '
        'combinações possíveis, ela avalia um determinado número de combinações aleatórias selecionando '
        'um valor aleatório para cada hiperparâmetro em cada iteração. Essa abordagem tem dois benefícios '
        'principais:</p>')
st.html('<ul class="fonte_texto">'
            '<li>Se você permitir que a pesquisa aleatória seja executada por, digamos, 1.000 iterações, essa '
            'abordagem explorará 1.000 valores diferentes para cada hiperparâmetro (em vez de apenas alguns '
            'valores por hiperparâmetro com a abordagem de pesquisa em grade).</li>'
            '<li>Simplesmente definindo o número de iterações, você terá mais controle sobre o orçamento de '
            'computação que deseja alocar para a pesquisa de hiperparâmetros.</li>'
        '</ul>')
st.html('<h2 class="fonte_subtitulo_aula">Métodos de conjunto</h2>')
st.html('<p class="fonte_texto">Outra forma de ajustar seu sistema é tentar combinar os modelos com melhor '
        'desempenho. O grupo (ou “conjunto”) muitas vezes terá um desempenho melhor do que o melhor modelo '
        'individual (assim como as Florestas Aleatórias têm um desempenho melhor do que as Árvores de '
        'Decisão individuais nas quais elas dependem), especialmente se os modelos individuais cometerem '
        'tipos de erros muito diferentes. Abordaremos esse tópico com mais detalhes no Capítulo 7.</p>')
st.html('<h2 class="fonte_subtitulo_aula">Analise os melhores modelos e seus erros</h2>')
st.html('<p class="fonte_texto">Frequentemente, você obterá bons insights sobre o problema inspecionando '
        'os melhores modelos. Por exemplo, o <b>RandomForestRegressor</b> pode indicar a importância '
        'relativa de cada atributo para fazer previsões precisas:</p>')
st.code('''importancia_features = grid_search.best_estimator_.feature_importances_
print(importancia_features)''', line_numbers=True)
st.html('<p class="fonte_texto">Vamos exibir essas pontuações de importância ao lado dos nomes dos '
        'atributos correspondentes:</p>')
st.code("""atributos_extra = ['aposentos_por_casa', 'populacao_por_casa', 'quartos_pos_aposentos']
codificador_cat = pipeline_completo.named_transformers_['cat']
atributos_cat_1_hot = list(codificador_cat.categories_[0])
atributos = num_atributos + atributos_extra + atributos_cat_1_hot
sorted(zip(importancia_features, atributos), reverse=True)""", line_numbers=True)
tabela_2_10 = pd.read_csv('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_02/tabela_2_10.csv')
st.dataframe(tabela_2_10, hide_index=True)
st.html('<p class="fonte_texto">Com essas informações, você pode tentar eliminar alguns dos recursos menos '
        'úteis (por exemplo, aparentemente apenas uma categoria <b>ocean_proximity</b> é realmente útil, '
        'então você pode tentar eliminar as outras).</p>')
st.html('<p class="fonte_texto">Você também deve observar os erros específicos que seu sistema comete e, '
        'em seguida, tentar entender por que ele os comete e o que poderia resolver o problema (adicionar '
        'recursos extras ou eliminar os não informativos, limpar valores discrepantes, etc.).</p>')
st.html('<h2 class="fonte_subtitulo_aula">Avalie seu sistema no conjunto de testes</h2>')
st.html('<p class="fonte_texto">Depois de ajustar seus modelos por um tempo, você eventualmente terá um '
        'sistema com desempenho suficientemente bom. Agora é a hora de avaliar o modelo final no conjunto '
        'de teste. Não há nada de especial neste processo; apenas pegue os preditores e os rótulos do seu '
        'conjunto de testes, execute seu <b>pipeline_completo</b> para transformar os dados (chame '
        '<b>transform()</b>, não <b>fit_transform()</b>, você não quer ajustar o conjunto de testes!) e '
        'avalie o modelo final no conjunto de testes:</p>')
st.code('''modelo_final = grid_search.best_estimator_

X_teste = conjunto_teste_estratificado.drop('median_house_value', axis=1)
y_teste = conjunto_teste_estratificado['median_house_value'].copy()

X_teste_preparado = pipeline_completo.transform(X_teste)

predicoes_finais = modelo_final.predict(X_teste_preparado)

eqm_final = mean_squared_error(y_teste, predicoes_finais)
reqm_final = np.sqrt(eqm_final)

print(reqm_final)''', line_numbers=True)
st.html('<p class="fonte_texto">Em alguns casos, essa estimativa pontual do erro de generalização não '
        'será suficiente para convencê-lo a lançar: e se for apenas 0,1% melhor que o modelo atualmente '
        'em produção? Você pode querer ter uma ideia de quão precisa é essa estimativa. Para isso, você '
        'pode calcular um <i>intervalo de confiança</i> de 95% para o erro de generalização usando '
        '<b>scipy.stats.t.interval()</b>:</p>')
st.code('''from scipy import stats

confianca = 0.95
quadrado_erros = (predicoes_finais - y_teste) ** 2
np.sqrt(stats.t.interval(
    confianca,
    len(quadrado_erros) - 1,
    loc=quadrado_erros.mean(),
    scale=stats.sem(quadrado_erros)
))''', line_numbers=True)
st.html('<p class="fonte_texto">Se você fez muitos ajustes de hiperparâmetros, o desempenho geralmente '
        'será um pouco pior do que o medido usando validação cruzada (porque seu sistema acaba sendo '
        'ajustado para ter um bom desempenho nos dados de validação e provavelmente não terá um '
        'desempenho tão bom em conjuntos de dados desconhecidos). Não é o caso neste exemplo, mas quando '
        'isso acontece você deve resistir à tentação de ajustar os hiperparâmetros para fazer com que os '
        'números pareçam bons no conjunto de teste; seria pouco provável que as melhorias se '
        'generalizassem para novos dados.</p>')
st.html('<p class="fonte_texto">Agora vem a fase de pré-lançamento do projeto: você precisa apresentar '
        'sua solução (destacando o que você aprendeu, o que funcionou e o que não funcionou, quais '
        'suposições foram feitas e quais são as limitações do seu sistema), documentar tudo e criar boas '
        'apresentações com visualizações claras e declarações fáceis de lembrar (por exemplo, “a renda '
        'mediana é o preditor número um dos preços da habitação”). Neste exemplo habitacional da '
        'Califórnia, o desempenho final do sistema não é melhor do que as estimativas de preços dos '
        'especialistas, que muitas vezes estavam erradas em cerca de 20%, mas ainda pode ser uma boa '
        'ideia lançá-lo, especialmente se isso libertar algum tempo para os especialistas, para que '
        'possam trabalhar em tarefas mais interessantes e produtivas.</p>')

# --- Inicie, monitore e mantenha seu sistema --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Inicie, monitore e mantenha seu sistema</h1>')
st.html('<p class="fonte_texto">Perfeito, você obteve aprovação para lançar! Agora você precisa preparar '
        'sua solução para produção (por exemplo, aprimorar o código, escrever documentação e testes e '
        'assim por diante). Em seguida, você poderá implantar seu modelo em seu ambiente de produção. Uma '
        'maneira de fazer isso é salvar o modelo treinado do Scikit-Learn (por exemplo, usando '
        '<b>joblib</b>), incluindo o pré-processamento completo e o pipeline de previsão, depois carregar '
        'esse modelo treinado em seu ambiente de produção e usá-lo para fazer previsões chamando seu '
        'método <b>predict()</b>. Por exemplo, talvez o modelo seja usado dentro de um site: o usuário '
        'digitará alguns dados sobre um novo distrito e clicará no botão Estimar Preço. Isso enviará uma '
        'consulta contendo os dados ao servidor web, que os encaminhará para sua aplicação web e, '
        'finalmente, seu código simplesmente chamará o método <b>predict()</b> do modelo (você deseja '
        'carregar o modelo na inicialização do servidor, em vez de sempre que o modelo for usado). Como '
        'alternativa, você pode agrupar o modelo em um serviço Web dedicado que seu aplicativo Web pode '
        'consultar por meio de uma API REST. Isso facilita a atualização do seu '
        'modelo para novas versões sem interromper o aplicativo principal. Ele também simplifica o '
        'dimensionamento, já que você pode iniciar quantos serviços Web forem necessários e balancear a '
        'carga das solicitações provenientes de seu aplicativo Web nesses serviços Web. Além disso, '
        'permite que seu aplicativo web use qualquer linguagem, não apenas Python.</p>')
st.html('<p class="fonte_texto">Outra estratégia popular é implantar seu modelo na nuvem, por exemplo, no '
        'Google Cloud AI Platform (anteriormente conhecido como Google Cloud ML Engine): basta salvar seu '
        'modelo usando <b>joblib</b> e carregá-lo no Google Cloud Storage (GCS), depois ir para o Google '
        'Cloud AI Platform e criar uma nova versão do modelo, apontando-a para o arquivo GCS. É isso! '
        'Isso fornece um serviço da Web simples que cuida do balanceamento de carga e do dimensionamento '
        'para você. São necessárias solicitações JSON contendo os dados de entrada (por exemplo, de um '
        'distrito) e retorna respostas JSON contendo as previsões. Você pode então usar este serviço da '
        'web em seu site (ou em qualquer ambiente de produção que estiver usando). Como veremos no '
        'Capítulo 19, a implantação de modelos do TensorFlow no AI Platform não é muito diferente da '
        'implantação de modelos do Scikit-Learn.</p>')
st.html('<p class="fonte_texto">Mas a implantação não é o fim da história. Você também precisa escrever '
        'um código de monitoramento para verificar o desempenho ao vivo do seu sistema em intervalos '
        'regulares e acionar alertas quando ele cair. Esta pode ser uma queda acentuada, provavelmente '
        'devido a um componente quebrado na sua infraestrutura, mas esteja ciente de que também pode ser '
        'uma queda suave que pode facilmente passar despercebida por um longo tempo. Isto é bastante '
        'comum porque os modelos tendem a “apodrecer” com o tempo: de fato, o mundo muda, por isso, se o '
        'modelo foi treinado com os dados do ano passado, pode não ser adaptado aos dados de hoje.</p>')
with st.expander('Alerta 5', icon='⚡'):
    st.html('<p class="fonte_texto">Mesmo um modelo treinado para classificar imagens de cães e gatos pode '
            'precisar ser treinado novamente regularmente, não porque cães e gatos sofrerão mutações '
            'durante a noite, mas porque as câmeras estão sempre mudando, junto com os formatos de imagem, '
            'nitidez, brilho e proporções de tamanho. Além disso, as pessoas podem adorar raças diferentes '
            'no próximo ano, ou podem decidir vestir os seus animais de estimação com chapéus minúsculos, '
            'quem sabe?</p>')
st.html('<p class="fonte_texto">Então você precisa monitorar o desempenho ao vivo do seu modelo. Mas como '
        'você faz isso? Bem, isso depende. Em alguns casos, o desempenho do modelo pode ser inferido a '
        'partir de métricas posteriores. Por exemplo, se o seu modelo faz parte de um sistema de '
        'recomendação e sugere produtos nos quais os usuários podem estar interessados, é fácil monitorar '
        'o número de produtos recomendados vendidos a cada dia. Se esse número cair (em comparação com '
        'produtos não recomendados), o principal suspeito é o modelo. Isso pode ocorrer porque o pipeline '
        'de dados está quebrado ou talvez o modelo precise ser treinado novamente com dados novos (como '
        'discutiremos em breve).</p>')
st.html('<p class="fonte_texto">Porém, nem sempre é possível determinar o desempenho do modelo sem '
        'qualquer análise humana. Por exemplo, suponha que você treinou um modelo de classificação de '
        'imagens (consulte o Capítulo 3) para detectar vários defeitos de produtos em uma linha de '
        'produção. Como você pode receber um alerta se o desempenho do modelo cair, antes que milhares de '
        'produtos defeituosos sejam enviados aos seus clientes? Uma solução é enviar aos avaliadores '
        'humanos uma amostra de todas as imagens que o modelo classificou (especialmente as imagens '
        'sobre as quais o modelo não tinha tanta certeza). Dependendo da tarefa, os avaliadores podem '
        'precisar ser especialistas ou não especialistas, como trabalhadores de uma plataforma de '
        'crowdsourcing (por exemplo, Amazon Mechanical Turk). Em algumas aplicações, podem até ser os '
        'próprios utilizadores, respondendo, por exemplo, através de inquéritos ou captchas '
        'reaproveitados.</p>')
st.html('<p class="fonte_texto">De qualquer forma, é necessário implementar um sistema de monitoramento '
        '(com ou sem avaliadores humanos para avaliar o modelo ao vivo), bem como todos os processos '
        'relevantes para definir o que fazer em caso de falhas e como se preparar para elas. Infelizmente, '
        'isso pode dar muito trabalho. Na verdade, muitas vezes dá muito mais trabalho do que construir e '
        'treinar um modelo.</p>')
st.html('<p class="fonte_texto">Se os dados continuarem evoluindo, você precisará atualizar seus conjuntos '
        'de dados e retreinar seu modelo regularmente. Você provavelmente deveria automatizar todo o '
        'processo tanto quanto possível. Aqui estão algumas coisas que você pode automatizar:</p>')
st.html('<ul class="fonte_texto">'
            '<li>Colete dados novos regularmente e rotule-os (por exemplo, usando avaliadores humanos).</li>'
            '<li>Escreva um script para treinar o modelo e ajustar os hiperparâmetros automaticamente. '
            'Este script pode ser executado automaticamente, por exemplo, todos os dias ou todas as '
            'semanas, dependendo das suas necessidades.</li>'
            '<li>Escreva outro script que avalie o novo modelo e o modelo anterior no conjunto de testes '
            'atualizado e implante o modelo em produção se o desempenho não tiver diminuído (se diminuiu, '
            'certifique-se de investigar o motivo).</li>'
        '</ul>')
st.html('<p class="fonte_texto">Você também deve avaliar a qualidade dos dados de entrada do modelo. Às '
        'vezes, o desempenho será ligeiramente degradado devido a um sinal de baixa qualidade (por '
        'exemplo, um sensor com defeito enviando valores aleatórios ou a saída de outra equipe ficando '
        'obsoleta), mas pode demorar um pouco até que o desempenho do seu sistema seja degradado o '
        'suficiente para acionar um alerta. Se você monitorar as entradas do seu modelo, poderá perceber '
        'isso mais cedo. Por exemplo, você pode acionar um alerta se mais e mais entradas estiverem '
        'faltando um recurso, ou se sua média ou desvio padrão se afastar muito do conjunto de '
        'treinamento, ou se um recurso categórico começar a conter novas categorias.</p>')
st.html('<p class="fonte_texto">Por fim, certifique-se de manter backups de cada modelo criado e de ter o '
        'processo e as ferramentas em vigor para reverter rapidamente para um modelo anterior, caso o '
        'novo modelo comece a falhar gravemente por algum motivo. Ter backups também permite comparar '
        'facilmente novos modelos com os anteriores. Da mesma forma, você deve manter backups de cada '
        'versão de seus conjuntos de dados para poder reverter para um conjunto de dados anterior se o '
        'novo for corrompido (por exemplo, se os dados novos adicionados a ele estiverem cheios de '
        'valores discrepantes). Ter backups de seus conjuntos de dados também permite avaliar qualquer '
        'modelo em relação a qualquer conjunto de dados anterior.</p>')
with st.expander('Dica 9', icon='💡'):
    st.html('<p class="fonte_texto">Você pode criar vários subconjuntos do conjunto de testes para avaliar '
            'o desempenho do seu modelo em partes específicas dos dados. Por exemplo, você pode querer ter '
            'um subconjunto contendo apenas os dados mais recentes ou um conjunto de testes para tipos '
            'específicos de dados (por exemplo, distritos localizados no interior versus distritos '
            'localizados perto do oceano). Isso lhe dará uma compreensão mais profunda dos pontos fortes e '
            'fracos do seu modelo.</p>')
st.html('<p class="fonte_texto">Como você pode ver, o Aprendizado de Máquina envolve muita infraestrutura, '
        'então não se surpreenda se seu primeiro projeto de AM exigir muito esforço e tempo para ser '
        'construído e implantado em produção. Felizmente, quando toda a infraestrutura estiver instalada, '
        'passar da ideia à produção será muito mais rápido.</p>')

# --- Experimente! --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Experimente!</h1>')
st.html('<p class="fonte_texto">Espero que este capítulo tenha lhe dado uma boa ideia de como é um '
        'projeto de Aprendizado de Máquina, além de mostrar algumas das ferramentas que você pode usar '
        'para treinar um ótimo sistema. Como você pode ver, grande parte do trabalho está na etapa de '
        'preparação de dados: construção de ferramentas de monitoramento, configuração de pipelines de '
        'avaliação humana e automatização do treinamento regular do modelo. Os algoritmos de aprendizado '
        'de máquina são importantes, é claro, mas provavelmente é preferível estar confortável com o '
        'processo geral e conhecer bem três ou quatro algoritmos, em vez de gastar todo o seu tempo '
        'explorando algoritmos avançados.</p>')
st.html('<p class="fonte_texto">Então, se você ainda não fez isso, agora é um bom momento para pegar um '
        'laptop, selecionar um conjunto de dados de seu interesse e tentar passar por todo o processo de '
        'A a Z. Um bom lugar para começar é em um site de competição como '
        '<a href="https://www.kaggle.com/">Kaggle</a>: você terá um conjunto de dados para brincar, um '
        'objetivo claro e pessoas com quem compartilhar a experiência. Divirta-se!</p>')