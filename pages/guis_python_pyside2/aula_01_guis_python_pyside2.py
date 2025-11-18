# --- Importar as bibliotecas --- #
from PIL import Image
import streamlit as st

# --- Configurações iniciais da página --- #
st.set_page_config(
    page_title='Capítulo 01 - Introdução à GUIs',
    page_icon=Image.open('./assets/logo/logo.png'),
    layout='wide'
)

# --- Carregar o estilo das fontes --- #
with open('./assets/css/style.css', 'r') as css:
    st.html(f'<style>{css.read()}</style>')

# --- Colocar o banner do capítulo --- #
st.image('./assets/imagens/guis_python_pyside2/aula_01/aula_01.png')

# --- Introdução --- #
st.html('<h1 class="fonte_titulo_aula">Introdução</h1>')
st.html('<p class="fonte_texto">Essa é o primeiro capítulo do nosso curso de <b>Interface Gráfica do '
        'Usuário</b> (GUI, em inglês <i>Graphical User Interface</i>) utilizando a linguagem Python e a '
        'biblioteca PySide2. Mas por que usaremos o Python e PySide2 nessas aulas? Eis aqui alguns '
        'motivos:</p>')
st.html('<ol class="fonte_texto" type="1">'
            '<li>Python é uma das linguagens mais usadas atualmente;</li>'
            '<li>É uma linguagem de fácil entendimento;</li>'
            '<li>A biblioteca PySide2 é muito versátil, fácil de encontrar projetos e simples de manusear;</li>'
            '<li>As aplicações geradas com PySide2 podem ser multiplataforma;</li>'
            '<li>Os aplicativos gerados com essa biblioteca não necessitam disponibilizar o código caso você '
            'comercialize o aplicativo e;</li>'
            '<li>A biblioteca PySide2 conta com uma GUI para desenhar as aplicações sem a necessidade de '
            'escrever o código.</li>'
        '<ol>')

# --- Uma breve história da Interface Gráfica do Usuário (GUI) --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Uma breve história da Interface Gráfica do Usuário (GUI)</h1>')
st.html('<p class="fonte_texto">A <b>Interface Gráfica do Usuário</b> tem uma longa e venerável história '
        'que remonta à década de 1960. O NLS (oN-Line System) de Stanford introduziu o conceito de mouse e '
        'janelas, demonstrado publicamente pela primeira vez em 1968. Isso foi seguido pela GUI do sistema '
        'Xerox PARC Smalltalk 1973, que é a base da maioria das GUIs modernas de uso geral.</p>')
colunas = st.columns(2)
with colunas[0]:
    st.image('./assets/imagens/guis_python_pyside2/aula_01/figura_01.png',
             caption='Figura 1: NLS (oN-Line System) de Stanford.')
with colunas[1]:
    st.image('./assets/imagens/guis_python_pyside2/aula_01/figura_02.png',
             caption='Figura 2: Xerox Alto da empresa Xerox Corporation.', width=400)
st.html('<p class="fonte_texto">Esses primeiros sistemas já tinham muitos dos recursos que consideramos '
        'garantidos nas GUIs de desktop modernas, incluindo janelas, menus, botões de opção, caixas de '
        'seleção e ícones posteriores. Essa combinação de recursos nos deu o primeiro acrônimo usado para '
        'esses tipos de interface: WIMP (<i>windows</i> [janelas], <i>icons</i> [ícones], <i>menus</i> e '
        'dispositivo apontador, um mouse).</p>')
st.html('<p class="fonte_texto">Em 1979, foi lançado o primeiro sistema comercial com interface gráfica, '
        'a estação de trabalho PERQ. Isso estimulou uma série de outros esforços de GUI, incluindo '
        'notavelmente o Apple Lisa (1983), que adicionou o conceito de barra de menu e controles de janela. '
        'Assim como muitos outros sistemas do Atari ST (GEM), Amiga. No UNIX (e posteriormente no Linux), '
        'o X Window System surgiu em 1984. A primeira versão do Windows para PC foi lançada em 1985.</p>')
colunas = st.columns(2)
with colunas[0]:
    st.image('./assets/imagens/guis_python_pyside2/aula_01/figura_03.png',
             caption='Figura 3: Tela do Microsoft Windows 3.1 (1992).')
with colunas[1]:
    st.image('./assets/imagens/guis_python_pyside2/aula_01/figura_04.png',
             caption='Figura 4: Tela do Apple System 7 (1991).')
st.html('<p class="fonte_texto">As primeiras GUIs não foram o sucesso instantâneo que poderíamos supor, '
        'devido à falta de software compatível no lançamento e aos requisitos de hardware caros, '
        'especialmente para usuários domésticos. Lentamente, mas de forma constante, a interface GUI '
        'tornou-se a forma preferida de interagir com computadores e a metáfora WIMP tornou-se firmemente '
        'estabelecida como padrão. Isso não quer dizer que não tenha havido <i>tentativas</i> de substituir '
        'a metáfora WIMP no desktop. Microsoft Bob (1995), por exemplo, foi a tentativa muito difamada da '
        'Microsoft de substituir o desktop por uma casa.</p>')
st.image('./assets/imagens/guis_python_pyside2/aula_01/figura_05.jpg',
             caption='Figura 5: Microsoft Bob (1995).')
