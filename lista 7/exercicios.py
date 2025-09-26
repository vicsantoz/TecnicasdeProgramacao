#funções

#1
import math

def eh_par(x):
    return x % 2 == 0

#2
def maior(a, b):
    return a if a > b else b

#3
def soma_inteiros_entre(a, b):
    if a > b:
        a, b = b, a
    soma = 0
    for i in range(a + 1, b):
        soma += i
    return soma

#4
def multiplica(a, b):
    return a * b

#5
def multiplica_somas(a, b):
    sinal = -1 if (a < 0) ^ (b < 0) else 1
    a, b = abs(a), abs(b)
    resultado = 0
    for _ in range(b):
        resultado += a
    return sinal * resultado

#6
def potencia(a, b):
    return a ** b

#7
def potencia_mult(a, b):
    if b == 0:
        return 1
    sinal = 1
    if a < 0 and b % 2 != 0:
        sinal = -1
    a = abs(a)
    resultado = 1
    for _ in range(b):
        resultado *= a
    return sinal * resultado

#8
def eh_primo(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

#9
def fat(n):
    if n < 0:
        return None
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

#10
def arranjos(n, p):
    if n < p:
        return -1
    return math.factorial(n) // math.factorial(n - p)

#11
def combinacoes(n, p):
    if n < p:
        return -1
    return math.factorial(n) // (math.factorial(p) * math.factorial(n - p))


#pergunte ao usuário

print("Escolha uma opção:")
print("1 - Verificar se número é par.")
print("2 - Retornar o maior de dois números.")
print("3 - Somar números inteiros entre a e b.")
print("4 - Multiplicar usando *.")
print("5 - Multiplicar usando somas sucessivas.")
print("6 - Potência usando **.")
print("7 - Potência usando multiplicações sucessivas.")
print("8 - Verificar se número é primo.")
print("9 - Calcular fatorial.")
print("10 - Calcular arranjos.")
print("11 - Calcular combinações.")

#a opcão escolhida irá cair em:

opcao = int(input("Digite a opção: "))

if opcao == 1:
    x = int(input("Digite um número: "))
    print("Resultado: ", eh_par(x))

elif opcao == 2:
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    print("Resultado: ", maior(a,b))

elif opcao == 3:
    a = int(input("Digite a: "))
    b = int(input("Digite b: "))
    print("Resultado: ", soma_inteiros_entre(a,b))

elif opcao == 4:
    a = int(input("Digite a: "))
    b = int(input("Digite b: "))
    print("Resultado: ", multiplica(a,b))

elif opcao == 5:
    a = int(input("Digite a: "))
    b = int(input("Digite b: "))
    print("Resultado: ", multiplica_somas(a,b))

elif opcao == 6:
    a = int(input("Digite a base: "))
    b = int(input("Digite o expoente: "))
    print("Resultado: ", potencia(a,b))

elif opcao == 7:
    a = int(input("Digite a base: "))
    b = int(input("Digite o expoente: "))
    print("Resultado: ", potencia_mult(a,b))

elif opcao == 8:
    x = int(input("Digite um número: "))
    print("Resultado: ", eh_primo(x))

elif opcao == 9:
    n = int(input("Digite n: "))
    print("Resultado: ", fat(n))

elif opcao == 10:
    n = int(input("Digite n: "))
    p = int(input("Digite p: "))
    print("Resultado: ", arranjos(n,p))

elif opcao == 11:
    n = int(input("Digite n: "))
    p = int(input("Digite p: "))
    print("Resultado: ", combinacoes(n,p))

else:
    print("Opção não encontrada.")