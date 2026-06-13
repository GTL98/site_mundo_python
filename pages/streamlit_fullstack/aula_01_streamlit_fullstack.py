# --- Importar as bibliotecas --- #
from PIL import Image
import streamlit as st

# --- Configurações iniciais da página --- #
st.set_page_config(
    page_title='Streamlit Fullstack - Aula 01',
    page_icon=Image.open('./assets/logo/logo.png'),
    layout='wide'
)

# --- Carregar o estilo das fontes --- #
with open('./assets/css/style.css', 'r') as css:
    st.html(f'<style>{css.read()}</style>')

# --- Colocar o título da aula --- #
st.html('<h1 class="fonte_titulo_aula">Aula 01: Widgets, Layout e Persistência!</h1>')

# --- Vídeo --- #
with st.expander('Se quiser acompanhar com o vídeo, acesse aqui! 👇'):
    st.video('https://youtu.be/ZPSdj4b7wsc')

# --- Código da aula --- #
st.subheader('Se quiser acessar o código completo da aula, clique [aqui](https://github.com/GTL98/canal_mundo_python/blob/main/Streamlit%20Full-Stack%3A%20Crie%20Aplica%C3%A7%C3%B5es%20Web%20Completas%20com%20Python/Aula%2001/aula_01.py)')
st.divider()

# --- Introdução --- #
st.subheader('E fala, devs! Tudo bem com vocês? Espero que sim!')
st.html('<h1 class="fonte_titulo_aula">Introdução</h1>')
st.html('''<p class="fonte_texto">Projetar aplicações web interativas e painéis de dados robustos em 
Python exige o domínio de ferramentas que eliminem a complexidade tradicional do desenvolvimento frontend 
(como HTML, CSS e JavaScript), permitindo focar estritamente na lógica de negócios e no fluxo de dados. 
O Streamlit consolidou-se como o principal framework para esse propósito devido à sua simplicidade e 
reatividade nativa. Este capítulo aborda desde a fundação arquitetural do framework (o modelo de 
reexecução linear) até a implementação de componentes visuais avançados e sistemas de persistência de 
estado de duas vias diretamente na URL do navegador. Ao longo desta aula, aprenderemos a estruturar 
interfaces dinâmicas, validar entradas de dados temporais e criar aplicações compartilháveis com estados 
altamente consistentes.</p>''')
st.subheader('Então sem mais delongas, bora para a aula!')
st.divider()

