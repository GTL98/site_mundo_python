# --- Importar as bibliotecas --- #
from PIL import Image
import streamlit as st

# --- Configurações iniciais da página --- #
st.set_page_config(
    page_title='Capítulo 01 - Introdução à redes neurais',
    page_icon=Image.open('./assets/logo/logo.png'),
    layout='wide'
)

# --- Carregar o estilo das fontes --- #
with open('./assets/css/style.css', 'r') as css:
    st.html(f'<style>{css.read()}</style>')

# --- Colocar o banner do capítulo --- #
st.image('./assets/imagens/redes_neurais_zero/aula_01/aula_01.png')

# --- Introdução --- #
st.html('<h1 class="fonte_titulo_aula">Introdução</h1>')
st.html('<p class="fonte_texto">Começamos com uma ideia geral do que são <b>redes neurais</b> e por que você '
        'pode estar interessado nelas. As redes neurais, também chamadas de <b>Redes Neurais '
        'Artificiais</b> (embora pareça que nos últimos anos tenhamos abandonado a parte “artificial”), são '
        'um tipo de aprendizado de máquina frequentemente confundido com aprendizado profundo. A '
        'característica definidora de uma rede neural <i>profunda</i> é ter duas ou mais <b>camadas '
        'ocultas</b> — um conceito que será explicado em breve, mas essas camadas ocultas são aquelas que '
        'a rede neural controla. É razoavelmente seguro dizer que a maioria das redes neurais em uso são '
        'uma forma de aprendizagem profunda.</p>')
st.image('./assets/imagens/redes_neurais_zero/aula_01/figura_01.png',
         caption='Figura 1-1. Representando os vários campos da inteligência artificial e onde eles se '
                 'enquadram em geral.')

# --- Uma breve história --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Uma breve história</h1>')
st.html('<p class="fonte_texto">Desde o advento dos computadores, os cientistas têm formulado maneiras de '
        'permitir que as máquinas recebam informações e produzam os resultados desejados para tarefas como '
        '<b>classificação</b> e <b>regressão</b>. Além disso, em geral, há aprendizado de máquina '
        '<b>supervisionado</b> e <b>não supervisionado</b>. O aprendizado de máquina supervisionado é usado '
        'quando você tem dados pré-estabelecidos e rotulados que podem ser usados para treinamento. '
        'Digamos que você tenha dados de sensor para um servidor com métricas como taxas de '
        'upload/download, temperatura e umidade, tudo organizado por horário a cada 10 minutos. '
        'Normalmente, este servidor opera conforme planejado e não apresenta interrupções, mas às vezes '
        'algumas peças falham e causam interrupções. Podemos coletar dados e depois dividi-los em duas '
        'classes: uma classe para horários/observações quando o servidor está operando normalmente e '
        'outra classe para horários/observações quando o servidor está sofrendo uma interrupção. Quando '
        'o servidor está falhando, queremos rotular os dados do sensor que levaram à falha como dados que '
        'precederam a falha. Quando o servidor está operando normalmente, simplesmente rotulamos esses '
        'dados como “normais”.</p>')
st.html('<p class="fonte_texto">O que cada sensor mede neste exemplo é chamado de <i>feature</i> '
        '(recuros/característica). Um grupo de '
        'recursos constitui um conjunto de recursos (representado como vetores/arrays), e os valores de '
        'um conjunto de recursos podem ser chamados de amostra. As amostras são alimentadas em modelos de '
        'redes neurais para treiná-las para ajustar as saídas desejadas dessas entradas ou para prever com '
        'base nelas durante a fase de inferência.</p>')
