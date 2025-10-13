# --- Importar as bibliotecas --- #
import pandas as pd
from PIL import Image
import streamlit as st

# --- Configurações iniciais da página --- #
st.set_page_config(
    page_title='Capítulo 01 - O cenário do aprendizado de máquina',
    page_icon=Image.open('./assets/logo/logo.png'),
    layout='wide'
)

# --- Carregar o estilo das fontes --- #
with open('./assets/css/style.css', 'r') as css:
    st.html(f'<style>{css.read()}</style>')

# --- Colocar o banner do capítulo --- #
st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_01/aula_01.png')

# --- Introdução --- #
st.html('<h1 class="fonte_titulo_aula">Introdução</h1>')
st.html('<p class="fonte_texto">Quando a maioria das pessoas ouve “Aprendizado de Máquina”, elas '
        'imaginam um robô: um mordomo confiável ou um Exterminador do Futuro mortal, dependendo para '
        'quem você perguntar. Mas o Aprendizado de Máquina não é apenas uma fantasia futurística; já está aqui. '
        'Na verdade, ele existe há décadas em algumas aplicações especializadas, como o reconhecimento '
        'óptico de caracteres (OCR). Mas a primeira aplicação de AM que realmente se tornou popular, '
        'melhorando a vida de centenas de milhões de pessoas, dominou o mundo na década de 1990: o filtro '
        'de spam. Não é exatamente uma Skynet autoconsciente, mas tecnicamente se qualifica como aprendizado '
        'de máquina (na verdade, ela aprendeu tão bem que raramente é necessário sinalizar um e-mail '
        'como spam). Ele foi seguido por centenas de aplicativos de AM que agora alimentam silenciosamente '
        'centenas de produtos e recursos que você usa regularmente, desde melhores recomendações até '
        'pesquisa por voz.</p>')
st.html('<p class="fonte_texto">Onde começa e onde termina o aprendizado de máquina? O que exatamente '
        'significa para uma máquina <i>aprender</i> alguma coisa? Se eu baixar uma cópia da Wikipédia, '
        'meu computador realmente aprendeu alguma coisa? De repente é mais inteligente? Neste capítulo '
        'começaremos esclarecendo o que é Aprendizado de Máquina e por que você pode querer usá-lo.</p>')
st.html('<p class="fonte_texto">Então, antes de partirmos para explorar o continente de Aprendizado de '
        'Máquina, daremos uma olhada no mapa e aprenderemos sobre as principais regiões e os marcos mais '
        'notáveis: aprendizagem supervisionada versus não supervisionada, aprendizagem on-line versus '
        'aprendizagem em lote, aprendizagem baseada em instâncias versus aprendizagem baseada em modelo. '
        'Em seguida, veremos o fluxo de trabalho de um projeto típico de AM, discutiremos os principais '
        'desafios que você pode enfrentar e abordaremos como avaliar e ajustar um sistema de aprendizado '
        'de máquina.</p>')
st.html('<p class="fonte_texto">Este capítulo apresenta muitos conceitos fundamentais (e jargões) que todo '
        'cientista de dados deve saber de cor. Será uma visão geral de alto nível (é o único capítulo sem '
        'muito código), tudo bastante simples, mas você deve ter certeza de que tudo está claro para você '
        'antes de prosseguir para o resto do estudo. Então pegue um café e vamos começar!</p>')
with st.expander('Dica 1', icon='💡'):
        st.html('<p class="fonte_texto">Se você já conhece todos os fundamentos do aprendizado de máquina,'
                ' pode pular diretamente para o Capítulo 2. Se não tiver certeza, permaneça neste capítulo '
                'para construir uma boa base.</p>')

# --- O que é aprendizado de máquina? --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">O que é aprendizado de máquina?</h1>')
st.html('<p class="fonte_texto">Machine Learning é a ciência (e arte) de programar computadores para '
        'que possam <i>aprender com os dados</i>.</p>')
st.html('<p class="fonte_texto">Aqui está uma definição um pouco mais geral:</p>')
st.html('<blockquote class="fonte_texto"><i>[Aprendizado de Máquina é o] campo de estudo que dá aos '
        'computadores a capacidade de aprender sem serem explicitamente programados.</i> '
        '(Arthur Samuel, 1959)</blockquote>')
st.html('<p class="fonte_texto">E um mais voltado para a engenharia:</p>')
st.html('<blockquote class="fonte_texto"><i>Diz-se que um programa de computador aprende com a experiência'
        ' E em relação a alguma tarefa T e alguma medida de desempenho P, se seu desempenho em T, medido'
        ' por P, melhora com a experiência E.</i> (Tom Mitchell, 1997)</blockquote>')
st.html('<p class="fonte_texto">Seu filtro de spam é um programa de aprendizado de máquina que, dados '
        'exemplos de e-mails de spam (por exemplo, sinalizados por usuários) e exemplos de e-mails '
        'regulares (não spam, também chamados de “ham”), pode aprender a sinalizar spam. Os exemplos que o'
        ' sistema usa para aprender são chamados de <i>conjunto de treinamento</i>. Cada exemplo de '
        'treinamento é chamado de <i>instância de treinamento</i> (ou <i>amostra</i>). Neste caso, a tarefa'
        ' <b>T</b> é sinalizar spam para novos e-mails, a experiência <b>E</b> são os <i>dados de '
        'treinamento</i> e a medida de desempenho <b>P</b> precisa ser definida; por exemplo, você pode '
        'usar a proporção de e-mails classificados corretamente. Essa medida de desempenho específica é '
        'chamada de <i>acurácia</i> e é frequentemente usada em tarefas de classificação.</p>')
st.html('<p class="fonte_texto">Se você apenas baixar uma cópia da Wikipedia, seu computador terá muito '
        'mais dados, mas não ficará subitamente melhor em nenhuma tarefa. Portanto, baixar uma cópia '
        'da Wikipedia não é aprendizado de máquina.</p>')

# --- Por que usar aprendizado de máquina? --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Por que usar aprendizado de máquina?</h1>')
st.html('<p class="fonte_texto">Considere como você escreveria um filtro de spam usando técnicas '
        'de programação tradicionais (Figura 1-1):</p>')
st.html('<ol class="fonte_texto" type="1">'
        '<li>Primeiro, você consideraria a aparência típica do spam. Você pode notar que algumas palavras '
        'ou frases (como “para você”, “cartão de crédito”, “grátis” e “incrível”) tendem a aparecer muito '
        'na linha de assunto. Talvez você também note alguns outros padrões no nome do remetente, no corpo '
        'do e-mail e em outras partes do e-mail.</li>'
        '<li>Você escreveria um algoritmo de detecção para cada um dos padrões observados e seu programa '
        'sinalizaria e-mails como spam se vários desses padrões fossem detectados.</li>'
        '<li>Você testaria seu programa e repetiria as etapas 1 e 2 até que estivesse bom o suficiente '
        'para ser utilizado em larga escala.</li>'
        '</ol>')
st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_01/figura_01.png',
         caption='Figura 1-1. Abordagem tradicional.')
st.html('<p class="fonte_texto">Como o problema é difícil, seu programa provavelmente se tornará uma longa '
        'lista de regras complexas – muito difíceis de manter.</p>')
st.html('<p class="fonte_texto">Em contraste, um filtro de spam baseado em técnicas de aprendizado de '
        'máquina aprende automaticamente quais palavras e frases são bons preditores de spam, detectando '
        'padrões de palavras incomumente frequentes nos exemplos de spam em comparação com os exemplos de '
        'spam (Figura 1-2). O programa é muito mais curto, mais fácil de manter e provavelmente mais '
        'preciso.</p>')
st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_01/figura_02.png',
         caption='Figura 1-2. Abordagem do aprendizado de máquina.')
st.html('<p class="fonte_texto">E se os spammers perceberem que todos os seus e-mails contendo “para você”'
        ' estão bloqueados? Eles podem começar a escrever “para vc”. Um filtro de spam usando técnicas '
        'de programação tradicionais precisaria ser atualizado para sinalizar e-mails “para vc”. Se os '
        'spammers continuarem contornando seu filtro de spam, você precisará continuar escrevendo novas '
        'regras para sempre.</p>')
st.html('<p class="fonte_texto">Por outro lado, um filtro de spam baseado em técnicas de aprendizado de '
        'máquina percebe automaticamente que “para vc” se tornou incomumente frequente em spam sinalizado'
        ' por usuários e começa a sinalizá-los sem a sua intervenção (Figura 1-3).</p>')
st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_01/figura_03.png',
         caption='Figura 1-3. Adapta-se automáticamente à mudança.')
st.html('<p class="fonte_texto">Outra área onde o aprendizado de máquina brilha é em problemas que são '
        'muito complexos para abordagens tradicionais ou que não possuem algoritmo conhecido. Por exemplo,'
        ' considere o reconhecimento de fala. Digamos que você queira começar de forma simples e escrever '
        'um programa capaz de distinguir as palavras “um” e “dois”. Você pode notar que a palavra “dois” '
        'começa com um som agudo, então você pode codificar um algoritmo que mede a intensidade do '
        'som agudo e usá-lo para distinguir uns e dois – mas obviamente essa técnica não será dimensionada'
        ' para milhares de palavras faladas por milhões de pessoas muito diferentes em ambientes '
        'barulhentos e em dezenas de idiomas. A melhor solução (pelo menos hoje) é escrever um algoritmo '
        'que aprenda por si só, dados muitos exemplos de gravações para cada palavra.</p>')
st.html('<p class="fonte_texto">Finalmente, o Aprendizado de Máquina pode ajudar os humanos a aprender'
        ' (Figura 1-4). Os algoritmos de AM podem ser inspecionados para ver o que aprenderam (embora '
        'para alguns algoritmos isso possa ser complicado). Por exemplo, uma vez treinado um filtro de '
        'spam, ele pode ser facilmente inspecionado para revelar a lista de palavras '
        'e combinações de palavras que ele acredita serem os melhores preditores de spam. Por vezes, '
        'isto revelará correlações insuspeitadas ou novas tendências, conduzindo assim a uma melhor '
        'compreensão do problema. A aplicação de técnicas de AM para investigar grandes quantidades de '
        'dados pode ajudar a descobrir padrões que não eram imediatamente aparentes. Isso é chamado de '
        '<i>mineração de dados</i>.</p>')