# --- O Paradigma da Reexecução Linear e Hierarquia Visual --- #
st.html('<h1 class="fonte_titulo_aula">O Paradigma da Reexecução Linear e Hierarquia Visual</h1>')
st.html('''<p class="fonte_texto">A base de qualquer aplicação desenvolvida em Streamlit é o seu modelo 
de execução sequencial de cima para baixo (<i>top-down</i>). Para compreender como os dados fluem pela 
interface, o primeiro passo consiste em configurar a estrutura básica de cabeçalhos e entender o 
comportamento do servidor toda vez que o usuário interage com os elementos gráficos dispostos na 
tela:</p>''')
st.code("""# --- Importar as bibliotecas --- #
import datetime
import streamlit as st

# --- Condifurações de layout da página --- #
st.set_page_config(layout='wide')

# --- Inicialização da hierarquia visual da aplicação --- #
st.title('Sistema de Gestão de Missões e Dados 🚀')
st.header('Módulo de Controle e Entrega de Parâmetros')
st.subheader('Configuração de Variáveis de Operação')
st.write('Este ambiente de controle utiliza a arquitetura de reexecução linear do Streamlit. '
         'Cada interação com os widgets abaixo desencadeia uma atualização do estado global, '
         'garantindo que a visualização reflita os dados em tempo real.')

# --- Linha de divisão --- #
st.divider()""")
st.html('''<p class="fonte_texto">Este bloco de código inicial estabelece a identidade visual e o ponto 
de partida do fluxo operacional da página, em que os componentes são renderizados de forma sequencial, 
seguindo estritamente a ordem de declaração no código Python. O título principal é gerado através do 
comando <span class='texto_python'>st.title</span>, que estabelece a maior hierarquia visual da interface, 
sendo seguido pelos cabeçalhos de níveis secundário e terciário organizados pelos comandos 
<span class='texto_python'>st.header</span> e <span class='texto_python'>st.subheader</span>, os quais 
definem divisões lógicas claras para guiar a leitura do usuário. O método 
<span class='texto_python'>st.write</span> atua como um formatador genérico altamente flexível, capaz 
de renderizar desde textos puros e marcações Markdown até objetos de dados complexos. Para concluir o 
layout básico e delimitar visualmente a área de cabeçalho estrutural das seções subsequentes de entrada de 
dados, o comando <span class='texto_python'>st.divider</span> insere uma linha divisória horizontal sutil 
de forma limpa.</p>''')
st.html('''<p class="fonte_texto">Toda vez que um usuário interage com qualquer seletor ou campo de 
entrada na página, o Streamlit encerra o processo de execução atual e reinicia o script Python por 
completo, da primeira à última linha. Matematicamente, a interface gerada <i>I</i> pode ser descrita 
como o produto de uma função global de renderização <i>R</i> aplicada ao conjunto de dados de estado 
dos componentes ativos <i>S</i>:</p>''')
st.latex('I=R(S)')
st.html('''<p class="fonte_texto">Sempre que um elemento <i>S</i> é modificado para um novo valor 
<i>v</i>, o interpretador avalia todo o pipeline novamente de forma síncrona:</p>''')
st.latex(r'I_{\text{novo}}=R(\{s_1,s_2,\dots,s_i=v,\dots,s_n\})')
st.html('''<p class="fonte_texto">Esse modelo garante que a tela sempre reflita com fidelidade o estado 
atual das variáveis na memória, eliminando a necessidade de escrever rotinas complexas de escuta de 
eventos (<i>event listeners</i>) e atualizações parciais manuais dos elementos da página.</p>''')
st.divider()

# --- Entrada Primitiva de Dados: Processamento de Textos e Variáveis Numéricas --- #
st.html('<h1 class="fonte_titulo_aula">Entrada Primitiva de Dados: Processamento de Textos e '
        'Variáveis Numéricas</h1>')
st.html('''<p class="fonte_texto">A captura de informações primárias do usuário inicia-se com componentes 
capazes de processar dados do tipo string e valores numéricos inteiros ou de ponto flutuante, aplicando 
restrições automáticas e validações de segurança diretamente no lado do cliente:</p>''')
st.code('''# --- Entrada de texto --- #
nome_operacao = st.text_input(
    label='Nome da operação de campo:',
    placeholder='Digite o codinome da missão...',
    key='entrada_nome_operacao',
    help='Este nome será usado para gerar os relatórios automáticos.'
)

# --- Entrada numérica com validação de limites --- #
capacidade_equipe = st.number_input(
    label='Capacidade total da equipe (membros):',
    min_value=1,
    max_value=50,
    value=5,
    step=1,
    key='entrada_capacidade_equipe'
)

# --- Escrever a saída --- #
st.write(f'Operação **{nome_operacao}** configurada para **{capacidade_equipe}** integrantes.')''', line_numbers=True)
st.html('''<p class="fonte_texto">Ao executar este bloco de código, o Streamlit renderiza campos de 
entrada robustos que realizam a validação automatizada de tipos de dados diretamente no navegador do 
usuário. O componente de entrada de texto, inicializado por 
<span class='texto_python'>st.text_input</span>, captura sequências curtas de caracteres de linha única. 
Ele utiliza um texto indicativo cinza definido no parâmetro 
<span class='texto_python'>placeholder</span> para orientar a digitação do usuário enquanto o campo 
estiver vazio, além de incorporar uma dica de contexto por meio do parâmetro 
<span class='texto_python'>help</span>, que renderiza um pequeno ícone flutuante de interrogação 
contendo explicações adicionais que aparecem quando o cursor é posicionado sobre o componente.</p>''')
st.html('''<p class="fonte_texto">Para o recebimento de valores inteiros, o widget 
<span class='texto_python'>st.number_input</span> assegura que apenas números válidos entrem no pipeline 
da aplicação. As restrições de limites são aplicadas de forma rígida através de 
<span class='texto_python'>min_value</span> e <span class='texto_python'>max_value</span>, impedindo 
que o usuário envie números fora do intervalo estipulado. O incremento numérico é ditado pelo 
parâmetro <span class='texto_python'>step</span>, que define o valor adicionado ou subtraído a cada 
clique nos botões laterais de controle, enquanto o parâmetro 
<span class='texto_python'>value</span> determina o valor que preenche o campo no primeiro carregamento 
do script.</p>''')
st.html('''<p class="fonte_texto">Ambos os elementos contam com o parâmetro 
<span class='texto_python'>key</span>, que associa uma string identificadora exclusiva ao widget. 
Essa chave é fundamental para estabilizar a identidade do componente durante os ciclos de reexecução 
linear do script, assegurando que o texto digitado ou a capacidade da equipe selecionada permaneçam 
preservados na memória e acessíveis dentro do dicionário global de estados de sessão da aplicação.</p>''')
st.divider()

