estoque = {
    'tomate': [1000, 2.59],
    'alface': [500, 0.99],
    'batata': [2000, 1.89]
}

print("ESTOQUE INICIAL")
for produto, dados in estoque.items():
    print(f"{produto.title()}: {dados[0]} unidades - R$ {dados[1]:.2f}")
print()

produto = input("Produto vendido: ").lower()
quantidade = int(input("Quantidade vendida: "))

if produto not in estoque:
    print("\n Produto não encontrado.")
else:
    if quantidade > estoque[produto][0]:
        print("\n Quantidade insuficiente no estoque.")
    else:
        preco = estoque[produto][1]
        total = preco * quantidade
        estoque[produto][0] -= quantidade
        print(f"\n Venda registrada!")
        print(f"{quantidade}x {produto.title()} a R$ {preco:.2f} = R$ {total:.2f}")

print("\n ESTOQUE ATUALIZADO")
for produto, dados in estoque.items():
    print(f"{produto.title()}: {dados[0]} unidades - R$ {dados[1]:.2f}")
