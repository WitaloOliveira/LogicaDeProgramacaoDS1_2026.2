# TODO: Implemente o carrinho de compras
carrinho_compras = []

# Adicione 3 produtos e ordene a lista
for i in range(3):
    produtos = input(f"Digite o produto {i + 1} ")
    carrinho_compras.append(produtos)

carrinho_compras.sort()
print("Carrinho de compras:", carrinho_compras)