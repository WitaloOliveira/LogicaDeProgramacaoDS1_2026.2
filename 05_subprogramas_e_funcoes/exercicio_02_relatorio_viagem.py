"""
EXERCÍCIO 02: Modularizando Relatório de Viagem
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie duas funções:
1. `calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel)`
2. `calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao)`

No programa principal, leia os dados, execute as funções e mostre o custo total da viagem.
"""

# TODO: Desenvolva as funções e o programa principal abaixo:
# Exercício 02
calcular_custo_transporte = lambda km, consumo, preco: km / consumo * preco
calcular_custo_alimentacao = lambda pessoas, dias, diaria: pessoas * dias * diaria

total = (calcular_custo_transporte(float(input("Distância (km): ")), float(input("Consumo (km/l): ")), float(input("Preço do combustível: ")))
    + calcular_custo_alimentacao(int(input("Quantidade de pessoas: ")), int(input("Quantidade de dias: ")), float(input("Valor da diária: "))))

print(f"Custo total da viagem: R$ {total:.2f}")