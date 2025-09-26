vetor = [int(input(f"Digite o {i+1}º elemento: ")) for i in range(50)]

maior = max(vetor)
posicao = vetor.index(maior)
print(f"Maior elemento: {maior}, posição: {posicao}")