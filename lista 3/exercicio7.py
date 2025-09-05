a = int(input("Digite o 1º número: "))
b = int(input("Digite o 2º número: "))
c = int(input("Digite o 3º número: "))

numeros = [a, b, c]
numeros.sort()
soma = numeros[1] + numeros[2]
print(f"A soma dos dois maiores é {soma}")