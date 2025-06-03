import csv

def escrever_csv(nome_arquivo, dados):
    with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(['Nome', 'Idade', 'Cidade'])
        for linha in dados:
            escritor.writerow(linha)
    print(f"Dados escritos com sucesso no arquivo {nome_arquivo}")

dados = [
    ["Ana", "28", "Traipu"],
    ["Bruno", "32", "Maceió"],
    ["Carlos", "25", "Palmeira dos Índios"],
    ["Diana", "30", "Penedo"],
    ["Eduardo", "27", "Delmiro Gouveia"]
]

if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo CSV para escrever os dados: ")
    escrever_csv(nome_arquivo, dados)