st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_01/figura_04.png',
         caption='Figura 1-4. O Aprendizado de Máquina pode ajudar no ensino dos humanos.')
st.html('<p class="fonte_texto">Para resumir, o aprendizado de máquina é ótimo para:</p>')
st.html('<ul class="fonte_texto">'
        '<li>Problemas para os quais as soluções existentes exigem muitos ajustes finos ou longas listas '
        'de regras: um algoritmo de aprendizado de máquina pode muitas vezes simplificar o código e ter '
        'um desempenho melhor do que a abordagem tradicional.</li>'
        '<li>Problemas complexos para os quais o uso de uma abordagem tradicional não produz uma boa '
        'solução: as melhores técnicas de Aprendizado de Máquina talvez possam encontrar uma solução.</li>'
        '<li>Ambientes flutuantes: um sistema de Aprendizado de Máquina pode se adaptar a novos dados.</li>'
        '<li>Obter insights sobre problemas complexos e grandes quantidades de dados.</li>'
        '</ul>')

# --- Exemplos de aplicação --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Exemplos de aplicação</h1>')
st.html('<p class="fonte_texto">Vejamos alguns exemplos concretos de tarefas de Aprendizado de Máquina, '
        'juntamente com as técnicas que podem resolvê-las:</p>')
st.html('<ul class="fonte_texto">'
        '<li>Análise de imagens de produtos em uma linha de produção para classificá-los automaticamente: '
        'Esta é a classificação de imagens, normalmente realizada usando redes neurais convolucionais (CNN).</li>'
        '<li>Detecção de tumores em exames cerebrais: Esta é a segmentação semântica, onde cada pixel da '
        'imagem é classificado (já que queremos determinar a localização e a forma exatas dos tumores), '
        'normalmente também usando CNNs.</li>'
        '<li>Classificação automática de artigos de notícias: trata-se do processamento de linguagem '
        'natural (PNL) e, mais especificamente, da classificação de texto, que pode ser abordada usando '
        'redes neurais recorrentes (RNNs), CNNs ou Transformers.</li>'
        '<li>Sinalização automática de comentários ofensivos em fóruns de discussão: Esta também é uma '
        'classificação de texto, usando as mesmas ferramentas de PNL.</li>'
        '<li>Resumindo documentos longos automaticamente: Este é um ramo da PNL chamado resumo de texto, '
        'novamente usando as mesmas ferramentas.</li>'
        '<li>Criando um chatbot ou assistente pessoal: Isso envolve muitos componentes de PNL, incluindo '
        'compreensão de linguagem natural (NLU) e módulos de resposta a perguntas.</li>'
        '<li>Previsão da receita da sua empresa no próximo ano, com base em muitas métricas de desempenho:'
        ' Esta é uma tarefa de regressão (ou seja, previsão de valores) que pode ser realizada usando '
        'qualquer modelo de regressão, como um modelo de regressão linear ou de regressão polinomial, '
        'uma regressão SVM, uma regressão Random Forest ou uma rede neural artificial. Se você quiser '
        'levar em conta sequências de métricas de desempenho anteriores, poderá usar RNNs, CNNs ou '
        'Transformers.</li>'
        '<li>Fazendo seu aplicativo reagir a comandos de voz: Este é o reconhecimento de fala, que requer '
        'o processamento de amostras de áudio: como são sequências longas e complexas, normalmente são '
        'processadas usando RNNs, CNNs ou Transformers.</li>'
        '<li>Detecção de fraude de cartão de crédito: Esta é a detecção de anomalias.</li>'
        '<li>Segmentar clientes com base em suas compras para que você possa criar uma estratégia de '
        'marketing diferente para cada segmento: Isso é clusterização.</li>'
        '<li>Representando um conjunto de dados complexo e de alta dimensão em um diagrama claro e '
        'esclarecedor: Esta é a visualização de dados, muitas vezes envolvendo técnicas de redução de '
        'dimensionalidade.</li>'
        '<li>Recomendar um produto no qual um cliente possa estar interessado, com base em compras '
        'anteriores: Este é um sistema de recomendação. Uma abordagem é alimentar uma rede neural '
        'artificial com compras anteriores (e outras informações sobre o cliente) e fazer com que ela '
        'produza a próxima compra mais provável. Essa rede neural normalmente seria treinada em sequências '
        'anteriores de compras de todos os clientes.</li>'
        '<li>Construindo um bot inteligente para um jogo: Isso geralmente é resolvido usando Aprendizado '
        'por Reforço (AR), que é um ramo do Aprendizado de Máquina que treina agentes (como bots) para '
        'escolher as ações que maximizarão suas recompensas ao longo do tempo (por exemplo, um bot pode '
        'receber uma recompensa toda vez que o jogador perde alguns pontos de vida), dentro de um '
        'determinado ambiente (como o jogo). O famoso programa AlphaGo que venceu o campeão mundial no '
        'jogo Go foi construído usando AR.</li>'
        '</ul>')
st.html('<p class="fonte_texto">Esta lista poderia continuar indefinidamente, mas espero que lhe dê uma '
        'noção da incrível amplitude e complexidade das tarefas que o aprendizado de máquina pode realizar '
        'e dos tipos de técnicas que você usaria para cada tarefa.</p>')

# --- Tipos de sistemas de aprendizado de máquina --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Tipos de sistemas de aprendizado de máquina</h1>')
st.html('<p class="fonte_texto">Existem tantos tipos diferentes de sistemas de Aprendizado de Máquina '
        'que é útil classificá-los em categorias amplas, com base nos seguintes critérios:</p>')
st.html('<ul class="fonte_texto">'
        '<li>Quer sejam ou não treinados com supervisão humana (supervisionado, não supervisionado, '
        'semissupervisionado e Aprendizagem por Reforço).</li>'
        '<li>Se eles podem ou não aprender de forma incremental em tempo real (aprendizado online '
        'versus aprendizado em lote).</li>'
        '<li>Quer funcionem simplesmente comparando novos pontos de dados com pontos de dados conhecidos '
        'ou, em vez disso, detectando padrões nos dados de treinamento e construindo um modelo preditivo, '
        'assim como fazem os cientistas (aprendizado baseado em instâncias versus aprendizado baseado em '
        'modelo).</li>'
        '</ul>')
st.html('<p class="fonte_texto">Estes critérios não são exclusivos; você pode combiná-los da maneira que '
        'quiser. Por exemplo, um filtro de spam de última geração pode aprender instantaneamente usando '
        'um modelo de rede neural profunda treinado com exemplos de spam e ham; isso o torna um sistema '
        'de aprendizagem online, baseado em modelo e supervisionado. Vejamos cada um desses critérios '
        'um pouco mais de perto.</p>')
st.html('<p class="fonte_subtitulo_aula"><b>Aprendizado supervisionado/não supervisionado</b></p>')
st.html('<p class="fonte_texto">Os sistemas de aprendizado de máquina podem ser classificados de acordo '
        'com a quantidade e o tipo de supervisão que recebem durante o treinamento. Existem quatro '
        'categorias principais: aprendizagem supervisionada, aprendizagem não supervisionada, aprendizagem '
        'semissupervisionada e aprendizagem por reforço.</p>')
st.html('<p class="fonte_sub_subtitulo_aula"><b>Aprendizado supervisionado</b></p>')
st.html('<p class="fonte_texto">No <i>aprendizado supervisionado</i>, o conjunto de treinamento que você '
        'alimenta o algoritmo inclui as soluções desejadas, chamadas rótulos (Figura 1-5).</p>')
st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_01/figura_05.png',
         caption='Figura 1-5. Um conjunto de treinamento rotulado para aprendizado supervisionado (por '
                 'exemplo, classificação de spam).')
st.html('<p class="fonte_texto">Uma tarefa típica de aprendizagem supervisionada é a classificação. O '
        'filtro de spam é um bom exemplo disso: ele é treinado com vários exemplos de e-mails junto com '
        'sua classe (spam ou ham), e deve aprender a classificar novos e-mails.</p>')
st.html('<p class="fonte_texto">Outra tarefa típica é prever um valor numérico alvo, como o preço de um '
        'carro, dado um conjunto de características (quilometragem, idade, marca, etc.) chamadas '
        'preditores. Esse tipo de tarefa é chamada de regressão (Figura 1.6). Para treinar o sistema, '
        'é necessário fornecer muitos exemplos de carros, incluindo seus preditores e rótulos (ou seja, '
        'seus preços).</p>')
st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_01/figura_06.png',
         caption='Figura 1-6. Regressão.')
with st.expander('Nota 1', icon='📝'):
        st.html('<p class="fonte_texto">No Aprendizado de Máquina, um atributo é um tipo de dado '
                '(por exemplo, “quilometragem”), enquanto uma <i>feature</i> (característica) tem vários '
                'significados, dependendo '
                'do contexto, mas geralmente significa um atributo mais seu valor (por exemplo, '
                '“quilometragem = 15.000”). Muitas pessoas usam as palavras <i>atributo</i> e '
                '<i>característica</i> de '
                'forma intercambiável.</p>')
st.html('<p class="fonte_texto">Observe que alguns algoritmos de regressão também podem ser '
        'usados para classificação e vice-versa. Por exemplo, a <i>regressão logística</i> é comumente '
        'usada para classificação, pois pode gerar um valor que corresponde à probabilidade de pertencer '
        'a uma determinada classe (por exemplo, 20% de chance de ser spam).</p>')
st.html('<p class="fonte_texto">Aqui estão alguns dos algoritmos de aprendizagem supervisionada mais '
        'importantes:</p>')
