N = int(input("Digite N: "))
M = int(input("Digite M: "))
if N >= M or N < 0 or M < 0:
    print("Erro: dados inválidos.")
else:
    soma = 0
    for i in range(N, M+1):
        if i % 3 != 0 and i % 7 != 0:
            soma += i
    print("Soma dos números do intervalo (não múltiplos de 3 nem 7):", soma)