st.html('<p class="fonte_texto">Não faltaram outras GUIs aclamadas como revolucionárias em sua época, '
        'desde o lançamento do Windows 95 (1995) até o Mac OS X (2001), GNOME Shell (2011), Windows 10 '
        '(2015) e Windows 11 (2021). Cada um deles revisou as UIs de seus respectivos sistemas de desktop, '
        'muitas vezes com muito alarde. Mas fundamentalmente nada realmente mudou. Essas novas UIs ainda '
        'são sistemas WIMP e funcionam exatamente da mesma maneira que as GUIs desde a década de 1980.</p>')
st.html('<p class="fonte_texto">Quando a revolução chegou, era mobile, o mouse foi substituído pelo toque '
        'e as janelas por aplicativos de tela inteira. Mas mesmo num mundo onde todos andamos com '
        'smartphones no bolso, uma enorme quantidade de trabalho diário ainda é feito em computadores '
        'desktop. O WIMP sobreviveu a mais de 40 anos de inovação e espera sobreviver por muitos mais.</p>')

# --- Um pouco sobre o Qt --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Um pouco sobre o Qt</h1>')
st.html('<p class="fonte_texto"><b>Qt</b> é um kit de <i>ferramentas de widget</i> gratuito e de código '
        'aberto para a criação de aplicativos GUI multiplataforma, permitindo que os aplicativos sejam '
        'direcionados a várias plataformas de Windows, macOS, Linux e Android com uma única base de código. '
        'Mas o Qt é muito mais do que um kit de ferramentas de widget e recursos integrados de suporte para '
        'multimídia, bancos de dados, gráficos vetoriais e interfaces MVC; é mais correto pensar nele como '
        'um <i>framework</i> de desenvolvimento de aplicativos.</p>')
st.html('<p class="fonte_texto">O Qt foi iniciado por Eirik Chambe-Eng e Haavard Nord em 1991, fundando a '
        'primeira empresa Qt, <i>Trolltech</i>, em 1994. O Qt é atualmente desenvolvido pela <i>The Qt '
        'Company</i> e continua a ser atualizado regularmente, adicionando recursos e estendendo o suporte '
        'mobile e multiplataforma.</p>')

# --- Qt e PySide2 --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Qt e PySide2</h1>')
st.html('<p class="fonte_texto"><b>PySide2</b>, também conhecido como <i>Qt para Python</i>, é uma '
        '<i>ligação</i> Python do kit de ferramentas Qt, atualmente desenvolvido pela <i>The Qt Company</i>. '
        'Quando você escreve aplicativos usando PySide2, o que você está <i>realmente</i> fazendo é '
        'escrever aplicativos em Qt. A biblioteca PySide2 é simplesmente (não é <i>tão</i> simples assim) '
        'um wrapper em torno da biblioteca Qt do C++, para permitir que ela seja usada em Python.</p>')
st.html('<p class="fonte_texto">Como esta é uma interface Python para uma biblioteca C++, as convenções de '
        'nomenclatura usadas no PySide2 não aderem aos padrões PEP8. Mais notavelmente, funções e variáveis '
        'são nomeadas usando <i><b>mixedCase</b></i> em vez de <i><b>snake_case</b></i>. Depende '
        'inteiramente de você aderir a esse padrão em seus próprios aplicativos, no entanto, acho que foi '
        'útil seguir os padrões Python para seu próprio código, para ajudar a esclarecer onde o código '
        'PySide2 termina e o seu começa.</p>')
st.html('<p class="fonte_texto">Por último, embora exista documentação específica do PySide2 disponível, '
        'muitas vezes você se verá lendo a própria documentação do Qt, pois ela é mais completa. Se fizer '
        'isso, você precisará traduzir a sintaxe do objeto e alguns métodos contendo nomes de funções '
        'reservados para Python, como segue:</p>')
colunas = st.columns(5)
with colunas[2]:
    st.html('''<style type="text/css">
    .tg  {border-collapse:collapse;border-spacing:0;}
    .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:20px;
      overflow:hidden;padding:10px 5px;word-break:normal;}
    .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:20px;
      font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
    .tg .tg-0lax{text-align:left;vertical-align:top}
    </style>
    <table class="tg"><thead>
      <tr>
        <th class="tg-0lax">Qt</th>
        <th class="tg-0lax">PySide2</th>
      </tr></thead>
    <tbody>
      <tr>
        <td class="tg-0lax">Qt::SomeValue</td>
        <td class="tg-0lax">Qt.SomeValue</td>
      </tr>
      <tr>
        <td class="tg-0lax">object.exec()</td>
        <td class="tg-0lax">object.exec_()</td>
      </tr>
      <tr>
        <td class="tg-0lax">object.print()</td>
        <td class="tg-0lax">object.print_()</td>
      </tr>
    </tbody>
    </table>''')

# --- Resumo --- #
st.write('---')
st.html('<h1 class="fonte_titulo_aula">Resumo</h1>')
st.html('<p class="fonte_texto">Nesta Aula 01, daremos os primeiros passos essenciais no universo das '
        '<b>Interfaces Gráficas de Usuário</b>(GUIs) com Python, utilizando a poderosa biblioteca '
        '<b>PySide2</b> (Qt para Python). Você aprenderá a configurar o ambiente e a entender os conceitos '
        'fundamentais que regem toda aplicação Qt, como o <b>QApplication</b> e o <b>QWidget</b>. O foco '
        'é criar sua primeira janela funcional, dominando o ciclo de vida básico de um aplicativo desktop '
        'para iniciar sua jornada no desenvolvimento de software com interfaces ricas e nativas.</p>')