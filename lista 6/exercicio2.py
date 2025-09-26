lista1 = [int(input(f"Digite o {i+1}º elemento da lista1: ")) for i in range(5)]
lista2 = [int(input(f"Digite o {i+1}º elemento da lista2: ")) for i in range(10)]

lista3 = lista1 + lista2
print("Lista3:", lista3)