st.html('<ul class="fonte_texto">'
        '<li>k-Nearest Neighbors</li>'
        '<li>Regressão linear</li>'
        '<li>Regressão logística</li>'
        '<li>Máquinas de Vetores de Suporte (SVM)</li>'
        '<li>Árvores de decisão e árvores aleatórias</li>'
        '<li>Redes neurais</li>'
        '</ul>')
st.html('<p class="fonte_sub_subtitulo_aula"><b>Aprendizado não supervisionado</b></p>')
st.html('<p class="fonte_texto">No <i>aprendizado não supervisionado</i>, como você pode imaginar, os '
        'dados de treinamento não são rotulados (Figura 1.7). O sistema tenta aprender sem professor.</p>')
st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_01/figura_07.png',
         caption='Figura 1-7. Conjunto de treinamento não rotulado para aprendizado não supervisionado.')
st.html('<p class="fonte_texto">Aqui estão alguns dos algoritmos de aprendizagem não supervisionados '
        'mais importantes:</p>')
st.html('<ul class="fonte_texto">'
                '<li>Clusterização:</li>'
                '<ul class="fonte_texto">'
                        '<li>K-mean</li>'
                        '<li>DBScan</li>'
                        '<li>Clusterização hierárquica (HCA)</li>'
                '</ul>'
                '<li>Visualização e redução da dimensionalidade</li>'
                '<ul class="fonte_texto">'
                        '<li>Análise de Componentes Principais (PCA)</li>'
                        '<li>Kernal PCA</li>'
                        '<li>Incorporação Linear Local (LLE)</li>'
                        '<li>Incorporação estocástica de vizinhos distribuída em t (t-SNE)</i>'
                '</ul>'
                '<li>Aprendizado da regra de associação</li>'
                '<ul class="fonte_texto">'
                        '<li>Apriori</li>'
                        '<li>Eclat</li>'
                '</ul>'
        '</ul>')
st.html('<p class="fonte_texto">Por exemplo, digamos que você tenha muitos dados sobre os visitantes do seu '
        'blog. Talvez você queira executar um algoritmo de <i>clusterização</i> para tentar detectar grupos '
        'de visitantes semelhantes (Figura 1.8). Em nenhum momento você informa ao algoritmo a qual grupo '
        'um visitante pertence: ele encontra essas conexões sem a sua ajuda. Por exemplo, pode notar que '
        '40% dos seus visitantes são homens que adoram histórias em quadrinhos e geralmente leem o seu '
        'blog à noite, enquanto 20% são jovens amantes de ficção científica que o visitam durante os fins '
        'de semana. Se você usar um algoritmo de agrupamento hierárquico, ele também poderá subdividir '
        'cada grupo em grupos menores. Isso pode ajudá-lo a direcionar suas postagens para cada grupo.</p>')
st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_01/figura_08.png',
         caption='Figura 1-8. Clusterização.')
st.html('<p class="fonte_texto">Algoritmos de <i>visualização</i> também são bons exemplos de algoritmos '
        'de aprendizagem não supervisionados: você os alimenta com muitos dados complexos e não rotulados, '
        'e eles produzem uma representação 2D ou 3D de seus dados que pode ser facilmente plotada '
        '(Figura 1-9). Esses algoritmos tentam preservar o máximo de estrutura possível (por exemplo, '
        'tentando evitar que clusters separados no espaço de entrada se sobreponham na visualização) para '
        'que você possa entender como os dados estão organizados e talvez identificar padrões '
        'inesperados.</p>')
st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_01/figura_09.png',
         caption='Figura 1-9. Exemplo de uma visualização t-SNE destacando grupos semânticos.')
st.html('<p class="fonte_texto">Uma tarefa relacionada é a <i>redução de dimensionalidade</i>, em que o '
        'objetivo é simplificar os dados sem perder muita informação. Uma maneira de fazer isso é mesclar '
        'vários recursos correlacionados em um. Por exemplo, a quilometragem de um carro pode estar '
        'fortemente correlacionada com a sua idade, pelo que o algoritmo de redução de dimensionalidade '
        'irá fundi-los numa característica que representa o desgaste do carro. Isso é chamado de '
        '<i>extração de recursos</i>.</p>')
with st.expander('Dica 2', icon='💡'):
        st.html('<p class="fonte_texto">Muitas vezes é uma boa ideia tentar reduzir a dimensão dos seus '
                'dados de treinamento usando um algoritmo de redução de dimensionalidade antes de '
                'alimentá-los para outro algoritmo de aprendizado de máquina (como um algoritmo de '
                'aprendizado supervisionado). Ele será executado muito mais rápido, os dados ocuparão '
                'menos espaço em disco e memória e, em alguns casos, também poderá ter um desempenho '
                'melhor.</p>')
st.html('<p class="fonte_texto">Outra tarefa não supervisionada importante é a <i>detecção de '
        'anomalias</i>, por exemplo, detectar transações incomuns de cartão de crédito para evitar '
        'fraudes, detectar defeitos de fabricação ou remover automaticamente valores discrepantes de um '
        'conjunto de dados antes de alimentá-los para outro algoritmo de aprendizagem. O sistema mostra '
        'principalmente instâncias normais durante o treinamento, então ele aprende a reconhecê-las; '
        'então, quando vê uma nova instância, ele pode dizer se ela parece normal ou se é provavelmente '
        'uma anomalia (veja a Figura 1.10). Uma tarefa muito semelhante é a <i>detecção de novidades</i>: '
        'ela visa detectar novas instâncias que pareçam diferentes de todas as instâncias no conjunto de '
        'treinamento. Isso requer um conjunto de treinamento muito “limpo”, desprovido de qualquer '
        'instância que você gostaria que o algoritmo detectasse. Por exemplo, se você tiver milhares de '
        'fotos de cachorros e 1% dessas fotos representar Chihuahuas, então um algoritmo de detecção de '
        'novidades não deve tratar novas fotos de Chihuahuas como novidades. Por outro lado, os algoritmos '
        'de detecção de anomalias podem considerar esses cães tão raros e tão diferentes de outros cães '
        'que provavelmente os classificariam como anomalias (sem ofensa aos chihuahuas).</p>')
st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_01/figura_10.png',
         caption='Figura 1-10. Detecção de anomalia.')
st.html('<p class="fonte_texto">Finalmente, outra tarefa não supervisionada comum é o <i>aprendizado de '
        'regras</i> de associação, em que o objetivo é investigar grandes quantidades de dados e descobrir '
        'relações interessantes entre atributos. Por exemplo, suponha que você possua um supermercado. '
        'Aplicar uma regra de associação em seus registros de vendas pode revelar que as pessoas que '
        'compram molho barbecue e batatas fritas também tendem a comprar bife. Portanto, você pode querer '
        'colocar esses itens próximos uns dos outros.</p>')
st.html('<p class="fonte_sub_subtitulo_aula"><b>Aprendizado semissupervisionado</b></p>')
st.html('<p class="fonte_texto">Como a rotulagem de dados geralmente é demorada e cara, muitas vezes você '
        'terá muitas instâncias não rotuladas e poucas instâncias rotuladas. Alguns algoritmos podem lidar '
        'com dados parcialmente rotulados. Isso é chamado de <i>aprendizado semissupervisionado</i> '
        '(Figura 1-11).</p>')
st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_01/figura_11.png',
         caption='Figura 1-11. Aprendizagem semissupervisionada com duas classes (triângulos e quadrados): '
                 'os exemplos não rotulados (círculos) ajudam a classificar uma nova instância (a cruz) '
                 'na classe triângulo em vez da classe quadrada, mesmo que esteja mais próxima dos '
                 'quadrados rotulados.')
st.html('<p class="fonte_texto">Alguns serviços de hospedagem de fotos, como o Google Fotos, são bons '
        'exemplos disso. Depois de enviar todas as fotos de sua família para o serviço, ele reconhece '
        'automaticamente que a mesma pessoa A aparece nas fotos 1, 5 e 11, enquanto outra pessoa B aparece '
        'nas fotos 2, 5 e 7. Esta é a parte não supervisionada do algoritmo (clusterização). Agora tudo o que '
        'o sistema precisa é que você diga quem são essas pessoas. Basta adicionar um rótulo por pessoa e '
        'ele poderá nomear todos em cada foto, o que é útil para pesquisar fotos.</p>')
st.html('<p class="fonte_texto">A maioria dos algoritmos de aprendizagem semissupervisionados são '
        'combinações de algoritmos não supervisionados e supervisionados. Por exemplo, '
        '<i>redes de crenças profundas</i> (DBNs) são baseadas em componentes não supervisionados '
        'chamados <i>máquinas de Boltzmann restritas</i> (RBMs) empilhados uns sobre os outros. Os '
        'RBMs são treinados sequencialmente de maneira não supervisionada e, em seguida, todo o sistema '
        'é ajustado usando técnicas de aprendizagem supervisionada.</p>')
st.html('<p class="fonte_sub_subtitulo_aula"><b>Aprendizado por reforço</b></p>')
st.html('<p class="fonte_texto"><i>Aprendizado por Reforço</i> é um bicho muito diferente. O sistema de '
        'aprendizagem, chamado de <i>agente</i> neste contexto, pode observar o ambiente, selecionar e '
        'executar '
        'ações e obter <i>recompensas</i> em troca (ou <i>penalidades</i> na forma de recompensas '
        'negativas, como mostrado na Figura 1-12). Deve então aprender por si mesmo qual é a melhor '
        'estratégia, chamada <i>política</i>, para obter a maior recompensa ao longo do tempo. Uma '
        'política define qual ação o agente deve escolher quando estiver em determinada situação.</p>')
st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_01/figura_12.png',
         caption='Figura 1-12. Aprendizado por reforço.')
