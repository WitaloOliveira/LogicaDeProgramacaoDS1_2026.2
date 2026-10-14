"""
EXERCÍCIO 04: Função Lambda de Desconto Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Escreva uma função anônima (lambda) que receba o valor de um produto
e retorne o valor com 15% de desconto à vista aplicado.
"""

# TODO: Desenvolva a expressão lambda e teste-a abaixo:
# Execício 04
desconto_vista = lambda valor: valor * 0.85

valor = float(input("Digite o valor do produto: "))
print(f"Valor com 15% de desconto à vista: R$ {desconto_vista(valor):.2f}")