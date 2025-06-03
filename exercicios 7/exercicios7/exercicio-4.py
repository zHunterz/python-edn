import json

def ler_json(arquivo):
    try:
        with open(arquivo, 'r', newline='', encoding='utf-8') as arquivo_json:
            dados = json.load(arquivo_json)
            print(dados)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")

def escrever_json(arquivo, dados):
    try:    
        with open(arquivo, 'w', newline='', encoding='utf-8') as arquivo_json:
            json.dump(dados, arquivo_json)
            print(f"Dados escritos com sucesso no arquivo '{arquivo}'.")
    except Exception as e:
        print(f"Erro: Não foi possível escrever no arquivo '{e}'.")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")

dados = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

if __name__ == "__main__":
    arquivo = input("Digite o nome do arquivo JSON (com extensão .json): ")
    
    # Escrever dados no arquivo JSON
    escrever_json(arquivo, dados)
    
    # Ler dados do arquivo JSON
    ler_json(arquivo)