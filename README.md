# BootCamp Machine Learning em Projetos 2024 🚔

**Projeto:** Otimização de Abordagens | Polícia Rodoviária Federal  
**Objetivo:** Classificar veículos que adentram na região de fronteira do Paraná com o Paraguai como "Lícito" ou "Ilícito".

## Aplicação:
- [Link para a Aplicação - Projeto PRF 2024](https://bit.ly/projetoenapprf2024)  
- [Demo - Hugging Face](https://huggingface.co/spaces/peeweesuper/BootCamp_ML_Enap_2024)

---

### Professores:
- Erick Muzart
- Fernando Melo

### Equipe:
- **Roberto Carlos Bordin** (PRF - Paraná) - [GitHub](https://github.com/rcbordin)
- **Thiago dos Santos Hendler** (PRF - São Paulo) - [GitHub](https://github.com/tdshendler) | [LinkedIn](https://www.linkedin.com/in/tdshendler/)  
- **Wallinson Oliveira Schutte** (UFVJM - Teófilo Otoni/MG) - [GitHub](https://github.com/wallinsonoliveira) | [LinkedIn](https://www.linkedin.com/in/wallinson-oliveira-schutte/)

---

## Descrição do Problema:
Este projeto visa melhorar a eficiência nas abordagens da Polícia Rodoviária Federal (PRF) ao classificar veículos na fronteira do Paraná com o Paraguai em duas categorias:
- **Lícito**
- **Ilícito**

Os veículos classificados como "Ilícitos" envolvem crimes como descaminho.

---

## Fonte de Dados:
Os dados usados no projeto foram obtidos a partir dos boletins de ocorrência e registros de abordagens da PRF nos últimos dois anos, incluindo:

- Veículos apreendidos com descaminho (Ilícito).
- Veículos abordados que não apresentaram irregularidades.

### Variáveis:
| Campo                   | Descrição                                                       |
|--------------------------|-----------------------------------------------------------------|
| **placa**                | Dado sensível                                                   |
| **tempofronteira**        | Tempo de permanência na fronteira (horas)                       |
| **anomodelo**            | Ano do modelo do veículo                                        |
| **categoria**            | Categoria do veículo                                            |
| **cor**                  | Cor do veículo                                                  |
| **dataemissaocrv**        | Data de emissão da CRV (Documento do veículo)                   |
| **tipodocumentoproprietario** | Tipo do documento do proprietário do veículo               |
| **marca**                | Marca do veículo                                                |
| **modelo**               | Modelo do veículo                                               |
| **municipioemplacamento** | Município de emplacamento do veículo                           |
| **ufemplacamento**       | UF de emplacamento do veículo                                   |
| **tipo**                 | Tipo do veículo                                                 |
| **consulta**             | Informações oriundas das consultas feitas no sistema            |
| **unicodono**            | Dado gerado através das colunas `anomodelo` e `dataemissaocrv`  |
| **situação**             | Variável target: 1 (ilícito), 0 (lícito)                        |

---
