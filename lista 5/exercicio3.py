num = int(input("Digite um número (0 para sair): "))
while num != 0:
    if num > 0 and num % 13 == 2:
        print(num)
    num = int(input("Digite um número (0 para sair): "))
