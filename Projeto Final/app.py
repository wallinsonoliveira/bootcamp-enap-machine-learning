import streamlit as st
import pandas as pd
import joblib
import json

# Configuração da página
st.set_page_config(
    page_title="Projeto Enap 2024",
    page_icon="👋",
)

#Emojis
#👨‍💻🚓​🚔​🚓​🚔​🚗​🤖​💻​📱​👋

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
        width: 100%; 
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

#st.sidebar.success("Select a demo above.")

#st.sidebar.markdown("""
#    ---
#    ### Conheça a equipe:
#    - <a href="https://github.com/seu-github" target="_blank"><img src="https://img.icons8.com/ios-glyphs/30/000000/github.png"/> GitHub - Nome do membro</a>
#    - <a href="https://linkedin.com/in/seu-linkedin" target="_blank"><img src="https://img.icons8.com/ios-filled/30/0077b5/linkedin.png"/> LinkedIn - Nome do membro</a>
#    - <a href="https://github.com/seu-github-2" target="_blank"><img src="https://img.icons8.com/ios-glyphs/30/000000/github.png"/> GitHub - Nome do membro 2</a>
#    - <a href="https://linkedin.com/in/seu-linkedin-2" target="_blank"><img src="https://img.icons8.com/ios-filled/30/0077b5/linkedin.png"/> LinkedIn - Nome do membro 2</a>
#""", unsafe_allow_html=True)

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
        - Roberto Carlos Bordin - (PRF - Paraná)
        - Thiago dos Santos Hendler - (PRF)
        - Wallinson Oliveira Schutte (UFVJM - Teófilo Otoni/MG) - 👉​ [GitHub](https://github.com/wallinsonoliveira) - [Linkedin](https://www.linkedin.com/in/wallinson-oliveira-schutte/)
        ### Projeto Anti-Muamba | Polícia Rodoviária Federal
        Objetivo: Classificar os veículos que adentram na região de fronteira do Paraná com o Paraguai, em “Lícito” ou “Ilícito”
        """
    )

# Conteúdo da Página de Análise de Dados
elif st.session_state['page'] == "Análise Preditiva":
    st.write("# Análise Preditiva 👨‍💻")
    # Carregar o modelo salvo
    modelo_reglog = joblib.load('modelo_reglog.pkl')

    # Carregar os valores únicos do arquivo JSON
    with open('valores_unicos.json', 'r') as arquivo_json:
        valores_unicos = json.load(arquivo_json)

    with open('colunas_X.json', 'r') as f:
        colunas_X = json.load(f)

    # Função para processar os dados de entrada
    def preprocessar_dados(tempofronteira, categoria, cor, tipodocumentoproprietario, tipo, ufemplacamento, municipioemplacamento,
                           marca, modelo, consulta_res, anomodelo, dataemissaocrv):
        
        # Cria um dicionário com os dados de entrada
        data = {
            'tempofronteira': [tempofronteira],
            'categoria': [categoria],
            'cor': [cor],
            'tipodocumentoproprietario': [tipodocumentoproprietario],
            'tipo': [tipo],
            'ufemplacamento': [ufemplacamento],
            'municipioemplacamento': [municipioemplacamento],
            'marca': [marca],
            'modelo': [modelo],
            'consulta_res': [consulta_res],
            'anomodelo': [anomodelo],
            'dataemissaocrv': [dataemissaocrv]
        }
        
        # Cria o DataFrame
        tab_prev = pd.DataFrame(data)

        # Converte as colunas numéricas
        tab_prev['tempofronteira'] = tab_prev['tempofronteira'].astype(int)
        tab_prev['anomodelo'] = tab_prev['anomodelo'].astype(int)
        tab_prev['dataemissaocrv'] = tab_prev['dataemissaocrv'].astype(int)

        # Adiciona coluna unicodono com base nas regras de negócio
        tab_prev['unicodono'] = tab_prev['dataemissaocrv'] <= tab_prev['anomodelo']
           
        # Aplica pd.get_dummies para colunas categóricas
        tab_prev = pd.get_dummies(tab_prev, columns=['categoria', 'cor', 'tipodocumentoproprietario', 'tipo',
                                                     'ufemplacamento', 'municipioemplacamento', 'marca', 'modelo', 'consulta_res'])
      
        # Reindexa as colunas para alinhar com as do modelo de treinamento
        tab_prev = tab_prev.reindex(columns=colunas_X, fill_value=0)

        return tab_prev

    import streamlit as st

    # Título do app
    st.text("Índice (Recall) de acertos para Lícito: 93% - Índice de acertos para Ilícito: 79%")
    st.text("Preencha os dados para fazer a previsão/classificação:")

    # Criando duas colunas
    col1, col2 = st.columns(2)

    # Inputs na primeira coluna
    with col1:
        tempofronteira = st.number_input("Tempo de Fronteira (horas)", min_value=0, step=1)
        categoria = st.selectbox("Categoria", valores_unicos['categoria'])  # Carregando os valores do JSON
        cor = st.selectbox("Cor", valores_unicos['cor'])  # Carregando os valores do JSON
        tipodocumentoproprietario = st.selectbox("Tipo de Documento do Proprietário", valores_unicos['tipodocumentoproprietario'])
        tipo = st.selectbox("Tipo", valores_unicos['tipo'])  # Valores únicos carregados do JSON
        dataemissaocrv = st.number_input("Ano de Emissão do CRV", min_value=2024, max_value=2025, step=1)

    # Inputs na segunda coluna
    with col2:
        ufemplacamento = st.selectbox("UF de Emplacamento", valores_unicos['ufemplacamento'])
        municipioemplacamento = st.selectbox("Município de Emplacamento", valores_unicos['municipioemplacamento'])
        marca = st.selectbox("Marca", valores_unicos['marca'])
        modelo = st.selectbox("Modelo", valores_unicos['modelo'])
        consulta_res = st.selectbox("Consulta Sistema", valores_unicos['consulta_res'])
        anomodelo = st.number_input("Ano do Modelo", min_value=2024, max_value=2025, step=1)

    # Quando o botão de previsão for clicado
    if st.button("Fazer Previsão"):
        # Preprocessa os dados de entrada
        dados_preprocessados = preprocessar_dados(tempofronteira, categoria, cor, tipodocumentoproprietario, tipo,
                                                  municipioemplacamento, ufemplacamento, marca, modelo, consulta_res,
                                                  anomodelo, dataemissaocrv)
        # Faz a previsão
        previsao = modelo_reglog.predict(dados_preprocessados)
        
        if previsao[0] == 0:
            #st.markdown("O resultado da previsão é: <strong><span style='color:green'>Lícito</strong></span>", unsafe_allow_html=True)
            st.success("O resultado da previsão é: Lícito")
        elif previsao[0] == 1:
            #st.markdown("O resultado da previsão é: <strong><span style='color:red'>Ilícito</span></strong>", unsafe_allow_html=True)
            st.warning("O resultado da previsão é: Ilícito")
        else:
            st.markdown("O resultado da previsão é: <strong><span style='color:orange'>Não foi possível fazer a previsão</span></strong>", unsafe_allow_html=True)


# Conteúdo da Página Sobre o Projeto
elif st.session_state['page'] == "Sobre o Projeto":
    st.write("# Sobre o Projeto 🚔")
    st.write("### Descrição do problema ou tarefa")
    st.write("Classificar os veículos que adentram na região de fronteira do Paraná com o Paraguai, em “Lícito” ou “Ilícito”")
    st.write("### Descrição da solução de IA")
    st.markdown("""
        Buscar dados dos últimos 2 anos dos seguintes veículos: 
        - Apreendidos pela PRF, com descaminho (Ilícito). 
        - Abordados pela PRF mas não foi encontrado Ilícito.
    """)
    st.write("### Fonde de Dados")
    st.write("Boletins de Ocorrências e registro de abordagens da PRF.")
    st.write("Tabela com variáveis independentes (preditoras/features) e target (situação):")
    st.write("""
        | **Campo**                   | **Descrição**                                           |
        |-------------------------|-----------------------------------------------------------|
        | placa                | Dado sensível                                             |
        | tempofronteira       | Tempo de permanência na fronteira (horas)                 |
        | anomodelo            | Ano do modelo do veículo                                  |
        | categoria            | Categoria do veículo                                      |
        | cor                  | Cor do veículo                                            |
        | dataemissaocrv       | Data da emissão da CRV (Documento do veículo)             |
        | tipodocumentoproprietario | Tipo do documento do proprietário do veículo         |
        | marca                | Marca do veículo                                          |
        | modelo               | Modelo do veículo                                         |
        | municipioemplacamento| Município de emplacamento do veículo                      |
        | ufemplacamento       | UF de emplacamento do veículo                             |
        | tipo                 | Tipo do veículo                                           |
        | consulta             | Informações oriundas das consultas feitas no sistema      |
        | unicodono            | Dado gerado através das colunas: anomodelo e dataemissaocrv (df['unicodono'] = df['dataemissaocrv'] <= df['anomodelo'])
        | situacao             | Variável target: 1 (ilícito), 0 (lícito)                  |
    """)
    
# Rodapé ou informações adicionais
st.markdown("---")
st.markdown("### Quer saber mais?")
st.markdown("Acesse o link **[Sobre o Projeto]** ao lado")