# --- Seleções Clássicas e Customizáveis: Estilo com Markdown e Novas Opções Dinâmicas --- #
st.html('<h1 class="fonte_titulo_aula">Seleções Clássicas e Customizáveis: Estilo com Markdown e '
        'Novas Opções Dinâmicas</h1>')
st.html('''<p class="fonte_texto">A tomada de decisão por parte do usuário pode ser guiada por botões 
de seleção exclusiva (<i>radio</i>) ou caixas de seleção suspensas (<i>dropdown</i>), que ganharam 
recursos modernos para renderização estética e criação flexível de opções em tempo de execução:</p>''')
st.code('''# --- Adicionar seleções tradicionais aprimoradas --- #
st.subheader('Parâmetros de Comunicação e Prioridade')

# --- st.radio() com captions (legendas) e suporte a Markdown --- #
canal_comunicacao = st.radio(
    label='Canal de comunicação preferencial:',
    options=['**Base Aérea**', '**Quartel**', '**Base Médica**', '**Torpedeiro**'],
    captions=['*Brig. Dantas*', '*Gen. Afonso*', '*Dr. Clóvis*', '*Alm. Peixoto*'],
    index=0,
    horizontal=True,
    key='radio_comunicacao'
)

# --- st.selection() com placeholder e entrada de novas opções --- #
prioridade_missao = st.selectbox(
    label='Nível de prioridade da missão:',
    options=['Baixa', 'Média', 'Alta'],
    index=None,
    placeholder='Selecione a prioridade...',
    accept_new_options=True,
    key='selecao_prioridade'
)

# --- Escrever a saída --- #
st.write(f'Canal: **{canal_comunicacao}** | Prioridade: **{prioridade_missao}**')''', line_numbers=True)
st.html('''<p class="fonte_texto">Este bloco de código eleva o nível de design e flexibilidade da 
interface ao utilizar recursos avançados de formatação estética e digitação assistida. O componente 
clássico de botões de <i>radio</i>, <span class='texto_python'>st.radio</span>, é configurado 
horizontalmente para otimizar o uso do espaço físico de tela e conta com suporte nativo para decorações 
em Markdown em suas opções, permitindo aplicar negritos diretamente nos rótulos de texto. O grande 
diferencial dessa implementação é o parâmetro <span class='texto_python'>captions</span>, que aceita 
um iterável de strings auxiliares renderizadas imediatamente abaixo de cada botão correspondente, 
fornecendo legendas contextuais em estilo itálico que descrevem os líderes associados a cada canal 
de comunicação e auxiliam na tomada de decisão.</p>''')
st.html('''<p class="fonte_texto">Complementando as opções de escolha, o menu suspenso 
<span class='texto_python'>st.selectbox</span> é configurado para inicializar sem uma pré-seleção ao 
definir o índice inicial como nulo, o que exibe o texto instrutivo de reserva na tela. O destaque 
técnico deste widget é a ativação do parâmetro <span class='texto_python'>accept_new_options</span>, 
que transforma o menu tradicional em um campo de seleção dinâmico. Ao habilitar essa funcionalidade, o 
usuário ganha a liberdade de digitar um termo inédito na caixa de busca e inseri-lo no fluxo de execução 
ao pressionar a tecla ENTER.</p>''')
st.html('''<p class="fonte_texto">O sistema realiza uma correspondência de busca aproximada contra a 
lista pré-existente e, caso não localize o termo, aceita e retorna a string digitada diretamente pelo 
usuário, sem que seja necessário cadastrar a opção estaticamente no código-fonte. O texto de ajuda no 
marcador de posição adapta-se de maneira inteligente, exibindo instruções claras para escolher ou 
adicionar novas opções conforme a disponibilidade do componente.</p>''')
st.divider()

