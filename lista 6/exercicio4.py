lista = [int(input(f"Digite o {i+1}º elemento: ")) for i in range(10)]
m = int(input("Digite o valor m a procurar: "))

if m in lista:
    print(f"Valor {m} encontrado na posição {lista.index(m)}")
else:
    print(f"Valor {m} não se encontra na lista.")