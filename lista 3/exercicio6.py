horas = int(input("Horas estacionado: "))
valor = 0

if horas <= 2:
    valor = horas * 1
elif horas <= 5:
    valor = 2 * 1 + (horas - 2) * 1.4
else:
    valor = 2 * 1 + 3 * 1.4 + (horas - 5) * 1.6

print(f"Valor pago: R$ {valor:.2f}")