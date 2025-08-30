media = float(input("Digite a média do aluno: "))
faltas = int(input("Digite o número de faltas: "))

if media >= 7 and faltas <= 32:
    print("Aprovado")
elif media < 7 and faltas <= 32:
    print("Reprovado por média")
elif media >= 7 and faltas > 32:
    print("Reprovado por faltas")
else:
    print("Reprovado por média e por faltas")
