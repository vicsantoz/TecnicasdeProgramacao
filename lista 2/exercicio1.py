salario = float(input("Digite o salário: "))
finan = float(input("Digite o valor do financiamento: "))

if finan <= 5 * salario:
    print("Financiamento Concedido")
else:
    print("Financiamento Negado")

print("Obrigado por nos consultar.")

