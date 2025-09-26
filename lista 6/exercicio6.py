lista = [int(input(f"Digite o {i+1}º elemento: ")) for i in range(12)]
x = int(input("Digite a posição X: "))
y = int(input("Digite a posição Y: "))

soma = lista[x] + lista[y]
print(f"Soma dos valores nas posições {x} e {y}: {soma}")