# --- O Novo Padrão de Design: Navegação Limpa com Pills e Segmented Control --- #
st.html('<h1 class="fonte_titulo_aula">O Novo Padrão de Design: Navegação Limpa com Pills e '
        'Segmented Control</h1>')
st.html('''<p class="fonte_texto">Para reduzir a quantidade de espaço em branco (<i>whitespace</i>) 
e criar layouts visuais compactos, foram integrados os seletores segmentados e de pílulas. Estes 
elementos de alta fidelidade visual substituem listas verticais longas por blocos horizontais 
interativos de clique rápido:</p>''')
st.code('''# --- Seleção moderna utilizando st.pills() e st.segmented_control() --- #
st.subheader('Configurações Avançadas de Seleção')

# --- Uso de st.pills() para seleção de status --- #
status_missao = st.pills(
    label='Status atual do projeto:',
    options=['Planejamento', 'Execução', 'Concluído', 'Arquivado'],
    selection_mode='single',
    default='Planejamento',
    key='pills_status'
)

# --- Uso de st.segmented_control() para múltiplos filtros --- #
setores_afetados = st.segmented_control(
    label='Setores de impacto direto:',
    options=['Adiministrativo', 'Arsenal', 'Suprimentos', 'Logística'],
    selection_mode='multi',
    default='Logística',
    width='stretch',
    key='segment_setores'
)

# --- Escrever a saída --- #
st.write(f'A missão está em fase de **{status_missao}** impactando: **{", ".join(setores_afetados)}**')''', line_numbers=True)
st.html('''<p class="fonte_texto">Esses novos seletores oferecem padrões de navegação modernos e 
dinâmicos que organizam as escolhas de forma compacta e reduzem significativamente a poluição visual 
na interface. O componente <span class='texto_python'>st.pills</span> dispõe as opções horizontalmente 
na forma de pequenos blocos arredondados isolados, sendo amplamente indicado para a seleção de status 
operacionais ou etiquetas rápidas de classificação. Configurado no modo de seleção única, ele se 
comporta de maneira semelhante a um grupo de botões de <i>radio</i> tradicionais, retornando o valor 
do bloco clicado ou um valor nulo caso nenhuma opção seja marcada.</p>''')
st.html('''<p class="fonte_texto">Por outro lado, o widget 
<span class='texto_python'>st.segmented_control</span> agrupa as opções em uma barra linear contígua 
de segmentos, funcionando de maneira equivalente a um interruptor físico segmentado. Ao definir seu 
modo de seleção como múltiplo, o controle aceita que o usuário marque e desmarque múltiplos segmentos 
simultaneamente, retornando uma lista de strings correspondente a todas as opções ativas.</p>''')
st.html('''<p class="fonte_texto">Uma característica de design avançada do controle de segmentos é o 
uso do parâmetro de largura definido como esticável (<span class='texto_python'>width=</span>
<span class='variaveis'>'stretch'</span>), que força o componente a se expandir de forma 
elástica até preencher toda a largura do contêiner onde está inserido. Isso garante um alinhamento 
perfeito e uniforme dos blocos com os demais elementos da página, preenchendo o espaço de forma 
equilibrada.</p>''')
st.divider()