st.html('<p class="fonte_texto">Por exemplo, muitos robôs implementam algoritmos de Aprendizagem por '
        'Reforço para aprender a andar. O programa AlphaGo da DeepMind também é um bom exemplo de '
        'Aprendizado por Reforço: ganhou as manchetes em maio de 2017, quando derrotou o campeão mundial '
        'Ke Jie no jogo Go. Aprendeu a sua política vencedora analisando milhões de jogos e depois jogando '
        'muitos jogos contra si mesmo. Observe que o aprendizado foi desligado durante os jogos contra o '
        'campeão; AlphaGo estava apenas aplicando a política que aprendeu.</p>')
st.html('<p class="fonte_subtitulo_aula"><b>Aprendizado online e em lote</b></p>')
st.html('<p class="fonte_texto">Outro critério usado para classificar sistemas de Aprendizado de Máquina '
        'é se o sistema pode ou não aprender de forma incremental a partir de um fluxo de dados '
        'recebidos.</p>')
st.html('<p class="fonte_sub_subtitulo_aula"><b>Aprendizado em lote</b></p>')
st.html('<p class="fonte_texto">No <i>aprendizado em lote</i>, o sistema é incapaz de aprender de forma '
        'incremental: ele deve ser treinado usando todos os dados disponíveis. Isso geralmente leva muito '
        'tempo e recursos de computação, por isso normalmente é feito offline. Primeiro o sistema é '
        'treinado e depois é lançado em produção e funciona sem mais aprendizado; apenas aplica o que '
        'aprendeu. Isso é chamado de <i>aprendizado offline</i>.</p>')
st.html('<p class="fonte_texto">Se você deseja que um sistema de aprendizagem em lote conheça novos dados '
        '(como um novo tipo de spam), você precisa treinar uma nova versão do sistema do zero no conjunto '
        'de dados completo (não apenas os novos dados, mas também os dados antigos) e, em seguida, '
        'interromper o sistema antigo e substituí-lo pelo novo.</p>')
st.html('<p class="fonte_texto">Felizmente, todo o processo de treinamento, avaliação e lançamento de um '
        'sistema de aprendizado de máquina pode ser automatizado com bastante facilidade (como mostrado '
        'na Figura 1-3), de modo que até mesmo um sistema de aprendizado em lote pode se adaptar às '
        'mudanças. Basta atualizar os dados e treinar uma nova versão do sistema do zero sempre que '
        'necessário.</p>')
st.html('<p class="fonte_texto">Essa solução é simples e geralmente funciona bem, mas o treinamento usando '
        'o conjunto completo de dados pode levar muitas horas, portanto, normalmente você treinaria um '
        'novo sistema apenas a cada 24 horas ou até mesmo semanalmente. Se o seu sistema precisa se adaptar '
        'a dados que mudam rapidamente (por exemplo, para prever preços de ações), então você precisa de '
        'uma solução mais reativa.</p>')
st.html('<p class="fonte_texto">Além disso, o treinamento no conjunto completo de dados requer muitos '
        'recursos de computação (CPU, espaço de memória, espaço em disco, E/S de disco, E/S de rede, '
        'etc.). Se você tiver muitos dados e automatizar seu sistema para treinar do zero todos os dias, '
        'isso acabará custando muito dinheiro. Se a quantidade de dados for enorme, pode até ser '
        'impossível usar um algoritmo de aprendizagem em lote.</p>')
st.html('<p class="fonte_texto">Finalmente, se o seu sistema precisa ser capaz de aprender de forma '
        'autônoma e possui recursos limitados (por exemplo, um aplicativo de smartphone ou um rover em '
        'Marte), transportar grandes quantidades de dados de treinamento e consumir muitos recursos para '
        'treinar durante horas todos os dias é um empecilho.</p>')
st.html('<p class="fonte_texto">Felizmente, a melhor opção em todos esses casos é usar algoritmos '
        'capazes de aprender de forma incremental.</p>')
st.html('<p class="fonte_sub_subtitulo_aula"><b>Aprendizado online</b></p>')
st.html('<p class="fonte_texto">No <i>aprendizado on-line</i>, você treina o sistema de forma incremental, '
        'alimentando-o com instâncias de dados sequencialmente, individualmente ou em pequenos grupos '
        'chamados <i>minilotes</i>. Cada etapa de aprendizagem é rápida e barata, de modo que o sistema '
        'pode aprender sobre novos dados dinamicamente, à medida que chegam (veja a Figura 1.13).</p>')
st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_01/figura_13.png',
         caption='Figura 1-13. No aprendizado online, um modelo é treinado e lançado em produção e, em '
                 'seguida, continua aprendendo à medida que novos dados chegam.')
st.html('<p class="fonte_texto">A aprendizagem online é excelente para sistemas que recebem dados como um '
        'fluxo contínuo (por exemplo, preços de ações) e precisam se adaptar às mudanças de forma rápida '
        'ou autônoma. Também é uma boa opção se você tiver recursos computacionais limitados: uma vez que '
        'um sistema de aprendizagem online tenha aprendido sobre novas instâncias de dados, ele não '
        'precisará mais delas, então você poderá descartá-las (a menos que queira reverter para um estado '
        'anterior e “reproduzir” os dados). Isso pode economizar uma enorme quantidade de espaço.</p>')
st.html('<p class="fonte_texto">Algoritmos de aprendizagem online também podem ser usados para treinar '
        'sistemas em enormes conjuntos de dados que não cabem na memória principal de uma máquina '
        '(isso é chamado de aprendizagem <i>out-of-core</i>). O algoritmo carrega parte dos dados, '
        'executa uma etapa de treinamento nesses dados e repete o processo até ter sido executado em '
        'todos os dados (veja a Figura 1.14).</p>')
st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_01/figura_14.png',
         caption='Figura 1-14. Utilizando aprendizado online para lidar com grandes conjuntos de dados.')
with st.expander('Alerta 1', icon='⚡'):
        st.html('<p class="fonte_texto">O aprendizado out-of-core geralmente é feito off-line (ou seja, '
                'não no sistema ao vivo), portanto, <i>aprendizado online</i> pode ser um nome confuso. '
                'Pense nisso como <i>aprendizado incremental</i>.</p>')
st.html('<p class="fonte_texto">Um parâmetro importante dos sistemas de aprendizagem online é a rapidez '
        'com que eles devem se adaptar às mudanças nos dados: isso é chamado de <i>taxa de '
        'aprendizagem</i>. Se você definir uma alta taxa de aprendizado, seu sistema se adaptará '
        'rapidamente aos novos dados, mas também tenderá a esquecer rapidamente os dados antigos (você '
        'não quer que um filtro de spam sinalize apenas os tipos de spam mais recentes que foram '
        'mostrados). Por outro lado, se você definir uma taxa de aprendizagem baixa, o sistema terá mais '
        'inércia; isto é, aprenderá mais lentamente, mas também será menos sensível ao ruído nos novos '
        'dados ou a sequências de pontos de dados não representativos (outliers).</p>')
st.html('<p class="fonte_texto">Um grande desafio da aprendizagem online é que, se dados incorretos forem '
        'alimentados no sistema, o desempenho do sistema diminuirá gradualmente. Se for um sistema ativo, '
        'seus clientes perceberão. Por exemplo, dados incorretos podem vir de um sensor com defeito em um '
        'robô ou de alguém enviando spam para um mecanismo de pesquisa para tentar obter uma classificação '
        'elevada nos resultados de pesquisa. Para reduzir esse risco, você precisa monitorar seu sistema '
        'de perto e desligar imediatamente o aprendizado (e possivelmente reverter para um estado de '
        'funcionamento anterior) se detectar uma queda no desempenho. Você também pode monitorar os dados '
        'de entrada e reagir a dados anormais (por exemplo, usando um algoritmo de detecção de '
        'anomalias).</p>')
st.html('<p class="fonte_subtitulo_aula"><b>Aprendizagem baseada em instância versus aprendizagem '
        'baseada em modelo</b></p>')
st.html('<p class="fonte_texto">Mais uma maneira de categorizar os sistemas de aprendizado de máquina é '
        'pela forma como eles <i>generalizam</i>. A maioria das tarefas de aprendizado de máquina trata '
        'de fazer previsões. Isto significa que, dados vários exemplos de treinamento, o sistema precisa '
        'ser capaz de fazer boas previsões (generalizar) para exemplos que nunca viu antes. Ter uma boa '
        'medida de desempenho nos dados de treinamento é bom, mas insuficiente; o verdadeiro objetivo é '
        'ter um bom desempenho em novas instâncias. Existem duas abordagens principais para generalização: '
        'aprendizagem baseada em instâncias e aprendizagem baseada em modelos.</p>')
st.html('<p class="fonte_sub_subtitulo_aula"><b>Aprendizagem baseada em instâncias</b></p>')
st.html('<p class="fonte_texto">Possivelmente a forma mais trivial de aprendizagem é simplesmente decorar. '
        'Se você criasse um filtro de spam dessa forma, ele apenas sinalizaria todos os e-mails idênticos '
        'aos e-mails que já foram sinalizados pelos usuários – o que não é a pior solução, mas certamente '
        'não é a melhor.</p>')
st.html('<p class="fonte_texto">Em vez de apenas sinalizar e-mails idênticos aos e-mails de spam '
        'conhecidos, seu filtro de spam pode ser programado para sinalizar também e-mails muito semelhantes '
        'aos e-mails de spam conhecidos. Isso requer uma <i>medida de semelhança</i> entre dois e-mails. '
        'Uma medida de semelhança (muito básica) entre dois e-mails poderia ser contar o número de palavras '
        'que eles têm em comum. O sistema sinalizaria um e-mail como spam se ele contivesse muitas palavras '
        'em comum com um e-mail de spam conhecido.</p>')
st.html('<p class="fonte_texto">Isso é chamado de <i>aprendizado baseado em instâncias</i>: o sistema '
        'aprende os exemplos de cor e depois generaliza para novos casos usando uma medida de similaridade '
        'para compará-los com os exemplos aprendidos (ou um subconjunto deles). Por exemplo, na Figura '
        '1.15 a nova instância seria classificada como um triângulo porque a maioria das instâncias mais '
        'semelhantes pertencem a essa classe.</p>')
