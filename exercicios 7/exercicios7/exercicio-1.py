import pandas as pd

def processar_logs_treinamento(nome_arquivo):
    try:
        df = pd.read_csv(nome_arquivo)
        desvio_padrao_temopo = df['tempo_execucao'].std()   
        media = df['tempo_execucao'].mean()
        print(f"Média do tempo de execução: {media}")
        print(f"Desvio padrão do tempo de execução: {desvio_padrao_temopo}")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except pd.errors.EmptyDataError:
        print("Erro: O arquivo está vazio.")
    except Exception as e:
        print(f"Ocorreu um erro ao processar o arquivo: {e}")

nome_arquivo = input("Digite o nome do arquivo de logs: ")
processar_logs_treinamento(nome_arquivo)