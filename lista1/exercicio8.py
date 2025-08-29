s0 = 2
v0 = 3
a = 10

t= float(input("Digite o tempo S: "))
s = s0 + v0*t + (a * (t**2)) / 2

print(f"O espaço percorrido é: {s:.2f} m")