try:
    I = int(input("Digite o nível de empolgação: "))
    if I < 0:
        print("Digite um número positivo!")
    else:
        letras_a = "a" * I
        print(f"Feliz nat{letras_a}l!")
except ValueError:
    print("Erro! Digite um número válido.")