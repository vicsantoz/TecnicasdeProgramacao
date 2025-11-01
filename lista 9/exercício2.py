compras = {}

while True:
    produto = input("Digite o nome do produto (ou FIM para encerrar): ").capitalize()
    if produto == "Fim":
        break
    preco = float(input(f"Digite o preço de {produto}: R$ "))
    compras[produto] = preco

print("\n Lista de compras:")
for p, v in compras.items():
    print(f"{p}: R$ {v:.2f}")

excluir = input("\n Digite o nome do produto a ser excluído: ").capitalize()
if excluir in compras:
    del compras[excluir]
    print(f"{excluir} foi removido da lista.")
else:
    print("Produto não encontrado.")

print("\n Lista final de compras:")
for p, v in compras.items():
    print(f"{p}: R$ {v:.2f}")
