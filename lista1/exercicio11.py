custo_fabrica = float(input("Digite o custo de fábrica do carro: "))

custo_final = custo_fabrica = (custo_fabrica * 0.28) + (custo_fabrica * 0.45)
print(f"O custo final do consumidor é: R$ {custo_final:.2f}")