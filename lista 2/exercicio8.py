km = float(input("Digite a distância percorrida (Km): "))
litros = float(input("Digite os litros gastos: "))
consumo = km / litros

if consumo < 8:
    print("Venda o carro!")
elif consumo <= 14:
    print("Econômico!")
else:
    print("Super econômico!")