st.html('<p class="fonte_texto">Os rótulos “normal” e “falha” são <b>classificações</b> ou <b>rótulos</b>. '
        'Você também pode vê-los chamados de <b>alvos</b> ou <b>verdades básicas</b> enquanto ajustamos um '
        'algoritmo de aprendizado de máquina. Esses alvos são as classificações que são o <i>objetivo</i> '
        'ou <i>alvo</i>, conhecido como <i>verdadeiro</i> e <i>correto</i>, para o algoritmo aprender. '
        'Para este exemplo, o objetivo é eventualmente treinar um algoritmo para ler os dados do sensor e '
        'prever com precisão quando uma falha é iminente. Este é apenas um exemplo de aprendizagem '
        'supervisionada na forma de classificação. Além da classificação, há também a regressão, que serve '
        'para prever valores numéricos, como preços de ações. Há também o aprendizado de máquina não '
        'supervisionado, onde a máquina encontra estrutura nos dados sem conhecer os rótulos/classes com '
        'antecedência. Existem conceitos adicionais (por exemplo, aprendizado por reforço e aprendizado '
        'de máquina semissupervisionado) que se enquadram nas redes neurais. E nosso estudo, focaremos na '
        'classificação e regressão com redes neurais, mas o que abordamos aqui leva a outros casos de '
        'uso.</p>')
st.html('<p class="fonte_texto">As redes neurais foram concebidas na década de 1940, mas descobrir como '
        'treiná-las permaneceu um mistério durante 20 anos. O conceito de <b>retropropagação</b> (explicado '
        'mais tarde) surgiu na década de 1960, mas as redes neurais ainda não receberam muita atenção até '
        'começarem a vencer competições em 2010. Desde então, as redes neurais tiveram uma ascensão '
        'meteórica devido à sua capacidade às vezes aparentemente mágica de resolver problemas '
        'anteriormente considerados insolúveis, como legendagem de imagens, tradução de idiomas, síntese '
        'de áudio e vídeo e muito mais.</p>')
st.html('<p class="fonte_texto">Atualmente, as redes neurais são a principal solução para a maioria das '
        'competições e problemas tecnológicos desafiadores, como carros autônomos, cálculo de riscos, '
        'detecção de fraudes e detecção precoce de câncer, para citar alguns.</p>')

# --- O que é uma rede neural? --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">O que é uma rede neural?</h1>')
st.html('<p class="fonte_texto">As redes neurais “artificiais” são inspiradas no cérebro orgânico, '
        'traduzidas para o computador. Não é uma comparação perfeita, mas existem neurônios, ativações '
        'e muita interconectividade, mesmo que os processos subjacentes sejam bem diferentes.</p>')
st.image('./assets/imagens/redes_neurais_zero/aula_01/figura_02.png',
         caption='Figura 1-2. Comparando um neurônio biológico com um neurônio artificial.')
st.html('<p class="fonte_texto">Um único neurônio por si só é relativamente inútil, mas, quando combinado '
        'com centenas ou milhares (ou muitos mais) de outros neurônios, a interconectividade produz '
        'relações e resultados que frequentemente superam qualquer outro método de aprendizado de '
        'máquina.</p>')
st.image('./assets/imagens/redes_neurais_zero/aula_01/figura_03.png',
         caption='Figura 1-3. Exemplo de rede neural com 3 camadas ocultas de 16 neurônios cada.')
with st.expander('Animação da Figura 1-3'):
        st.video('https://www.youtube.com/watch?v=Ls1dJqZtI7w')
st.html('<p class="fonte_texto">A animação acima mostra os exemplos das estruturas do modelo e o número de '
        'parâmetros que o modelo precisa aprender a ajustar para produzir os resultados desejados. Os '
        'detalhes do que é visto aqui serão assuntos de capítulos futuros.</p>')
st.html('<p class="fonte_texto">Pode parecer um tanto complicado quando você olha dessa maneira. As redes '
        'neurais são consideradas “caixas pretas”, pois muitas vezes não temos ideia de por que elas '
        'chegam às conclusões que chegam. Nós entendemos <i>como</i> eles fazem isso, no entanto.</p>')
st.html('<p class="fonte_texto">Camadas densas, as camadas mais comuns, consistem em neurônios '
        'interconectados. Em uma camada densa, cada neurônio de uma determinada camada está conectado a '
        'todos os neurônios da próxima camada, o que significa que seu valor de saída se torna uma '
        'entrada para os próximos neurônios. Cada conexão entre neurônios tem um peso associado a ela, '
        'que é um fator treinável de quanto dessa entrada deve ser usada, e esse peso é multiplicado '
        'pelo valor da entrada. Depois que todos os <i>pesos de entrada</i> fluem para nosso neurônio, '
        'eles são somados e um viés, outro parâmetro treinável, é adicionado. O objetivo do viés é '
        'compensar o resultado positiva ou negativamente, o que pode nos ajudar ainda mais a mapear mais '
        'tipos de dados dinâmicos do mundo real. No capítulo 4, mostraremos alguns exemplos de como isso '
        'funciona.</p>')
