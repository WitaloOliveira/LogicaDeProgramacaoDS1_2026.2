"""
EXERCÍCIO 05: Média Ponderada da Avaliação Técnica
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Solicite as notas de três avaliações do curso técnico.
A primeira prova tem peso 2, a segunda peso 3 e a terceira peso 5.
Calcule e exiba a média final ponderada utilizando apenas operadores aritméticos.
"""

# TODO: Desenvolva o algoritmo abaixo:
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))

peso1 = 2
peso2 = 3 
peso3 = 5

soma_pesos = peso1 + peso2 + peso3
media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / soma_pesos
print(f"a media final poderada é: {media:.2f}")