tipo = input("Digite o tipo (I/C/R): ").upper()
consumo = float(input("Digite o consumo: "))

if tipo == "I":
    valor = 0.68 * consumo + 34
elif tipo == "C":
    valor = 0.37 * consumo + 45
else:
    valor = 0.77 * consumo - 22

print(f"Valor a pagar: R$ {valor:.2f}")