"""
Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). 
O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual,
máximo e mínimo da cotação, além da data e hora da última atualização. 
Utilize a API da AwesomeAPI para obter os dados de cotação.

"""
import requests
def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    response = requests.get(url)
    
    if response.status_code == 200:
        dados = response.json()
        if moeda not in dados:
            raise ValueError("Moeda inválida ou não encontrada.")
        return dados[moeda]
    else:
        raise Exception("Erro ao acessar a API AwesomeAPI")
def main():
    try:
        moeda = input("Digite o código da moeda que deseja consultar (ex: USD, EUR, GBP): ").upper()
        cotacao = consultar_cotacao(moeda)
        
        print(f"Cotação atual de {moeda} em relação ao BRL:")
        print(f"Valor: R$ {cotacao['bid']}")
        print(f"Máximo: R$ {cotacao['high']}")
        print(f"Mínimo: R$ {cotacao['low']}")
        print(f"Data e hora da última atualização: {cotacao['create_date']}")
    except ValueError as ve:
        print(f"Erro de validação: {ve}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()