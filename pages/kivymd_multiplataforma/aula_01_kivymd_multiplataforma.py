# --- Importar as bibliotecas --- #
from PIL import Image
import streamlit as st
from carregar_css import carregar_css

# --- Configurações iniciais da página --- #
st.set_page_config(
    page_title='KivyMD Multiplataforma - Aula 01',
    page_icon=Image.open('./assets/logo/logo.png'),
    layout='wide'
)

# --- Carregar o CSS --- #
carregar_css()

# --- Colocar o título da aula --- #
st.html('<h1 class="fonte_titulo_aula">Aula 01: Tema, Tela e Ciclo de Vida!</h1>')

# --- Vídeo --- #
with st.expander('Se quiser acompanhar com o vídeo, acesse aqui! 👇'):
    st.video('https://youtu.be/C0FVN7VCTvs')

# --- Código da aula --- #
st.subheader('Se quiser acessar o código completo da aula, clique [aqui](https://github.com/GTL98/canal_mundo_python/blob/main/Desenvolvedor%20KivyMD%3A%20Do%20Zero%20ao%20App%20Multiplataforma/Aula%2001/aula_01.py)')
st.divider()

# --- Introdução --- #
st.subheader('E fala, devs! Tudo bem com vocês? Espero que sim!')
st.html('<h1 class="fonte_titulo_aula">Introdução</h1>')
st.html('''<p class="fonte_texto">Está começando o nosso curso de KivyMD aqui no Mundo Python, e se você 
quer aprender a criar interfaces gráficas incríveis, modernas e totalmente multiplataforma usando apenas 
o Python, você está no lugar certo! O KivyMD é uma biblioteca fantástica que implementa o Material Design 
do Google para o motor gráfico do Kivy. Isso significa que com o mesmíssimo código escrito no seu 
computador, você consegue gerar um aplicativo lindão que roda no Windows, Linux, Mac, Android e iOS, 
sem precisar esquentar a cabeça aprendendo linguagens nativas como Swift, Java ou Kotlin. É o Python 
dominando o mundo mobile!</p>''')
st.subheader('Então sem mais delongas, bora para a aula!')
st.divider()

# --- Arquitetura fundamental do MDApp --- #
st.html('<h1 class="fonte_titulo_aula">Arquitetura fundamental do MDApp</h1>')
st.html('''<p class="fonte_texto">Antes de colocarmos a mão na massa e vermos as coisas surgindo na tela, 
precisamos entender a espinha dorsal de qualquer aplicativo feito com essa biblioteca: o ciclo de vida e 
a arquitetura fundamental. No KivyMD, tudo gira em torno de uma classe principal que gerencia o 
aplicativo inteiro. Essa classe herda recursos de um motor potente que lida com a janela do app, as 
configurações visuais e os eventos de inicialização e fechamento. O ponto central dessa arquitetura é 
um método especial que funciona como o "construtor visual" do seu projeto; é dentro dele que nós 
preparamos a tela e dizemos ao Python exatamente o que deve ser desenhado quando o aplicativo começar a 
rodar.</p>''')
st.html('''<p class="fonte_texto">Aqui está o código inicial com essa estrutura básica e limpa para 
você começar:</p>''')
st.code('''# --- Importar os módulos --- #
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen


class Aula1(MDApp):
    def build(self):
        """Este método será o responsável por retornar a estrutura da interface."""
        pass


if __name__ == '__main__':
    # --- Instanciação da classe e execução do loop principal --- #
    Aula1().run()''', line_numbers=True)
