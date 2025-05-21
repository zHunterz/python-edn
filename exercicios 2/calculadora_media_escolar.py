"""
Calculadora de Média Escolar
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

- Nota 1: 7.5
- Nota 2: 8.0
- Nota 3: 6.5
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.

"""
# Definindo as variáveis
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5
# Calculando a média
media = (nota1 + nota2 + nota3) / 3
# Exibindo os resultados
print(f"Nota 1: {nota1:.2f}")
print(f"Nota 2: {nota2:.2f}")
print(f"Nota 3: {nota3:.2f}")
print(f"Média: {media:.2f}")
# Verificando se o aluno foi aprovado ou reprovado
if media >= 7.0:
    print("Resultado: Aprovado")
else:   
    print("Resultado: Reprovado")