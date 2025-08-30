aco = int(input("Qtd de hastes de aço: "))
cobre = int(input("Qtd de hastes de cobre: "))
aluminio = int(input("Qtd de hastes de alumínio: "))

total = (aco*2.5) + (cobre*4) + (aluminio*5)
qtd_total = aco + cobre + aluminio

if qtd_total < 6:
    desconto = 0
elif qtd_total <= 15:
    desconto = 0.10
elif qtd_total <= 20:
    desconto = 0.15
else:
    desconto = 0.20

total_com_desconto = total * (1 - desconto)
print(f"Total a pagar: R$ {total_com_desconto:.2f}")
