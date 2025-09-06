pos = 0  # posição inicial da bandeirinha

while True:
    d = int(input("Informe d: "))
    pos += d
    
    # Verifica se alguma equipe venceu
    if pos <= -100:
        print("Vermelho é o vencedor!")
        break
    elif pos >= 100:
        print("Azul é o vencedor!")
        break
