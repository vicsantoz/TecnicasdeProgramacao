sexo = input("Digite o sexo (M/F): ").upper()
peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (cm): "))
idade = int(input("Digite a idade: "))

if sexo == "M":
    calorias = 66 + (13.7 * peso) + (5.0 * altura) - (6.8 * idade)
else:
    calorias = 665 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)

print("Calorias ideais por dia:", calorias)
