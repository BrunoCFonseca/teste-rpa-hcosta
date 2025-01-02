# README - Automação de Download do Python com Selenium e MongoDB

## Descrição
Este projeto automatiza o processo de download da versão mais recente do Python (Python 3.11.9) através do uso do Selenium WebDriver. O script realiza uma busca no Google, acessa o site oficial do Python, verifica a arquitetura do sistema operacional (32-bit ou 64-bit) e realiza o download do instalador correspondente. Além disso, o script registra as informações do processo de download em um banco de dados MongoDB para fins de auditoria.

## Funcionalidades
Realiza uma busca no Google para encontrar o site oficial do Python.
Acessa a página de downloads do Python e seleciona a versão correta (com base na arquitetura do sistema operacional).
Faz o download do instalador do Python para o diretório padrão de downloads.
Registra logs detalhados sobre o processo de download, incluindo o status da operação e informações sobre o arquivo, no MongoDB.

## Tecnologias Utilizadas
Selenium WebDriver: Biblioteca para automação de navegação web.
MongoDB: Banco de dados NoSQL para armazenar os logs da automação.
Python 3.12.4: Linguagem utilizada para implementar a automação.

## Pré-requisitos
Antes de rodar o script, é necessário garantir que os seguintes requisitos estão atendidos:

1. MongoDB: Instalar o MongoDB e garantir que o serviço esteja rodando.
2. Python 3.12.4: Instalar o Python (versão 3.12.4) em seu sistema.
3. Instalar o selenium e o pymongo
   pip install selenium pymongo

## Como Rodar
1. Instale o MongoDB e verifique que está rodando na porta padrão 27017.
2. Instale o Selenium e o ChromeDriver conforme mencionado nos pré-requisitos.
3.Execute o Script Python:
    Certifique-se de que o MongoDB está em execução.
    Execute o código Python no terminal ou em um ambiente de desenvolvimento:
      rpa_download_python.py

## Fluxo do Código
1. Log de Início: O script começa registrando um timestamp de início da execução.
2. Conexão com MongoDB: Verifica a conexão com o banco de dados MongoDB para armazenar os logs.
3. Automação de Navegação: O Selenium realiza a busca do Python no Google, navega até o site oficial e faz o download da versão adequada.
4. Registro de Logs: Ao final do processo, o status do download (sucesso ou falha) é registrado no MongoDB.
5. Fechamento do Navegador: O navegador é fechado ao final da automação.

## Estrutura do Banco de Dados
Os logs são armazenados em uma coleção chamada automation_logs dentro do banco de dados rpa. Cada log contém as seguintes informações:

- data_inicio: Data e hora de início da automação.
- acao: Descrição da ação realizada.
- status: Status da operação (sucesso ou falha).
- arquivo_nome: Nome do arquivo baixado (se aplicável).
- diretorio: Diretório de download onde o arquivo foi salvo.
- data_fim: Data e hora de conclusão da automação.

## Exemplo de Log no MongoDB
Sucesso:
![image](https://github.com/user-attachments/assets/43817400-a1bf-401f-ae3d-aa1cc6cba7c2)

Falha:
![image](https://github.com/user-attachments/assets/742832be-a7dc-4cd4-8f86-60d77b6a4df7)

## Logs de Execução
Durante a execução, o script imprime logs no console para acompanhamento do processo, incluindo informações sobre cada etapa, como:
- Conexão com MongoDB.
- Abertura do navegador e navegação nas páginas.
- Status final do download.

## Problemas Comuns
- Erro de Conexão com o MongoDB: Se o MongoDB não estiver em execução ou configurado corretamente, o script falhará na etapa de conexão.
- Erro no Driver do Chrome: Certifique-se de que a versão do ChromeDriver é compatível com a versão do navegador Chrome instalado no sistema.
- Se você encontrar algum outro problema, consulte os logs de erro detalhados no terminal ou nos logs do MongoDB.
