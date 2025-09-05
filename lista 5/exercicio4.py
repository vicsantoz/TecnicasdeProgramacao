cont10 = cont5 = cont2 = contNenhum = 0

num = int(input("Digite um número (negativo para sair): "))
while num >= 0:
    if num % 10 == 0:
        cont10 += 1
    elif num % 5 == 0:
        cont5 += 1
    elif num % 2 == 0:
        cont2 += 1
    else:
        contNenhum += 1
    num = int(input("Digite um número (negativo para sair): "))

print("Divisíveis por 10:", cont10)
print("Divisíveis por 5:", cont5)
print("Divisíveis por 2:", cont2)
print("Não divisíveis por 10, 5 ou 2:", contNenhum)