st.html('<p class="fonte_texto">O conceito de pesos e vieses pode ser pensado como “botões” que podemos '
        'ajustar nosso modelo aos dados. Em uma rede neural, muitas vezes temos milhares ou '
        'até milhões desses parâmetros ajustados pelo otimizador durante o treinamento. Alguns podem '
        'perguntar: “por que não ter apenas vieses ou apenas pesos?” Vieses e pesos são parâmetros '
        'ajustáveis e impactarão as saídas dos neurônios, mas o fazem de maneiras diferentes. '
        'Como os pesos são multiplicados, eles apenas alterarão a magnitude ou até mesmo inverterão '
        'completamente o sinal de positivo para negativo, ou vice-versa. <i>Saída = peso·entrada+viés</i> '
        'não é diferente da equação para uma reta <i>y = ax+b</i>. Podemos visualizar isso com:</p>')
st.image('./assets/imagens/redes_neurais_zero/aula_01/figura_04.png',
         caption='Figura 1-4. Gráfico da saída de um neurônio de entrada única com peso 1, '
                 'viés 0 e entrada x.')
st.html('<p class="fonte_texto">Ajustar o peso terá impacto na inclinação da função:</p>')
st.image('./assets/imagens/redes_neurais_zero/aula_01/figura_05.png',
         caption='Figura 1-5. Gráfico da saída de um neurônio de entrada única com peso 2, '
                 'viés 0 e entrada x.')
st.html('<p class="fonte_texto">À medida que aumentamos o valor do peso, a inclinação fica mais acentuada. '
        'Se diminuirmos o peso, a inclinação diminuirá. Se o peso for negativo, a inclinação se torna '
        'negativa:</p>')
st.image('./assets/imagens/redes_neurais_zero/aula_01/figura_06.png',
         caption='Figura 1-6. Gráfico da saída de um neurônio de entrada única com peso -0.70 '
                 'viés 0 e entrada x.')
st.html('<p class="fonte_texto">Isso deve lhe dar uma ideia de como o peso afeta o valor de saída do '
        'neurônio que obtemos das <i>entradas·pesos+viés</i>. Agora, que tal o parâmetro do viés? O '
        'viés compensa a função geral. Por exemplo, com um peso de 1 e um viés de 2:</p>')
st.image('./assets/imagens/redes_neurais_zero/aula_01/figura_07.png',
         caption='Figura 1-7. Gráfico da saída de um neurônio de entrada única com peso 1 '
                 'viés 2 e entrada x.')
st.html('<p class="fonte_texto">À medida que aumentamos o viés, a saída geral da função se desloca para '
        'cima. Se diminuirmos o viés, a saída geral da função diminuirá. Por exemplo, com um viés '
        'negativo:</p>')
st.image('./assets/imagens/redes_neurais_zero/aula_01/figura_08.png',
         caption='Figura 1-8. Gráfico da saída de um neurônio de entrada única com peso 1 '
                 'viés -0.70 e entrada x.')
with st.expander('Animação das figuras 1-4 a 1-8'):
        st.video('https://www.youtube.com/watch?v=SRAFVJ5UbB0')
st.html('<p class="fonte_texto">Como você pode ver, os pesos e os vieses ajudam a impactar as saídas '
        'dos neurônios, mas fazem isso de maneiras ligeiramente diferentes. Isso fará ainda mais sentido '
        'quando abordarmos as <b>funções de ativação</b> no capítulo 4. Ainda assim, esperamos que você '
        'já possa ver as diferenças entre pesos e vieses e como eles podem ajudar individualmente a '
        'influenciar a saída. Por que isso é importante e será abordado em breve.</p>')
