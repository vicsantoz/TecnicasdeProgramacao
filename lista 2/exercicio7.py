a1 = int(input("Digite o 1º ângulo: "))
a2 = int(input("Digite o 2º ângulo: "))
a3 = int(input("Digite o 3º ângulo: "))

if a1 + a2 + a3 == 180:
    if a1 < 90 and a2 < 90 and a3 < 90:
        print("Triângulo Acutângulo")
    elif a1 == 90 or a2 == 90 or a3 == 90:
        print("Triângulo Retângulo")
    else:
        print("Triângulo Obtusângulo")
else:
    print("Os ângulos informados não formam um triângulo.")