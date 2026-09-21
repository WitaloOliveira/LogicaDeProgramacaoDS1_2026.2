"""
EXERCÍCIO 04: Cardápio da Lanchonete
Disciplina: Lógica de Programação com Python

TABELA:
1 - Cachorro Quente: R$ 4.00
2 - X-Salada: R$ 4.50
3 - X-Bacon: R$ 5.00
4 - Torrada Simples: R$ 2.00
5 - Refrigerante: R$ 1.50

ENUNCIADO:
Leia o código do item e a quantidade consumida.
Calcule e mostre o total a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:
# Leitura do código do item e da quantidade na mesma linha
entrada = input().split()
codigo = int(entrada[0])
quantidade = int(entrada[1])

# Estrutura de decisão para definir o preço com base no código do cardápio
if codigo == 1:
    preco = 4.00
elif codigo == 2:
    preco = 4.50
elif codigo == 3:
    preco = 5.00
elif codigo == 4:
    preco = 2.00
elif codigo == 5:
    preco = 1.50
else:
    preco = 0.00 # Caso seja inserido um código inválido

# Cálculo do valor total a pagar
total = preco * quantidade

# Impressão do resultado formatado com 2 casas decimais
print(f"Total: R$ {total:.2f}")