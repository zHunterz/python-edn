"""
Crie uma função que calcule a idade de uma pessoa em dias,
baseada no ano de nascimento.
"""
def calcular_idade_em_dias(ano_nascimento, ano_atual):
    idade = ano_atual - ano_nascimento
    return idade * 365  # Considerando 365 dias por ano

ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
idade_em_dias = calcular_idade_em_dias(ano_nascimento, ano_atual)
print(f"A idade em dias é: {idade_em_dias} dias")
