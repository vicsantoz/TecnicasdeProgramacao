qtd_carros = int(input("Digite a quantidade de carros vendidos: "))
val_total_vendas = float(input("Digite o valor total das vendas: "))
sal_fixo = float(input("Digite o slário fixo: "))
val_comissao = float(input("Digite o valor da comissão por carro: "))

sal_final = sal_fixo + (val_comissao * qtd_carros) + (0.05 * val_total_vendas)
print(f"O salário final do vendedor é: R$ {sal_final:.2f}")