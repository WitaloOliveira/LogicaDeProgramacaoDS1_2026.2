"""
DESAFIO 04: REFATORAÇÃO INVESTIGATIVA
Disciplina: Lógica de Programação com Python

RELATÓRIO DA INVESTIGAÇÃO:
O código monolítico repete cálculos de desconto e impostos várias vezes.

SUA MISSÃO:
1. Crie uma função calcular_preco_final(preco_base, taxa_desc, taxa_imp) com return.
2. Crie um procedimento exibir_relatorio_item(numero_item, preco_final) com print.
3. Teste suas funções refatoradas.
"""

# TODO: Desenvolva as funções modulares abaixo:
# Desafio 04
def calcular_preco_final(preco_base, taxa_desc, taxa_imp):
    return preco_base * (1 - taxa_desc) * (1 + taxa_imp)

def exibir_relatorio_item(numero_item, preco_final):
    print(f"Item {numero_item}: R$ {preco_final:.2f}")

# Testes
exibir_relatorio_item(1, calcular_preco_final(100, 0.10, 0.05)) 
exibir_relatorio_item(2, calcular_preco_final(250, 0.20, 0.12))