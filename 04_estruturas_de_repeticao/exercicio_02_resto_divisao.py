"""
EXERCÍCIO 02: Resto da Divisão por 5
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia dois valores inteiros X e Y.
Utilize o laço for para imprimir todos os inteiros entre X e Y (em ordem crescente)
cujo resto da divisão por 5 seja igual a 2 ou igual a 3.
"""

# TODO: Desenvolva o algoritmo abaixo:
# EXERCÍCIO Q2: Resto da Divisão por 5
# Disciplina: Lógica de Programação com Python

# Leia dois valores inteiros X e Y
X = int(input("Digite o primeiro valor (X): "))
Y = int(input("Digite o segundo valor (Y): "))

# Utilize o laço for para imprimir todos os inteiros entre X e Y
# cujo resto da divisão por 5 seja igual a 2 ou igual a 3
print("Números entre", X, "e", Y, "com resto 2 ou 3 na divisão por 5:")

for numero in range(X, Y + 1):
    resto = numero % 5
    if resto == 2 or resto == 3:
        print(numero, end=" ")

print()  # Quebra de linha ao final
