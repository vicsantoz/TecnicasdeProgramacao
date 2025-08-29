import math

r = float(input("Digite o raio da esfera: "))
volume = (4/3) * math.pi * (r ** 3)
area = 4 * math.pi * (r ** 2)

print(f"Volume = {volume:.2f}")
print(f"Area = {area:.2f}")
