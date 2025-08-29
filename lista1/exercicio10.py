anos = int(input("Digite a idade em anos: "))
meses = int(input("Digite os meses: "))
dias = int(input("Digite os dias: "))

total_dias = anos*365 + meses*30 + dias
print(f"A idade total em dias é: {total_dias}")