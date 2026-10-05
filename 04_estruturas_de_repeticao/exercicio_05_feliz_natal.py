"""
EXERCÍCIO 05: Feliz Nataaal!
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba um número inteiro I (nível de empolgação).
Utilize repetição para exibir a frase "Feliz natal!" repetindo a letra 'a'
da palavra natal exatamente I vezes (ex: I=5 -> "Feliz nataaaal!").
"""

# TODO: Desenvolva o algoritmo abaixo:
try:
    I = int(input("Digite o nível de empolgação: "))
    if I < 0:
        print("Digite um número positivo!")
    else:
        letras_a = "a" * I
        print(f"Feliz nat{letras_a}l!")
except ValueError:
    print("Erro! Digite um número válido.")