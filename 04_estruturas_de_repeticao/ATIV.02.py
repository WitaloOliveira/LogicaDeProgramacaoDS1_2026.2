
# TODO: Desenvolva o acumulador com parada no 0
soma = 0

# Escreva a estrutura de repetição whilesoma = 0

numero = int(input("Digite um número inteiro (0 para sair): "))

while numero != 0:
    soma += numero
    numero = int(input("Digite um número inteiro (0 para sair): "))

print(f"A soma de todos os números digitados é: {soma}")