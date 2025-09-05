import math

tipo = input("Digite o tipo de média (G/P/H/A): ").upper()
x = float(input("x: "))
y = float(input("y: "))
z = float(input("z: "))

if tipo == "G":
    media = (x * y * z) ** (1/3)
elif tipo == "P":
    media = (x + 2*y + 3*z) / 6
elif tipo == "H":
    media = 3 / ((1/x) + (1/y) + (1/z))
elif tipo == "A":
    media = (x + y + z) / 3
else:
    media = None

if media is None:
    print("Erro. Caracter inválido.")
else:
    print(f"Média ({tipo}): {media:.2f}")