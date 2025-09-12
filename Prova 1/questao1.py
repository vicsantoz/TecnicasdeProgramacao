import os
import time

andares = int(input("Informe o número de andares: "))

andar_atual = 0

while True:
    os.system("cls")

    for i in range(andares, 0, -1):
        if i == andar_atual:
            print("0")
        else:
            print("=")

    deslocamento = int(input("Informe o d: "))

    if deslocamento == 0:
        print("Fim do programa!")
        break

    andar_atual += deslocamento

    if andar_atual > andares:
        andar_atual = andares
    elif andar_atual < 0:
        andar_atual = 0
