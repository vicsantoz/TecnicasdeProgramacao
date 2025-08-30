z = float(input("Digite o valor de z: "))
w = float(input("Digite o valor de w: "))

if w > 0 or z < 7:
    x = (5*w + 1) / 3
    t = (z + 2) / 3
else:
    x = z + 2
    t = w + 5

y = (7*x*3 - 3(x*0.5) - 8*t) / (5(x + 1))
print("Valor de y:", y)