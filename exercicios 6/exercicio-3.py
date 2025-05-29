"""
Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, 
utilizando a API ViaCEP. O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP 
consultado.

"""
import requests
def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    
    if response.status_code == 200:
        dados = response.json()
        if 'erro' in dados:
            raise ValueError("CEP inválido ou não encontrado.")
        return dados
    else:
        raise Exception("Erro ao acessar a API ViaCEP")
def main():
    try:
        cep = input("Digite o CEP que deseja consultar (somente números): ")
        if not cep.isdigit() or len(cep) != 8:
            raise ValueError("CEP deve conter 8 dígitos numéricos.")
        
        endereco = consultar_cep(cep)
        
        print(f"Logradouro: {endereco['logradouro']}")
        print(f"Bairro: {endereco['bairro']}")
        print(f"Cidade: {endereco['localidade']}")
        print(f"Estado: {endereco['uf']}")
    except ValueError as ve:
        print(f"Erro de validação: {ve}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()