# --- Domínio Temporal: Agendamento de Data e Hora Unificado --- #
st.html('<h1 class="fonte_titulo_aula">Domínio Temporal: Agendamento de Data e Hora Unificado</h1>')
st.html('''<p class="fonte_texto">O tratamento de variáveis temporais exige cuidado redobrado no 
desenvolvimento de interfaces interativas para evitar reinicializações desnecessárias do interpretador 
e problemas de consistência de datas:</p>''')
st.code('''# --- Controle de cronograma com widgets temporais --- #
st.subheader('Agendamento Cronológico')

# --- st.date_input() --- #
data_inicio = st.date_input(
    label='Data de mobilização:',
    value=datetime.date.today(),
    format='DD/MM/YYYY',
    key='data_mobilizacao'
)

# --- st.datetime_input() --- #
data_hora_limite = st.datetime_input(
    label='Data e hora limite para reporte:',
    value='now',  # inicialização com o momento atual
    step=datetime.timedelta(minutes=15),
    key='datetime_limite',
    help='Define o prazo final para a submissão do relatório.'
)

# --- Escrever a saída --- #
st.write(f'Início: {data_inicio} | Prazo final: {data_hora_limite}')''', line_numbers=True)
st.html('''<p class="fonte_texto">A evolução dos componentes temporais do Streamlit resolveu uma 
limitação histórica de performance e usabilidade que afetava o desenvolvimento de formulários e 
dashboards. Tradicionalmente, para capturar uma data e um horário específicos, o desenvolvedor 
precisava posicionar um seletor de data e um seletor de hora de forma consecutiva. Esse arranjo gerava 
o incômodo efeito de reexecução dupla, no qual o script Python era reiniciado por completo uma vez 
quando o usuário escolhia a data e uma segunda vez quando ele ajustava as horas, consumindo 
processamento e gerando lentidão no carregamento.</p>''')
st.html('''<p class="fonte_texto">O novo componente unificado de data e hora, chamado 
<span class='texto_python'>st.datetime_input</span>, soluciona essa ineficiência ao permitir a 
seleção conjunta e atômica de ambas as variáveis em uma única etapa e sob uma única reexecução linear 
do interpretador. No código apresentado, o seletor simples de datas, 
<span class='texto_python'>st.date_input</span>, lida exclusivamente com valores diários e exibe o 
calendário formatado no padrão brasileiro através do parâmetro 
<span class='texto_python'>format</span>, muito embora armazene e manipule os dados internamente 
como objetos padrão de data no Python.</p>''')
st.html('''<p class="fonte_texto">O seletor completo, 
<span class='texto_python'>st.datetime_input</span>, é inicializado de forma dinâmica com o carimbo 
de tempo atual do servidor por meio da string <span class='variaveis'>'now'</span>. Ele utiliza um 
controle de incremento configurado via objeto de intervalo de tempo para ditar saltos precisos de 15 
minutos no ajuste de horário no lado visual, oferecendo um controle robusto e refinado para 
cronogramas operacionais sem sobrecarregar a execução do sistema.</p>''')
st.divider()