st.html('''<p class="fonte_texto">Agora, vamos destrinchar cada linha desse código para que você 
entenda perfeitamente o que está acontecendo por baixo dos panos. Nada de apenas copiar e colar, o foco 
aqui é o aprendizado de verdade!</p>''')
st.html('''<p class="fonte_texto">Logo no início, temos as linhas de importação (
<span class="palavras_reservadas">imports</span>). É aqui que trazemos as ferramentas da biblioteca 
KivyMD para o nosso ambiente. Na primeira linha, importamos o 
<span class="texto_python">MDApp</span>, que é a classe base para criar qualquer aplicativo 
KivyMD. É ela quem traz toda a mágica do ciclo de vida do app. Nas linhas seguintes, importamos o 
<span class="texto_python">MDLabel</span> (usado para colocar textos e rótulos na tela) e o 
<span class="texto_python">MDScreen</span> (que funciona como a nossa tela em branco, o plano de fundo 
onde vamos "pintar" os nossos elementos gráficos). Repare em um detalhe muito importante da didática 
do KivyMD: todas as classes específicas dessa biblioteca começam com o prefixo <b>MD</b> (MDApp, 
MDLabel, MDScreen). Isso ajuda a diferenciar o que é do Kivy puro e o que já vem estilizado com o 
Material Design.</p>''')
st.html('''<p class="fonte_texto">Na sequência, criamos a nossa classe 
<span class="palavras_reservadas">class</span> <span class="classe_python">Aula1</span>
<span class="texto_python">(MDApp):</span>. Ao colocar o MDApp entre parênteses, estamos aplicando um 
conceito fundamental da programação orientada a objetos chamado herança. Isso significa que a nossa 
classe <span class="classe_python">Aula1</span> ganha, de presente, todos os superpoderes, funções e 
comportamentos que o KivyMD já tem configurados de fábrica para um aplicativo profissional.</p>''')
st.html('''<p class="fonte_texto">Dentro da nossa classe, definimos o método 
<span class="palavras_reservadas">def</span> <span class="funcao_python">build</span>
<span class="texto_python">(</span><span class="self_python">self</span>
<span class="texto_python">):</span>. Esse método é obrigatório e crucial! Ele faz parte do ciclo de vida 
do framework. Quando o aplicativo é iniciado, o KivyMD chama o 
<span class="texto_python">build</span> automaticamente. A função principal dele é estruturar a 
interface e dar um <span class="palavras_reservadas">return</span> no elemento que será a raiz do seu app 
(como uma tela principal cheia de botões e textos). Como neste primeiro passo estamos apenas montando a 
estrutura sem nenhum elemento visual ainda, utilizamos a palavra-chave 
<span class="palavras_reservadas">pass</span>, que serve como um ponto de marcação no Python para dizer: 
"olha, por enquanto não faça nada aqui".</p>''')
st.html('''<p class="fonte_texto">Por fim, chegamos ao bloco 
<span class="palavras_reservadas">if</span> <span class="texto_python">__name__ == </span>
<span class="variaveis">'__main__'</span><span class="texto_python">:</span>. Essa é uma boa prática 
clássica no Python para garantir que o código dentro dele só seja executado se você rodar este arquivo 
diretamente. Dentro desse bloco, temos a linha de execução: 
<span class="texto_python">Aula1().run()</span>. Aqui, nós instanciamos a nossa classe (criamos o 
objeto do nosso aplicativo na memória) e chamamos o método <span class="texto_python">.run()</span>. Esse 
método liga os motores do KivyMD e inicia o chamado Main Loop (o loop principal). Esse loop é o que 
mantém a janela do seu aplicativo aberta, atualizando a tela constantemente e esperando por interações 
do usuário, como cliques ou toques, até que o programa seja fechado. Se você executar esse código agora, 
verá uma janela preta padrão surgir na sua tela, indicando que a estrutura está pronta e funcionando 
perfeitamente!</p>''')
st.divider()

# --- Método build() e widgets raiz --- #
st.html('<h1 class="fonte_titulo_aula">Método '
        '<span class="funcao_python">build</span>'
        '<span class="texto_python">()</span> e widgets raiz</h1>')
st.html('''<p class="fonte_texto">Agora que já temos o esqueleto do nosso aplicativo pronto, as coisas 
começam a ficar divertidas! Chegou a hora de darmos vida à nossa interface. No desenvolvimento com Kivy 
e KivyMD, trabalhamos com o conceito de "Widgets". Pense nos widgets como as peças de Lego do seu 
aplicativo: botões, caixas de texto, imagens e rótulos são todos widgets. Para que essas peças não 
fiquem flutuando no vazio, precisamos de uma base sólida para encaixá-las, que é a nossa tela 
(<span class="texto_python">Screen</span>).</p>''')
st.html('''<p class="fonte_texto">Na parte teórica desse processo, é fundamental entender a relação de 
"pai e filho" (<i>parent</i>/<i>child</i>) na montagem da interface. A nossa tela principal atua como o 
widget "pai" ou a "raiz" (<i>root</i>). Todos os outros elementos visuais que criarmos, como os textos, 
serão os widgets "filhos" e precisarão ser explicitamente adicionados a essa tela. Ao final, o nosso 
método <span class="funcao_python">build</span><span class="texto_python">()</span> deve pegar essa 
tela principal (já com todos os elementos dentro dela) e retorná-la para o aplicativo, dizendo: 
"Aqui está a interface pronta para ser exibida!".</p>''')
st.html('''<p class="fonte_texto">Vejamos como isso funciona na prática com a nossa primeira 
atualização no código:</p>''')
st.code('''...(continuação do código)
class Aula1(MDApp):
    def build(self):
        """Este método será o responsável por retornar a estrutura da interface."""
        # --- Criação de um MDScreen fornece a base para os widgets do Material Design --- #
        tela_principal = MDScreen()

        # --- O MDLabel estente o Label do Kivy com tipografia do Material Design --- #
        texto_central = MDLabel(
            text='Explorando o MDApp',
            halign='center',
            font_style='H4'
        )

        # --- Adicionar a label como widget filho da tela principal --- #
        tela_principal.add_widget(texto_central)

        # --- O retorno deste widget define a raiz da aplicação --- #
        return tela_principal
        (continuação do código)...''', line_numbers=True)