st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_01/figura_15.png',
         caption='Figura 1-15. Aprendizado baseado em instância.')
st.html('<p class="fonte_sub_subtitulo_aula"><b>Aprendizagem baseada em modelo</b></p>')
st.html('<p class="fonte_texto">Outra forma de generalizar a partir de um conjunto de exemplos é construir '
        'um modelo desses exemplos e depois usar esse modelo para fazer previsões. Isso é chamado de '
        '<i>aprendizado baseado em modelo</i> (Figura 1-16).</p>')
st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_01/figura_16.png',
         caption='Figura 1-16. Aprendizado baseado em modelo.')
st.html('<p class="fonte_texto">Por exemplo, suponha que você queira saber se o dinheiro deixa as pessoas '
        'felizes, então você baixa os dados do Índice para uma Vida Melhor do site da <a '
        'href="https://data-explorer.oecd.org/vis?tenant=archive&df[ds]=DisseminateArchiveDMZ&df[id]=D'
        'F_BLI&df[ag]=OECD&dq=...&to[TIME]=false&vw=ov">OECD</a> e as '
        'estatísticas sobre o produto interno bruto (PIB) per capita do site do '
        '<a href="https://www.imf.org/en/Home">FMI</a>. Aí você junta '
        'as tabelas e classifica por PIB per capita. A tabela abaixo mostra um trecho do que você obtém.</p>')
tabela_1 = pd.DataFrame(
        {
                'País': ['Hungria', 'Coreia', 'França', 'Austrália', 'Estados Unidos'],
                'PIB per capita (USD)': ['12.240', '27.195', '37.675', '50.962', '55.805'],
                'Satisfação de vida': ['4,9', '5,8', '6,5', '7,3', '7,2']
        }
)
st.dataframe(tabela_1, hide_index=True)
st.html('<p class="fonte_texto">Vamos representar graficamente os dados para esses países '
        '(Figura 1-17).</p>')
st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_01/figura_17.png',
         caption='Figura 1-17. Você vê uma tendência aqui?')
st.html('<p class="fonte_texto">Parece haver uma tendência aqui! Embora os dados sejam <i>ruidosos</i> '
        '(ou seja, parcialmente aleatórios), parece que a satisfação com a vida aumenta de forma mais ou '
        'menos linear à medida que o PIB per capita do país aumenta. Então você decide modelar a '
        'satisfação com a vida como uma função linear do PIB per capita. Esta etapa é chamada de seleção '
        'de modelo: você selecionou um <i>modelo linear</i> de satisfação com a vida com apenas um '
        'atributo, PIB per capita. A equação abaixo mostra o cáculo deste modelo.</p>')
st.latex(r'satisfacao \, vida = \theta _{0} + \theta_{1} \times PIB \, per \, capita')
st.html('<p class="fonte_texto">Este modelo possui dois <i>parâmetros de modelo</i>, <b>θ0</b> e <b>θ1</b>. '
        'Ajustando esses parâmetros, você pode fazer com que seu modelo represente qualquer função linear, '
        'conforme mostrado na Figura 1.18.</p>')
st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_01/figura_18.png',
         caption='Figura 1-18. Alguns modelos lineares possíveis.')
st.html('<p class="fonte_texto">Antes de poder usar seu modelo, você precisa definir os valores dos '
        'parâmetros <b>θ0</b> e <b>θ1</b> . Como você pode saber quais valores farão com que seu modelo '
        'tenha o melhor desempenho? Para responder a esta pergunta, você precisa especificar uma medida '
        'de desempenho. Você pode definir uma <i>função de utilidade</i> (ou <i>função de aptidão</i>) '
        'que mede quão <i>bom</i> é seu modelo, ou pode definir uma <i>função de custo</i> que mede quão '
        '<i>ruim</i> ele é. Para problemas de regressão linear, as pessoas normalmente usam uma função de '
        'custo que mede a distância entre as previsões do modelo linear e os exemplos de treinamento; o '
        'objetivo é minimizar essa distância.</p>')
st.html('<p class="fonte_texto">É aqui que entra o algoritmo de regressão linear: você o alimenta com seus '
        'exemplos de treinamento e ele encontra os parâmetros que fazem o modelo linear se ajustar melhor '
        'aos seus dados. Isso é chamado de <i>treinamento</i> do modelo. No nosso caso, o algoritmo '
        'descobre que os valores ideais dos parâmetros são <b>θ0 = 4,85</b> e <b>θ1 = 4,91 × '
        '10&#8315;&#8309;</b>.</p>')
with st.expander('Alerta 2', icon='⚡'):
        st.html('<p class="fonte_texto">Confusamente, a mesma palavra “modelo” pode se referir a um '
                '<i>tipo de modelo</i> (por exemplo, Regressão Linear), a uma <i>arquitetura de modelo '
                'totalmente especificada</i> (por exemplo, Regressão Linear com uma entrada e uma saída), '
                'ou ao <i>modelo final treinado</i> pronto para ser usado para previsões (por exemplo, '
                'Regressão Linear com uma entrada e uma saída, usando <b>θ0 = 4,85</b> e <b>θ1 = 4,91 × '
                '10&#8315;&#8309;</b>). A seleção do modelo consiste em escolher o tipo de modelo e '
                'especificar completamente sua arquitetura. Treinar um modelo significa executar um '
                'algoritmo para encontrar os parâmetros do modelo que o ajustarão melhor aos dados de '
                'treinamento (e, esperançosamente, fará boas previsões sobre novos dados).</p>')
st.html('<p class="fonte_texto">Agora o modelo ajusta os dados de treinamento o mais próximo possível '
        '(para um modelo linear), como você pode ver na Figura 1.19.</p>')
st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_01/figura_19.png',
         caption='Figura 1-19. O modelo linear que melhor se ajusta aos dados de treinamento.')
st.html('<p class="fonte_texto">Você finalmente está pronto para executar o modelo para fazer previsões. '
        'Por exemplo, digamos que você queira saber até que ponto os cipriotas estão felizes e os dados da '
        'OECD não têm a resposta. Felizmente, você pode usar seu modelo para fazer uma boa previsão: '
        'você pesquisa o PIB per capita de Chipre, encontra US$ 22.587 e, em seguida, aplica seu modelo '
        'e descobre que a satisfação com a vida provavelmente estará em algum lugar em torno de '
        '<b>4,85 + 22.587 × 4,91 × 10&#8315;&#8309; = 5,96</b>.</p>')
st.html('<p class="fonte_texto">Para ter uma palinha do que veremos ao longo do nosso estudo, '
        'o código abaixo mostra o código Python que carrega os dados, os prepara, cria um gráfico de '
        'dispersão para visualização e, em seguida, treina um modelo linear e faz uma previsão.</p>')
st.code(r'''# --- Importar as bibliotecas --- #
import numpy as np
import pandas as pd
import sklearn.linear_model
import matplotlib.pyplot as plt

# --- Carregar os dados --- #
oecd = pd.read_csv('oecd_2024.csv', thousands=',')
pib = pd.read_csv(
        'pib_per_capita.csv',
        thousands=',',
        delimiter='\t',
        encoding='latin1',
        na_values='n/a'
)

# --- Preparar os dados --- #
estatisticas_paises = preparar_estatistica_paises(oecd, pib)
X = np.c_[estatisticas_paises['PIB per capita']]
y= np.c_[estatisticas_paises['Satisfação vida']]

# --- Visualizar os dados --- #
estatisticas_paises.plot(
        kind='scatter',
        x='PIB per capita',
        y='Satisfação vida'
)
plt.show()

# --- Criar o modelo --- #
modelo = sklearn.linear_model.LinearRegression()

# --- Treinar o modelo --- #
modelo.fit(X, y)

# --- Previsão para Chipre --- #
X_novo = [[22587]]  # PIB per capita do Chipre
print(modelo.predict(X_novo))  # saída: 5.96242338''', line_numbers=True)
with st.expander('Nota 2', icon='📝'):
        st.html('<p class="fonte_texto">Se, em vez disso, tivesse utilizado um algoritmo de aprendizagem '
                'baseado em instância, teríamos descoberto que a Eslovénia tem o PIB per capita mais '
                'próximo do de Chipre ($20.732) e, uma vez que os dados da OECD nos dizem que a '
                'satisfação com a vida dos eslovenos é de 5,7, teríamos previsto uma satisfação com a '
                'vida de 5,7 para Chipre. Se diminuir um pouco o zoom e olhar para os dois países mais '
                'próximos, encontrará Portugal e Espanha com satisfações de vida de 5,1 e 6,5, '
                'respetivamente. Fazendo a média desses três valores, você obtém 5,77, o que é bastante '
                'próximo da sua previsão baseada no modelo. Este algoritmo simples é chamado de regressão '
                '<i>k-Nearest Neighbors</i> (neste exemplo, k = 3).</p>')
        st.html('<p class="fonte_texto">Substituir o modelo de regressão linear pela regressão k-Nearest '
                'Neighbors no código anterior é tão simples quanto substituir estas duas linhas:</p>')
        st.code('''import sklearn.linear_model
modelo = sklearn.linar_model.LinearRgression()''', line_numbers=True)
        st.html('<p class="fonte_texto">por essas:</p>')
        st.code('''import sklearn.neighbors
modelo = sklearn.neighbors.KNeighborsRegressor(n_neighbors=3)''', line_numbers=True)
st.html('<p class="fonte_texto">Se tudo correr bem, seu modelo fará boas previsões. Caso contrário, pode '
        'ser necessário usar mais atributos (taxa de emprego, saúde, poluição do ar, etc.), obter mais '
        'dados de treinamento ou de melhor qualidade ou talvez selecionar um modelo mais poderoso (por '
        'exemplo, um modelo de regressão polinomial).</p>')