st.html('<p class="fonte_texto">Como uma visão geral, a função de degrau pretendia imitar um neurônio no '
        'cérebro, “disparando” ou não, como um botão liga-desliga. Na programação, um botão liga-desliga '
        'como função seria chamado de <b>função de passo</b> porque parece um passo se o representarmos '
        'graficamente.</p>')
st.image('./assets/imagens/redes_neurais_zero/aula_01/figura_09.png',
         caption='Figura 1-9. Gráfico da função de passo.')
st.html('<p class="fonte_texto">Para uma função degrau, se o valor de saída do neurônio, que é calculado '
        'por <i>soma(entradas · pesos) + viés</i>, for maior que 0, o neurônio dispara (portanto, '
        'geraria 1). Caso contrário, ele não dispara e passaria um 0. A fórmula para um único neurônio '
        'poderia ser algo como:</p>')
st.code('saida = sum(entradas * pesos) + vies', line_numbers=True)
st.html('<p class="fonte_texto">Geralmente aplicamos uma função de ativação a esta saída, chamada por '
        '<b>ativacao()</b>:</p>')
st.code('saida = ativacao(saida)', line_numbers=True)
st.html('<p class="fonte_texto">Embora você possa usar uma função de passo para sua função de ativação, '
        'tendemos a usar algo um pouco mais avançado. As redes neurais de hoje tendem a usar funções de '
        'ativação mais informativas (em vez de uma função degrau), como a função de ativação <b><i>Rectified '
        'Linear</i></b> (ReLU), que abordaremos em profundidade no Capítulo 4. A saída de cada neurônio pode '
        'fazer parte da camada de saída final, bem como a entrada para outra camada de neurônios. Embora '
        'a função completa de uma rede neural possa ser muito grande, vamos começar com um exemplo simples '
        'com 2 camadas ocultas de 4 neurônios cada.</p>')
st.image('./assets/imagens/redes_neurais_zero/aula_01/figura_10.png',
         caption='Figura 1-10. Exemplo básico de uma rede neural.')
st.html('<p class="fonte_texto">Junto com essas 2 camadas ocultas, há também mais duas camadas aqui, as '
        'camadas de entrada e saída. A camada de entrada representa seus dados de entrada reais, por '
        'exemplo, valores de pixel de uma imagem ou dados de um sensor de temperatura. Embora esses dados '
        'possam ser “brutos” na forma exata em que foram coletados, normalmente você <b>pré-processará</b> '
        'seus dados por meio de funções como <b>normalização</b> e <b>escalonamento</b>, e sua entrada '
        'precisa estar no '
        'formato numérico. Conceitos como escalonamento e normalização serão abordados '
        'posteriormente em nosso estudo. No entanto, é comum pré-processar dados mantendo seus recursos e '
        'tendo os valores em intervalos semelhantes entre 0 e 1 ou -1 e 1. Para conseguir isso, você '
        'usará uma ou ambas as funções de escala e normalização. A camada de saída é tudo o que a rede '
        'neural retorna. Com a classificação, onde pretendemos prever a classe da entrada, a camada de '
        'saída geralmente possui tantos neurônios quanto o conjunto de dados de treinamento possui classes, '
        'mas também pode ter um único neurônio de saída para classificação binária (duas classes). '
        'Discutiremos esse tipo de modelo posteriormente e, por enquanto, focaremos em um classificador '
        'que usa um neurônio de saída separado para cada classe. Por exemplo, se nosso objetivo é '
        'classificar uma coleção de imagens como “cachorro” ou “gato”, então existem duas classes no total. '
        'Isso significa que nossa camada de saída consistirá de dois neurônios; um neurônio associado a '
        '“cachorro” e outro a “gato”. Você também pode ter apenas um único neurônio de saída que seja '
        '“cachorro” ou “não cachorro”.</p>')
st.image('./assets/imagens/redes_neurais_zero/aula_01/figura_11.png',
         caption='Figura 1-11. Representação visual da passagem de dados de imagem por uma rede '
                 'neural, obtendo uma classificação.')
st.html('<p class="fonte_texto">Para cada imagem passada por esta rede neural, a saída final terá um valor '
        'calculado no neurônio de saída “gato” e um valor calculado no neurônio de saída “cachorro”. O '
        'neurônio de saída que recebeu a pontuação mais alta torna-se a predição de classe para a imagem '
        'usada como entrada.</p>')