st.html('''<p class="fonte_texto">Vamos esmiuçar essa nova etapa, linha por linha! O nosso método 
<span class="funcao_python">build</span><span class="texto_python">()</span> deixou de ter apenas aquele 
<span class="palavras_reservadas">pass</span> e agora está trabalhando de verdade.</p>''')
st.html('''<p class="fonte_texto">A primeira coisa que fazemos é criar a nossa tela base com o comando 
<span class="texto_python">tela_principal = MDScreen()</span>. Aqui, estamos instanciando um objeto da 
classe <span class="texto_python">MDScreen</span> e guardando-o na variável 
<span class="texto_python">tela_principal</span>. Imagine que acabamos de esticar uma tela em branco 
no nosso cavalete de pintura. É em cima dela que o Material Design renderizará os nossos 
elementos.</p>''')
st.html('''<p class="fonte_texto">Em seguida, partimos para a criação do nosso primeiro componente 
visual: o <span class="texto_python">MDLabel</span>. Nós armazenamos esse componente na variável 
<span class="texto_python">texto_central</span>. Repare que, diferente da tela, passamos alguns 
parâmetros muito importantes entre os parênteses para configurar o visual desse texto logo de cara. O 
<span class="texto_python">text=</span><span class="variaveis">'Explorando o MDApp'</span> é o conteúdo 
exato que aparecerá escrito para o usuário. O parâmetro <span class="texto_python">halign=</span>
<span class="variaveis">'center'</span> cuida do alinhamento horizontal (<i>horizontal align</i>), 
garantindo que o texto fique perfeitamente centralizado na tela, em vez de grudar no canto esquerdo, 
que é o padrão. Já o <span class="texto_python">font_style=</span><span class="variaveis">'H4'</span>
 é onde a mágica da tipografia do Material Design acontece. Se você já mexeu com HTML, reconhecerá 
 isso na hora: estamos definindo o tamanho e o peso da fonte como um cabeçalho (Heading 4), o que deixa 
 a letra maior, elegante e com a formatação padronizada do Google para títulos.</p>''')
st.html('''<p class="fonte_texto">Mas atenção a um detalhe crucial: criar o texto não faz com que ele 
apareça automaticamente na tela. Ele existe na memória, mas está "solto". É por isso que usamos o 
comando <span class="texto_python">tela_principal.add_widget(texto_central)</span>. Essa é a função que 
pega o nosso rótulo recém-criado e o "cola" dentro da nossa tela base. Estamos formalizando a relação 
dizendo que <span class="texto_python">texto_central</span> é agora um filho de 
<span class="texto_python">tela_principal</span>. Você usará a função 
<span class="texto_python">add_widget()</span> o tempo todo no KivyMD para montar suas telas!</p>''')
st.html('''<p class="fonte_texto">Por fim, a última instrução do método é 
<span class="texto_python">return</span> <span class="texto_python">tela_principal</span>. Como o motor 
do KivyMD espera que o método <span class="funcao_python">build</span>
<span class="texto_python">()</span> entregue a interface pronta, nós retornamos a nossa tela principal 
(que agora já contém o nosso texto centralizado). Ao rodar o código agora, a janela preta ganha uma tela 
com o seu texto perfeitamente posicionado e estilizado. E o mais legal: tente redimensionar a janela 
do aplicativo no seu computador! Você notará que o texto se ajusta e se mantém centralizado de 
forma totalmente responsiva e automática.</p>''')
st.divider()

# --- Poder do ThemeManager e propriedade theme_cls --- #
st.html('<h1 class="fonte_titulo_aula">Poder do ThemeManager e propriedade '
        '<span class="texto_python">theme_cls</span></h1>')