st.html('<p class="fonte_texto">Em resumo:</p>')
st.html('<ul class="fonte_texto">'
        '<li>Você estudou os dados.</li>'
        '<li>Você selecionou um modelo.</li>'
        '<li>Você o treinou nos dados de treinamento (ou seja, o algoritmo de aprendizado procurou os '
        'valores dos parâmetros do modelo que minimizam uma função de custo).</li>'
        '<li>Por fim, você aplicou o modelo para fazer previsões sobre novos casos (isso é chamado de '
        '<i>inferência</i>), esperando que esse modelo generalize bem.</li>'
        '</ul>')
st.html('<p class="fonte_texto">Esta é a aparência de um projeto típico de aprendizado de máquina. No '
        'Capítulo 2 você experimentará isso em primeira mão, percorrendo um projeto de ponta a ponta.</p>')
st.html('<p class="fonte_texto">Abordamos muito assunto até aqui: agora você sabe do que realmente se '
        'trata o Aprendizado de máquina, por que ele é útil, quais são algumas das categorias mais comuns de '
        'sistemas de AM e como é um fluxo de trabalho típico de projeto. Agora vamos ver o que pode dar '
        'errado no aprendizado e impedir que você faça previsões precisas.</p>')

# --- Principais desafios do aprendizado de máquina --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Principais desafios do aprendizado de máquina</h1>')
st.html('<p class="fonte_texto">Resumindo, como sua tarefa principal é selecionar um algoritmo de '
        'aprendizagem e treiná-lo com alguns dados, as duas coisas que podem dar errado são “algoritmo '
        'ruim” e “dados ruins”. Vamos começar com exemplos de dados incorretos.</p>')
st.html('<p class="fonte_subtitulo_aula"><b>Quantidade insuficiente de dados de treinamento</b></p>')
st.html('<p class="fonte_texto">Para que uma criança aprenda o que é uma maçã, basta apontar para uma '
        'maçã e dizer “maçã” (possivelmente repetindo este procedimento algumas vezes). Agora a criança '
        'é capaz de reconhecer maçãs de todos os tipos de cores e formatos. Gênio.</p>')
st.html('<p class="fonte_texto">O aprendizado de máquina ainda não chegou lá; são necessários muitos dados '
        'para que a maioria dos algoritmos de aprendizado de máquina funcionem corretamente. Mesmo para '
        'problemas muito simples você normalmente precisa de milhares de exemplos, e para problemas '
        'complexos como reconhecimento de imagem ou fala você pode precisar de milhões de exemplos (a '
        'menos que você possa reutilizar partes de um modelo existente).</p>')
with st.expander('A eficácia irracional dos dados'):
        st.html('<p class="fonte_texto">Num famoso <a href="https://dl.acm.org/doi/10.3115/1073012.1073017"'
                '>artigo</a> publicado em 2001, os investigadores da Microsoft Michele Banko e Eric Brill '
                'mostraram que algoritmos de aprendizagem automática muito diferentes, incluindo alguns '
                'bastante simples, tiveram um desempenho quase idêntico num problema complexo de '
                'desambiguação de linguagem natural, uma vez que receberam dados suficientes (como pode '
                'ver na Figura 1-20).</p>')
        st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_01/figura_20.png',
                 caption='Figura 1-20. A importância dos dados versus algoritmos.')
        st.html('<p class="fonte_texto">Como afirmam os autores, “estes resultados sugerem que podemos '
                'querer reconsiderar a compensação entre gastar tempo e dinheiro no desenvolvimento de '
                'algoritmos versus gastá-los no desenvolvimento de <i>corpus</i>”.</p>')
        st.html('<p class="fonte_texto">A ideia de que os dados são mais importantes do que os algoritmos '
                'para problemas complexos foi posteriormente popularizada por Peter Norvig et al. '
                'num artigo intitulado <a href="https://static.googleusercontent.com/media/research.'
                'google.com/pt-BR//pubs/archive/35179.pdf">The Unreasonable Effectiveness of Data</a>, '
                'publicado em 2009. Deve-se notar, no entanto, que conjuntos de dados de pequeno e médio '
                'porte ainda são muito comuns e nem sempre é fácil ou barato obter dados de treinamento '
                'extras, portanto, não abandone os algoritmos ainda.</p>')
st.html('<p class="fonte_subtitulo_aula"><b>Dados de treinamento não representativos</b></p>')
st.html('<p class="fonte_texto">Para generalizar bem, é crucial que os seus dados de treinamento sejam '
        'representativos dos novos casos para os quais você deseja generalizar. Isso é verdade quer você '
        'use aprendizado baseado em instâncias ou aprendizado baseado em modelo.</p>')
st.html('<p class="fonte_texto">Por exemplo, o conjunto de países que utilizámos anteriormente para treinar '
        'o modelo linear não era perfeitamente representativo; alguns países estavam faltando. A Figura '
        '1-21 mostra a aparência dos dados quando você adiciona os países ausentes.</p>')
st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_01/figura_21.png',
                 caption='Figura 1-21. Uma amostra de treinamento mais representativa.')
st.html('<p class="fonte_texto">Ao utilizar um conjunto de formação não representativo, treinámos um modelo '
        'que dificilmente fará previsões precisas, especialmente para países muito pobres e muito ricos.</p>')
st.html('<p class="fonte_texto">É crucial usar um conjunto de treinamento que seja representativo dos casos '
        'para os quais você deseja generalizar. Isso geralmente é mais difícil do que parece: se a amostra '
        'for muito pequena, você terá <i>ruído de amostragem</i> (ou seja, dados não representativos como '
        'resultado do acaso), mas mesmo amostras muito grandes podem ser não representativas se o método '
        'de amostragem for falho. Isso é chamado de <i>viés de amostragem</i>.</p>')
with st.expander('Exemplos de viés de amostragem'):
        st.html('<p class="fonte_texto">Talvez o exemplo mais famoso de parcialidade na amostragem tenha '
                'acontecido durante a eleição presidencial dos EUA em 1936, que colocou Landon contra '
                'Roosevelt: a <i>Literary Digest</i> realizou uma pesquisa muito grande, enviando '
                'correspondência para cerca de 10 milhões de pessoas. Obteve 2,4 milhões de respostas e '
                'previu com grande confiança que Landon obteria 57% dos votos. Em vez disso, Roosevelt '
                'venceu com 62% dos votos. A falha estava no método de amostragem do '
                '<i>Literary Digest</i>:</p>')
        st.html('<ul class="fonte_texto">'
                '<li>Primeiro, para obter os endereços para onde enviar as pesquisas, a <i>Literary '
                'Digest</i> usou listas telefônicas, listas de assinantes de revistas, listas de associados '
                'de clubes e assim por diante. Todas essas listas tendiam a favorecer as pessoas mais ricas, '
                'que tinham maior probabilidade de votar nos republicanos (daí Landon).</li>'
                '<li>Em segundo lugar, menos de 25% das pessoas entrevistadas responderam. Mais uma vez, '
                'isto introduziu um viés de amostragem, ao excluir potencialmente pessoas que não se '
                'importavam muito com política, pessoas que não gostavam do <i>Literary Digest</i> e '
                'outros grupos-chave. Este é um tipo especial de viés de amostragem denominado <i>viés de '
                'não resposta</i>.</li>'
                '</ul>')
        st.html('<p class="fonte_texto">Aqui está outro exemplo: digamos que você queira construir um '
                'sistema para reconhecer vídeos de música funk. Uma maneira de construir seu conjunto de '
                'treinamento é pesquisar <b>música funk</b> no YouTube e usar os vídeos resultantes. Mas isso '
                'pressupõe que o mecanismo de busca do YouTube retorne um conjunto de vídeos '
                'representativos de todos os videoclipes de funk do YouTube. Na realidade, os resultados '
                'da pesquisa provavelmente serão tendenciosos para artistas populares, já que no Brasil '
                'veremos muitos vídeos de <b>funk carioca</b>, que não se parecem em nada com James '
                'Brown. Por outro lado, de que outra forma você pode obter um grande conjunto de '
                'treinamento?</p>')
st.html('<p class="fonte_subtitulo_aula"><b>Dados de baixa qualidade</b></p>')
st.html('<p class="fonte_texto">Obviamente, se seus dados de treinamento estiverem cheios de erros, '
        'valores discrepantes e ruídos (por exemplo, devido a medições de baixa qualidade), será mais '
        'difícil para o sistema detectar os padrões subjacentes, portanto, será menos provável que seu '
        'sistema tenha um bom desempenho. Muitas vezes vale a pena gastar tempo limpando seus dados de '
        'treinamento. A verdade é que a maioria dos cientistas de dados passa uma parte significativa do '
        'seu tempo fazendo exatamente isso. A seguir estão alguns exemplos de quando você deseja limpar '
        'os dados de treinamento:</p>')
st.html('<ul class="fonte_texto">'
        '<li>Se algumas instâncias forem claramente discrepantes, pode ser útil simplesmente descartá-las '
        'ou tentar corrigir os erros manualmente.</li>'
        '<li>Se algumas instâncias estiverem faltando alguns recursos (por exemplo, 5% de seus clientes não '
        'especificaram sua idade), você deve decidir se deseja ignorar esse atributo completamente, '
        'ignorar essas instâncias, preencher os valores ausentes (por exemplo, com a idade média) ou '
        'treinar um modelo com o recurso e um modelo sem ele.</li>'
        '</ul>')
st.html('<p class="fonte_subtitulo_aula"><b>Características irrelevantes</b></p>')
st.html('<p class="fonte_texto">Como diz o ditado: entra lixo, sai lixo. Seu sistema só será capaz de '
        'aprender se os dados de treinamento contiverem recursos relevantes suficientes e não muitos '
        'irrelevantes. Uma parte crítica do sucesso de um projeto de aprendizado de máquina é criar um '
        'bom conjunto de recursos para treinar. Esse processo, chamado de <i>engenharia de características</i>, '
        'envolve as seguintes etapas:</p>')
st.html('<ul class="fonte_texto">'
        '<li>Seleção de recursos: seleção dos recursos mais úteis para treinar entre os recursos '
        'existentes.</li>'
        '<li>Extração de recursos: combinar recursos existentes para produzir um recurso mais útil, '
        'como vimos anteriormente, algoritmos de redução de dimensionalidade podem ajudar.</li>'
        '<li>Criação de novos recursos através da coleta de novos dados.</li>'
        '</ul>')
