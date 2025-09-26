notas = []
matriculas = []
for i in range(50):
    m = input(f"Digite a matrícula do aluno {i+1}: ")
    n = float(input(f"Digite a nota do aluno {i+1}: "))
    matriculas.append(m)
    notas.append(n)

media = sum(notas) / len(notas)
print("Média das notas:", media)

acima = sum(1 for n in notas if n > media)
abaixo = sum(1 for n in notas if n < media)
print(f"Notas acima da média: {acima}")
print(f"Notas abaixo da média: {abaixo}")