st.html('''<p class="fonte_texto">Uma das características mais incríveis de se usar o KivyMD no lugar 
do Kivy padrão é a facilidade absurda para gerenciar o visual do seu aplicativo. Sabe aquela dor de 
cabeça de ter que configurar a cor de fundo de cada tela e a cor da fonte de cada texto individualmente? 
Com o Material Design, nós resolvemos isso de forma centralizada usando o Gerenciador de Temas, 
conhecido no código como <span class="texto_python">theme_cls</span>.</p>''')
st.html('''<p class="fonte_texto">Na teoria, o KivyMD possui uma paleta de cores e estilos pré-definidos 
pelo Google. Tudo o que você precisa fazer é dizer ao aplicativo qual é a cor primária (aquela que vai 
dominar botões e barras superiores), qual é a cor de destaque (usada para botões flutuantes e pequenos 
detalhes) e se você quer que o aplicativo rode no modo claro (Light) ou escuro (Dark). Ao definir essas 
três regrinhas logo na inicialização, todos os widgets que você adicionar à tela vão automaticamente 
"ouvir" e respeitar essa identidade visual, adaptando-se sem que você precise escrever uma linha a mais 
de código para eles!</p>''')
st.html('''<p class="fonte_texto">Dê uma olhada na evolução do nosso código com o tema configurado:</p>''')
st.code('''...(continuação do código)
class Aula1(MDApp):
    def build(self):
        """Este método será o responsável por retornar a estrutura da interface."""
        # --- Acessar o ThemeManager para configurar a identidade visual --- #
        self.theme_cls.theme_style = 'Dark'  # mudança para modo escuro
        self.theme_cls.accent_palette = 'Amber'  # cor de destaque
        self.theme_cls.primary_palette = 'Indigo'  # paleta de cor principal

        # --- Criação de um MDScreen fornece a base para os widgets do Material Design
        tela_principal = MDScreen()

        # --- O MDLabel reage automaticamente ao modo Dark --- #
        texto_central = MDLabel(
            text='Tema Indigo em modo Escuro',
            halign='center',
            font_style='H4',
            theme_text_color='Primary'  # vincula a cor do texto à paleta primária
        )
        (continuação do código)...
''', line_numbers=True)
st.html('''<p class="fonte_texto">Vamos entender exatamente a mágica que incluímos antes de criar a 
nossa tela principal. Tudo começa com o comando <span class="self_python">self</span>
<span class="texto_python">.theme_cls</span>. Como estamos dentro do método 
<span class="funcao_python">build</span>, a palavra <span class="self_python">self</span> se refere ao 
nosso próprio aplicativo (<span class="texto_python">MDApp</span>). O atributo 
<span class="texto_python">theme_cls</span> é o painel de controle visual dele.</p>''')
st.html('''<p class="fonte_texto">Em seguida, definimos a nossa paleta de cores. Com 
<span class="self_python">self</span><span class="texto_python">.theme_cls.primary_palette = </span>
<span class="variaveis">'Indigo'</span> (um tom de azul arroxeado) e 
<span class="self_python">self</span><span class="texto_python">.theme_cls.accent_palette = </span>
<span class="variaveis">'Amber'</span> (um tom de âmbar/amarelo), nós preparamos as tintas do nosso app. 
Embora ainda não tenhamos botões na tela para ver o âmbar brilhando, já deixamos a regra definida. É uma 
excelente prática de programação já setar essas cores logo de cara.</p>''')
st.html('''<p class="fonte_texto">Agora, olhe atentamente para o nosso 
<span class="texto_python">MDLabel</span>. Nós mudamos o texto para refletir o nosso novo visual, mas a 
grande sacada está no novo parâmetro: <span class="texto_python">theme_text_color=</span>
<span class="variaveis">'Primary'</span>. Lembra que eu disse que no modo escuro o texto ficaria branco 
automaticamente? Pois é, mas com esse comando nós dizemos ao widget: "Não use a cor padrão, eu quero que 
você assuma a cor da minha Paleta Primária!". Como definimos a nossa paleta primária como 
<span class="variaveis">'Indigo'</span> lá em cima, o nosso texto puxará essa cor dinamicamente. Se 
amanhã você mudar o <span class="texto_python">primary_palette</span> para 
<span class="variaveis">'Red'</span>, o texto do seu aplicativo inteiro muda sozinho para vermelho, sem 
você precisar mexer no <span class="texto_python">MDLabel</span>. Isso poupa muito trabalho!</p>''')
st.html('''<p class="fonte_texto">Se você executar o código agora, o resultado é muito bacana: uma 
interface com fundo escuro de aparência profissional e um texto centralizado perfeitamente tingido com 
a cor Indigo. Estamos no caminho certo!</p>''')
st.divider()

