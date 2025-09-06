def print_triangle(n):
    for i in range(n):
        spaces = n - i - 1
        chars = 2 * i + 1
        print(" " * spaces + "%" * chars)

def print_diamond(n):
    # parte superior (incluindo meio)
    for i in range(n):
        spaces = n - i - 1
        chars = 2 * i + 1
        print(" " * spaces + "%" * chars)
    # parte inferior
    for i in range(n-2, -1, -1):
        spaces = n - i - 1
        chars = 2 * i + 1
        print(" " * spaces + "%" * chars)

# Programa principal
figura = input("Escolha a figura (losango/triangulo): ").strip().lower()
tamanho = int(input("Informe o tamanho (número de linhas): "))

if figura == "triangulo":
    print_triangle(tamanho)
elif figura == "losango":
    print_diamond(tamanho)
else:
    print("Figura inválida!")
