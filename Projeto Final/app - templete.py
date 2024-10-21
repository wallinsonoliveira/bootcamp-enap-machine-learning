import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Projeto Enap 2024",
    page_icon="👋",
)

# Estilo customizado para os botões da barra lateral
st.markdown("""
    <style>
    .css-1aumxhk {
        padding: 0;
    }
    .sidebar .sidebar-content {
        width: 100%;
    }
    .stButton button {
        width: 95%; 
        background-color: #E0E0E0;
        border: 0px solid #e6e6e6;
        border-radius: 4px;
        padding: 5px;
        margin-bottom: 0px;
        font-size: 16px;
        color: black;
    }
    .stButton button:hover {
        background-color: #d0d0d0;
        transition: background-color 0.3s ease;
        color: black; /* Mantém a cor da fonte azul ao passar o mouse */
   
     .stButton button:focus {
        color: black !important; /* Força a fonte azul ao clicar */
    }
    .stButton button:active {
        color: black !important; /* Força a fonte azul ao manter clicado */
    }
    </style>
""", unsafe_allow_html=True)

# Função para criar um botão estilizado
def styled_button(label, page_name):
    if st.sidebar.button(label):
        st.session_state['page'] = page_name

# Título da barra lateral
st.sidebar.title("Navegação")

# Adicionando botões estilizados
styled_button("Página Principal", "Página Principal")
styled_button("Análise Preditiva", "Análise Preditiva")
styled_button("Sobre o Projeto", "Sobre o Projeto")

# Inicializando a página padrão
if 'page' not in st.session_state:
    st.session_state['page'] = "Página Principal"

# Conteúdo da Página Principal
if st.session_state['page'] == "Página Principal":
    st.write("# Seja bem-vindo! 👋")
    st.markdown(
        """
        ## BootCamp Machine Learning em Projetos 2024
        Professores: Erick Muzart e Fernando Melo e Fernando Melo
        - Roberto Carlos Bordin
        - Thiago dos Santos Hendler
        - Wallinson Oliveira Schutte
        ### Projeto Anti-Muamba | Polícia Rodoviária Federal
        Objetivo: Classificar os veículos que adentram na região de fronteira do Paraná com o Paraguai, em “Lícito” ou “Ilícito”
        """
    )

# Conteúdo da Página de Análise de Dados
elif st.session_state['page'] == "Análise Preditiva":
    st.write("# Análise Preditiva")
    st.markdown("""
        Nesta página, você poderá realizar análises de dados específicas.
    """)

# Conteúdo da Página Sobre o Projeto
elif st.session_state['page'] == "Sobre o Projeto":
    st.write("# Sobre o Projeto")
    st.markdown("""
        O Projeto Enap 2024 visa oferecer insights e soluções baseadas em dados para a administração pública.
    """)

# Rodapé ou informações adicionais
st.markdown("---")
st.markdown("### Quer saber mais?")
st.markdown("Acesse o link **[Sobre o Projeto]** ao lado")