# --- Ciclo de vida da aplicação e hooks de evento --- #
st.html('<h1 class="fonte_titulo_aula">Ciclo de vida da aplicação e hooks de evento</h1>')
st.html('''<p class="fonte_texto">Agora que a nossa interface já tem cor e estilo, vamos entrar em um dos 
conceitos mais poderosos do desenvolvimento mobile: o <b>Ciclo de Vida</b> do aplicativo. Imagine o dia a 
dia de uso de um celular: você abre um app, de repente chega uma mensagem no WhatsApp, você minimiza o 
app atual, responde a mensagem e depois volta para onde estava. Durante todo esse processo, o aplicativo 
passou por diferentes "estados" (iniciou, pausou, retornou).</p>''')
st.html('''<p class="fonte_texto">Na teoria, gerenciar isso do zero seria uma dor de cabeça imensa, mas 
o <span class="texto_python">MDApp</span> já traz funções pré-fabricadas, chamadas de "hooks" (ganchos) 
de evento, que disparam automaticamente quando essas mudanças de estado acontecem. Isso nos permite 
colocar lógicas precisas em momentos chave: como carregar dados apenas quando a tela já estiver pronta (
<span class="texto_python">on_start</span>), salvar informações ou evitar que o app feche ao ir para o 
segundo plano (<span class="texto_python">on_pause</span>) e atualizar a tela com um "bem-vindo de volta" 
quando o usuário retornar (<span class="texto_python">on_resume</span>).</p>''')
st.html('''<p class="fonte_texto">Vejamos como implementar esses eventos no nosso código:</p>''')
st.code("""...(continuação do código)
class Aula1(MDApp):
    def build(self):
        ...
        # --- O MDLabel reage automaticamente ao modo Dark --- #
        self.texto_central = MDLabel(
            text='Estado: Inicializando...',
            halign='center',
            font_style='H4',
            theme_text_color='Primary'  # vincula a cor do texto à paleta primária
        )
        ...

    def on_start(self):
        # --- Este método é perfeito para lógicas que dependem da UI estar pronta --- #
        print('A aplicação iniciou com sucesso!')
        self.texto_central.text = 'Aplicação ativa e pronta!'

    def on_pause(self):
        # --- IMPORTANTE: no Android, retornar True evita que o app seja fechado --- #
        print('Aplicação em segundo plano...')
        return True

    def on_resume(self):
        # --- Executado ao voltar para o app --- #
        print('Aplicação restaurada!')
        self.texto_central.text = 'Bem-vindo de volta!'
    (continuação do código)...""", line_numbers=True)
st.html('''<p class="fonte_texto">Vamos destrinchar essa novidade! Antes de falarmos das novas funções, 
note uma mudança importantíssima que fizemos no método <span class="funcao_python">build</span>
<span class="texto_python">():</span> nós adicionamos o prefixo <span class="self_python">self</span> 
antes das nossas variáveis, transformando <span class="texto_python">tela_principal</span> em 
<span class="self_python">self</span><span class="texto_python">.tela_principal</span> e 
<span class="texto_python">texto_central</span> em 
<span class="self_python">self</span><span class="texto_python">.texto_central</span>. Por que fizemos 
isso? Pela regra de escopo do Python! Se criássemos essas variáveis sem o 
<span class="self_python">self</span>, elas só existiriam dentro do método 
<span class="funcao_python">build</span><span class="texto_python">()</span>. Como agora queremos 
alterar o texto do nosso label a partir de outras funções (como o 
<span class="texto_python">on_start</span>), precisamos que ele pertença à classe inteira para ser 
acessado de qualquer lugar. O <span class="self_python">self</span> faz exatamente essa ponte!</p>''')
st.html('''<p class="fonte_texto">Agora vamos aos protagonistas desta etapa: os métodos de ciclo de vida, 
que ficam alinhados junto com o <span class="funcao_python">build</span>
<span class="texto_python">()</span>, diretamente dentro da nossa classe 
<span class="classe_python">Aula1</span>.</p>''')
st.html('''<ul class="fonte_texto">
        <li><span class="palavras_reservadas">def</span> <span class="funcao_python">on_start</span>
        <span class="texto_python">(</span><span class="self_python">self</span>
        <span class="texto_python">)</span>: Esse é o gatilho disparado no exato momento em que o 
        aplicativo termina de ser construído e a interface (UI) já está visível para o usuário. É o 
        lugar perfeito para colocar animações de entrada, tocar um som de inicialização ou buscar dados 
        de um banco de dados. No nosso código, usamos o <span class="funcoes_python">print</span>
        <span class="texto_python">()</span> para jogar uma mensagem no terminal (excelente para nós, 
        desenvolvedores, monitorarmos o que está acontecendo) e, o mais legal, acessamos o nosso 
        <span class="self_python">self</span><span class="texto_python">.texto_central.text</span> 
        para mudar a mensagem dinamicamente de "Estado: Inicializando..." para "Aplicação ativa 
        e pronta!".</li>
        <li><span class="palavras_reservadas">def</span> <span class="funcao_python">on_pause</span>
        <span class="texto_python">(</span><span class="self_python">self</span>
        <span class="texto_python">)</span>: Aqui entra um segredo valioso do desenvolvimento mobile. 
        Quando você minimiza um app no celular, o sistema operacional costuma "congelar" ou até matar o 
        aplicativo para economizar memória RAM. Esse método é chamado logo antes do app ir para o segundo 
        plano. O comando <span class="palavras_reservadas">return True</span> no final é essencial para 
        dispositivos Android: ele diz ao sistema "Por favor, mantenha o meu aplicativo vivo em segundo 
        plano, não o feche!". No computador (desktop) você não vai notar o efeito prático desse método, 
        mas no celular ele é indispensável para evitar que o app reinicie do zero toda vez que o usuário 
        trocar de janela.</li>
        <li><span class="palavras_reservadas">def</span> <span class="funcao_python">on_resume</span>
        <span class="texto_python">(</span><span class="self_python">self</span>
        <span class="texto_python">)</span>: O complemento natural do 
        <span class="texto_python">on_pause</span>. Se o seu app ficou dormindo em segundo plano e o 
        usuário voltou para ele, esse método entra em ação! É o momento ideal para atualizar informações 
        na tela. No nosso caso, nós fazemos um novo <span class="funcoes_python">print</span>
        <span class="texto_python">()</span> no terminal e alteramos o texto central para uma saudação: 
        "Bem-vindo de volta!".</li>
        </ul>''')
