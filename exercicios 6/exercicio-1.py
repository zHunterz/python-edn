"""
Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais, 
possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória.

"""

import random
def gerar_senha(tamanho):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    try:
        tamanho = int(input("Digite o tamanho da senha desejada: "))
        if tamanho <= 0:
            print("O tamanho da senha deve ser um número positivo.")
            return
        senha = gerar_senha(tamanho)
        print(f"Sua senha aleatória é: {senha}")
    except ValueError:
        print("Por favor, insira um número válido.")

if __name__ == "__main__":
    main()