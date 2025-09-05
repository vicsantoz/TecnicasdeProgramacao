cobre = int(input("Quantidade de hastes de cobre: "))
aluminio = int(input("Quantidade de hastes de alumínio: "))

total_hastes = cobre + aluminio
preco_total = cobre * 2 + aluminio * 4

if total_hastes < 5:
    desconto = 0
elif total_hastes <= 15:
    desconto = 0.10
elif total_hastes <= 20:
    desconto = 0.15
else:
    desconto = 0.20

valor_final = preco_total * (1 - desconto)
print(f"Total a pagar: R$ {valor_final:.2f}")