"""
EXERCÍCIO 04: Positivos e Média
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 6 valores numéricos.
Conte quantos foram estritamente positivos (> 0) e calcule a média aritmética deles.
Imprima a quantidade de positivos e a média formatada com 1 casa decimal.
"""

# TODO: Desenvolva o algoritmo abaixo:
# EXERCÍCIO Q4: Positivos e Média
# Disciplina: Lógica de Programação com Python

# Inicializar variáveis
quantidade_positivos = 0
soma_positivos = 0

# Ler 6 valores numéricos
print("Digite 6 valores numéricos:")

for i in range(1, 7):
    valor = float(input(f"Digite o {i}º valor: "))
    
    # Verificar se é estritamente positivo (> 0)
    if valor > 0:
        quantidade_positivos += 1
        soma_positivos += valor

# Calcular a média aritmética dos positivos
if quantidade_positivos > 0:
    media = soma_positivos / quantidade_positivos
    print(f"\nQuantidade de positivos: {quantidade_positivos}")
    print(f"Média dos positivos: {media:.1f}")
else:
    print(f"\nQuantidade de positivos: 0")
    print("Não há positivos para calcular a média.")
