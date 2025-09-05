import math
N = int(input("Digite N: "))
M = int(input("Digite M: "))
if N < 0 or M < 0:
    print("Erro: valores inválidos.")
else:
    soma = math.factorial(N) + math.factorial(M)
    print("Soma dos fatoriais:", soma)