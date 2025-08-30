nome = input("Nome do aluno: ")
nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
media = (nota1 + nota2) / 2

if media < 5:
    print(nome, "Reprovado")
elif media < 7:
    print(nome, "Recuperação")
else:
    print(nome, "Aprovado")
