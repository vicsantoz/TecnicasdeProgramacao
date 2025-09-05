TC = int(input("Tempo de contribuição: "))
ID = int(input("Idade: "))
ano_aposentar = int(input("Ano que pretende aposentar: "))
ano_atual = int(input("Ano atual: "))
sexo = input("Sexo (M/F): ").upper()

if ano_aposentar < ano_atual:
    print("Ano inválido. Não é possível cálculo.")
else:
    formula = (ano_aposentar - ano_atual) // 2
    if sexo == "F":
        condicao = TC + ID >= formula + 85
    else:
        condicao = TC + ID >= formula + 95

    if condicao:
        print("O empregado poderá se aposentar")
    else:
        print("O empregado não poderá se aposentar")
