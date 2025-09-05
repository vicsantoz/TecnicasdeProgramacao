H = 0
num = 1
den = 1
for i in range(50):
    H += num / den
    num += 2
    den += 1
print("Valor de H:", H)