# --- Persistência de Estado e Compartilhabilidade via URL --- #
st.html('<h1 class="fonte_titulo_aula">Persistência de Estado e Compartilhabilidade via URL</h1>')
st.html('''<p class="fonte_texto">Um dos maiores desafios no desenvolvimento de dashboards de dados 
é a compartilhabilidade de relatórios. Se um analista aplica uma série de filtros em uma página e 
envia o link para um colega, a outra pessoa normalmente abre o painel redefinido para as configurações 
padrão. A introdução da sincronização de parâmetros na URL via <i>binding</i> resolve esse problema de 
forma nativa e automática:</p>''')
st.code('''# --- Implementação de widget binding para persistência via URL --- #
st.subheader('Persistência e Compartilhamento')

# --- Widget vinculado aos parâmetros da URL --- #
regiao_foco = st.pills(
    label='Região de monitoramento (sincronizada):',
    options=['Fronteira', 'Deserto', 'Floresta', 'Costa'],
    key='regiao_foco',
    bind='query-params'
)

# --- Escrever a saída --- #
st.write(f'Você está monitorando a região: **{regiao_foco}**')''', line_numbers=True)
st.html('''<p class="fonte_texto">A vinculação de parâmetros de consulta à URL do navegador introduz 
um mecanismo nativo de sincronização bidirecional que transforma a forma como compartilhamos o estado 
das aplicações web. Ao declarar o parâmetro <span class='texto_python'>bind=</span>
<span class='variaveis'>'query-params'</span>, o Streamlit passa a monitorar e atualizar a barra de 
endereços do navegador de maneira totalmente automatizada. Assim que o usuário clica em uma pílula ou 
altera a seleção do widget integrado, a escolha é imediatamente convertida em um parâmetro de busca 
visível na barra de endereços. Isso garante que, se a página for recarregada ou se o link for enviado 
para outro usuário, o Streamlit interceptará esses parâmetros na inicialização do script e aplicará os 
valores correspondentes como estados iniciais de cada widget respectivo.</p>''')
st.html('''<p class="fonte_texto">Essa vinculação exige obrigatoriamente a declaração de uma chave de 
identificação única no widget, a qual será empregada diretamente como o nome do parâmetro exposto na 
URL. Para garantir que os links permaneçam limpos e legíveis, o framework remove automaticamente os 
parâmetros da URL caso as seleções retornem aos seus valores padrões de inicialização.</p>''')
st.html('''<p class="fonte_texto">Adicionalmente, aplica-se uma regra rígida de proteção de estado que 
proíbe o desenvolvedor de alterar ou remover os parâmetros da URL de forma direta por meio do objeto 
de manipulação de parâmetros. Qualquer alteração programática intencional (como limpar filtros através 
de um botão de reinicialização) deve ser realizada exclusivamente por meio da modificação direta do 
valor correspondente no dicionário de estados de sessão da aplicação, o qual se propaga de forma segura 
e consistente para os componentes visuais e para a URL na próxima reexecução linear do script.</p>''')
st.divider()

# --- Resumo --- #
st.html('<h1 class="fonte_titulo_aula">Resumo</h1>')
st.html('''<p class="fonte_texto">Esta aula forneceu um guia didático e completo sobre as 
inovações que amadureceram o ecossistema do Streamlit para o desenvolvimento de aplicações analíticas 
de alta performance. Iniciamos nossa exploração pela arquitetura de reexecução linear, compreendendo 
como cada interação do usuário dispara uma reexecução sequencial do código para manter a tela sempre 
atualizada de forma determinística. Em seguida, abordamos a validação de tipos de dados básicos por 
meio de campos estruturados de digitação textual e numérica, analisando como restrições e 
identificadores únicos garantem a estabilidade das variáveis na memória.</p>''')
st.html('''<p class="fonte_texto">Avançamos para o estudo de seletores modernos, onde vimos que botões 
<i>radio</i> e caixas de seleção ganharam recursos para legendas descritivas e inserção de dados em tempo 
de execução. Também examinamos o design limpo proporcionado pelos novos componentes de pílulas e 
controles segmentados, que otimizam o layout e preenchem uniformemente a tela. O tratamento temporal 
foi simplificado de forma inteligente com a introdução do seletor unificado de data e hora, eliminando 
os atrasos provocados pela reexecução de múltiplos widgets independentes. Por fim, desvendamos o 
poder da sincronização bidirecional de parâmetros na URL do navegador, que viabiliza o compartilhamento 
seguro e a persistência exata de estados e filtros dentro de um ecossistema robusto e focado 
na usabilidade.</p>''')
st.divider()

# --- Conclusão --- #
st.html('<h1 class="fonte_titulo_aula">Conclusão</h1>')
st.html('''<p class="fonte_texto">Dominar a estruturação de interfaces em Streamlit vai além de conhecer 
a sintaxe dos componentes; exige entender o fluxo reativo que governa a aplicação. As atualizações 
contínuas do framework trazem soluções elegantes para problemas históricos de usabilidade e 
performance, como o acúmulo de espaço vazio em layouts e o atraso computacional gerado por interações 
sequenciais de tempo.</p>''')
st.html('''<p class="fonte_texto">Ao incorporar componentes de seleção modernos e vincular o estado 
interno da aplicação diretamente aos parâmetros de consulta da URL do navegador, o desenvolvedor 
Python adquire a habilidade de construir produtos de dados altamente profissionais, intuitivos, de 
alto desempenho e facilmente compartilháveis em qualquer ambiente corporativo.</p>''')