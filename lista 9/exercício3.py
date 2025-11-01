notas = {}

while True:
    nome = input("Nome do aluno (ou 'fim' para encerrar): ").capitalize()
    if nome == "Fim":
        break
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    notas[nome] = [n1, n2]

medias = {aluno: (sum(nota) / 2) for aluno, nota in notas.items()}

reprovados = recuperacao = aprovados = 0

for media in medias.values():
    if media < 5:
        reprovados += 1
    elif media < 7:
        recuperacao += 1
    else:
        aprovados += 1

print("\n Resultados:")
print(f"Reprovados: {reprovados}")
print(f"Recuperação: {recuperacao}")
print(f"Aprovados: {aprovados}")

print("\n Médias dos alunos:")
for aluno, media in medias.items():
    print(f"{aluno}: {media:.2f}")