st.image('./assets/imagens/redes_neurais_zero/aula_01/figura_12.png',
         caption='Figura 1-12. Representação visual da passagem de dados de imagem por uma rede '
                 'neural, obtendo uma classificação.')
with st.expander('Animações das figura 1-11 e 1-12'):
        st.video('https://www.youtube.com/watch?v=fXSRfzhHPm0')
st.html('<p class="fonte_texto">O que faz as redes neurais parecerem desafiadoras é a matemática envolvida '
        'e o quão assustadora às vezes pode parecer. Por exemplo, vamos imaginar uma rede neural e fazer '
        'uma viagem pelo que está acontecendo durante uma simples transmissão de dados e a matemática '
        'por trás disso. As redes neurais são, na verdade, apenas um monte de equações matemáticas que '
        'nós, programadores, podemos transformar em código. Para isso, não se preocupe em entender tudo. '
        'A ideia aqui é dar a você uma impressão de alto nível do que está acontecendo em geral. Então, '
        'o objetivo deste estudo é dividir cada um desses elementos em explicações dolorosamente simples, '
        'que cobrirão os passos para frente e para trás envolvidos no treinamento de redes neurais.'
        'Quando representado como uma função gigante, um exemplo de passagem direta de uma rede neural seria '
        'calculado com:</p>')
st.image('./assets/imagens/redes_neurais_zero/aula_01/figura_13.png',
         caption='Figura 1-13. Fórmula completa para a passagem direta de um modelo de rede neural '
                 'de exemplo.')
with st.expander('Animações das figura 1-13'):
        st.video('https://www.youtube.com/watch?v=xtzVuln1PV8')
st.html('<p class="fonte_texto">Naturalmente, isso parece extremamente confuso, e o que foi dito acima '
        'é, na verdade, a parte fácil das redes neurais. Isso afasta as pessoas, compreensivelmente. '
        'Em nosso estudo, entretanto, codificaremos tudo do zero e, ao fazer isso, você descobrirá que não '
        'há nenhuma etapa no caminho para produzir a função acima que seja muito difícil de entender. '
        'Por exemplo, a função acima também pode ser representada em funções Python aninhadas como:</p>')
st.code('''perda = -np.log(
        np.sum(
                y * np.exp(
                        np.dot(
                                np.maximum(
                                        0, np.dot(
                                                np.maximum(
                                                        0, np.dot(
                                                                X, p_1.T
                                                        ) + v_1),
                                                p_2.T) + v_2),
                                p_3.T) + v_3) / 
                np.sum(
                        np.exp(
                                np.dot(
                                        np.maximum(
                                                0, np.dot(
                                                        np.maximum(
                                                                0, np.dot(
                                                                        X, p_1.T
                                                                ) + v_1),
                                                        p_2.T) + v_2),
                                        p_3.T) + v_3),
                        axis=1,
                        keepdims=True
                )
        )
)''', line_numbers=True)
st.html('<p class="fonte_texto">Pode haver algumas funções que você ainda não entende. Por exemplo, talvez '
        'você não saiba o que é uma função de log, mas isso é algo simples que abordaremos. Então temos '
        'uma operação de soma, uma operação de exponenciação (novamente, você pode não saber exatamente o '
        'que isso faz, mas não é nada difícil). Depois temos um produto escalar, que ainda é apenas uma '
        'questão de entender como funciona, não há nada que passe pela sua cabeça se você souber como '
        'funciona a multiplicação! Finalmente, temos algumas transposições, anotadas como .T, que, '
        'novamente, uma vez que você aprende o que essa operação faz, não é um conceito desafiador. '
        'Depois de separarmos cada um desses elementos, aprendendo o que eles fazem e como funcionam, '
        'de repente, as coisas não parecerão tão assustadoras ou estranhas. Nada neste avanço requer '
        'educação além da álgebra básica do ensino médio! Para uma animação que retrata como tudo isso '
        'funciona em Python, você pode conferir a animação a seguir, mas certamente não é esperado que '
        'você entenda imediatamente o que está acontecendo. A questão é que esse tema aparentemente '
        'complexo pode ser dividido em partes pequenas e fáceis de entender, que é o objetivo dos próximos '
        'capítulos!</p>')
