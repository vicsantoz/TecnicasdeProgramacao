N = int(input("Digite N: "))
if N <= 0:
    print("Erro: número inválido.")
else:
    S = 0
    for i in range(1, N+1):
        S += 1/i
    print("Valor de S:", S)