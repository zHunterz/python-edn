"""
4- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

"""
# Conversor de Temperatura Simples

temp = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C, F, K): ").upper()
destino = input("Unidade de destino (C, F, K): ").upper()

if origem == destino:
    resultado = temp
elif origem == "C" and destino == "F":
    resultado = (temp * 9/5) + 32
elif origem == "C" and destino == "K":
    resultado = temp + 273.15
elif origem == "F" and destino == "C":
    resultado = (temp - 32) * 5/9
elif origem == "F" and destino == "K":
    resultado = (temp - 32) * 5/9 + 273.15
elif origem == "K" and destino == "C":
    resultado = temp - 273.15
elif origem == "K" and destino == "F":
    resultado = (temp - 273.15) * 9/5 + 32
else:
    print("Unidade inválida.")
    exit()

print(f"Temperatura convertida: {resultado:.2f} {destino}")