with st.expander('Animação do código'):
        st.video('https://www.youtube.com/watch?v=-6mZWjIEkDc')
st.html('<p class="fonte_texto">Uma rede neural típica tem milhares ou até milhões de <b>parâmetros</b> '
        'ajustáveis (pesos e vieses). Dessa forma, as redes neurais atuam como funções '
        'enormes com um grande número de <b>parâmetros</b>. O conceito de uma função longa com milhões '
        'de variáveis que poderiam ser usadas para resolver um problema não é tão difícil. Com '
        'tantas variáveis relacionadas aos neurônios, dispostas como camadas interconectadas, '
        'podemos imaginar que existem algumas combinações de valores para essas variáveis que produzirão '
        'os resultados desejados. Encontrar essa combinação de valores de parâmetros (peso e vieses) '
        'é a parte desafiadora.</p>')
st.html('<p class="fonte_texto">O objetivo final das redes neurais é ajustar seus pesos e vieses (os '
        'parâmetros), de modo que, quando aplicados a um exemplo ainda não visto na entrada, produzam a '
        'saída desejada. Quando algoritmos de aprendizado de máquina supervisionado são treinados, '
        'mostramos exemplos de entradas do algoritmo e suas saídas desejadas associadas. Um grande '
        'problema com esse conceito é o <b>overfitting<b>, quando o algoritmo apenas aprende a ajustar '
        'os dados de treinamento, mas na verdade não “entende” nada sobre as dependências subjacentes de '
        'entrada-saída. A rede basicamente apenas “memoriza” os dados de treinamento.</p>')
st.html('<p class="fonte_texto">Assim, tendemos a usar dados “dentro da amostra” para treinar um modelo e '
        'depois usar dados “fora da amostra” para validar um algoritmo (ou um modelo de rede neural em '
        'nosso caso). Certas porcentagens são reservadas para ambos os conjuntos de dados particionarem '
        'os dados. Por exemplo, se houver um conjunto de dados de 100.000 amostras de dados e rótulos, '
        'você pegará imediatamente 10.000 e as reservará para serem seus dados “fora da amostra” ou de '
        '“validação”. Em seguida, você treinará seu modelo com os outros 90.000 dados dentro da amostra '
        'ou de “treinamento” e, finalmente, validará seu modelo com os 10.000 dados fora da amostra que '
        'o modelo ainda não viu. O objetivo é que o modelo não apenas preveja com precisão os dados de '
        'treinamento, mas também seja igualmente preciso ao prever os dados de validação fora da amostra '
        'retidos.</p>')
st.html('<p class="fonte_texto">Isso é chamado de <b>generalização</b>, o que significa aprender a ajustar '
        'os dados em vez de memorizá-los. A ideia é “treinar” (ajustando lentamente pesos e vieses) uma '
        'rede neural em muitos exemplos de dados. Em seguida, pegamos dados fora da amostra que a rede '
        'neural nunca foi apresentada e esperamos que ela também possa prever com precisão esses dados.</p>')
st.html('<p class="fonte_texto">Agora você deve ter uma compreensão geral do que são redes neurais, ou pelo '
        'menos qual é o objetivo, e como planejamos alcançá-lo. Para treinar essas redes neurais, '
        'calculamos o quão “erradas” elas estão usando algoritmos para calcular o erro (chamado '
        '<b>perda</b>) e tentamos ajustar lentamente seus parâmetros (pesos e vieses) para que, ao longo '
        'de muitas iterações, a rede gradualmente se torne menos errada. O objetivo de todas as redes '
        'neurais é generalizar, o que significa que a rede pode ver muitos exemplos de dados nunca antes '
        'vistos e produzir com precisão os valores que esperamos alcançar. As redes neurais podem ser '
        'usadas para mais do que apenas classificação. Elas podem realizar regressão (prever um valor '
        'escalar, singular), clustering (atribuir dados não estruturados em grupos) e muitas outras '
        'tarefas. A classificação é apenas uma tarefa comum para redes neurais.</p>')