st.html('''<p class="fonte_texto">Ao rodar esse código no seu computador, você verá que o texto exibido 
na tela será quase que instantaneamente "Aplicação ativa e pronta!", pois o método 
<span class="texto_python">on_start</span> age assim que a tela pisca na sua frente. É o KivyMD 
mostrando o seu poder de interatividade e deixando a nossa estrutura preparada para o mundo real dos 
smartphones!</p>''')
st.divider()

# --- Tamanho e título do App --- #
st.html('<h1 class="fonte_titulo_aula">Tamanho e título do App</h1>')
st.html('''<p class="fonte_texto">Um dos maiores desafios ao desenvolver um aplicativo mobile direto no 
computador é ter a real noção de como os elementos visuais se comportarão na tela de um celular. Se 
deixarmos a janela do programa livre e redimensionável com o tamanho padrão do desktop, podemos acabar 
criando um layout que fica lindo no monitor, mas totalmente espremido ou desalinhado no smartphone. Para 
resolver isso, precisamos simular a proporção de uma tela mobile logo de cara, garantindo que o que 
estamos vendo no desenvolvimento será o mais fiel possível ao resultado final na palma da mão do 
usuário!</p>''')
st.html('''<p class="fonte_texto">Além disso, todo aplicativo profissional merece um nome adequado na 
barra superior da janela, e não apenas o nome técnico da classe no código. Como bônus, nesta etapa 
também conheceremos uma ferramenta nativa incrível para monitorar a performance do nosso app enquanto 
ele roda.</p>''')
st.html('''<p class="fonte_texto">Veja como o nosso código ganha esses novos superpoderes:</p>''')
st.code('''# --- Importar os módulos --- #
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen

# --- Configuração do tamanho da janela --- #
Window.size = (360, 640)


class Aula1(MDApp):
    def build(self):
        """Este método será o responsável por retornar a estrutura da interface."""
        # --- Definir o título do app --- #
        self.title = 'Curso de KivyMD: Aula 01'
        ...
    
    def on_start(self):
        # --- Ativar o modo FPS nativo do KivyMD para depuração --- #
        self.fps_monitor_start()
        self.texto_central.text = 'Monitoramento de performance'
    (continuação do código)...''', line_numbers=True)
st.html('''<p class="fonte_texto">Vamos entender essas novidades espetaculares, começando lá no topo 
do nosso arquivo!</p>''')
st.html('''<p class="fonte_texto">Adicionamos uma nova linha de importação: 
<span class="palavras_reservadas">from</span> <span class="texto_python">kivy.core.window</span> 
<span class="palavras_reservadas">import</span> <span class="texto_python">Window</span>. Note um 
detalhe fundamental: nós importamos isso do <span class="texto_python">kivy</span> puro, e não do 
<span class="texto_python">kivymd</span>. Lembra que o KivyMD é uma camada visual construída por cima 
do motor gráfico do Kivy? O gerenciamento da janela do sistema operacional (tamanho, minimizar, 
maximizar) é uma responsabilidade do motor base. É por isso que chamamos o 
<span class="texto_python">Window</span> do núcleo do framework!</p>''')
st.html('''<p class="fonte_texto">Logo abaixo das importações, nós usamos o comando 
<span class="texto_python">Window.size = (</span><span class="numeros">360</span>
<span class="texto_python">, </span><span class="numeros">640</span>
<span class="texto_python">)</span>. O que estamos fazendo aqui é passar uma tupla (esses valores entre 
parênteses) definindo a largura e a altura da janela em pixels. Essa proporção específica simula 
perfeitamente a orientação retrato (em pé) de um smartphone padrão. Fazendo isso antes da classe do 
aplicativo começar, garantimos que a janela já abrirá no formato de um celular, permitindo que você 
posicione seus widgets com confiança.</p>''')
st.html('''<p class="fonte_texto">Agora, mergulhando no método 
<span class="funcao_python">build</span><span class="texto_python">()</span>, logo na primeira linha 
adicionamos <span class="self_python">self</span><span class="texto_python">.title = </span>
<span class="variaveis">'Curso de KivyMD: Aula 01'</span>. Por padrão, se você não disser nada, o Kivy 
usará o nome da sua classe principal (que no nosso caso é <span class="classe_python">Aula1</span>) 
como título da janela. Ao modificar o atributo <span class="texto_python">title</span>, nós deixamos o 
aplicativo com uma cara muito mais amigável e profissional. É esse o nome que aparecerá lá na barra 
superior do seu programa no Windows, Mac ou Linux.</p>''')
st.html('''<p class="fonte_texto">E para fechar com chave de ouro, fomos até o método 
<span class="funcao_python">on_start</span><span class="texto_python">()</span> (aquele que roda assim 
que o app carrega a interface) e adicionamos o comando 
<span class="self_python">self</span><span class="texto_python">.fps_monitor_start()</span>. Essa é uma 
daquelas funções escondidas que salvam vidas! O KivyMD possui um monitor de FPS (Frames Por Segundo) 
nativo. Ao chamar essa função, um pequeno contador visual aparecerá flutuando na tela do seu 
aplicativo, mostrando em tempo real o desempenho do seu app e quantos quadros estão sendo renderizados 
por segundo. Isso é uma ferramenta de depuração (<i>debug</i>) maravilhosa para garantir que o seu 
aplicativo mobile não está travando ou pesando muito a memória!</p>''')
st.divider()

