lista = [float(input(f"Digite o {i+1}º elemento: ")) for i in range(20)]
for i in range(10):
    lista[i], lista[-(i+1)] = lista[-(i+1)], lista[i]
print("Lista invertida por pares:", lista)