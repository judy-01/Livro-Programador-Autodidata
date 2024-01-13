import os

def encontrar_arquivo(nome_arquivo):
    # Obtém o caminho absoluto do diretório atual
    diretorio_atual = os.getcwd()

    # Lista todos os arquivos no diretório atual e subdiretórios
    for pasta_atual, _, arquivos in os.walk(diretorio_atual):
        if nome_arquivo in arquivos:
            caminho_completo = os.path.join(pasta_atual, nome_arquivo)
            return caminho_completo

    return None

def exibir_conteudo_arquivo(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print(f"Conteúdo do arquivo {caminho_arquivo}:\n")
            print(conteudo)
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho_arquivo}")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

# Solicita ao usuário o nome do arquivo a ser procurado
nome_arquivo_procurado = input("Digite o nome do arquivo a ser encontrado: ")

# Procura o arquivo e exibe seu conteúdo, se encontrado
caminho_arquivo_encontrado = encontrar_arquivo(nome_arquivo_procurado)
if caminho_arquivo_encontrado:
    exibir_conteudo_arquivo(caminho_arquivo_encontrado)
else:
    print(f"Arquivo '{nome_arquivo_procurado}' não encontrado no diretório atual e subdiretórios.")
