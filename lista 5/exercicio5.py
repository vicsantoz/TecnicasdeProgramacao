soma_salarios = 0
cont_pessoas = 0
maior_idade = -999
menor_idade = 999
cont_mulheres = 0
menor_salario = 999999
idade_menor_sal = 0
sexo_menor_sal = ""

idade = int(input("Digite a idade (idade negativa para sair): "))
while idade >= 0:
    sexo = input("Digite o sexo (M/F): ").upper()
    salario = float(input("Digite o salário: "))

    soma_salarios += salario
    cont_pessoas += 1

    if idade > maior_idade:
        maior_idade = idade
    if idade < menor_idade:
        menor_idade = idade

    if sexo == "F":
        cont_mulheres += 1

    if salario < menor_salario:
        menor_salario = salario
        idade_menor_sal = idade
        sexo_menor_sal = sexo

    idade = int(input("Digite a idade (idade negativa para sair): "))

if cont_pessoas > 0:
    media_salario = soma_salarios / cont_pessoas
    print("Média dos salários:", media_salario)
    print("Maior idade:", maior_idade)
    print("Menor idade:", menor_idade)
    print("Quantidade de mulheres:", cont_mulheres)
    print("Pessoa com menor salário -> Idade:", idade_menor_sal, "Sexo:", sexo_menor_sal)
else:
    print("Nenhum dado informado.")