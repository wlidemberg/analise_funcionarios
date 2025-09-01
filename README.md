# 📊 Relatório de Funcionários  

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python) ![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow) ![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-brightgreen)

Projeto desenvolvido com **Aprendizado Baseado em Projetos (PBL)**, cujo objetivo é analisar dados de funcionários a partir de um arquivo CSV e gerar estatísticas úteis para a gestão.  

## 🚀 Funcionalidades até o momento (Versão 2)  
- Base de dados originalmente criada em **Excel (`funcionarios.xlsx`)** e exportada para **CSV (`funcionarios.csv`)** para processamento.  
- Leitura e tratamento de dados:  
  - Nome  
  - Cargo  
  - Salário  
  - Data de admissão  
  - Setor  
- Tratamento de **acentuação e encoding** para evitar erros de leitura.  
- Padronização dos nomes das colunas.  
- Conversão da coluna `Data_admissao` para o formato de **data real** (`datetime`).  
- Análises estatísticas:  
  - Quantidade de funcionários.  
  - Média salarial geral.  
  - Maior e menor salário.  
  - Funcionário mais antigo da empresa.  
- Agrupamento por setor, mostrando quantos funcionários existem em cada área.  
- Impressão formatada no **console**.  

## 📂 Estrutura do Projeto  
analise_funcionarios/
│-- funcionarios.xlsx # Base original de dados (alimentada manualmente)
│-- funcionarios.csv # Arquivo exportado do Excel para análise
│-- analise_funcionarios.py # Código principal
│-- README.md # Documentação do projeto

markdown
Copiar código

## 🛠️ Tecnologias Utilizadas  
- **Python 3.13**  
- **Pandas** para análise de dados  
- **Excel/LibreOffice** para criação e manutenção da base de dados  

## 📖 Como Executar  
1. Clone o repositório:  
   ```bash
   git clone https://github.com/seu-usuario/analise_funcionarios.git
   cd analise_funcionarios
Instale as dependências (se necessário):

bash
Copiar código
pip install pandas
Abra o arquivo funcionarios.xlsx e faça as atualizações necessárias.

Exporte o arquivo atualizado para funcionarios.csv (mesmo formato de separador ;).

Execute o script principal:

bash
Copiar código
python analise_funcionarios.py
📌 Próximos Passos (Versão 3 e além)
 Geração automática de relatório em TXT/PDF.

 Visualização com gráficos (salários, setores, admissões).

 Criação de uma interface simples (Tkinter ou Streamlit).

 Integração com banco de dados (SQLite ou PostgreSQL).

🔹 Projeto desenvolvido como parte de um aprendizado progressivo (PBL - Project Based Learning).