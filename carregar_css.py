import base64
import streamlit as st


def obter_imagem_base64(caminho_imagem):
    with open(caminho_imagem, 'rb') as f:
        return base64.b64encode(f.read()).decode()


def carregar_css():
    # --- Obter a imagem de fundo --- #
    imagem_base64 = obter_imagem_base64('./assets/fundo/fundo_aero.png')

    # --- Carregar o estilo das fontes --- #
    with open('./assets/css/style.css', 'r', encoding='utf-8') as css:
        st.html(f'''
        <style>
            {css.read()}
    
            /* 1. Fundo limpo original para o corpo do site */
                .stApp {{
                    background: linear-gradient(135deg, #e0f7fa 0%, #ffffff 50%, #e8f5e9 100%) !important;
                }}
    
                /* 2. Preparando a Sidebar para receber a camada fantasma */
                [data-testid="stSidebar"] {{
                    background-color: transparent !important;
                    border-right: 1px solid rgba(255, 255, 255, 0.8) !important;
                    box-shadow: 2px 0px 10px rgba(0,0,0,0.1) !important;
                    overflow: hidden !important; /* Evita que o desfoque vaze para fora do menu */
                    position: relative !important;
                }}
    
                /* 3. A CAMADA MÁGICA: Imagem de fundo com desfoque real */
                [data-testid="stSidebar"]::before {{
                    content: "";
                    position: absolute;
                    top: -15px; left: -15px; right: -15px; bottom: -15px; /* Margem negativa para o blur não criar bordas brancas */
                    background-image: url("data:image/png;base64,{imagem_base64}") !important;
                    background-size: cover !important;
                    background-position: center !important;
    
                    /* --- CONTROLES DE IMAGEM --- */
                    filter: blur(2px) !important; /* Aumente este número para deixar MAIS desfocado */
                    opacity: 0.60 !important;      /* Diminua este número (ex: 0.4) para deixar mais branco/claro */
    
                    z-index: -1 !important; /* Garante que a imagem fique ATRÁS do texto */
                }}
    
                /* 4. Melhorando a leitura do texto do menu com "Glow" branco */
                [data-testid="stSidebarNav"] span {{
                    color: #1e374d !important; /* Azul bem escuro para dar contraste */
                    font-weight: 600 !important; /* Deixa a letra um pouco mais gordinha */
                    text-shadow: 0px 0px 8px rgba(255,255,255,1), 
                                 0px 0px 4px rgba(255,255,255,1) !important; /* Brilho branco ao redor da letra */
                }}
        </style>''')