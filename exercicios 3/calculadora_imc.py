"""
Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.


< 18.5: classificacao = "Abaixo do peso" 

< 25: classificacao = "Peso normal"

 < 30: classificacao = "Sobrepeso"

 Para os demais cenários: classificacao = "Obeso"
"""
# Solicita o peso e a altura do usuário
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
# Calcula o IMC
imc = peso / (altura ** 2)
# Classifica o IMC
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"
# Exibe o resultado
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")
# Exibe a classificação de acordo com a tabela padrão de IMC
print("Tabela de Classificação do IMC:")
print("Abaixo do peso: IMC < 18.5")
print("Peso normal: 18.5 <= IMC < 25")
print("Sobrepeso: 25 <= IMC < 30")
print("Obeso: IMC >= 30")