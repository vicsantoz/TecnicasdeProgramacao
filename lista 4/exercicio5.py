N = int(input("Digite N: "))
M = int(input("Digite M: "))
if N > M:
    print("Erro: N deve ser menor ou igual a M.")
else:
    for i in range(N, M+1):
        if i % 2 == 0:
            print(i, end=" ")
