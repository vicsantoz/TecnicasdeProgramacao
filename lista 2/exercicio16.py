num = int(input("Digite um número de 3 dígitos: "))
soma = (num // 100) + ((num // 10) % 10) + (num % 10)
print("Soma dos dígitos:", soma)

if num % 16 == 0 and num % 4 == 0:
    print("Número é divisor de 16 e múltiplo de 4")
else:
    print("Não atende à condição")
