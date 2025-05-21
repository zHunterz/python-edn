"""
Conversor de Moeda
Crie um programa que converta um valor em reais para dólares, euros. Use os seguintes dados:
- Valor em reais: R$ 100.00
- Cotação do dólar: R$ 5.70
- Cotação do euro: R$ 6.40
O programa deve calcular e exibir os valores convertidos, arrendondando para duas casas decimais.
"""

# Conversor de Moeda

#Valores das moedas
valor_reais = 100.00
taxa_dolar = 5.70
taxa_euro = 6.40

#Conversões
valor_em_dolar = valor_reais / taxa_dolar
valor_em_euro = valor_reais / taxa_euro

#Exibição dos resultados
print(f"Valor em reais: R$ {valor_reais:.2f}")
print(f"Valor em doláres: $ {valor_em_dolar:.2f}")
print(f"Valor em euros: € {valor_em_euro:.2f}")