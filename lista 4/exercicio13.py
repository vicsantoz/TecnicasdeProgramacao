maior_altura = 0
menor_altura = 9999
nome_menor = ""
cont_fem = 0

for i in range(20):
    nome = input("Nome: ")
    sexo = input("Sexo (M/F): ").upper()
    altura = float(input("Altura: "))

    if altura > maior_altura:
        maior_altura = altura
    if altura < menor_altura:
        menor_altura = altura
        nome_menor = nome
    if sexo == "F":
        cont_fem += 1

print("Maior altura:", maior_altura)
print("Quantidade de mulheres:", cont_fem)
print("Pessoa mais baixa:", nome_menor)