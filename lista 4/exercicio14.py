print("Graus Fahrenheit   Graus Celsius")
for F in range(32, 213):
    C = 5/9 * (F - 32)
    print(f"{F:<17} {C:.1f}")