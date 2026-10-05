"""
EXERCÍCIO 03: Pares entre Cinco Números
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Solicite 5 números inteiros ao usuário.
Utilize uma estrutura de repetição e um contador para verificar quantos números pares
foram digitados. Ao final, imprima a quantidade total.
"""

# TODO: Desenvolva o algoritmo abaixo:
# EXERCÍCIO Q3: Pares entre Cinco Números
# Disciplina: Lógica de Programação com Python

# Inicializar o contador de números pares
contador_pares = 0

# Solicite 5 números inteiros ao usuário
print("Digite 5 números inteiros:")

for i in range(1, 6):
    numero = int(input(f"Digite o {i}º número: "))
    
    # Verificar se o número é par
    if numero % 2 == 0:
        contador_pares += 1

# Imprimir a quantidade total de números pares
print(f"\nQuantidade de números pares digitados: {contador_pares}")