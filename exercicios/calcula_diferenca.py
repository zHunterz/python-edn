#Esse código tem como objetivo ler valores inteiros inputados pelo usuário e calcular a diferença.

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
D = int(input("Digite o valor de D: "))

#Calcula a diferença

DIFERENCA = (A * B) - (C * D)

#Exibe o resultado
print("A formula para calcular a diferença é: DIFERENCA = (A * B) - (C * D)")
print(f"Substituindo os valores fornecidos: DIFERENCA = ({A} * {B}) - ({C} * {D})")
print(f"A diferença é: {DIFERENCA}")