st.html('<p class="fonte_texto">Agora que vimos muitos exemplos de dados ruins, vejamos alguns exemplos '
        'de algoritmos ruins.</p>')
st.html('<p class="fonte_subtitulo_aula"><b>Overfitting dos dados de treinamento</b></p>')
st.html('<p class="fonte_texto">Digamos que você esteja visitando um país estrangeiro e o taxista o engane. '
        'Você pode ficar tentado a dizer que <i>todos</i> os motoristas de táxi naquele país são ladrões. '
        'Generalizar demais é algo que nós, humanos, fazemos com muita frequência e, infelizmente, as '
        'máquinas podem cair na mesma armadilha se não tomarmos cuidado. No Aprendizado de Máquina isso é '
        'chamado de <i>overfitting</i>: significa que o modelo tem um bom desempenho nos dados de '
        'treinamento, mas não generaliza bem.</p>')
st.html('<p class="fonte_texto">A Figura 1.22 mostra um exemplo de modelo polinomial de satisfação com a '
        'vida de alto grau que superajusta fortemente os dados de treinamento. Embora ele tenha um '
        'desempenho muito melhor nos dados de treinamento do que o modelo linear simples, você realmente '
        'confiaria em suas previsões?</p>')
st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_01/figura_22.png',
                 caption='Figura 1-22. Overfitting (sobreajustando) nos dados de treinamento.')
st.html('<p class="fonte_texto">Modelos complexos, como redes neurais profundas, podem detectar padrões '
        'sutis nos dados, mas se o conjunto de treinamento for ruidoso ou muito pequeno (o que introduz '
        'ruído de amostragem), é provável que o modelo detecte padrões no próprio ruído. Obviamente estes '
        'padrões não serão generalizados para novas instâncias. Por exemplo, digamos que você alimente '
        'seu modelo de satisfação com a vida com muitos mais atributos, incluindo atributos não '
        'informativos, como o nome do país. Nesse caso, um modelo complexo pode detectar padrões como o '
        'fato de todos os países nos dados de formação com um <b>U</b> no nome terem uma satisfação com a vida '
        'superior a 7: Noruega (7,4), Suécia (7,2) e Suíça (7,5). Quão confiante '
        'você está de que a regra da satisfação da letra <b>U</b> se generaliza para Ruanda ou Zimbábue? Obviamente esse '
        'padrão ocorreu nos dados de treinamento por puro acaso, mas o modelo não tem como dizer se um '
        'padrão é real ou simplesmente resultado de ruído nos dados.</p>')
with st.expander('Alerta 3', icon='⚡'):
        st.html('<p class="fonte_texto">O overfitting ocorre quando o modelo é muito complexo em relação à '
                'quantidade e ao ruído dos dados de treinamento. Aqui estão possíveis soluções:</p>')
        st.html('<ul class="fonte_texto">'
                '<li>Simplifique o modelo selecionando um com menos parâmetros (por exemplo, um modelo '
                'linear em vez de um modelo polinomial de alto grau), reduzindo o número de atributos nos '
                'dados de treinamento ou restringindo o modelo.</li>'
                '<li>Tenha mais dados de treinamento.</li>'
                '<li>Reduza o ruído nos dados de treinamento (por exemplo, corrija erros de dados e '
                'remova valores discrepantes).</li>'
                '</ul>')
st.html('<p class="fonte_texto">Restringir um modelo para torná-lo mais simples e reduzir o risco de '
        'overfitting é chamado de <i>regularização</i>. Por exemplo, o modelo linear que definimos '
        'anteriormente tem dois parâmetros, <b>θ0</b> e <b>θ1</b>. Isso dá ao algoritmo de aprendizagem '
        'dois <i>graus de liberdade</i> para adaptar o modelo aos dados de treinamento: ele pode ajustar '
        'a altura (<b>θ0</b>) e a inclinação (<b>θ1</b>) da linha. Se forçarmos <b>θ1 = 0</b>, o '
        'algoritmo teria apenas um grau de liberdade e teria muito mais dificuldade em ajustar os dados '
        'corretamente: tudo o que ele poderia fazer seria mover a linha para cima ou para baixo para '
        'chegar o mais próximo possível das instâncias de treinamento, de modo que terminaria próximo da '
        'média. Realmente um modelo muito simples! Se permitirmos que o algoritmo modifique <b>θ1</b> mas '
        'o forçarmos a mantê-lo pequeno, então o algoritmo de aprendizagem terá efetivamente algo entre '
        'um e dois graus de liberdade. Produzirá um modelo que é mais simples do que aquele com dois '
        'graus de liberdade, mas mais complexo do que aquele com apenas um. Você deseja encontrar o '
        'equilíbrio certo entre ajustar perfeitamente os dados de treinamento e manter o modelo simples '
        'o suficiente para garantir que ele será bem generalizado.</p>')
st.html('<p class="fonte_texto">A Figura 1-23 mostra três modelos. A linha pontilhada representa o modelo '
        'original que foi treinado nos países representados como círculos (sem os países representados '
        'como quadrados), a linha tracejada é o nosso segundo modelo treinado com todos os países '
        '(círculos e quadrados) e a linha sólida é um modelo treinado com os mesmos dados do primeiro '
        'modelo, mas com uma restrição de regularização. Você pode ver que a regularização forçou o '
        'modelo a ter uma inclinação menor: este modelo não se ajusta aos dados de treinamento (círculos) '
        'tão bem quanto o primeiro modelo, mas na verdade generaliza melhor para novos exemplos que não '
        'viu durante o treinamento (quadrados).</p>')
st.image('./assets/imagens/ia_scikit_learn_keras_tensorflow/aula_01/figura_23.png',
                 caption='Figura 1-23. A regularização reduz o risco de overfitting.')
st.html('<p class="fonte_texto">A quantidade de regularização a ser aplicada durante o aprendizado pode '
        'ser controlada por um <i>hiperparâmetro</i>. Um hiperparâmetro é um parâmetro de um algoritmo de '
        'aprendizagem (não do modelo). Como tal, não é afetado pelo próprio algoritmo de aprendizagem; '
        'deve ser definido antes do treino e permanece constante durante o treino. Se você definir o '
        'hiperparâmetro de regularização para um valor muito grande, obterá um modelo quase plano (uma '
        'inclinação próxima de zero); o algoritmo de aprendizagem quase certamente não ajustará demais '
        'os dados de treinamento, mas será menos provável que encontre uma boa solução. Ajustar '
        'hiperparâmetros é uma parte importante da construção de um sistema de aprendizado de máquina '
        '(você verá um exemplo detalhado no próximo capítulo).</p>')
st.html('<p class="fonte_subtitulo_aula"><b>Underfitting os dados de treinamento</b></p>')
st.html('<p class="fonte_texto">Como você pode imaginar, <i>underfitting</i> é o oposto de overfitting: '
        'ocorre quando seu modelo é simples demais para aprender a estrutura subjacente dos dados. '
        'Por exemplo, um modelo linear de satisfação com a vida tende a ser inadequado; a realidade '
        'é apenas mais complexa que o modelo, portanto suas previsões serão imprecisas, mesmo nos '
        'exemplos de treinamento.</p>')
st.html('<p class="fonte_texto">Aqui estão as principais opções para corrigir esse problema:</p>')
st.html('<ul class="fonte_texto">'
        '<li>Selecione um modelo mais poderoso, com mais parâmetros.</li>'
        '<li>Alimente com melhores características o algoritmo de aprendizagem (engenharia '
        'de features).</li>'
        '<li>Reduza as restrições do modelo (por exemplo, reduza o hiperparâmetro de regularização).</li>'
        '</ul>')
st.html('<p class="fonte_subtitulo_aula"><b>Recapitulando</b></p>')
st.html('<p class="fonte_texto">Agora você já sabe muito sobre aprendizado de máquina. No entanto, '
        'passamos por tantos conceitos que você pode estar se sentindo um pouco perdido, então vamos '
        'dar um passo atrás e ter uma visão geral:</p>')
st.html('<ul class="fonte_texto">'
        '<li>O aprendizado de máquina consiste em fazer com que as máquinas melhorem em alguma tarefa, '
        'aprendendo com os dados, em vez de ter que codificar regras explicitamente.</li>'
        '<li>Existem muitos tipos diferentes de sistemas de AM: supervisionados ou não, em lote ou '
        'online, baseados em instâncias ou baseados em modelo.</li>'
        '<li>Em um projeto de AM, você coleta dados em um conjunto de treinamento e alimenta o conjunto '
        'de treinamento em um algoritmo de aprendizado. Se o algoritmo for baseado em modelo, ele ajusta '
        'alguns parâmetros para ajustar o modelo ao conjunto de treinamento (ou seja, para fazer boas '
        'previsões no próprio conjunto de treinamento) e, então, esperançosamente, será capaz de fazer '
        'boas previsões também em novos casos. Se o algoritmo for baseado em instâncias, ele apenas '
        'aprende os exemplos de cor e generaliza para novas instâncias usando uma medida de similaridade '
        'para compará-los com as instâncias aprendidas.</li>'
        '<li>O sistema não terá um bom desempenho se o seu conjunto de treinamento for muito pequeno, ou se '
        'os dados não forem representativos, tiverem ruído ou estiverem poluídos com recursos irrelevantes '
        '(entra lixo, sai lixo). Por último, seu modelo não precisa ser nem muito simples, nesse caso, terá '
        'underfitting (subajustado) nem muito complexo, nesse caso, terá overfitting (superajustado).</li>'
        '</ul>')
st.html('<p class="fonte_texto">Há apenas um último tópico importante a abordar: depois de treinar um '
        'modelo, você não quer apenas “esperar” que ele se generalize para novos casos. Você deseja '
        'avaliá-lo e ajustá-lo, se necessário. Vejamos como fazer isso.</p>')

