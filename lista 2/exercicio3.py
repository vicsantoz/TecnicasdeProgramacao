from datetime import date
ano_atual = date.today().year

nome1 = input("Nome da primeira pessoa: ")
idade1 = int(input("Idade da primeira pessoa: "))
nome2 = input("Nome da segunda pessoa: ")
idade2 = int(input("Idade da segunda pessoa: "))

if idade1 < idade2:
    print(f"{nome1} é mais novo(a), ano de nascimento: {ano_atual - idade1}")
else:
    print(f"{nome2} é mais novo(a), ano de nascimento: {ano_atual - idade2}")