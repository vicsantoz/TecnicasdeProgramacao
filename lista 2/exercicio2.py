dist1 = float(input("Digite a distância percorrida pelo carro 1: "))
tempo1 = float(input("Digite o tempo gasto pelo carro 1: "))
dist2 = float(input("Digite a distância percorrida pelo carro 2: "))
tempo2 = float(input("Digite o tempo gasto pelo carro 2: "))

v1 = dist1 / tempo1
v2 = dist2 / tempo2

if v1 > v2:
    print("Carro 1 tem maior velocidade média.")
elif v2 > v1:
    print("Carro 2 tem maior velocidade média.")
else:
    print("Os dois carros têm a mesma velocidade média.")

    
