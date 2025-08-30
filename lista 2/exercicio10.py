salario = float(input("Digite o salário bruto: "))

if salario <= 1903.98:
    imposto = 0
elif salario <= 2826.65:
    imposto = salario * 0.075 - 142.80
elif salario <= 3751.05:
    imposto = salario * 0.15 - 548.82
elif salario <= 4664.68:
    imposto = salario * 0.225 - 636.13
else:
    imposto = salario * 0.275 - 869.36

salario_liquido = salario - imposto
print(f"Imposto: R$ {imposto:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")
