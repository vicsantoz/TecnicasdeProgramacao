cont_intervalo = 0
soma_fora = 0

num = int(input("Digite um número (0 para sair): "))
while num != 0:
    if 10 <= num <= 50:
        cont_intervalo += 1
    else:
        soma_fora += num
    num = int(input("Digite um número (0 para sair): "))

print("Quantidade entre 10 e 50:", cont_intervalo)
print("Soma dos números fora do intervalo:", soma_fora)