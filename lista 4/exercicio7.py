N = int(input("Digite um número: "))
if N <= 0:
    print("Erro: número deve ser positivo.")
else:
    for i in range(11):
        print(f"{N} x {i} = {N*i}")
