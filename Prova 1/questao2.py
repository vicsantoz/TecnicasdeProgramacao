figura = input("Escolha a figura (triângulo/losango): ").strip().lower()

tamanho = int(input("Informe o tamanho (número de linhas): "))

def desenhar_triangulo(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "%" * (2 * i - 1))

def desenhar_losango(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "%" * (2 * i - 1))

    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "%" * (2 * i - 1))

if figura == "triângulo" or figura == "triangulo":
    desenhar_triangulo(tamanho)
elif figura == "losango":
    desenhar_losango(tamanho)
else:
    print("Figura inválida! Escolha 'triângulo' ou 'losango'.")
