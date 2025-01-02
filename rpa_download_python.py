# Pacotes necessários para a funcionalidade do código
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import platform
import os
import time
from datetime import datetime
import pymongo
from pymongo.errors import ConnectionFailure, PyMongoError
import sys

# Função para registrar o timestamp
def log_step(step_name):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{current_time}] - {step_name}")

log_step("Etapa 1: Início do Processo")

# A linha abaixo salva o tempo de inicio do código para documentar no mongoDb após a execução
data_inicio = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

log_step("Etapa 2: Realizando conexão com o Banco de Dados")


# O bloco abaixo valida a configuração do MongoDB para acessar o servidor e o collection
try:
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    # Força uma verificação de conexão
    client.admin.command('ping')
    db = client["rpa"]
    collection = db["automation_logs"]
except ConnectionFailure:
    log_step("Erro na etapa!")
    print("Falha ao conectar ao MongoDB. Verifique se o servidor está em execução.")
    sys.exit(1)
except PyMongoError as e:
    print(f"Erro ao conectar ao MongoDB: {e}")
    sys.exit(1)

log_step("Etapa 3: Conexão realizada com sucesso!")

# Função para registrar log no MongoDB
def registrar_log(data_inicio, acao, status, arquivo_nome=None, local_download=None):
    log = {
        "data_inicio": data_inicio,
        "acao": acao,
        "status": status,
        "arquivo_nome": arquivo_nome,
        "diretorio": local_download,
        "data_fim": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    collection.insert_one(log)

def automacao_download_python():
    # Verifica se a versão do sistema operacional é 32bits ou 64bits para decidir qual versão do Python irá realizar o download
    arquitetura = platform.architecture()[0]

    # Verifica o nome do usuário para verificar o diretórido de download no fim do código
    usuario = os.getenv('USERNAME')

    # A linha abaixo mostra onde vai ser realizado o download do arquivo
    local_download = f"C:/Users/{usuario}/Downloads/"

    # Abre o navegador e maximiza a janela
    navegador = webdriver.Chrome()
    navegador.maximize_window()

    try:
        # O bloco de código abaixo realiza a busca no google e acessa o site oficial do Python
        navegador.get("https://www.google.com.br/")
        caixa_pesquisa = navegador.find_element(By.ID, "APjFqb")
        caixa_pesquisa.send_keys("baixar Python" + Keys.ENTER)
        python_link = navegador.find_element(By.PARTIAL_LINK_TEXT, "Python.org")
        python_link.click()
        time.sleep(1)
        
        # O bloco de código abaixo entra na aba de downloads e após isso clica no link que abre a página onde está o download de todas as versões do python
        downloads_link = navegador.find_element(By.LINK_TEXT, "Downloads")
        downloads_link.click()
        time.sleep(1)
        download_todas_versoes = navegador.find_element(By.LINK_TEXT, "View the full list of downloads")
        download_todas_versoes.click()
        time.sleep(1)

        # O bloco abaixo acessa a pagina de download da versão selecionada do python
        download_python = navegador.find_element(By.PARTIAL_LINK_TEXT, "Python 3.11.9")
        download_python.click()
        time.sleep(1)

        # O bloco abaixo avalia se o sistema operacional é 64bits ou 32bits e após isso baixa a versão correta do Python de acordo com a versão do windows
        if(arquitetura == "64bit"):
            baixar_versao_64bits = navegador.find_element(By.LINK_TEXT, "Windows installer (64-bit)")
            baixar_versao_64bits.click()
        else:
            baixar_versao_32bits = navegador.find_element(By.LINK_TEXT,"Windows installer (32-bit)")
            baixar_versao_32bits.click()

        # A linha abaixo aguarda 10 segundos para dar tempo do download concluir
        time.sleep(10)


        # O bloco abaixo verifica se o arquivo baixado se encontra na pasta de download do usuário
        arquivo_nome = "python-3.11.9-amd64.exe"
        arquivo_baixado = os.path.join(local_download, arquivo_nome)
        if os.path.exists(arquivo_baixado):
            status = "sucesso"
            print("Download concluído com sucesso!")
        else:
            status = "falha"
            print("Download não concluído.")

        # A linha abaixo registra o log no banco de dados de acordo com o status do download

        if status == "sucesso":
            registrar_log(data_inicio,"Download Python 3.11.9", status, arquivo_nome, local_download)
        else:
            registrar_log(data_inicio, "Download Python 3.11.9", status, "Erro, sem informação do download", local_download)

    except Exception as e:
        print(f"Erro na automação: {e}")
    finally:
        navegador.quit()
    
log_step("Etapa 4: Iniciando driver da automação")

# Executa a automação
automacao_download_python()

log_step("Etapa 5: Processo finalizado!")
log_step("Etapa 6: Consulte o logs no MongoDB para mais detalhes!")