# --- Testando e validando --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Testando e validando</h1>')
st.html('<p class="fonte_texto">A única maneira de saber até que ponto um modelo irá generalizar para '
        'novos casos é experimentá-lo em novos casos. Uma maneira de fazer isso é colocar seu modelo em '
        'produção e monitorar seu desempenho. Isso funciona bem, mas se o seu modelo for terrivelmente '
        'ruim, seus usuários reclamarão; o que não é a melhor ideia.</p>')
st.html('<p class="fonte_texto">Uma opção melhor é dividir seus dados em dois conjuntos: o <i>conjunto de '
        'treinamento</i> e o <i>conjunto de teste</i>. Como esses nomes indicam, você treina seu modelo '
        'usando o conjunto de treinamento e testa-o usando o conjunto de teste. A taxa de erro em novos '
        'casos é chamada de <i>erro de generalização</i> (ou <i>erro fora da amostra</i>) e, ao avaliar '
        'seu modelo no conjunto de testes, você obtém uma estimativa desse erro. Este valor informa o '
        'desempenho do seu modelo em instâncias nunca vistas antes.</p>')
st.html('<p class="fonte_texto">Se o erro de treinamento for baixo (ou seja, seu modelo comete poucos '
        'erros no conjunto de treinamento), mas o erro de generalização for alto, significa que seu '
        'modelo está fazendo overfitting (superajustando) os dados de treinamento.</p>')
with st.expander('Dica 3', icon='💡'):
        st.html('<p class="fonte_texto">É comum usar 80% dos dados para treinamento e <i>reservar</i> 20% '
                'para testes. No entanto, isso depende do tamanho do conjunto de dados: se ele contiver '
                '10 milhões de instâncias, separar 1% significa que seu conjunto de teste conterá 100.000 '
                'instâncias, provavelmente mais do que suficiente para obter uma boa estimativa do erro '
                'de generalização.</p>')
st.html('<p class="fonte_subtitulo_aula"><b>Ajuste de hiperparâmetros e seleção de modelo</b></p>')
st.html('<p class="fonte_texto">Avaliar um modelo é bastante simples: basta usar um conjunto de testes. '
        'Mas suponha que você esteja hesitando entre dois tipos de modelos (digamos, um modelo linear e '
        'um modelo polinomial): como você pode decidir entre eles? Uma opção é treinar ambos e comparar o '
        'quão bem eles generalizam usando o conjunto de testes.</p>')
st.html('<p class="fonte_texto">Agora suponha que o modelo linear generalize melhor, mas você deseja '
        'aplicar alguma regularização para evitar ajuste excessivo. A questão é: como você escolhe o '
        'valor do hiperparâmetro de regularização? Uma opção é treinar 100 modelos diferentes usando 100 '
        'valores diferentes para este hiperparâmetro. Suponha que você encontre o melhor valor do '
        'hiperparâmetro que produz um modelo com o menor erro de generalização, digamos, apenas 5% de '
        'erro. Você lança este modelo em produção, mas infelizmente ele não funciona tão bem quanto o '
        'esperado e produz 15% de erros. O que aconteceu?</p>')
st.html('<p class="fonte_texto">O problema é que você mediu o erro de generalização diversas vezes no '
        'conjunto de teste e adaptou o modelo e os hiperparâmetros para produzir o melhor modelo <i>para '
        'aquele conjunto específico</i>. Isso significa que é improvável que o modelo tenha um desempenho '
        'tão bom com novos dados.</p>')
st.html('<p class="fonte_texto">Uma solução comum para esse problema é chamada de <i>conjunto de '
        'validação</i>: você simplesmente separa parte do conjunto de treinamento para avaliar vários '
        'modelos candidatos e selecionar o melhor. O novo conjunto retido é chamado de <i>conjunto de '
        'validação</i> (ou às vezes <i>conjunto de desenvolvimento</i> ou <i>dev set</i>). Mais '
        'especificamente, você treina vários modelos com vários hiperparâmetros '
        'no conjunto de treinamento reduzido (ou seja, o conjunto de treinamento completo menos o conjunto '
        'de validação) e seleciona o modelo com melhor desempenho no conjunto de validação. Após esse '
        'processo de validação, você treina o melhor modelo no conjunto de treinamento '
        'completo (incluindo o conjunto de validação), e isso lhe dá o modelo final. Por último, você '
        'avalia este modelo final no conjunto de testes para obter uma estimativa do erro de '
        'generalização.</p>')
st.html('<p class="fonte_texto">Esta solução geralmente funciona muito bem. No entanto, se o conjunto '
        'de validação for muito pequeno, as avaliações do modelo serão imprecisas: você poderá acabar '
        'selecionando um modelo abaixo do ideal por engano. Por outro lado, se o conjunto de validação '
        'for muito grande, o conjunto de treinamento restante será muito menor que o conjunto de '
        'treinamento completo. Por que isso é ruim? Bem, como o modelo final será treinado no conjunto '
        'de treinamento completo, não é ideal comparar modelos candidatos treinados em um conjunto de '
        'treinamento muito menor. Seria como selecionar o velocista mais rápido para participar de uma '
        'maratona. Uma maneira de resolver esse problema é realizar <i>validações cruzadas</i> repetidas, '
        'usando muitos pequenos conjuntos de validação. Cada modelo é avaliado uma vez por conjunto de '
        'validação após ser treinado no restante dos dados. Ao calcular a média de todas as avaliações '
        'de um modelo, você obtém uma medida muito mais precisa de seu desempenho. Porém, há uma '
        'desvantagem: o tempo de treinamento é multiplicado pelo número de conjuntos de validação.</p>')
st.html('<p class="fonte_subtitulo_aula"><b>Incompatibilidade de dados</b></p>')
st.html('<p class="fonte_texto">Em alguns casos, é fácil obter uma grande quantidade de dados para '
        'treinamento, mas esses dados provavelmente não serão perfeitamente representativos dos dados '
        'que serão usados na produção. Por exemplo, suponha que você queira criar um aplicativo '
        'mobile para tirar fotos de flores e determinar automaticamente suas espécies. Você pode facilmente '
        'baixar milhões de fotos de flores na web, mas elas não serão perfeitamente representativas das '
        'fotos que serão realmente tiradas usando o aplicativo em um dispositivo mobile. Talvez você tenha '
        'apenas 10.000 fotos representativas (ou seja, tiradas com o aplicativo). Nesse caso, a regra '
        'mais importante a lembrar é que o conjunto de validação e o conjunto de teste devem ser tão '
        'representativos quanto possível dos dados que você espera usar na produção, portanto, devem ser '
        'compostos exclusivamente por imagens representativas: você pode embaralhá-los e colocar metade '
        'no conjunto de validação e metade no conjunto de teste (certificando-se de que nenhuma duplicata '
        'ou quase-duplicata acabe em ambos os conjuntos). Mas depois de treinar seu modelo nas imagens da '
        'web, se você observar que o desempenho do modelo no conjunto de validação é decepcionante, você '
        'não saberá se isso ocorre porque seu modelo se ajustou demais ao conjunto de treinamento ou se '
        'isso se deve apenas à incompatibilidade entre as imagens da web e as imagens do aplicativo '
        'mobile. Uma solução é exibir algumas das imagens de treinamento (da web) em outro conjunto que '
        'Andrew Ng chama de <i>conjunto train-dev</i>. Depois que o modelo for treinado (no conjunto '
        'de treinamento, <i>não</i> no conjunto train-dev), você poderá avaliá-lo no conjunto train-dev. '
        'Se tiver um bom desempenho, o modelo não está superajustando o conjunto de treinamento. Se o '
        'desempenho for insatisfatório no conjunto de validação, o problema deve ser proveniente da '
        'incompatibilidade de dados. Você pode tentar resolver esse problema pré-processando as imagens '
        'da web para torná-las mais parecidas com as fotos que serão tiradas pelo aplicativo mobile e, em '
        'seguida, treinando novamente o modelo. Por outro lado, se o modelo tiver um desempenho ruim no '
        'conjunto train-dev, então ele deve ter se ajustado demais ao conjunto de treinamento, portanto, '
        'você deve tentar simplificar ou regularizar o modelo, obter mais dados de treinamento e limpar '
        'os dados de treinamento.</p>')
with st.expander('Teorema do No Free Lunch'):
        st.html('<p class="fonte_texto">Um modelo é uma versão simplificada das observações. As '
                'simplificações destinam-se a descartar os detalhes supérfluos que provavelmente não '
                'serão generalizados para novas instâncias. Para decidir quais dados descartar e quais '
                'manter, você deve fazer <i>suposições</i>. Por exemplo, um modelo linear pressupõe que '
                'os dados são fundamentalmente lineares e que a distância entre as instâncias e a linha '
                'reta é apenas ruído, que pode ser ignorado com segurança.</p>')
        st.html('<p class="fonte_texto">Num famoso <a href="https://direct.mit.edu/neco/article-abstract/'
                '8/7/1341/6016/The-Lack-of-A-Priori-Distinctions-Between-Learning">artigo</a> de 1996, '
                'David Wolpert demonstrou que se não fizermos absolutamente '
                'nenhuma suposição sobre os dados, então não há razão para preferir um modelo a qualquer '
                'outro. Isso é chamado de teorema <i>No Free Lunch</i> (NFL). Para alguns conjuntos de '
                'dados o melhor modelo é um modelo linear, enquanto para outros conjuntos de dados é uma '
                'rede neural. Não existe nenhum modelo que <i>a priori</i> garanta que funcione melhor '
                '(daí o nome do teorema). A única maneira de saber com certeza qual modelo é o melhor é '
                'avaliando todos eles. Como isso não é possível, na prática você faz algumas suposições '
                'razoáveis sobre os dados e avalia apenas alguns modelos razoáveis. Por exemplo, '
                'para tarefas simples você pode avaliar modelos lineares com vários níveis de '
                'regularização, e para um problema complexo você pode avaliar várias redes neurais.</p>')
