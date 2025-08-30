mes = int(input("Digite o mês (1-12): "))
ano = int(input("Digite o ano: "))

if mes in [1,3,5,7,8,10,12]:
    dias = 31
elif mes in [4,6,9,11]:
    dias = 30
elif mes == 2:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        dias = 29
    else:
        dias = 28
print("Quantidade de dias:", dias)