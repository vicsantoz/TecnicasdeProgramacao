dentro = 0
fora_soma = 0
for i in range(10):
    num = int(input("Digite um número: "))
    if 10 <= num <= 50:
        dentro += 1
    else:
        fora_soma += num
print("Quantidade entre 10 e 50:", dentro)
print("Soma dos números fora do intervalo:", fora_soma)