# --- Código Final: A Obra Completa! --- #
st.html('<h1 class="fonte_titulo_aula">Código Final: A Obra Completa!</h1>')
st.html('''<p class="fonte_texto">Chegamos ao fim da nossa primeira aula, e agora você tem em mãos a 
estrutura completa e profissional de um aplicativo construído com KivyMD! Juntamos todas as peças do 
nosso quebra-cabeça: a importação correta, a configuração de tela simulando um mobile, a estilização 
centralizada com o <b>ThemeManager</b>, a criação do nosso widget de texto e, claro, o poderoso 
controle do ciclo de vida da aplicação.</p>''')
st.html('''<p class="fonte_texto">Para fechar com chave de ouro, adicionamos apenas mais um gancho de 
evento ao nosso código final: o método <span class="texto_python">on_stop</span>.</p>''')
st.html('''<p class="fonte_texto">Dê uma olhada em como ficou o nosso arquivo completo:</p>''')
st.code('''# --- Importar os módulos --- #
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen

# --- Configuração do tamanho da janela --- #
Window.size = (360, 640)


class Aula1(MDApp):
    """Classe principal que demonstra o MDApp."""
    def build(self):
        """Este método será o responsável por retornar a estrutura da interface."""
        # --- Definir o título do app --- #
        self.title = 'Curso de KivyMD: Aula 01'

        # --- Acessar o ThemeManager para configurar a identidade visual --- #
        self.theme_cls.theme_style = 'Dark'  # mudança para modo escuro
        self.theme_cls.accent_palette = 'Amber'  # cor de destaque
        self.theme_cls.primary_palette = 'Indigo'  # paleta de cor principal

        # --- Criação de um MDScreen fornece a base para os widgets do Material Design --- #
        self.tela_principal = MDScreen()

        # --- Criação de uma label --- #
        self.texto_central = MDLabel(
            text='Estado: Inicializando...',
            halign='center',
            font_style='H4',
            theme_text_color='Primary'  # vincula a cor do texto à paleta primária
        )

        # --- Adicionar a label como widget filho da tela principal --- #
        self.tela_principal.add_widget(self.texto_central)

        # --- O retorno deste widget define a raiz da aplicação --- #
        return self.tela_principal

    def on_start(self):
        """Disparado quando a UI está pronta e visível."""
        print('Evento: App iniciado')
        self.fps_monitor_start()
        self.texto_central.text = 'Bem-vindo ao MDApp!'

    def on_pause(self):
        """Disparado quando o app vai para segundo plano"""
        print('Evento: App pausado')
        return True

    def on_resume(self):
        """Disparado quando o usuário volta para o aplicativo."""
        print('Aplicação restaurada!')
        self.texto_central.text = 'App retomado com sucesso!'

    def on_stop(self):
        """Disparado no fechamento total da aplicação."""
        print('Evento: App encerrado. Limpando memória...')


if __name__ == '__main__':
    # --- Instanciação da classe e execução do loop principal --- #
    Aula1().run()''', line_numbers=True)
st.html('''<p class="fonte_texto">Como você pode notar ali no finalzinho da nossa classe, incluímos o 
<span class="palavras_reservadas">def</span> <span class="funcao_python">on_start</span>
<span class="texto_python">(</span><span class="self_python">self</span>
<span class="texto_python">):</span>. Esse é o último suspiro do seu aplicativo! Ele é acionado no 
exato momento em que o usuário decide fechar o programa de vez.</p>''')
st.html('''<p class="fonte_texto">Na prática, por que isso é tão útil? Imagine que o seu app gerou 
arquivos temporários, fez o download de imagens em cache ou precisa enviar um último log de erro para 
um servidor. Você não quer que esses arquivos fiquem ocupando espaço na memória do celular do usuário 
para sempre, certo? É no <span class="texto_python">on_stop</span> que você programa a "faxina" da casa, 
garantindo que o seu aplicativo seja encerrado de forma limpa e otimizada.</p>''')
st.divider()

# --- Resumo --- #
st.html('<h1 class="fonte_titulo_aula">Resumo</h1>')
st.html('''<p class="fonte_texto">Nesta primeira aula, mergulhamos de cabeça no universo do KivyMD, 
descobrindo como essa biblioteca incrível nos permite criar aplicativos com o visual moderno do 
Material Design, rodando em qualquer plataforma (Windows, Mac, Linux, Android e iOS) usando pura e 
simplesmente o Python! Aprendemos que a espinha dorsal de qualquer projeto é a classe que herda de 
<span class="texto_python">MDApp</span> e o seu método obrigatório 
<span class="funcao_python">build</span><span class="texto_python">()</span>. Foi a partir dessa base 
que configuramos o ambiente, simulando a tela de um celular com o módulo 
<span class="texto_python">Window</span> e definindo o nosso <span class="texto_python">MDScreen</span>, 
que funciona como a grande tela em branco onde todos os nossos elementos gráficos são perfeitamente 
encaixados.</p>''')
st.html('''<p class="fonte_texto">Com a estrutura montada, demos vida à interface utilizando o conceito 
de widgets e a facilidade do <b>ThemeManager</b> (<span class="texto_python">theme_cls</span>). Criamos 
o nosso primeiro componente de texto estilizado com o <span class="texto_python">MDLabel</span> e o 
adicionamos à tela principal de forma lógica. Mas o grande "pulo do gato" do KivyMD brilhou quando vimos 
como é fácil gerenciar o visual: com apenas algumas linhas de código, ativamos o Modo Escuro e definimos 
paletas de cores primárias e de destaque (como Indigo e Amber). O sistema é tão inteligente que adapta 
automaticamente as cores das fontes e dos componentes, garantindo uma identidade visual padronizada e 
profissional sem dor de cabeça.</p>''')
st.html('''<p class="fonte_texto">Por fim, fomos além da parte visual e dominamos o poderoso Ciclo de Vida 
da aplicação, um conceito absolutamente vital para o desenvolvimento mobile. Compreendemos como utilizar 
os ganchos de evento nativos (<span class="texto_python">on_start</span>, 
<span class="texto_python">on_pause</span>, <span class="texto_python">on_resume</span> e 
<span class="texto_python">on_stop</span>) para controlar o comportamento do nosso aplicativo nos 
bastidores. Seja para carregar dados ao iniciar, manter o app vivo em segundo plano, dar boas-vindas no 
retorno do usuário ou limpar a memória no fechamento, agora temos o controle total. Em resumo, 
construímos uma fundação sólida, inteligente e pronta para escalar para projetos reais de altíssimo 
nível!</p>''')
st.divider()

# --- Conclusão --- #
st.html('<h1 class="fonte_titulo_aula">Conclusão</h1>')
st.html('''<p class="fonte_texto">E assim nós fechamos o nosso primeiro grande passo no mundo do KivyMD! 
Percebeu a grandiosidade do que acabamos de fazer aqui? Nós pegamos aquele Python que você, muito 
provavelmente, já está acostumado a usar no terminal para scripts ou manipulação de dados e o 
transformamos em uma interface visual de verdade. O velho mito de que "Python é complicado para criar 
aplicativos de celular" acabou de ser quebrado na sua frente! Com um único código, você já tem uma tela 
com design moderno, responsiva e pronta para brilhar em qualquer sistema operacional.</p>''')
st.html('''<p class="fonte_texto">Não subestime a simplicidade deste nosso primeiro projeto. Essa 
estrutura que montamos (definindo o tamanho da tela, dominando o <b>ThemeManager</b> para as cores e 
controlando os batimentos cardíacos do app com o Ciclo de Vida é o verdadeiro DNA de qualquer aplicativo 
profissional. Você acabou de construir a base de concreto do seu prédio; agora, o limite de quantos 
andares ele terá é apenas a sua imaginação. Você tem em mãos os superpoderes para tirar aquelas ideias 
de aplicativos da gaveta e dar vida a elas!</p>''')
st.html('''<p class="fonte_texto">O meu maior conselho para você agora é: "fuçar" e quebrar o código! 
Mude as paletas de cores para ver como o app reage, teste novos tamanhos de fonte no 
<span class="texto_python">MDLabel</span>, altere os textos dos eventos de inicialização. É na prática 
e na curiosidade que o aprendizado realmente se consolida na nossa mente.</p>''')
st.subheader('No mais é isso, nos vemos na próxima aula! Até lá, fiquem com Deus e fui!')